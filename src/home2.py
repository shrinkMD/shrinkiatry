# -*- coding: utf-8 -*-
"""Homepage (clean module)."""
import engine as S

HERO_IMG = ("https://d8j0ntlcm91z4.cloudfront.net/user_3EbtPZagpCp9mIUJbMMZKZ0oURN/"
            "hf_20260627_041526_5f26dd36-c2bb-4092-b1a1-7d47da05d492.png")

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

def _start_here_cards():
    rows = [
        ("I want to understand the profession", "/start-here/", "Profession"),
        ("I'm interested in psychiatry training", "/careers/", "Training"),
        ("I want to understand private practice", "/business/", "Business"),
        ("I want to understand telepsychiatry", "/technology/what-telepsychiatry-changes/", "Technology"),
        ("I want to understand ethics", "/ethics/", "Ethics"),
        ("I want behind-the-scenes commentary", "/culture/", "Culture"),
        ("I'm looking for clinical care", "https://shrinkmd.com", "shrinkMD"),
    ]
    return S.card_grid([S.card(l, "", h, tag=t, tagclass="tag--olive", more="Go") for l, h, t in rows], 3)

def _or_cards():
    cards = [
        S.card("Training", "How psychiatrists are made.", "/careers/how-psychiatry-residency-works/", more="Enter"),
        S.card("Documentation", "Why the note shapes the care.", "/business/why-documentation-shapes-care/", more="Enter"),
        S.card("Telepsychiatry", "What the screen changed.", "/technology/what-telepsychiatry-changes/", more="Enter"),
        S.card("Burnout", "The cost of the work.", "/culture/burnout-in-psychiatry/", more="Enter"),
    ]
    return S.card_grid(cards, 4)

BODY = """
<section class="hero"><div class="wrap"><div class="hero__grid">
<div>
<span class="eyebrow">Part of The Shrink Network</span>
<h1>The profession.<br>Understood.</h1>
<p class="hero__sub">shrinkiatry explains the profession behind psychiatric care: how psychiatrists are trained, how practices run, how technology is changing the work, and what the public rarely sees behind the clinical encounter.</p>
<div class="hero__cta">
<a class="btn btn--onslate btn--lg" href="/start-here/">Start here</a>
<a class="btn btn--ghost btn--lg" href="/psychiatry-operating-room/" style="color:#fff;border-color:rgba(255,255,255,.35)">Explore the profession</a>
</div>
</div>
<div>
<figure class="hero__media">
<img src="__HERO__" width="800" height="600" alt="A psychiatrist's desk during a telepsychiatry session: an open laptop showing a softly blurred video call, a notebook and fountain pen, and a coffee mug in soft window light." loading="eager" onerror="this.style.display='none'">
</figure>
</div>
</div></div></section>

<section class="section section--surface"><div class="wrap">
<div class="maxread center">
<span class="eyebrow">Why shrinkiatry exists</span>
<h2>Psychiatry is more than the appointment.</h2>
<p class="lede mt-2">Most people only ever see the clinical encounter. But psychiatry is shaped by training, ethics, documentation, business models, medication rules, technology, access barriers, professional culture, and the realities of modern healthcare. shrinkiatry exists to explain the profession behind the care, clearly and from the inside.</p>
</div>
</div></section>

<section class="section section--tint"><div class="wrap">
<span class="eyebrow">Editor's picks</span>
<h2 class="mt-1">Start with these.</h2>
<div class="mt-3">__PICKS__</div>
</div></section>

<section class="section section--slate"><div class="wrap">
<div class="hero__grid" style="align-items:start">
<div>
<span class="eyebrow">The flagship</span>
<h2 class="mt-1">The Psychiatry Operating Room</h2>
<p class="mt-2" style="color:#d7d4cd;font-size:1.15rem;max-width:42ch">The decisions, systems, and habits that usually stay behind the scenes: how psychiatric judgment is made, how psychiatrists are trained, how practices operate, how documentation shapes care, and how the field is changing. Ten rooms, one map of the profession.</p>
<a class="btn btn--onslate btn--lg mt-3" href="/psychiatry-operating-room/">Enter the Operating Room</a>
</div>
<div>__ORCARDS__</div>
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
<div class="mt-3">__STARTCARDS__</div>
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
        .replace("__HERO__", HERO_IMG)
        .replace("__PICKS__", _picks())
        .replace("__ORCARDS__", _or_cards())
        .replace("__SECTIONS__", _sections())
        .replace("__STARTCARDS__", _start_here_cards())
        .replace("__NETCONT__", S.network_continue(["shrinkopedia", "psychiatryrx", "shrinkmd", "shariqrefai", "shrinknetwork"], heading="Continue through the network")))

PAGES = [{
    "slug": "",
    "title": "shrinkiatry | The Profession. Understood.",
    "desc": "shrinkiatry explains the profession, culture, business, ethics, training, technology, and behind-the-scenes realities of psychiatry. Part of The Shrink Network.",
    "active": "/",
    "og_type": "website",
    "body": BODY,
}]
