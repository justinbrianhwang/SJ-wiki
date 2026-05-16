"""Quote node labels inside ```mermaid``` fenced blocks.

Codex agents occasionally emit Mermaid node labels with characters that the
Mermaid parser treats specially. Mermaid accepts any character inside a label
when the label is wrapped in double quotes and internal ``"`` is replaced by
the HTML entity ``#quot;``, so this script normalizes labels to that form.

Bracket shapes handled (in matching priority — longest/most-specific first):

- ``A[(text)]``  cylinder
- ``A[[text]]``  subroutine
- ``A((text))``  circle
- ``A{{text}}``  hexagon
- ``A[/text/]``  parallelogram
- ``A[\\text\\]``  parallelogram (alt)
- ``A[text]``    rectangle
- ``A(text)``    rounded
- ``A{text}``    diamond

Edge labels (``A -->|label| B``) are handled separately.

The original implementation ran each bracket shape as its own regex pass,
which caused content inside ``[label]`` to be re-processed by the later
``(label)`` pass — accumulating layers of escaping. This version does a
single left-to-right scan with an alternation pattern so each bracketed
region is consumed exactly once.

A recovery step collapses ``"#quot;`` / ``#quot;"`` / ``#quot;#quot;``
chains created by the older buggy script.
"""
import re
import sys
import pathlib


HAZARDOUS = re.compile(r"[\(\)=\?:'<>&,;|\"]")

# (open, close) pairs in priority order — longest opening literal first.
NODE_BRACKETS = [
    ("[(", ")]"),
    ("[[", "]]"),
    ("((", "))"),
    ("{{", "}}"),
    ("[/", "/]"),
    ("[\\", "\\]"),
    ("[", "]"),
    ("(", ")"),
    ("{", "}"),
]


def quote_label(label: str) -> str:
    s = label.strip()
    # If already wrapped in "...", strip and revalidate.
    if len(s) >= 2 and s.startswith('"') and s.endswith('"'):
        inner = s[1:-1]
    else:
        inner = label
    if not HAZARDOUS.search(inner):
        return label
    escaped = inner.replace('"', "#quot;")
    return f'"{escaped}"'


# Build a single alternation regex that matches any node-shape bracket pair.
# Each alternative uses its own named group so we can identify which fired.
def _build_node_regex() -> "re.Pattern[str]":
    parts = []
    for i, (open_b, close_b) in enumerate(NODE_BRACKETS):
        # The lazy body excludes the closing bracket's first character to
        # keep the match bounded but tolerant of unrelated chars inside.
        open_esc = re.escape(open_b)
        close_esc = re.escape(close_b)
        body = rf"[^{re.escape(close_b[0])}\n]+?"
        parts.append(rf"(?P<o{i}>{open_esc})(?P<b{i}>{body})(?P<c{i}>{close_esc})")
    return re.compile("|".join(parts))


NODE_REGEX = _build_node_regex()


def fix_mermaid_block(block_body: str) -> str:
    lines = block_body.split("\n")
    out = []
    for line in lines:
        # 1) Edge labels --|...|, ==>|...|, etc. — single pass.
        def edge_sub(m: "re.Match[str]") -> str:
            return f"{m.group(1)}{quote_label(m.group(2))}{m.group(3)}"
        line = re.sub(r"(\|)([^|\n]+)(\|)", edge_sub, line)

        # 2) Recovery: collapse compound `#quot;` chains and stray quotes
        # introduced by an earlier buggy version of this script.
        while '"#quot;' in line or '#quot;"' in line or '#quot;#quot;' in line:
            line = line.replace('"#quot;', '#quot;')
            line = line.replace('#quot;"', '#quot;')
            line = line.replace('#quot;#quot;', '#quot;')

        # 3) Node-shape labels — single left-to-right pass via alternation.
        def node_sub(m: "re.Match[str]") -> str:
            for i in range(len(NODE_BRACKETS)):
                o = m.group(f"o{i}")
                if o is not None:
                    b = m.group(f"b{i}")
                    c = m.group(f"c{i}")
                    return f"{o}{quote_label(b)}{c}"
            return m.group(0)

        line = NODE_REGEX.sub(node_sub, line)
        out.append(line)
    return "\n".join(out)


def fix(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)

    def block_sub(m: "re.Match[str]") -> str:
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
