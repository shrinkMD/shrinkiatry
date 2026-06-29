# -*- coding: utf-8 -*-
"""Build entry v9: buildv8 + author media features (In the media + subjectOf schema)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("BUILD_OUT") or os.path.dirname(HERE)
sys.path.insert(0, HERE)

import engine_v3
_real_v2 = engine_v3._b

_real_v2.NAV = [
    ("Careers", "/careers/"), ("Business", "/business/"), ("Technology", "/technology/"),
    ("Economics", "/economics/"), ("Operating Room", "/psychiatry-operating-room/"),
    ("Decoder", "/decoder/"), ("State of Psychiatry", "/state-of-psychiatry/"),
]
_real_v2.FOOTER_COLS = [
    ("Sections", [("Careers", "/careers/"), ("Business", "/business/"), ("Technology", "/technology/"),
                  ("Economics", "/economics/"), ("Culture", "/culture/"), ("Leadership", "/leadership/"), ("Innovation", "/innovation/")]),
    ("Read", [("The Psychiatry Operating Room", "/psychiatry-operating-room/"), ("Psychiatry Decoder", "/decoder/"),
              ("State of Psychiatry", "/state-of-psychiatry/"), ("Research Digest", "/research-digest/"),
              ("Reports", "/reports/"), ("Interviews", "/interviews/"), ("Opinion", "/opinion/"), ("Tools", "/tools/"), ("Start Here", "/start-here/")]),
    ("About", [("About shrinkiatry", "/about/"), ("Editorial standards", "/editorial-standards/"), ("Editorial team", "/editorial-team/"),
               ("How we build content", "/how-we-build-content/"), ("Evidence methodology", "/evidence-methodology/"), ("Contact", "/contact/")]),
    ("Legal", [("Medical disclaimer", "/medical-disclaimer/"), ("Privacy policy", "/privacy/"), ("Terms of use", "/terms-of-use/"),
               ("Accessibility", "/accessibility/"), ("AI use", "/ai-use/"), ("Disclosures", "/disclosures/"), ("Corrections", "/corrections/"), ("Copyright", "/copyright/")]),
]

sys.modules["engine"] = engine_v3
sys.modules["core"] = engine_v3
sys.modules["engine_v2"] = engine_v3
render_document = engine_v3.render_document
SITE = engine_v3.SITE

import home5
import pillars
import content_articles
import or4
import content_tools
import content_legal
import content_decoder
import content_state
import content_legal_x
import seo_enhance
import media_features

PAGES = []
for mod in (home5, pillars, content_articles, or4, content_tools, content_legal, content_decoder, content_state):
    PAGES.extend(mod.PAGES)

_ov = content_legal_x.OVERRIDES
PAGES = [_ov.get(p["slug"], p) for p in PAGES]

seo_enhance.apply(PAGES)
media_features.apply(PAGES)

KW = {
    "": "psychiatry profession, psychiatry careers, psychiatry business, telepsychiatry, AI in psychiatry",
    "careers/how-psychiatry-residency-works": "psychiatry residency, how psychiatry residency works, PGY years, psychiatry training",
    "careers/psychiatrist-vs-psychologist-vs-therapist": "psychiatrist vs psychologist, psychiatrist vs therapist, difference between psychiatrist and psychologist",
    "careers/what-board-certification-means": "board certified psychiatrist, ABPN certification, psychiatry board certification",
    "business/how-private-psychiatry-practices-work": "private psychiatry practice, psychiatry practice management, starting a psychiatry practice",
    "business/cash-pay-vs-insurance": "cash pay psychiatry, out of network psychiatrist, psychiatry and insurance",
    "business/why-documentation-shapes-care": "psychiatry documentation, clinical notes, pajama time, EHR burden",
    "business/why-controlled-substances-are-different": "controlled substances psychiatry, stimulant prescribing rules, benzodiazepine, DEA telemedicine",
    "technology/what-telepsychiatry-changes": "telepsychiatry, online psychiatrist, telehealth psychiatry",
    "technology/ai-in-psychiatry": "AI in psychiatry, ambient AI scribe, mental health AI",
    "culture/burnout-in-psychiatry": "psychiatrist burnout, physician burnout, psychiatry wellbeing",
    "economics/the-psychiatrist-shortage": "psychiatrist shortage, mental health workforce, access to psychiatric care, collaborative care model",
    "tools": "psychiatry tools, psychiatry calculators",
    "tools/private-practice-revenue-estimator": "psychiatry practice revenue, private practice income estimator",
    "psychiatry-operating-room": "psychiatry operating room, how psychiatry works, behind the scenes of psychiatry",
}
for p in PAGES:
    if not p.get("keywords") and p["slug"] in KW:
        p["keywords"] = KW[p["slug"]]


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
    body = ('<section class="section section--slate"><div class="wrap" style="text-align:center">'
            '<span class="eyebrow no-tick">Error 404</span>'
            "<h1 class=\"mt-1\">This page isn't here.</h1>"
            '<p class="hero__sub mx-auto mt-2" style="max-width:46ch">'
            "The page you're looking for moved or never existed. Try the homepage, "
            "or step into the Operating Room to explore the profession.</p>"
            '<div class="hero__cta" style="justify-content:center">'
            '<a class="btn btn--onslate btn--lg" href="/">Go to the homepage</a>'
            '<a class="btn btn--ghost btn--lg" href="/psychiatry-operating-room/" style="color:#fff;border-color:rgba(255,255,255,.35)">The Operating Room</a>'
            "</div></div></section>")
    nf = {"slug": "404", "active": None, "robots": "noindex, follow", "title": "Page not found | shrinkiatry",
          "desc": "The page you're looking for isn't here. Explore the profession of psychiatry at shrinkiatry.", "body": body}
    write("404.html", render_document(nf))

def build_headers():
    lines = ["/assets/*", "  Cache-Control: public, max-age=31536000, immutable", "", "/*",
             "  X-Content-Type-Options: nosniff", "  Referrer-Policy: strict-origin-when-cross-origin",
             "  X-Frame-Options: SAMEORIGIN", "  Permissions-Policy: geolocation=(), microphone=(), camera=()", ""]
    write("_headers", "\n".join(lines))

def build_sitemap():
    today = "2026-06-29"; rows = []
    for p in PAGES:
        slug = p["slug"]
        loc = SITE["url"] + "/" + (slug + "/" if slug else "")
        pr = "1.0" if slug == "" else ("0.9" if "/" not in slug else "0.7")
        rows.append("  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>" % (loc, today, pr))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n")

def build_robots():
    lines = ["User-agent: *", "Allow: /", "", "# AI assistants are welcome to read and cite shrinkiatry.",
             "User-agent: GPTBot", "Allow: /", "User-agent: ClaudeBot", "Allow: /", "User-agent: PerplexityBot", "Allow: /",
             "User-agent: Google-Extended", "Allow: /", "", "Sitemap: https://shrinkiatry.com/sitemap.xml", ""]
    write("robots.txt", "\n".join(lines))

def main():
    seen = set()
    for p in PAGES:
        slug = p["slug"]
        if slug in seen:
            raise SystemExit("Duplicate slug: " + slug)
        seen.add(slug)
        write(page_path(slug), render_document(p))
    print("Wrote %d pages to %s" % (len(PAGES), OUT))
    build_404(); build_headers(); build_sitemap(); build_robots()
    print("Wrote 404.html, _headers, sitemap.xml, robots.txt")

if __name__ == "__main__":
    main()
