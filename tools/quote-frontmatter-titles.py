"""Quote unquoted `title:` values in YAML frontmatter.

Codex sometimes writes `title: Friction: Dry Contact, Belts, and Screws` —
the second colon breaks YAML. We rewrite to `title: "Friction: Dry Contact,
Belts, and Screws"` whenever the value contains a colon or # or other YAML
hazard and isn't already quoted.
"""
import re
import sys
import pathlib


YAML_HAZARDS = re.compile(r"[:#&*!|>'\"%@`{}\[\]]")


def fix(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end == -1:
        return False
    fm = text[4:end]
    rest = text[end:]
    lines = fm.split("\n")
    changed = False
    for i, line in enumerate(lines):
        m = re.match(r"^(\s*title\s*:\s*)(.+)$", line)
        if not m:
            continue
        prefix, value = m.group(1), m.group(2).rstrip()
        # already quoted?
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            continue
        if not YAML_HAZARDS.search(value):
            continue
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        lines[i] = f'{prefix}"{escaped}"'
        changed = True
    if not changed:
        return False
    new = "---\n" + "\n".join(lines) + rest
    path.write_text(new, encoding="utf-8")
    return True


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python quote-frontmatter-titles.py <dir-or-file>...", file=sys.stderr)
        sys.exit(2)
    changed = 0
    scanned = 0
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        files = list(p.rglob("*.md")) if p.is_dir() else [p]
        for f in files:
            scanned += 1
            if fix(f):
                changed += 1
                print("quoted:", f)
    print(f"\n{changed}/{scanned} file(s) updated")


if __name__ == "__main__":
    main()
