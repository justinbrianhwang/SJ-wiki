"""Escape literal `{` and `}` in prose so MDX 3 doesn't mis-parse them as JSX.

Codex frequently writes set notation like `{apple, milk}` in narrative text. In
MDX 3 these become JSX expressions referencing undefined identifiers (`apple`,
`milk`). This script escapes `{` and `}` to `\\{` / `\\}` ONLY outside of:

- fenced code blocks (``` ... ``` or ~~~ ... ~~~)
- inline code (`...`)
- math regions ($...$ and $$...$$)
- existing JSX-like `<Component ... />` blocks (heuristic: tag-start with
  ASCII letter)
- frontmatter (--- block at top)
- import / export statement lines (start with `import ` or `export `)

The escape uses MDX 3's literal-character syntax `\\{` and `\\}` which renders
as a real brace at runtime.
"""
import re
import sys
import pathlib


def split_safe_and_prose(text: str) -> list[tuple[str, str]]:
    """Split into ('safe', s) | ('prose', s) segments.

    Safe segments are passed through untouched. Prose segments get the brace
    escape applied.
    """
    # Pattern alternation: anything we DON'T want to touch.
    # Order matters: longer/more-specific first.
    pattern = re.compile(
        r"```[\s\S]*?```"  # fenced code blocks
        r"|~~~[\s\S]*?~~~"  # alt fenced
        r"|`[^`\n]*`"  # inline code
        r"|\$\$[\s\S]*?\$\$"  # display math
        r"|(?<!\$)\$(?!\$)[^\$\n]*?(?<!\$)\$(?!\$)"  # inline math
        r"|^---\n[\s\S]*?\n---\n"  # YAML frontmatter at top
        r"|^(?:import|export)\s[^\n]*\n"  # MDX import/export lines
        r"|<[A-Za-z][^>]*>"  # JSX-like opening tag
        r"|</[A-Za-z][^>]*>",  # JSX-like closing tag
        re.MULTILINE,
    )
    segments: list[tuple[str, str]] = []
    last = 0
    for m in pattern.finditer(text):
        if m.start() > last:
            segments.append(("prose", text[last : m.start()]))
        segments.append(("safe", m.group(0)))
        last = m.end()
    if last < len(text):
        segments.append(("prose", text[last:]))
    return segments


def escape_braces(prose: str) -> str:
    # Only escape `{` followed by something that looks like an identifier
    # OR plain commas/spaces (set notation). Leave `\{` alone (already escaped).
    # Also escape matching `}` in the same patterns.
    # Strategy: escape ALL `{` not already escaped, and same for `}`.
    prose = re.sub(r"(?<!\\)\{", r"\\{", prose)
    prose = re.sub(r"(?<!\\)\}", r"\\}", prose)
    return prose


def fix(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    segments = split_safe_and_prose(text)
    rebuilt = []
    for kind, s in segments:
        if kind == "prose":
            rebuilt.append(escape_braces(s))
        else:
            rebuilt.append(s)
    new = "".join(rebuilt)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python escape-jsx-braces.py <dir-or-file>...", file=sys.stderr)
        sys.exit(2)
    changed = 0
    scanned = 0
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        if p.is_dir():
            files = list(p.rglob("*.md"))
        else:
            files = [p]
        for f in files:
            scanned += 1
            if fix(f):
                changed += 1
                print("fixed:", f)
    print(f"\n{changed}/{scanned} file(s) updated")


if __name__ == "__main__":
    main()
