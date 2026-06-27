# -*- coding: utf-8 -*-
"""Clean build entrypoint (uses home2 to avoid a stale cached module)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import engine as S
from engine import render_document, SITE

import home2
import content_hubs
import content_articles
import content_or
import content_tools
import content_legal

PAGES = []
for mod in (home2, content_hubs, content_articles, content_or,
            content_tools, content_legal):
    PAGES.extend(mod.PAGES)


def write(path, text):
    full = os.path.join(OUT, path)
    d = os.path.dirname(full)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def page_path(slug):
    return "index.html" if slug == "" else os.path.join(slug, "index.html")


def build_404():
    body = (
        '<section class="section section--slate"><div class="wrap" style="text-align:center">'
        '<span class="eyebrow">Error 404</span>'
        "<h1 class=\"mt-1\">This page isn't here.</h1>"
        '<p class="hero__sub mx-auto mt-2" style="max-width:46ch">'
        "The page you're looking for moved or never existed. Try the homepage, "
        "or step into the Operating Room to explore the profession.</p>"
        '<div class="hero__cta" style="justify-content:center">'
        '<a class="btn btn--onslate btn--lg" href="/">Go to the homepage</a>'
        '<a class="btn btn--ghost btn--lg" href="/psychiatry-operating-room/" '
        'style="color:#fff;border-color:rgba(255,255,255,.35)">The Operating Room</a>'
        "</div></div></section>"
    )
    nf = {"slug": "404", "active": None, "robots": "noindex, follow",
          "title": "Page not found | shrinkiatry",
          "desc": "The page you're looking for isn't here. Explore the profession of psychiatry at shrinkiatry.",
          "body": body}
    write("404.html", render_document(nf))


def build_headers():
    lines = ["/assets/*", "  Cache-Control: public, max-age=31536000, immutable", "",
             "/*", "  X-Content-Type-Options: nosniff",
             "  Referrer-Policy: strict-origin-when-cross-origin",
             "  X-Frame-Options: SAMEORIGIN",
             "  Permissions-Policy: geolocation=(), microphone=(), camera=()", ""]
    write("_headers", "\n".join(lines))


def build_sitemap():
    today = "2026-06-27"
    rows = []
    for p in PAGES:
        slug = p["slug"]
        loc = SITE["url"] + "/" + (slug + "/" if slug else "")
        pr = "1.0" if slug == "" else ("0.9" if "/" not in slug else "0.7")
        rows.append("  <url><loc>%s</loc><lastmod>%s</lastmod>"
                    "<changefreq>monthly</changefreq><priority>%s</priority></url>"
                    % (loc, today, pr))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    write("sitemap.xml", xml)


def build_robots():
    lines = ["User-agent: *", "Allow: /", "",
             "# AI assistants are welcome to read and cite shrinkiatry.",
             "User-agent: GPTBot", "Allow: /", "User-agent: ClaudeBot", "Allow: /",
             "User-agent: PerplexityBot", "Allow: /", "User-agent: Google-Extended", "Allow: /",
             "", "Sitemap: https://shrinkiatry.com/sitemap.xml", ""]
    write("robots.txt", "\n".join(lines))


def main():
    seen = set()
    for p in PAGES:
        slug = p["slug"]
        if slug in seen:
            raise SystemExit("Duplicate slug: " + slug)
        seen.add(slug)
        write(page_path(slug), render_document(p))
    print("Wrote %d pages" % len(PAGES))
    build_404(); build_headers(); build_sitemap(); build_robots()
    print("Wrote 404.html, _headers, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
