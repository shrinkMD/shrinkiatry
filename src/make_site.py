# -*- coding: utf-8 -*-
"""Build shrinkiatry.com to static HTML in the repo root."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # repo root
sys.path.insert(0, HERE)

import engine as S
from engine import render_document, SITE

import content_home
import content_hubs
import content_articles
import content_or
import content_tools
import content_legal

PAGES = []
for mod in (content_home, content_hubs, content_articles, content_or,
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
    if slug == "":
        return "index.html"
    return os.path.join(slug, "index.html")


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
    lines = [
        "/assets/*",
        "  Cache-Control: public, max-age=31536000, immutable",
        "",
        "/*",
        "  X-Content-Type-Options: nosniff",
        "  Referrer-Policy: strict-origin-when-cross-origin",
        "  X-Frame-Options: SAMEORIGIN",
        "  Permissions-Policy: geolocation=(), microphone=(), camera=()",
        "",
    ]
    write("_headers", "\n".join(lines))


