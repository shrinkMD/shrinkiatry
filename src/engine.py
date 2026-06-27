# -*- coding: utf-8 -*-
"""shrinkiatry.com static site engine: config, layout, components."""
import json

SITE = {
    "url": "https://shrinkiatry.com",
    "brand": "shrinkiatry",
    "tagline": "The profession. Understood.",
    "blurb": ("shrinkiatry is the publication about the profession of psychiatry: "
              "careers, training, business, technology, economics, culture, and ethics. "
              "Part of The Shrink Network."),
    "email": "support@shrinkiatry.com",
    "publisher": "shrinkMD Publishing, LLC",
    "reviewer": "Shariq Refai, MD, MBA",
    "year": "2026",
    "og_image": "https://shrinkiatry.com/opengraph.jpg",
}

# Primary navigation
NAV = [
    ("Careers", "/careers/"),
    ("Business", "/business/"),
    ("Technology", "/technology/"),
    ("Economics", "/economics/"),
    ("Culture", "/culture/"),
    ("Innovation", "/innovation/"),
    ("Operating Room", "/psychiatry-operating-room/"),
]

# Footer link columns
FOOTER_COLS = [
    ("Sections", [
        ("Careers", "/careers/"),
        ("Business", "/business/"),
        ("Technology", "/technology/"),
        ("Economics", "/economics/"),
        ("Culture", "/culture/"),
        ("Leadership", "/leadership/"),
        ("Innovation", "/innovation/"),
    ]),
    ("Read", [
        ("The Psychiatry Operating Room", "/psychiatry-operating-room/"),
        ("Research Digest", "/research-digest/"),
        ("Reports", "/reports/"),
        ("Interviews", "/interviews/"),
        ("Opinion", "/opinion/"),
        ("Tools", "/tools/"),
        ("Start Here", "/start-here/"),
    ]),
    ("About", [
        ("About shrinkiatry", "/about/"),
        ("Editorial standards", "/editorial-standards/"),
        ("Editorial team", "/editorial-team/"),
        ("How we build content", "/how-we-build-content/"),
        ("Evidence methodology", "/evidence-methodology/"),
        ("Contact", "/contact/"),
    ]),
    ("Legal", [
        ("Medical disclaimer", "/medical-disclaimer/"),
        ("Privacy policy", "/privacy/"),
        ("Terms of use", "/terms-of-use/"),
        ("Accessibility", "/accessibility/"),
        ("AI use", "/ai-use/"),
        ("Disclosures", "/disclosures/"),
        ("Corrections", "/corrections/"),
        ("Copyright", "/copyright/"),
    ]),
]

# The Shrink Network footer groups (exact network convention)
NETWORK_GROUPS = [
    ("Understand", [
        ("Shrinkopedia", "https://shrinkopedia.com"),
        ("Shrinktionary", "https://shrinktionary.com"),
        ("AnxietyResource", "https://anxietyresource.org"),
        ("DepressionResource", "https://depressionresource.org"),
        ("AnxietyResearch", "https://anxietyresearch.org"),
        ("PsychiatryRx", "https://psychiatryrx.org"),
    ]),
    ("Apply", [
        ("shrinQ", "https://shrinq.com"),
        ("Unstuck", "https://beunstuck.app"),
        ("QuitScrolling", "https://quitscrolling.app"),
    ]),
    ("Care", [
        ("shrinkMD", "https://shrinkmd.com"),
    ]),
    ("Profession", [
        ("shrinkiatry", "/"),
        ("Shariq Refai", "https://shariqrefai.com"),
    ]),
]

NETWORK_LINKS = [
    ("About the network", "https://shrinknetwork.com/"),
    ("Network editorial standards", "https://shrinknetwork.com/editorial-standards/"),
    ("Crisis and safety", "https://shrinknetwork.com/crisis/"),
    ("Contact", "https://shrinknetwork.com/contact/"),
]

# ---- Reusable network-continue link targets ----
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

# =====================================================================
# Components
# =====================================================================

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))

def ext(url):
    """Attributes for external (network) links."""
    return ' target="_blank" rel="noopener noreferrer"'

def card(title, desc, href, tag=None, tagclass="", more="Read"):
    is_ext = href.startswith("http")
    tag_html = f'<span class="tag {tagclass}">{tag}</span>' if tag else ""
    more_html = f'<span class="card__more">{more} &rarr;</span>' if more else ""
    a = f'<a class="card card--link" href="{href}"{ext(href) if is_ext else ""}>'
    return (f'{a}{tag_html}<h3>{title}</h3><p>{desc}</p>{more_html}</a>')

def card_grid(cards, cols=3):
    return f'<div class="grid grid-{cols}">' + "".join(cards) + "</div>"

def breadcrumb(trail):
    """trail = [(label, href), ... , (current_label, None)]"""
    parts = []
    for label, href in trail:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span aria-current="page">{label}</span>')
    sep = '<span aria-hidden="true">/</span>'
    return f'<nav class="breadcrumb" aria-label="Breadcrumb">{sep.join(parts)}</nav>'

def sources_block(items):
    """items = list of (text, url) or (text, None)."""
    lis = []
    for it in items:
        text, url = it
        if url:
            lis.append(f'<li>{text} <a href="{url}"{ext(url)}>{url}</a></li>')
        else:
            lis.append(f'<li>{text}</li>')
    return ('<section class="sources" aria-labelledby="sources-h">'
            '<h2 id="sources-h">Sources</h2><ol>' + "".join(lis) + "</ol></section>")

def reviewer_card(date="June 26, 2026", note=None):
    note = note or ("This article is professional commentary and education about the practice "
                    "of psychiatry. It isn't medical advice, and reading it doesn't create a "
                    "doctor-patient relationship.")
    return (
        '<aside class="reviewer" aria-label="Reviewer">'
        '<div class="reviewer__avatar" aria-hidden="true">SR</div>'
        '<div><div class="reviewer__name">Written or reviewed by Shariq Refai, MD, MBA</div>'
        '<div class="reviewer__role">Board-certified psychiatrist &middot; Founder of shrinkMD &middot; '
        f'Last reviewed {date}</div>'
        f'<p>{note}</p></div></aside>'
    )

def network_continue(keys, heading="Continue through The Shrink Network"):
    lis = []
    for k in keys:
        name, url, desc = NET[k]
        is_ext = url.startswith("http")
        lis.append(
            f'<li><a href="{url}"{ext(url) if is_ext else ""}>'
            f'<span class="nc-site">{name} &rarr;</span> '
            f'<span class="nc-desc">{desc}</span></a></li>'
        )
    return (f'<aside class="network-continue" aria-labelledby="nc-h">'
            f'<span class="eyebrow" id="nc-h">{heading}</span>'
            f'<ul>' + "".join(lis) + "</ul></aside>")

def disclaimer_box():
    return ('<div class="disclaimer-box"><strong>Educational and professional commentary only.</strong> '
            'shrinkiatry explains the profession of psychiatry. It doesn\'t provide medical advice, '
            'isn\'t a substitute for evaluation or treatment by a licensed clinician, and reading it '
            'doesn\'t create a doctor-patient relationship. If you\'re looking for psychiatric care, '
            '<a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> '
            'is the network\'s clinical practice.</div>')

def article_shell(meta):
    """Render a full long-form article from a structured dict.
    meta keys: kicker, title, breadcrumbs, reading_time, updated, quick_answer,
    takeaways(list), toc(list of (id,label)), body(html), faq(list of (q,a)),
    sources(list), network(list of keys)."""
    crumbs = breadcrumb(meta["breadcrumbs"])
    kicker = f'<span class="eyebrow">{meta["kicker"]}</span>' if meta.get("kicker") else ""
    metaline = (f'<div class="article__meta">'
                f'<span>By {SITE["reviewer"]}</span>'
                f'<span>&middot;</span><span>Reviewed {meta.get("updated","June 26, 2026")}</span>'
                f'<span>&middot;</span><span>{meta.get("reading_time","8 min read")}</span></div>')
    qa = ""
    if meta.get("quick_answer"):
        qa = (f'<div class="quickanswer"><span class="eyebrow">In plain English</span>'
              f'<p>{meta["quick_answer"]}</p></div>')
    tk = ""
    if meta.get("takeaways"):
        lis = "".join(f"<li>{t}</li>" for t in meta["takeaways"])
        tk = (f'<section class="keytakeaways" aria-labelledby="kt-h"><h2 id="kt-h">Key takeaways</h2>'
              f'<ul>{lis}</ul></section>')
    toc = ""
    if meta.get("toc"):
        lis = "".join(f'<li><a href="#{i}">{l}</a></li>' for i, l in meta["toc"])
        toc = (f'<nav class="toc" aria-label="On this page"><strong>On this page</strong>'
               f'<ol>{lis}</ol></nav>')
    faq = ""
    if meta.get("faq"):
        items = ""
        for q, a in meta["faq"]:
            items += f'<h3>{q}</h3><p>{a}</p>'
        faq = f'<h2 id="faq">Common questions</h2>{items}'
    src = sources_block(meta["sources"]) if meta.get("sources") else ""
    net = network_continue(meta["network"]) if meta.get("network") else ""

    head = (f'<header class="article__head">{crumbs}{kicker}'
            f'<h1>{meta["title"]}</h1>'
            f'<p class="lede">{meta["lede"]}</p>{metaline}</header>')

    intro_blocks = "".join(x for x in [qa, tk] if x)
    body = (f'<div class="article__body flow">'
            f'{toc}{intro_blocks}{meta["body"]}{faq}'
            f'<hr>{src}'
            f'<div class="mt-3">{reviewer_card(meta.get("updated","June 26, 2026"))}</div>'
            f'<div class="mt-3">{net}</div>'
            f'<div class="mt-3">{disclaimer_box()}</div>'
            f'</div>')
    return f'<article class="article"><div class="wrap">{head}{body}</div></article>'


# =====================================================================
# Document shell
# =====================================================================

def _jsonld_org():
    return {
        "@type": "Organization", "@id": "https://shrinkiatry.com/#org",
        "name": "shrinkiatry", "url": "https://shrinkiatry.com/",
        "logo": "https://shrinkiatry.com/assets/img/logo.png",
        "publisher": {"@type": "Organization", "name": "shrinkMD Publishing, LLC"},
        "parentOrganization": {"@type": "Organization", "name": "The Shrink Network",
                                "url": "https://shrinknetwork.com/"},
        "sameAs": ["https://shrinknetwork.com/", "https://shrinkmd.com/"],
    }

def _jsonld_website():
    return {
        "@type": "WebSite", "@id": "https://shrinkiatry.com/#website",
        "name": "shrinkiatry", "url": "https://shrinkiatry.com/",
        "publisher": {"@id": "https://shrinkiatry.com/#org"},
        "inLanguage": "en-US",
    }

def _jsonld_person():
    return {
        "@type": "Person", "@id": "https://shrinkiatry.com/#refai",
        "name": "Shariq Refai, MD, MBA",
        "honorificSuffix": "MD, MBA",
        "jobTitle": "Board-certified psychiatrist",
        "url": "https://shariqrefai.com/",
        "affiliation": {"@type": "Organization", "name": "shrinkMD"},
        "alumniOf": ["Duke University", "St. George's University School of Medicine"],
        "knowsAbout": ["Psychiatry", "Telepsychiatry", "Medical education",
                        "Physician entrepreneurship"],
    }

def _jsonld_breadcrumbs(trail):
    items = []
    for i, (label, href) in enumerate(trail, start=1):
        url = "https://shrinkiatry.com" + (href if href else "")
        items.append({"@type": "ListItem", "position": i, "name": label,
                      "item": url if href else None})
    return {"@type": "BreadcrumbList", "itemListElement":
            [{k: v for k, v in it.items() if v is not None} for it in items]}

def render_head(page):
    title = page["title"]
    desc = page["desc"]
    canon = SITE["url"] + "/" + (page["slug"] + "/" if page["slug"] else "")
    canon = canon.replace("//", "/").replace("https:/", "https://")
    og_type = page.get("og_type", "website")
    img = page.get("og_image", SITE["og_image"])
    robots = page.get("robots", "index, follow")

    graph = [_jsonld_org(), _jsonld_website()]
    if page.get("breadcrumbs"):
        graph.append(_jsonld_breadcrumbs(page["breadcrumbs"]))
    for extra in page.get("schema", []):
        graph.append(extra)
    ld = {"@context": "https://schema.org", "@graph": graph}
    ld_json = json.dumps(ld, ensure_ascii=False, separators=(",", ":"))

    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
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
<link rel="stylesheet" href="/assets/css/main.css?v=3">
<script type="application/ld+json">{ld_json}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>"""

def render_header(active=None):
    items = []
    for label, href in NAV:
        cur = ' aria-current="page"' if active == href else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    nav_items = "".join(items)
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
<ul class="nav__list">{nav_items}
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
        lis = ""
        for l, h in links:
            is_ext = h.startswith("http")
            lis += f'<li><a href="{h}"{ext(h) if is_ext else ""}>{l}</a></li>'
        groups += f'<div><h4>{heading}</h4><ul>{lis}</ul></div>'

    netlinks = " ".join(
        f'<a href="{h}" target="_blank" rel="noopener noreferrer">{l}</a>'
        for l, h in NETWORK_LINKS)

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
<script src="/assets/js/main.js?v=3" defer></script>
</body>
</html>"""

def render_document(page):
    return (render_head(page)
            + render_header(page.get("active"))
            + page["body"]
            + render_footer())
