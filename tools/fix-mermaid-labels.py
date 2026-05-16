"""Quote node labels inside ```mermaid``` fenced blocks.

Codex agents occasionally emit Mermaid node labels with characters that the
Mermaid parser treats specially: ``'``, ``=``, ``(``, ``)``, ``?``, ``:``,
``<``, ``>``, ``&``, ``,`` and ``"``. These cause client-side render errors
even though the markdown builds fine.

Mermaid accepts any character inside a label when the label is wrapped in
double quotes, so we wrap any *unquoted* label that contains one of those
characters. Already-quoted labels are left as-is.

Supported node shapes:
- ``A[text]``        rectangle
- ``A(text)``        rounded rectangle
- ``A((text))``      circle
- ``A{text}``        diamond
- ``A{{text}}``      hexagon
- ``A[/text/]``      parallelogram
- ``A[\\text\\]``    parallelogram (alt)
- ``A[(text)]``      cylinder
- ``A[[text]]``      subroutine

We do not try to be exhaustive — just the common shapes.

Edge labels (``A -->|label| B``) get the same treatment.
"""
import re
import sys
import pathlib


HAZARDOUS = re.compile(r"[\(\)=\?:'<>&,;|\"]")


# Mermaid bracket variants in order: longer/specific first.
NODE_BRACKETS = [
    ("[(", ")]"),    # cylinder
    ("[[", "]]"),    # subroutine
    ("((", "))"),    # circle
    ("{{", "}}"),    # hexagon
    ("[/", "/]"),    # parallelogram
    ("[\\", "\\]"),  # parallelogram alt
    ("[", "]"),      # rectangle
    ("(", ")"),      # rounded
    ("{", "}"),      # diamond
]


def quote_label(label: str) -> str:
    s = label.strip()
    # If already wrapped in "...", strip the outer wrap so we can re-validate
    # the inner content. (Codex sometimes emits `"y' = f("x,y")"` which is
    # broken because the inner `"`s need to be escaped to #quot;.)
    if len(s) >= 2 and s.startswith('"') and s.endswith('"'):
        inner = s[1:-1]
        wrapped_already = True
    else:
        inner = label
        wrapped_already = False
    # Safe? No hazardous chars and no stray " inside.
    if not HAZARDOUS.search(inner):
        return label
    # Escape any remaining literal " to #quot; (Mermaid HTML entity)
    escaped = inner.replace('"', "#quot;")
    return f'"{escaped}"'


def fix_mermaid_block(block_body: str) -> str:
    """Walk lines and rewrite node labels."""
    lines = block_body.split("\n")
    out = []
    for line in lines:
        new_line = line
        # First, edge labels: --|...| or ===|...| or ---|...|
        # Pattern: any of -->|, --o|, --x|, ==>|, ---|, etc., followed by content, then |
        def edge_label_sub(m):
            prefix, label, suffix = m.group(1), m.group(2), m.group(3)
            return prefix + quote_label(label) + suffix
        new_line = re.sub(
            r"(\|)([^|\n]+)(\|)",
            edge_label_sub,
            new_line,
        )
        # Node-shape labels. Try each bracket pair (longest first to avoid
        # rectangles eating into cylinders, subroutines, etc.).
        for open_b, close_b in NODE_BRACKETS:
            open_esc = re.escape(open_b)
            close_esc = re.escape(close_b)
            pat = re.compile(
                rf"({open_esc})([^{re.escape(close_b[0])}\n]+?)({close_esc})"
            )
            new_line = pat.sub(
                lambda m: m.group(1) + quote_label(m.group(2)) + m.group(3),
                new_line,
            )
        out.append(new_line)
    return "\n".join(out)


def fix(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)
    def block_sub(m):
        body = m.group(1)
        new_body = fix_mermaid_block(body)
        return f"```mermaid\n{new_body}\n```"
    new = pattern.sub(block_sub, text)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python fix-mermaid-labels.py <dir-or-file>...", file=sys.stderr)
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
                print("fixed:", f)
    print(f"\n{changed}/{scanned} file(s) updated")


if __name__ == "__main__":
    main()
