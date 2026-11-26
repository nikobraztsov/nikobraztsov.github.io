#!/usr/bin/env python3
"""Check internal HTML links in a clean Hugo build (Python 3, stdlib only)."""
import argparse
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import subprocess
import tempfile
from urllib.parse import quote, unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = 'nikitaobraztsov.com'
LOCAL = {'localhost', '127.0.0.1', '::1'}
HOSTS = {DOMAIN, 'www.' + DOMAIN} | LOCAL


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.anchors = set()
        self.base = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.anchors.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.anchors.add(attrs['name'])
        if tag == 'base':
            if self.base is None:
                self.base = attrs.get('href')
            return
        for attr in ('href', 'src', 'poster'):
            if attrs.get(attr):
                self.links.append(attrs[attr])


def audit(build):
    files = {p.relative_to(build).as_posix() for p in build.rglob('*') if p.is_file()}
    if 'index.html' not in files:
        raise ValueError(f'No index.html in {build}; check the build directory.')
    lower = defaultdict(list)
    for f in sorted(files):
        lower[f.casefold()].append(f)
    pages = {}
    for f in sorted(files):
        if f.endswith('.html'):
            p = Page()
            p.feed((build / f).read_text(encoding='utf-8', errors='replace'))
            p.close()
            pages[f] = p
    problems = defaultdict(set)
    checked = external = 0
    for source, page in pages.items():
        route = source[:-len('index.html')] if source.endswith('/index.html') or source == 'index.html' else source
        base = 'https://' + DOMAIN + '/' + quote(route)
        if page.base:
            base = urljoin(base, page.base)
        for link in page.links:
            link = link.strip()
            if not link:
                continue
            try:
                url = urlsplit(urljoin(base, link))
                host = url.hostname
            except ValueError:
                problems['INVALID URL', link].add((source, link))
                continue
            if url.scheme not in ('http', 'https'):
                continue
            if host not in HOSTS:
                external += 1
                continue
            checked += 1
            if host in LOCAL:
                problems['LOCALHOST LINK', link].add((source, link))
            path = posixpath.normpath(unquote(url.path)).lstrip('/')
            if path == '.':
                path = ''
            candidates = [path] if path and not url.path.endswith('/') else []
            candidates.append(posixpath.join(path, 'index.html'))
            target = next((c for c in candidates if c in files), None)
            if target is None:
                matches = sorted({m for c in candidates for m in lower.get(c.casefold(), [])})
                if matches:
                    kind, label = 'WRONG CASE', '/' + path + ' -> ' + ', '.join(matches)
                else:
                    kind = 'WRONG STATIC PATH' if 'static' in path.split('/') else 'MISSING FILE OR PAGE'
                    label = '/' + path
                problems[kind, label].add((source, link))
                continue
            fragment = unquote(url.fragment)
            if (fragment and fragment.lower() != 'top' and ':~:' not in fragment
                    and target in pages and fragment not in pages[target].anchors):
                problems['MISSING ANCHOR', '/' + target + '#' + fragment].add((source, link))
    lines = ['========== SITE LINK AUDIT ==========', '',
             f'HTML pages: {len(pages)}', f'Generated files: {len(files)}',
             f'Internal links checked: {checked}', f'External links skipped: {external}',
             f'Unique problems: {len(problems)}', '']
    for (kind, target), refs in sorted(problems.items()):
        lines.extend([f'[{kind}]', f'TARGET: {target}'])
        for source, link in sorted(refs):
            lines.extend([f'  PAGE: {source}', f'  LINK: {link}'])
        lines.append('')
    return '\n'.join(lines), len(problems)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, help='Check an existing build rather than running Hugo.')
    parser.add_argument('--report', type=Path, help='Optional output path for a text report.')
    args = parser.parse_args()
    try:
        if args.site_dir:
            report, count = audit(args.site_dir.resolve())
        else:
            with tempfile.TemporaryDirectory(prefix='hugo-link-audit-') as tmp:
                subprocess.run(['hugo', '--environment', 'production', '--destination', tmp], cwd=ROOT, check=True)
                report, count = audit(Path(tmp))
        print(report)
        if args.report:
            args.report.expanduser().write_text(report + '\n', encoding='utf-8')
        return 1 if count else 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'AUDIT ERROR: {exc}')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
