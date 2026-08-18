#!/usr/bin/env python3
"""Regenerate sitemap.xml with <lastmod> taken from each page's last git commit.
Run after adding/editing pages:  python3 build_sitemap.py"""
import subprocess, glob, os
SITE="https://www.mykurtains.com"
def lastmod(path):
    out=subprocess.run(['git','log','-1','--format=%cs','--',path],capture_output=True,text=True).stdout.strip()
    return out or subprocess.run(['date','+%Y-%m-%d'],capture_output=True,text=True).stdout.strip()
posts=sorted(os.path.basename(p) for p in glob.glob('blog/*.html') if os.path.basename(p)!='index.html')
def url(loc,en,fr,pri,freq,path):
    return (f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod(path)}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n'
            f'    <xhtml:link rel="alternate" hreflang="en" href="{en}"/>\n    <xhtml:link rel="alternate" hreflang="fr" href="{fr}"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="{en}"/>\n  </url>\n')
o='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
o+=url(f"{SITE}/",f"{SITE}/",f"{SITE}/index-fr.html","1.0","weekly","index.html")
o+=url(f"{SITE}/index-fr.html",f"{SITE}/",f"{SITE}/index-fr.html","1.0","weekly","index-fr.html")
o+=url(f"{SITE}/blog/",f"{SITE}/blog/",f"{SITE}/blog/fr/","0.9","weekly","blog/index.html")
o+=url(f"{SITE}/blog/fr/",f"{SITE}/blog/",f"{SITE}/blog/fr/","0.9","weekly","blog/fr/index.html")
for p in posts:
    en=f"{SITE}/blog/{p}"; fr=f"{SITE}/blog/fr/{p}"
    o+=url(en,en,fr,"0.8","monthly",f"blog/{p}"); o+=url(fr,en,fr,"0.8","monthly",f"blog/fr/{p}")
o+='</urlset>\n'
open('sitemap.xml','w').write(o); print("sitemap.xml:",o.count('<url>'),"urls")
