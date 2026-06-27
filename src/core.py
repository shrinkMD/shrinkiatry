# -*- coding: utf-8 -*-
"""shrinkiatry.com engine + pillar framework (fresh module; mount-safe clone of engine)."""
import json

SITE = {
    "url": "https://shrinkiatry.com",
    "brand": "shrinkiatry",
    "tagline": "The profession. Understood.",
    "email": "support@shrinkiatry.com",
    "publisher": "shrinkMD Publishing, LLC",
    "reviewer": "Shariq Refai, MD, MBA",
    "year": "2026",
    "og_image": "https://shrinkiatry.com/opengraph.jpg",
}

NAV = [
    ("Careers", "/careers/"),
    ("Business", "/business/"),
    ("Technology", "/technology/"),
    ("Economics", "/economics/"),
    ("Culture", "/culture/"),
    ("Innovation", "/innovation/"),
    ("Operating Room", "/psychiatry-operating-room/"),
]

FOOTER_COLS = [
    ("Sections", [("Careers", "/careers/"), ("Business", "/business/"), ("Technology", "/technology/"),
                  ("Economics", "/economics/"), ("Culture", "/culture/"), ("Leadership", "/leadership/"),
                  ("Innovation", "/innovation/")]),
    ("Read", [("The Psychiatry Operating Room", "/psychiatry-operating-room/"), ("Research Digest", "/research-digest/"),
              ("Reports", "/reports/"), ("Interviews", "/interviews/"), ("Opinion", "/opinion/"),
              ("Tools", "/tools/"), ("Start Here", "/start-here/")]),
    ("About", [("About shrinkiatry", "/about/"), ("Editorial standards", "/editorial-standards/"),
               ("Editorial team", "/editorial-team/"), ("How we build content", "/how-we-build-content/"),
               ("Evidence methodology", "/evidence-methodology/"), ("Contact", "/contact/")]),
    ("Legal", [("Medical disclaimer", "/medical-disclaimer/"), ("Privacy policy", "/privacy/"),
               ("Terms of use", "/terms-of-use/"), ("Accessibility", "/accessibility/"), ("AI use", "/ai-use/"),
               ("Disclosures", "/disclosures/"), ("Corrections", "/corrections/"), ("Copyright", "/copyright/")]),
]

NETWORK_GROUPS = [
    ("Understand", [("Shrinkopedia", "https://shrinkopedia.com"), ("Shrinktionary", "https://shrinktionary.com"),
                    ("AnxietyResource", "https://anxietyresource.org"), ("DepressionResource", "https://depressionresource.org"),
                    ("AnxietyResearch", "https://anxietyresearch.org"), ("PsychiatryRx", "https://psychiatryrx.org")]),
    ("Apply", [("shrinQ", "https://shrinq.com"), ("Unstuck", "https://beunstuck.app"), ("QuitScrolling", "https://quitscrolling.app")]),
    ("Care", [("shrinkMD", "https://shrinkmd.com")]),
    ("Profession", [("shrinkiatry", "/"), ("Shariq Refai", "https://shariqrefai.com")]),
]

NETWORK_LINKS = [
    ("About the network", "https://shrinknetwork.com/"),
    ("Network editorial standards", "https://shrinknetwork.com/editorial-standards/"),
    ("Crisis and safety", "https://shrinknetwork.com/crisis/"),
    ("Contact", "https://shrinknetwork.com/contact/"),
]

NET = {
    "shrinkopedia": ("Shrinkopedia", "https://shrinkopedia.com", "Look up the clinical concept itself, explained in depth."),
    "psychiatryrx": ("PsychiatryRx", "https://psychiatryrx.org", "How a specific medication works, and what to expect."),
    "anxietyresource": ("AnxietyResource", "https://anxietyresource.org", "Plain-language education about anxiety for the public."),
    "depressionresource": ("DepressionResource", "https://depressionresource.org", "A long-form library for understanding depression."),
    "anxietyresearch": ("AnxietyResearch", "https://anxietyresearch.org", "What the evidence on anxiety actually says."),
    "shrinkmd": ("shrinkMD", "https://shrinkmd.com", "Independent multistate telepsychiatry care with one clinician."),
    "shariqrefai": ("Shariq Refai", "https://shariqrefai.com", "The perspective and background of the psychiatrist behind the network."),
    "shrinknetwork": ("The Shrink Network", "https://shrinknetwork.com", "How the whole ecosystem fits together."),
    "shrinktionary": ("Shrinktionary", "https://shrinktionary.com", "Plain-language definitions of the terms behind the field."),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def ext(url):
    return ' target="_blank" rel="noopener noreferrer"'

def card(title, desc, href, tag=None, tagclass="", more="Read"):
    is_ext = href.startswith("http")
    tag_html = f'<span class="tag {tagclass}">{tag}</span>' if tag else ""
    more_html = f'<span class="card__more">{more} &rarr;</span>' if more else ""
    a = f'<a class="card card--link" href="{href}"{ext(href) if is_ext else ""}>'
    return f'{a}{tag_html}<h3>{title}</h3><p>{desc}</p>{more_html}</a>'

def card_grid(cards, cols=3):
    return f'<div class="grid grid-{cols}">' + "".join(cards) + "</div>"

def breadcrumb(trail):
    parts = []
    for label, href in trail:
        parts.append(f'<a href="{href}">{label}</a>' if href else f'<span aria-current="page">{label}</span>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + '<span aria-hidden="true">/</span>'.join(parts) + '</nav>'

def sources_block(items):
    lis = []
    for text, url in items:
        if url:
            lis.append(f'<li>{text} <a href="{url}"{ext(url)}>{url}</a></li>')
        else:
            lis.append(f'<li>{text}</li>')
    return '<section class="sources" aria-labelledby="sources-h"><h2 id="sources-h">Sources</h2><ol>' + "".join(lis) + "</ol></section>"

def reviewer_card(date="June 27, 2026", note=None):
    note = note or ("This page is professional commentary and education about the practice of psychiatry. "
                    "It isn't medical advice, and reading it doesn't create a doctor-patient relationship.")
    return ('<aside class="reviewer" aria-label="Reviewer"><div class="reviewer__avatar" aria-hidden="true">SR</div>'
            '<div><div class="reviewer__name">Written or reviewed by Shariq Refai, MD, MBA</div>'
            '<div class="reviewer__role">Board-certified psychiatrist &middot; Founder of shrinkMD &middot; '
            f'Last reviewed {date}</div><p>{note}</p></div></aside>')

def network_continue(keys, heading="Continue through The Shrink Network"):
    lis = []
    for k in keys:
        name, url, desc = NET[k]
        is_ext = url.startswith("http")
        lis.append(f'<li><a href="{url}"{ext(url) if is_ext else ""}><span class="nc-site">{name} &rarr;</span> '
                   f'<span class="nc-desc">{desc}</span></a></li>')
    return (f'<aside class="network-continue" aria-labelledby="nc-h"><span class="eyebrow" id="nc-h">{heading}</span>'
            f'<ul>' + "".join(lis) + "</ul></aside>")

def disclaimer_box():
    return ('<div class="disclaimer-box"><strong>Educational and professional commentary only.</strong> '
            'shrinkiatry explains the profession of psychiatry. It doesn\'t provide medical advice, isn\'t a substitute '
            'for evaluation or treatment by a licensed clinician, and reading it doesn\'t create a doctor-patient '
            'relationship. If you\'re looking for psychiatric care, '
            '<a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network\'s clinical practice.</div>')

# ---- Pillar components ----

def why_trust_box():
    items = [
        ('Written or reviewed by <a href="/editorial-team/">Shariq Refai, MD, MBA</a>, a board-certified psychiatrist'),
        ('Held to documented <a href="/editorial-standards/">editorial standards</a>'),
        ('Open <a href="/corrections/">corrections policy</a>'),
        ('Documented <a href="/evidence-methodology/">evidence methodology</a>'),
        ('Transparent <a href="/ai-use/">AI use</a>'),
        ('Independent and ad-free, with interests <a href="/disclosures/">disclosed</a>'),
        ('Education and commentary, not medical advice. <a href="/medical-disclaimer/">Read the disclaimer</a>'),
    ]
    lis = "".join(f'<li>{i}</li>' for i in items)
    return ('<aside class="why-trust" aria-labelledby="wt-h"><span class="eyebrow no-tick" id="wt-h">Why trust this page</span>'
            f'<ul class="why-trust__list">{lis}</ul></aside>')

def review_panel(meta):
    rows = [
        ("Reviewer", '<a href="/editorial-team/">Shariq Refai, MD, MBA</a>, board-certified psychiatrist'),
        ("Evidence basis", meta.get("evidence", "Accreditation and certification bodies, federal data, professional associations, and peer-reviewed research")),
        ("Published", meta.get("published", "June 2026")),
        ("Last reviewed", meta.get("updated", "June 27, 2026")),
        ("Review status", "Reviewed and published"),
    ]
    dts = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    return ('<aside class="review-panel" aria-labelledby="rp-h"><span class="eyebrow no-tick" id="rp-h">Review panel</span>'
            f'<dl class="review-panel__grid">{dts}</dl>'
            '<p class="small muted">Read <a href="/how-we-build-content/">how shrinkiatry builds and reviews its content</a>.</p></aside>')

def related_cluster(items, heading="Related on shrinkiatry"):
    if not items:
        return ""
    pills = "".join(f'<a class="relpill" href="{h}">{l}</a>' for l, h in items)
    return (f'<section class="related-cluster" aria-labelledby="rel-h"><h2 id="rel-h">{heading}</h2>'
            f'<div class="relpills">{pills}</div></section>')

def article_shell(meta):
    crumbs = breadcrumb(meta["breadcrumbs"])
    kicker = f'<span class="eyebrow">{meta["kicker"]}</span>' if meta.get("kicker") else ""
    metaline = (f'<div class="article__meta"><span>By {SITE["reviewer"]}</span>'
                f'<span>&middot;</span><span>Reviewed {meta.get("updated","June 27, 2026")}</span>'
                f'<span>&middot;</span><span>{meta.get("reading_time","8 min read")}</span></div>')
    qa = (f'<div class="quickanswer"><span class="eyebrow">In plain English</span><p>{meta["quick_answer"]}</p></div>'
          if meta.get("quick_answer") else "")
    tk = ""
    if meta.get("takeaways"):
        lis = "".join(f"<li>{t}</li>" for t in meta["takeaways"])
        tk = f'<section class="keytakeaways" aria-labelledby="kt-h"><h2 id="kt-h">Key takeaways</h2><ul>{lis}</ul></section>'
    toc = ""
    if meta.get("toc"):
        lis = "".join(f'<li><a href="#{i}">{l}</a></li>' for i, l in meta["toc"])
        toc = f'<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>{lis}</ol></nav>'
    faq = ""
    if meta.get("faq"):
        items = "".join(f'<h3>{q}</h3><p>{a}</p>' for q, a in meta["faq"])
        faq = f'<h2 id="faq">Common questions</h2>{items}'
    rel = related_cluster(meta.get("related"))
    src = sources_block(meta["sources"]) if meta.get("sources") else ""
    net = network_continue(meta["network"]) if meta.get("network") else ""

    head = (f'<header class="article__head">{crumbs}{kicker}<h1>{meta["title"]}</h1>'
            f'<p class="lede">{meta["lede"]}</p>{metaline}</header>')
    intro = "".join(x for x in [why_trust_box(), toc, qa, tk] if x)
    body = (f'<div class="article__body flow">{intro}{meta["body"]}{faq}{rel}'
            f'<hr>{src}'
            f'<div class="mt-3">{review_panel(meta)}</div>'
            f'<div class="mt-3">{reviewer_card(meta.get("updated","June 27, 2026"))}</div>'
            f'<div class="mt-3">{net}</div>'
            f'<div class="mt-3">{disclaimer_box()}</div></div>')
    return f'<article class="article"><div class="wrap">{head}{body}</div></article>'


# ---- JSON-LD ----

def _jsonld_org():
    return {"@type": "Organization", "@id": "https://shrinkiatry.com/#org", "name": "shrinkiatry",
            "url": "https://shrinkiatry.com/", "logo": "https://shrinkiatry.com/assets/img/logo.png",
            "publisher": {"@type": "Organization", "name": "shrinkMD Publishing, LLC"},
            "parentOrganization": {"@type": "Organization", "name": "The Shrink Network", "url": "https://shrinknetwork.com/"},
            "sameAs": ["https://shrinknetwork.com/", "https://shrinkmd.com/"]}

def _jsonld_website():
    return {"@type": "WebSite", "@id": "https://shrinkiatry.com/#website", "name": "shrinkiatry",
            "url": "https://shrinkiatry.com/", "publisher": {"@id": "https://shrinkiatry.com/#org"}, "inLanguage": "en-US"}

def _jsonld_person():
    return {"@type": "Person", "@id": "https://shrinkiatry.com/#refai", "name": "Shariq Refai, MD, MBA",
            "honorificSuffix": "MD, MBA", "jobTitle": "Board-certified psychiatrist", "url": "https://shariqrefai.com/",
            "affiliation": {"@type": "Organization", "name": "shrinkMD"},
            "alumniOf": ["Duke University", "St. George's University School of Medicine"],
            "knowsAbout": ["Psychiatry", "Telepsychiatry", "Medical education", "Physician entrepreneurship"]}

def _jsonld_breadcrumbs(trail):
    items = []
    for i, (label, href) in enumerate(trail, start=1):
        url = "https://shrinkiatry.com" + (href if href else "")
        items.append({"@type": "ListItem", "position": i, "name": label, "item": url if href else None})
    return {"@type": "BreadcrumbList", "itemListElement": [{k: v for k, v in it.items() if v is not None} for it in items]}

def render_head(page):
    title = page["title"]; desc = page["desc"]
    canon = SITE["url"] + "/" + (page["slug"] + "/" if page["slug"] else "")
    canon = canon.replace("//", "/").replace("https:/", "https://")
    og_type = page.get("og_type", "website")
    img = page.get("og_image", SITE["og_image"])
    robots = page.get("robots", "index, follow")
    kw = page.get("keywords")
    kw_tag = f'\n<meta name="keywords" content="{esc(kw)}">' if kw else ""

    graph = [_jsonld_org(), _jsonld_website()]
    if page.get("breadcrumbs"):
        graph.append(_jsonld_breadcrumbs(page["breadcrumbs"]))
    for extra in page.get("schema", []):
        graph.append(extra)
    ld_json = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))

    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">{kw_tag}
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#3b3c46">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="shrinkiatry">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{img}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..600;1,8..60,400&display=swap">
<link rel="stylesheet" href="/assets/css/main.css?v=6">
<script type="application/ld+json">{ld_json}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>"""

def render_header(active=None):
    items = ""
    for label, href in NAV:
        cur = ' aria-current="page"' if active == href else ""
        items += f'<li><a href="{href}"{cur}>{label}</a></li>'
    return f"""
<div class="topbar"><div class="wrap">
<span><strong>shrinkiatry</strong> is professional commentary, not medical advice.</span>
<span>If you need care, <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network's practice.</span>
<span>In crisis? Call or text <strong>988</strong> in the US.</span>
</div></div>
<header class="masthead"><div class="wrap"><div class="masthead__inner">
<a class="brand" href="/">shrinkiatry<span class="dot">.</span><span class="brand__sub">Part of The Shrink Network</span></a>
<button class="iconbtn menu-toggle" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
</button>
<nav class="nav" id="primary-nav" aria-label="Primary">
<ul class="nav__list">{items}
<li class="nav__cta"><a class="btn btn--primary" href="/start-here/">Start Here</a></li>
<li><button class="iconbtn" data-theme-toggle aria-pressed="false" aria-label="Switch to dark mode" title="Toggle theme">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
</button></li>
</ul>
</nav>
</div></div></header>
<div class="nav-backdrop" aria-hidden="true"></div>
<main id="main">"""

def render_footer():
    cols = ""
    for heading, links in FOOTER_COLS:
        lis = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in links)
        cols += f'<div class="footer-col"><h4>{heading}</h4><ul>{lis}</ul></div>'
    groups = ""
    for heading, links in NETWORK_GROUPS:
        lis = "".join(f'<li><a href="{h}"{ext(h) if h.startswith("http") else ""}>{l}</a></li>' for l, h in links)
        groups += f'<div><h4>{heading}</h4><ul>{lis}</ul></div>'
    netlinks = " ".join(f'<a href="{h}" target="_blank" rel="noopener noreferrer">{l}</a>' for l, h in NETWORK_LINKS)
    return f"""</main>
<footer class="site-footer">
<div class="footer-main"><div class="wrap"><div class="footer-top">
<div class="footer-brand">
<a class="brand" href="/">shrinkiatry<span class="dot">.</span></a>
<p>The profession of psychiatry, explained from the inside. Careers, business, technology, economics, culture, and ethics.</p>
</div>
<div class="footer-cols">{cols}</div>
</div></div></div>
<div class="network-bar"><div class="wrap">
<div class="network-bar__head"><span class="brandline">Part of The Shrink Network</span><span class="tagline">Your mind. Understood.</span></div>
<div class="network-groups">{groups}</div>
<div class="network-bar__links">{netlinks}</div>
<p class="network-bar__copy">The Shrink Network is independent. Each site is its own resource with its own purpose. &copy; {SITE['year']} The Shrink Network.</p>
</div></div>
<div class="legal-strip"><div class="wrap">
<p><strong>Educational network only.</strong> shrinkiatry publishes professional commentary and education about the profession of psychiatry. It is general education, not medical advice. It isn't a substitute for evaluation, diagnosis, or treatment by a licensed clinician, and reading it doesn't create a doctor-patient relationship. Read the full <a href="/medical-disclaimer/">medical disclaimer</a>.</p>
<p><strong>If you're in crisis.</strong> Call or text <strong>988</strong> in the US to reach the Suicide and Crisis Lifeline, available 24 hours a day. Call 911 if someone is in immediate danger.</p>
<p><a href="mailto:{SITE['email']}">{SITE['email']}</a> &middot; &copy; {SITE['year']} {SITE['publisher']} &middot; shrinkiatry is written or reviewed by {SITE['reviewer']}, a board-certified psychiatrist.</p>
</div></div>
</footer>
<script src="/assets/js/main.js?v=6" defer></script>
</body>
</html>"""

def render_document(page):
    return render_head(page) + render_header(page.get("active")) + page["body"] + render_footer()
