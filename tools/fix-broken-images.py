"""Remove markdown/HTML image embeds whose URLs are listed in a broken-URLs file.

Usage:
    python check-image-urls.py > broken-report.txt
    # manually pull the URL list, or:
    python check-image-urls.py 2>/dev/null | python fix-broken-images.py

Or pass a list of URLs (one per line) via stdin to this script. The script
walks all .md files and removes any `![alt](BAD_URL)` / `<img src="BAD_URL"...>`
that matches. It also removes the immediately-following italic caption line of
the form `*Figure: ... Image: ... ...*` if present (within 3 lines below the
removed image).
"""
import pathlib
import re
import sys


def remove_image_block(text: str, url: str) -> tuple[str, int]:
    md_pat = re.compile(rf"!\[[^\]]*\]\({re.escape(url)}\)\s*\n(?:[ \t]*\n)?(?:[ \t]*\*[^\n]*\*\s*\n)?")
    html_pat = re.compile(rf"<img[^>]+src=[\"']{re.escape(url)}[\"'][^>]*/?>(?:\s*\n)?(?:[ \t]*\n)?(?:[ \t]*\*[^\n]*\*\s*\n)?", re.IGNORECASE)
    new, n1 = md_pat.subn("", text)
    new, n2 = html_pat.subn("", new)
    return new, n1 + n2


def main():
    urls = [line.strip() for line in sys.stdin if line.strip().startswith("http")]
    print(f"Removing {len(urls)} broken URLs from docs/ ...", file=sys.stderr)
    total = 0
    for p in pathlib.Path("docs").rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        new = text
        for url in urls:
            new, n = remove_image_block(new, url)
            total += n
        if new != text:
            p.write_text(new, encoding="utf-8")
            print(f"  cleaned {p}", file=sys.stderr)
    print(f"Removed {total} embeds.", file=sys.stderr)


if __name__ == "__main__":
    main()
