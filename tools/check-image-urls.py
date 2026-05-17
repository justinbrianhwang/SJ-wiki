"""Verify every external image URL in markdown files. Polite (rate-limited)
HEAD requests with retry-on-429.
"""
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from threading import Lock

MD_IMG_RE = re.compile(r"!\[[^\]]*\]\((https?://[^\s\)]+)\)")
HTML_IMG_RE = re.compile(r'<img[^>]+src=["\'](https?://[^"\']+)["\']', re.IGNORECASE)
TIMEOUT = 12

# Per-host minimum interval (seconds between requests to that host)
HOST_INTERVAL = {
    "upload.wikimedia.org": 0.6,
    "commons.wikimedia.org": 0.6,
    "ar5iv.labs.arxiv.org": 0.4,
    "github.com": 0.3,
    "raw.githubusercontent.com": 0.3,
}
DEFAULT_INTERVAL = 0.3

_last_call: dict[str, float] = {}
_lock = Lock()


def throttle(host: str) -> None:
    interval = HOST_INTERVAL.get(host, DEFAULT_INTERVAL)
    with _lock:
        last = _last_call.get(host, 0.0)
        now = time.monotonic()
        wait = (last + interval) - now
        if wait > 0:
            time.sleep(wait)
        _last_call[host] = time.monotonic()


def collect_urls(docs_dir: pathlib.Path):
    url_to_refs = defaultdict(list)
    for p in docs_dir.rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        for ln, line in enumerate(text.splitlines(), 1):
            for m in MD_IMG_RE.finditer(line):
                url_to_refs[m.group(1)].append((str(p), ln))
            for m in HTML_IMG_RE.finditer(line):
                url_to_refs[m.group(1)].append((str(p), ln))
    return url_to_refs


def host_of(url: str) -> str:
    return url.split("/", 3)[2] if "://" in url else ""


def check_once(url: str, method: str) -> tuple[int | None, str]:
    headers = {"User-Agent": "Mozilla/5.0 (SJ-Wiki link checker)"}
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    req = urllib.request.Request(url, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, "ok"
    except urllib.error.HTTPError as e:
        return e.code, f"HTTP {e.code}"
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def check_url(url: str) -> tuple[str, int | None, str]:
    host = host_of(url)
    # Try HEAD with up to 3 attempts; on 429 wait and retry.
    for attempt in range(3):
        throttle(host)
        status, msg = check_once(url, "HEAD")
        if status == 200 or status == 206:
            return url, status, "ok"
        if status in (403, 405, 501):
            # method-not-allowed — retry with GET range
            throttle(host)
            status, msg = check_once(url, "GET")
            return url, status, msg
        if status == 429:
            time.sleep(2.0 + attempt)
            continue
        return url, status, msg
    return url, 429, "rate-limited after retries"


def main():
    docs = pathlib.Path("docs")
    url_to_refs = collect_urls(docs)
    urls = sorted(url_to_refs.keys())
    print(f"Found {len(urls)} unique URLs across {sum(len(v) for v in url_to_refs.values())} embeds.", file=sys.stderr)

    broken = []
    ok = 0
    rate_limited = []
    for i, url in enumerate(urls, 1):
        _, status, msg = check_url(url)
        if status in (200, 206):
            ok += 1
        elif status == 429:
            rate_limited.append((url, msg))
        else:
            broken.append((url, status, msg))
        if i % 20 == 0 or i == len(urls):
            print(f"  {i}/{len(urls)}  ok={ok}  broken={len(broken)}  rate-limited={len(rate_limited)}", file=sys.stderr)

    print(f"\n=== Summary ===")
    print(f"Total: {len(urls)}  OK: {ok}  Broken: {len(broken)}  Rate-limited (not classified): {len(rate_limited)}")
    if broken:
        print(f"\n=== Broken (will be removed) ===")
        for url, status, msg in broken:
            print(f"BROKEN {url}")
            print(f"  status={status} {msg}")
            for f, ln in url_to_refs[url]:
                print(f"  ref {f}:{ln}")
    if rate_limited:
        print(f"\n=== Rate-limited (skipped, treat as OK) ===")
        for url, msg in rate_limited[:5]:
            print(f"  {url}")
        if len(rate_limited) > 5:
            print(f"  ... and {len(rate_limited) - 5} more")


if __name__ == "__main__":
    main()
