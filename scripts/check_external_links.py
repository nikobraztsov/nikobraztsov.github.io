#!/usr/bin/env python3
"""Check external hyperlinks in a clean Hugo build. No changes to content."""
import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import subprocess, tempfile, urllib.request, urllib.error
from urllib.parse import urlsplit, urljoin, urldefrag

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ('a','area') and a.get('href'): self.urls.append(a['href'])
        if tag=='iframe' and a.get('src'): self.urls.append(a['src'])

def collect(root, domain):
    refs=defaultdict(set)
    own={domain,'www.'+domain,'localhost','127.0.0.1','nikobraztsov.github.io'}
    for p in sorted(root.rglob('*.html')):
        parser=Links(); parser.feed(p.read_text(encoding='utf-8',errors='replace'))
        for original in parser.urls:
            try:
                url=urldefrag(urljoin('https://'+domain+'/',original.strip()))[0]; parts=urlsplit(url)
                if parts.scheme in ('http','https') and parts.hostname and parts.hostname not in own:
                    refs[url].add((p.relative_to(root).as_posix(), original))
            except ValueError: continue
    return refs

def probe(url, timeout):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; PersonalSiteLinkAudit/1.0)','Accept':'text/html,application/pdf,*/*;q=0.8'})
        with urllib.request.urlopen(req,timeout=timeout) as response:
            code=response.getcode(); final=response.geturl()
            return ('REDIRECT' if final!=url else 'OK',str(code),final)
    except urllib.error.HTTPError as e:
        status='NOT FOUND' if e.code in (404,410) else 'MANUAL CHECK'
        return status,str(e.code),e.geturl()
    except (OSError,ValueError) as e:
        return 'MANUAL CHECK',str(e),url

def run(root,args):
    refs=collect(root,args.domain); print(f'External URLs: {len(refs)}',flush=True)
    lines=['EXTERNAL LINK AUDIT','HTTP checks only; 200 does not establish correct content. Fragments are not sent to servers. 403/429/timeouts require manual checking.','']
    counts=defaultdict(int)
    if args.inventory_only:
        results=[('NOT CHECKED','',url) for url in refs]
    else:
        with ThreadPoolExecutor(max_workers=4) as executor:
            results=list(executor.map(lambda url:probe(url,args.timeout),refs))
    for url,(status,detail,final) in zip(refs,results):
        counts[status]+=1; lines.append(f'[{status}] {url} {detail}')
        if final!=url: lines.append('  FINAL: '+final)
        for page,original in sorted(refs[url]): lines.append(f'  {page} | {original}')
        lines.append('')
    lines[2]=' | '.join(f'{k}: {v}' for k,v in sorted(counts.items()))
    report=args.report.expanduser(); report.parent.mkdir(parents=True,exist_ok=True);report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(lines[2]);print('REPORT:',report)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--site-dir',type=Path);p.add_argument('--domain',default='nikitaobraztsov.com');p.add_argument('--timeout',type=float,default=10);p.add_argument('--inventory-only',action='store_true');p.add_argument('--report',type=Path,default=Path.home()/'Documents/site-external-link-audit.txt');a=p.parse_args()
    if a.site_dir: run(a.site_dir.resolve(),a)
    else:
        root=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(prefix='external-audit-') as tmp:
            subprocess.run(['hugo','--environment','production','--destination',tmp],cwd=root,check=True);run(Path(tmp),a)
if __name__=='__main__':main()
