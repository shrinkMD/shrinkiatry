# -*- coding: utf-8 -*-
"""The Psychiatry Operating Room, Atlas-level. Fixed column order (anchor, desc)."""
import engine as S
from or3 import ROOMS, FILTERS, _sources, INTRO

# ROOMS tuple order: num, title, tags, stage, anchor, desc, deep, what, why, misconception

def _cards():
    out = []
    for num, title, tags, stage, anchor, desc, deep, what, why, mis in ROOMS:
        out.append(
            f'<a class="or-card" data-or-card data-or-tags="{tags}" href="#{anchor}">'
            f'<span class="or-card__num">Room {num}</span>'
            f'<h3>{title}</h3><p>{desc}</p>'
            f'<span class="or-card__stage">{stage} &rarr;</span></a>')
    return "".join(out)

def _filters():
    out = []
    for val, label in FILTERS:
        pressed = "true" if val == "all" else "false"
        out.append(f'<button type="button" class="or-filter" data-or-filter="{val}" aria-pressed="{pressed}">{label}</button>')
    return "".join(out)

def _rooms_detail():
    out = []
    for i, (num, title, tags, stage, anchor, desc, deep, what, why, mis) in enumerate(ROOMS):
        band = "section--surface" if i % 2 == 0 else "section--tint"
        links = ", ".join(
            (f'<a href="{h}"{S.ext(h) if h.startswith("http") else ""}>{l}</a>') for l, h in deep)
        out.append(
            f'<section class="section {band} section--tight" id="{anchor}"><div class="wrap"><div class="maxread flow">'
            f'<span class="eyebrow no-tick">Room {num} &middot; {title}</span>'
            f'<h2 class="mt-1">{stage}</h2>'
            f'<p><strong>What it explains.</strong> {what}</p>'
            f'<p><strong>Why it matters.</strong> {why}</p>'
            f'<p><strong>A common misconception.</strong> {mis}</p>'
            f'<p class="muted small"><strong>Go deeper:</strong> {links}.</p>'
            f'<p><a class="backtop" href="#or-floor">Back to the floor &uarr;</a></p>'
            f'</div></div></section>')
    return "".join(out)

_itemlist = {
    "@type": "ItemList",
    "name": "The Psychiatry Operating Room",
    "description": "Twelve areas of psychiatric practice that usually stay behind the scenes, from training and clinical judgment to economics, access, and the future of the field.",
    "numberOfItems": len(ROOMS),
    "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": r[1],
         "url": "https://shrinkiatry.com/psychiatry-operating-room/#" + r[4]}
        for i, r in enumerate(ROOMS)
    ],
}

BODY = f"""
<section class="section section--slate section--tight"><div class="wrap">
<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">The Psychiatry Operating Room</span></nav>
<span class="eyebrow">The flagship</span>
<h1 class="mt-1">The Psychiatry Operating Room</h1>
<p class="hero__sub mt-2" style="max-width:62ch">The decisions, systems, and habits that usually stay behind the scenes. Twelve rooms that map how psychiatric judgment is made, how psychiatrists are trained, how practices run, how documentation and prescribing shape care, and where the field is under strain. A psychiatrist-led map of the profession behind the care.</p>
</div></section>

<section class="section section--surface" id="or-floor"><div class="wrap">
<div class="maxread flow">{INTRO}</div>
<div class="or-controls" role="group" aria-label="Filter rooms by theme">{_filters()}</div>
<p id="or-status" class="sr-only" aria-live="polite">All twelve rooms shown.</p>
<div class="or-grid">{_cards()}</div>
</div></section>

{_rooms_detail()}

<section class="section section--surface section--tight"><div class="wrap"><div class="maxread flow">
{S.why_trust_box()}
{S.sources_block(_sources)}
<div class="mt-3">{S.review_panel({"evidence": "Accreditation and certification bodies (ACGME, ABPN), professional associations (APA, AMA), and federal data (HRSA, DEA).", "published": "June 2026", "updated": "June 27, 2026"})}</div>
</div></div></section>

<section class="section section--tint"><div class="wrap"><div class="maxread">
{S.network_continue(["shrinkopedia", "psychiatryrx", "shrinktionary", "shrinkmd", "shariqrefai", "shrinknetwork"])}
<div class="mt-3">{S.disclaimer_box()}</div>
</div></div></section>
"""

PAGES = [{
    "slug": "psychiatry-operating-room",
    "active": "/psychiatry-operating-room/",
    "title": "The Psychiatry Operating Room | shrinkiatry",
    "desc": "The behind-the-scenes map of psychiatric practice: training, judgment, documentation, telepsychiatry, ethics, medication rules, AI, and access.",
    "keywords": "psychiatry operating room, how psychiatry works, behind the scenes of psychiatry, psychiatry profession",
    "breadcrumbs": [("Home", "/"), ("The Psychiatry Operating Room", None)],
    "schema": [_itemlist],
    "body": BODY,
}]
