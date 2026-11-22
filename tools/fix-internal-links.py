"""Repair absolute internal doc links against the routes in build/.

Fixes: section roots (/cs/nlp -> /cs/nlp/intro), trailing slashes, and
number-prefixed filenames that Docusaurus strips from slugs
(/cs/embedded/8051-foo -> /cs/embedded/foo). Run after `npm run build`.
Usage: python tools/fix-internal-links.py docs/
"""
import pathlib
import re
import sys

build = pathlib.Path('build')
routes = {'/' + p.relative_to(build).with_suffix('').as_posix() for p in build.rglob('*.html')}
routes |= {r[: -len('/index')] for r in routes if r.endswith('/index')}

LINK = re.compile(r'\]\((/(?:math|cs|physics|chemistry|quantum-information-science)[^)\s#]*)(#[^)\s]*)?\)')


MANUAL = {
    '/math/calculus/limits': '/math/calculus/limits-and-continuity',
    '/cs/control-engineering/digital-control-sampling-z-transform-design': '/cs/control-engineering/digital-control-sampling-and-z-transform',
    '/physics/general/thermodynamics': '/physics/general/first-law-entropy-and-second-law',
}


def resolve(path):
    p = path.rstrip('/') or '/'
    p = MANUAL.get(p, p)
    if p in routes:
        return p
    for cand in (p + '/intro', re.sub(r'/\d+-([^/]+)$', r'/\1', p)):
        if cand in routes:
            return cand
    return None


changed = unresolved = 0
for f in pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'docs').rglob('*.md'):
    text = f.read_text(encoding='utf8')

    def sub(m):
        global unresolved
        new = resolve(m.group(1))
        if new is None:
            unresolved += 1
            print(f'UNRESOLVED {f.as_posix()}: {m.group(1)}')
            return m.group(0)
        return f']({new}{m.group(2) or ""})'

    out = LINK.sub(sub, text)
    if out != text:
        f.write_text(out, encoding='utf8', newline='')
        changed += 1
print(f'{changed} file(s) updated, {unresolved} unresolved link(s)')
