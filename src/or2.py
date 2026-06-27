# -*- coding: utf-8 -*-
"""The Psychiatry Operating Room (clean module, internal note removed)."""
import engine as S

ROOMS = [
    ("01", "Training", "training", "Becoming a psychiatrist",
     "Four years of residency after medical school, built on a fixed sequence the ACGME defines. What each year actually trains.",
     "/careers/how-psychiatry-residency-works/"),
    ("02", "Clinical judgment", "training practice", "How decisions get made",
     "Diagnosis in psychiatry rests on history and observation, not a blood test. How that judgment is formed, and why it isn't guesswork.",
     "/careers/psychiatrist-vs-psychologist-vs-therapist/"),
    ("03", "Documentation", "practice ethics", "The note behind the visit",
     "The clinical note drives billing, liability, continuity, and time. Why it shapes care as much as it records it.",
     "/business/why-documentation-shapes-care/"),
    ("04", "Practice models", "practice", "How practices are built",
     "Solo, group, hospital-employed, hybrid. The structures behind psychiatric care and the tradeoffs baked into each one.",
     "/business/how-private-psychiatry-practices-work/"),
    ("05", "Telepsychiatry", "technology practice", "Care through a screen",
     "What moved online, what the rules now allow, and which parts of the work the screen genuinely changed.",
     "/technology/what-telepsychiatry-changes/"),
    ("06", "Medication systems", "practice ethics", "Prescribing and its rules",
     "Why controlled substances like stimulants and benzodiazepines come with rules that reshape how a whole practice runs.",
     "/business/why-controlled-substances-are-different/"),
    ("07", "Ethics", "ethics", "The lines that define the work",
     "Confidentiality, capacity, consent, boundaries, and the rare duty to act. The ethical structure underneath ordinary visits.",
     "/ethics/"),
    ("08", "Burnout", "wellbeing", "The cost of the work",
     "What national data shows about burnout in psychiatry, where the specialty sits relative to others, and what protects against it.",
     "/culture/burnout-in-psychiatry/"),
    ("09", "AI and technology", "technology", "What's automating, what isn't",
     "Ambient scribes, decision support, and chatbots. A grounded read on what the tools do and where the risks sit.",
     "/technology/ai-in-psychiatry/"),
    ("10", "Private practice", "practice", "Owning the practice",
     "Cash-pay versus insurance, overhead, and the economics that pull psychiatrists toward independent practice.",
     "/business/cash-pay-vs-insurance/"),
]

FILTERS = [
    ("all", "All rooms"),
    ("training", "Training & judgment"),
    ("practice", "Practice & operations"),
    ("technology", "Technology"),
    ("ethics", "Ethics"),
    ("wellbeing", "Wellbeing"),
]

def _cards():
    out = []
    for num, title, tags, stage, desc, href in ROOMS:
        out.append(
            f'<a class="or-card" data-or-card data-or-tags="{tags}" href="{href}">'
            f'<span class="or-card__num">Room {num}</span>'
            f'<h3>{title}</h3><p>{desc}</p>'
            f'<span class="or-card__stage">{stage} &rarr;</span></a>'
        )
    return "".join(out)

def _filters():
    out = []
    for val, label in FILTERS:
        pressed = "true" if val == "all" else "false"
        out.append(f'<button type="button" class="or-filter" data-or-filter="{val}" aria-pressed="{pressed}">{label}</button>')
    return "".join(out)

_itemlist = {
    "@type": "ItemList",
    "name": "The Psychiatry Operating Room",
    "description": "Ten areas of psychiatric practice that usually stay behind the scenes.",
    "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": r[1],
         "url": "https://shrinkiatry.com" + r[5]}
        for i, r in enumerate(ROOMS)
    ],
}

BODY = """
<section class="section section--slate section--tight"><div class="wrap">
<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">The Psychiatry Operating Room</span></nav>
<span class="eyebrow">The flagship</span>
<h1 class="mt-1">The Psychiatry Operating Room</h1>
<p class="hero__sub mt-2" style="max-width:60ch">The decisions, systems, and habits that usually stay behind the scenes. Ten rooms that explain how psychiatric judgment is made, how psychiatrists are trained, how practices run, how documentation shapes care, and how the field is changing. Filter by what you want to understand, then step inside.</p>
</div></section>

<section class="section section--surface"><div class="wrap">
<div class="maxread flow">
<p>Patients see the encounter. They don't see the four years of training that shaped the clinician across from them, the documentation that follows every visit, the prescribing rules that govern a single line on the chart, or the economics that decided how long the appointment would last. The Psychiatry Operating Room opens those rooms one at a time.</p>
<p>Use the filters to narrow by theme, or walk the whole floor one room at a time.</p>
</div>

<div class="or-controls" role="group" aria-label="Filter rooms by theme">__FILTERS__</div>
<p id="or-status" class="sr-only" aria-live="polite">All ten rooms shown.</p>
<div class="or-grid">__CARDS__</div>
</div></section>

<section class="section section--tint"><div class="wrap"><div class="maxread">
__NETCONT__
</div></div></section>
"""

BODY = (BODY.replace("__FILTERS__", _filters())
            .replace("__CARDS__", _cards())
            .replace("__NETCONT__", S.network_continue(["shrinkopedia", "psychiatryrx", "shrinkmd", "shariqrefai", "shrinknetwork"])))

PAGES = [{
    "slug": "psychiatry-operating-room",
    "active": "/psychiatry-operating-room/",
    "title": "The Psychiatry Operating Room | shrinkiatry",
    "desc": "The behind-the-scenes map of psychiatric practice: training, clinical judgment, documentation, practice models, telepsychiatry, medication rules, ethics, burnout, AI, and private practice.",
    "breadcrumbs": [("Home", "/"), ("The Psychiatry Operating Room", None)],
    "schema": [_itemlist],
    "body": BODY,
}]
