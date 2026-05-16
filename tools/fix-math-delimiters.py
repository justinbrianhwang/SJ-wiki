"""Sanitize math delimiters and inline `<` / `>` for MDX 3 + KaTeX.

- Converts LaTeX `\\(...\\)` and `\\[...\\]` to KaTeX `$...$` and `$$...$$`.
- Normalizes multi-line display blocks so the opening `$$` is on its own line.
- Inside inline `$...$` math, replaces bare `<` with `\\lt` and bare `>` with
  `\\gt`. KaTeX renders `\\lt`/`\\gt` identically, but MDX 3 mis-parses
  `$...<1$` inside markdown table cells as JSX tag start.
"""
import re
import sys
import pathlib


def fix(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # 1. Display math: \[ ... \] -> $$ ... $$
    text = re.sub(
        r"\\\[\s*(.*?)\s*\\\]",
        lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n",
        text,
        flags=re.DOTALL,
    )
    # 2. Inline math: \( ... \) -> $ ... $
    text = re.sub(
        r"\\\((.*?)\\\)",
        lambda m: "$" + m.group(1) + "$",
        text,
        flags=re.DOTALL,
    )

    # 3. Normalize multi-line display blocks. The match swallows any leading
    # whitespace on the opening-$$ line and any leading whitespace on the
    # closing-$$ line, so the rewrite is always at column 0.
    def normalize_block(match: "re.Match[str]") -> str:
        body = match.group(1)
        if "\n" not in body:
            # Single-line $$x$$ — leave unchanged.
            return match.group(0)
        lines = body.split("\n")
        while lines and lines[0].strip() == "":
            lines.pop(0)
        while lines and lines[-1].strip() == "":
            lines.pop()
        indents = [len(l) - len(l.lstrip(" ")) for l in lines if l.strip()]
        if indents:
            common = min(indents)
            if common > 0:
                lines = [l[common:] if l.strip() else l for l in lines]
        return "\n$$\n" + "\n".join(lines) + "\n$$\n"

    text = re.sub(
        r"[ \t]*\$\$(.+?)\$\$[ \t]*",
        normalize_block,
        text,
        flags=re.DOTALL,
    )

    # Collapse the extra newlines added by the prefix/suffix above.
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 4. Inside INLINE $...$ math (NOT $$...$$), replace bare `<` and `>` with
    # `\lt` and `\gt`. `\le`, `\ge`, `\ll`, `\gg`, `\leftarrow`, `\rightarrow`
    # are preserved because we match only `<`/`>` not preceded by a backslash.
    def sanitize_inline(match: "re.Match[str]") -> str:
        body = match.group(1)
        body = re.sub(r"(?<!\\)<", r"\\lt ", body)
        body = re.sub(r"(?<!\\)>", r"\\gt ", body)
        # Markdown tables use `|` as cell separator. Inside inline math sitting
        # in a table cell, bare `|` breaks the math span and triggers MDX-as-JSX
        # mis-parsing. KaTeX renders `\vert` identically to `|`.
        body = re.sub(r"(?<!\\)\|", r"\\vert ", body)
        return "$" + body + "$"

    text = re.sub(
        r"(?<!\$)\$(?!\$)([^\$\n]+?)(?<!\$)\$(?!\$)",
        sanitize_inline,
        text,
    )

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python fix-math-delimiters.py <dir-or-file> [...]", file=sys.stderr)
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
