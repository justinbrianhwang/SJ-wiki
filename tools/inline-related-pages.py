"""Turn the trailing '## Related pages' / '## Connections' / '## Related notes'
link list into a compact 'See also' footer (no heading, not in the TOC).

Bare-link lists become one line ("See also: a · b · c"); annotated lists keep
their bullets under a 'See also' label. The section must be last, or directly
followed by '## References'. Anything else is left alone.
Usage: python tools/inline-related-pages.py docs/
"""
import pathlib
import re
import sys

SECTION = re.compile(
    r'\n## (?:Related pages|Connections|Related notes)\s*\n\n'
    r'((?:- [^\n]+\n?)+)\s*(?=\n## References\b|\Z)'
)
BARE = re.compile(r'- (\[[^\]]+\]\([^)]+\))\s*$')


def footer(items):
    bare = [BARE.match(i) for i in items]
    if all(bare):
        body = 'See also: ' + ' · '.join(m.group(1) for m in bare)
    else:
        body = 'See also:\n\n' + '\n'.join(items)
    return f'\n<div className="see-also">\n\n{body}\n\n</div>\n'


n = 0
for f in pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'docs').rglob('*.md'):
    text = f.read_text(encoding='utf8')
    m = SECTION.search(text)
    if not m:
        continue
    items = [l.rstrip() for l in m.group(1).splitlines() if l.strip()]
    rest = text[m.end():]
    out = text[: m.start()] + footer(items) + (('\n' + rest.lstrip('\n')) if rest.strip() else '')
    f.write_text(out, encoding='utf8', newline='')
    n += 1
print(f'{n} file(s) updated')
