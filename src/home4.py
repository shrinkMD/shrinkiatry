# -*- coding: utf-8 -*-
"""Homepage v4: showpiece animated hero + redesigned sections."""
import engine as S

HERO_IMG = ("https://d8j0ntlcm91z4.cloudfront.net/user_3EbtPZagpCp9mIUJbMMZKZ0oURN/"
            "hf_20260627_041526_5f26dd36-c2bb-4092-b1a1-7d47da05d492.png")

SPARK = ('<svg class="hero__spark" viewBox="0 0 100 100" aria-hidden="true">'
         '<defs><linearGradient id="skSpark" x1="0" y1="0" x2="1" y2="1">'
         '<stop offset="0" stop-color="#e7a93f"/><stop offset="1" stop-color="#86b3d1"/>'
         '</linearGradient></defs>'
         '<path d="M50 3 C56 38 62 44 97 50 C62 56 56 62 50 97 C44 62 38 56 3 50 C38 44 44 38 50 3 Z" '
         'fill="url(#skSpark)"/></svg>')

MEDALLION = ('<svg class="hero__medallion" viewBox="0 0 100 100" aria-hidden="true">'
             '<defs><linearGradient id="skCoin" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0" stop-color="#454654"/><stop offset="1" stop-color="#1d1f27"/>'
             '</linearGradient></defs>'
             '<circle cx="50" cy="50" r="46" fill="url(#skCoin)" stroke="#86b3d1" stroke-width="2"/>'
             '<circle cx="50" cy="50" r="38" fill="none" stroke="rgba(231,169,63,.55)" stroke-width="1.4"/>'
             '<text x="50" y="67" text-anchor="middle" font-family="Georgia,serif" font-size="48" fill="#f4f2ed">s</text>'
             '<circle cx="70" cy="62" r="4.6" fill="#e7a93f"/></svg>')

DOTS = ('<span class="hero__dot"></span><span class="hero__dot b"></span>'
        '<span class="hero__dot"></span><span class="hero__dot b"></span><span class="hero__dot"></span>')

def _picks():
    cards = [
        S.card("How psychiatry residency actually works",
               "Four years, the PGY ladder, what each year trains, and why the first year looks like internal medicine.",
               "/careers/how-psychiatry-residency-works/", tag="Careers", tagclass="tag--blue"),
        S.card("Psychiatrist, psychologist, therapist: the real differences",
               "Different training, different tools, different scope. Why the words aren't interchangeable, and where they overlap.",
               "/careers/psychiatrist-vs-psychologist-vs-therapist/", tag="Careers", tagclass="tag--blue"),
        S.card("What telepsychiatry changes, and what it doesn't",
               "Access went up. The exam, the rules, and the clinical judgment mostly stayed the same. A clear look at both.",
               "/technology/what-telepsychiatry-changes/", tag="Technology", tagclass="tag--blue"),
    ]
    return S.card_grid(cards, 3)

def _sections():
    cards = [
        S.card("Careers", "Training, residency, fellowships, subspecialties, compensation, and the many shapes a psychiatry career can take.", "/careers/", more="Explore"),
        S.card("Business", "Starting and running a practice: cash-pay and insurance, operations, documentation, credentialing, and growth.", "/business/", more="Explore"),
        S.card("Technology", "Telepsychiatry, EHRs, ambient documentation, and artificial intelligence in clinical work.", "/technology/", more="Explore"),
        S.card("Economics", "The workforce shortage, reimbursement, supply and demand, and the money behind mental health care.", "/economics/", more="Explore"),
        S.card("Culture", "History, ethics, public perception, professional identity, and how psychiatry shows up in the wider world.", "/culture/", more="Explore"),
        S.card("Innovation", "Where the field is heading: measurement-based care, digital therapeutics, precision psychiatry, and more.", "/innovation/", more="Explore"),
    ]
    return S.card_grid(cards, 3)

OR_ROOMS = [
    ("01", "Training", "How psychiatrists are made.", "/careers/how-psychiatry-residency-works/"),
    ("02", "Documentation", "Why the note shapes the care.", "/business/why-documentation-shapes-care/"),
    ("03", "Telepsychiatry", "What the screen changed.", "/technology/what-telepsychiatry-changes/"),
    ("04", "Ethics", "The lines that define the work.", "/ethics/"),
    ("05", "AI and tech", "What's automating, what isn't.", "/technology/ai-in-psychiatry/"),
    ("06", "Burnout", "The cost of the work.", "/culture/burnout-in-psychiatry/"),
]

def _or_mini():
    out = []
    for num, title, desc, href in OR_ROOMS:
        out.append(
            f'<a class="or-mini__card" href="{href}">'
            f'<span class="or-mini__num">Room {num}</span>'
            f'<h3>{title}</h3><p>{desc}</p>'
            f'<span class="arrow">Enter &rarr;</span></a>'
        )
    return '<div class="or-mini">' + "".join(out) + "</div>"

QROWS = [
    ("I want to understand the profession", "/start-here/", "Profession"),
    ("I'm interested in psychiatry training", "/careers/", "Training"),
    ("I want to understand private practice", "/business/", "Business"),
    ("I want to understand telepsychiatry", "/technology/what-telepsychiatry-changes/", "Technology"),
    ("I want to understand ethics", "/ethics/", "Ethics"),
    ("I want behind-the-scenes commentary", "/culture/", "Culture"),
    ("I'm looking for clinical care", "https://shrinkmd.com", "shrinkMD"),
]

def _qcards():
    out = []
    for label, href, tag in QROWS:
        is_ext = href.startswith("http")
        ext = ' target="_blank" rel="noopener noreferrer"' if is_ext else ""
        out.append(
            f'<a class="qcard" href="{href}"{ext}>'
            f'<span class="tag tag--olive">{tag}</span>'
            f'<h3>{label}</h3>'
            f'<span class="go">Go <span class="ar">&rarr;</span></span></a>'
        )
    return '<div class="qgrid">' + "".join(out) + "</div>"

BODY = """
<section class="hero hero--xl">
<div class="hero__bg" aria-hidden="true">
<span class="hero__blob hero__blob--amber"></span>
<span class="hero__blob hero__blob--blue"></span>
<span class="hero__gridlines"></span>
__DOTS__
</div>
<div class="wrap"><div class="hero__grid">
<div class="hero__col">
<span class="eyebrow">Part of The Shrink Network</span>
<h1>The profession.<br><span class="hero__accent">Understood.</span></h1>
<p class="hero__sub">shrinkiatry explains the profession behind psychiatric care: how psychiatrists are trained, how practices run, how technology is changing the work, and what the public rarely sees behind the clinical encounter.</p>
<div class="hero__cta">
<a class="btn btn--onslate btn--lg" href="/start-here/">Start here</a>
<a class="btn btn--ghost btn--lg" href="/psychiatry-operating-room/" style="color:#fff;border-color:rgba(255,255,255,.35)">Explore the profession</a>
</div>
<ul class="hero__chips">
<li>Reviewed by a board-certified psychiatrist</li>
<li>Every claim sourced</li>
<li>No ads, nothing for sale</li>
</ul>
</div>
<div class="hero__art">
<span class="hero__glow" aria-hidden="true"></span>
__SPARK__
<figure class="hero__media">
<img src="__HERO__" width="800" height="600" alt="A psychiatrist's desk during a telepsychiatry session: an open laptop showing a softly blurred video call, a notebook and fountain pen, and a coffee mug in soft window light." loading="eager" onerror="this.style.display='none'">
</figure>
__MEDALLION__
<div class="hero__stat hero__stat--a"><strong>48</strong><span>months of residency</span></div>
<div class="hero__stat hero__stat--b"><strong>10</strong><span>rooms in the OR</span></div>
</div>
</div></div>
<a class="hero__scroll" href="#why-exists" aria-label="Scroll to content"><span>Scroll</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></a>
</section>

<section class="section section--surface" id="why-exists"><div class="wrap">
<div class="maxread center">
<span class="eyebrow no-tick">Why shrinkiatry exists</span>
<h2>Psychiatry is more than the appointment.</h2>
<p class="lede mt-2">Most people only ever see the clinical encounter. But psychiatry is shaped by training, ethics, documentation, business models, medication rules, technology, access barriers, professional culture, and the realities of modern healthcare. shrinkiatry exists to explain the profession behind the care, clearly and from the inside.</p>
</div>
</div></section>

<section class="section section--tint"><div class="wrap">
<span class="eyebrow">Editor's picks</span>
<h2 class="mt-1">Start with these.</h2>
<div class="mt-3">__PICKS__</div>
</div></section>

<section class="section section--slate or-promo"><div class="wrap">
<div class="hero__grid" style="align-items:center">
<div>
<span class="eyebrow">The flagship</span>
<h2 class="mt-1">The Psychiatry Operating Room</h2>
<p class="mt-2" style="color:#d7d4cd;font-size:1.15rem;max-width:42ch">The decisions, systems, and habits that usually stay behind the scenes: how psychiatric judgment is made, how psychiatrists are trained, how practices operate, how documentation shapes care, and how the field is changing. Ten rooms, one map of the profession.</p>
<a class="btn btn--onslate btn--lg mt-3" href="/psychiatry-operating-room/">Enter the Operating Room &rarr;</a>
</div>
__ORMINI__
</div>
</div></section>

<section class="section section--surface"><div class="wrap">
<span class="eyebrow">Explore the profession</span>
<h2 class="mt-1">Six ways into the work.</h2>
<div class="mt-3">__SECTIONS__</div>
</div></section>

<section class="section section--slate"><div class="wrap">
<span class="eyebrow">By the numbers</span>
<h2 class="mt-1" style="max-width:20ch">The profession, in context.</h2>
<div class="stats-strip mt-4">
<div class="stat"><div class="stat__num">48</div><div class="stat__label">Months of residency required to train a psychiatrist, per ACGME</div></div>
<div class="stat"><div class="stat__num">~137M</div><div class="stat__label">Americans living in a federally designated mental health shortage area (HRSA)</div></div>
<div class="stat"><div class="stat__num">~32%</div><div class="stat__label">Psychiatrist burnout in 2025 AMA data, among the lower rates in medicine</div></div>
<div class="stat"><div class="stat__num">80+</div><div class="stat__label">Trials supporting the Collaborative Care Model for expanding access</div></div>
</div>
<p class="small mt-3" style="color:#aeb6bd">Figures are sourced and explained on the pages where they appear. See <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a> and <a href="/culture/burnout-in-psychiatry/">burnout in psychiatry</a>.</p>
</div></section>

<section class="section section--tint"><div class="wrap">
<span class="eyebrow">Start here</span>
<h2 class="mt-1">What part of psychiatry are you trying to understand?</h2>
<div class="mt-3">__QCARDS__</div>
</div></section>

<section class="section section--surface"><div class="wrap">
<div class="hero__grid" style="align-items:center">
<div>
<span class="eyebrow">Where shrinkiatry fits</span>
<h2 class="mt-1">The profession layer of The Shrink Network.</h2>
<p class="mt-2 lede">The Shrink Network helps people understand mental health from several angles. Shrinkopedia explains concepts. PsychiatryRx explains medications. AnxietyResource and DepressionResource explain specific conditions. shrinkMD provides clinical care. shrinkiatry explains the profession behind all of it.</p>
<p class="mt-2"><a class="btn btn--ghost" href="https://shrinknetwork.com" target="_blank" rel="noopener noreferrer">See the whole network</a></p>
</div>
<div>__NETCONT__</div>
</div>
</div></section>
"""

BODY = (BODY
        .replace("__DOTS__", DOTS)
        .replace("__HERO__", HERO_IMG)
        .replace("__SPARK__", SPARK)
        .replace("__MEDALLION__", MEDALLION)
        .replace("__PICKS__", _picks())
        .replace("__ORMINI__", _or_mini())
        .replace("__SECTIONS__", _sections())
        .replace("__QCARDS__", _qcards())
        .replace("__NETCONT__", S.network_continue(["shrinkopedia", "psychiatryrx", "shrinkmd", "shariqrefai", "shrinknetwork"], heading="Continue through the network")))

PAGES = [{
    "slug": "",
    "title": "shrinkiatry | The Profession. Understood.",
    "desc": "shrinkiatry explains the profession, culture, business, ethics, training, technology, and behind-the-scenes realities of psychiatry. Part of The Shrink Network.",
    "active": "/",
    "og_type": "website",
    "body": BODY,
}]
