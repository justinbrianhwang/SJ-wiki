"""Repair `#quot;` artifacts created by the older sanitizer when paired with [...] inside Mermaid labels.

The broken pattern looks like:
    Label["#quot;text with [N, 100, 1, 1"]"]
    Label["#quot;some [content"] more"]

We clean these to:
    Label["text with #lsqb;N, 100, 1, 1#rsqb;"]
    Label["some #lsqb;content#rsqb; more"]

Strategy: walk each ```mermaid``` block, and inside each block:
1. For lines that contain a `#quot;`, parse labels and rewrite them by:
   - removing `#quot;` markers
   - converting `[` and `]` that are *inside the label text* (not the bracket delimiters) to `#lsqb;`/`#rsqb;`
   - rewrapping in a single `"..."` pair
"""
import re
import sys
import pathlib


def fix_mermaid_block(body: str) -> str:
    lines = body.split("\n")
    out = []
    for line in lines:
        if "#quot;" not in line:
            out.append(line)
            continue
        # Pattern: NodeName["...broken..."] possibly with extra ] inside
        # Greedy fix: find each Mermaid-style bracket `[" ... "]` region that contains #quot;
        # and replace the inner content.
        def repair_segment(m: "re.Match[str]") -> str:
            inner = m.group(1)
            # Strip artifacts
            inner = inner.replace('#quot;', '').strip()
            # Trim leading/trailing literal quotes left over from the broken pattern
            while inner.startswith('"'):
                inner = inner[1:]
            while inner.endswith('"'):
                inner = inner[:-1]
            # Replace any remaining literal `[` and `]` with HTML entities for Mermaid
            inner = inner.replace('[', '#lsqb;').replace(']', '#rsqb;')
            return f'["{inner}"]'

        # Pattern A: `[" ... "]` regions across the whole line.
        # We have to be careful with nested brackets. Use a non-greedy match.
        new_line = re.sub(r'\["([^\]]*?#quot;[^\]]*?)"\]', repair_segment, line)

        # Some lines have multiple nested broken segments mashed together.
        # Run a second pass to clean any remaining `#quot;` artifacts.
        if '#quot;' in new_line:
            # Last-resort: in any remaining `"..."` containing `#quot;`, just strip and entity-encode.
            def repair_strict(m: "re.Match[str]") -> str:
                inner = m.group(1).replace('#quot;', '').strip().strip('"')
                inner = inner.replace('[', '#lsqb;').replace(']', '#rsqb;')
                return f'"{inner}"'
            new_line = re.sub(r'"([^"\n]*?#quot;[^"\n]*?)"', repair_strict, new_line)

        out.append(new_line)
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
        print("usage: python fix-mermaid-broken-quot.py <dir-or-file>...", file=sys.stderr)
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
