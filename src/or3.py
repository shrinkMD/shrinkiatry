# -*- coding: utf-8 -*-
"""The Psychiatry Operating Room, Atlas-level (12 rooms, interactive grid + detail bands)."""
import engine as S

# num, title, tags, stage, card_desc, anchor, deep[(label,href)], what, why, misconception
ROOMS = [
 ("01", "Training", "training", "Becoming a psychiatrist", "room-01",
  "Four years of residency after medical school, in a sequence the ACGME fixes at 48 months, then board certification.",
  [("How psychiatry residency works", "/careers/how-psychiatry-residency-works/"),
   ("What board certification means", "/careers/what-board-certification-means/")],
  "It explains the path from medical school through a residency the Accreditation Council for Graduate Medical Education sets at 48 months, and on into certification by the American Board of Psychiatry and Neurology. Each year trains something specific, from inpatient and emergency work early on to outpatient continuity and subspecialty exposure later.",
  "The length and shape of that training is why a psychiatrist can prescribe, weigh medical causes of psychiatric symptoms, and carry final clinical responsibility for a case. You're not just paying for the visit in front of you. You're getting the years that stand behind it.",
  "That psychiatrists mostly do talk therapy, or that the MD is interchangeable with the other mental-health degrees. The training, the scope, and the legal responsibility are different, even when the work in the room looks similar."),
 ("02", "Clinical judgment", "training", "How decisions get made", "room-02",
  "Diagnosis rests on history, collateral, and observation, not a single blood test. How that judgment is built, and why it isn't guesswork.",
  [("Psychiatrist vs psychologist vs therapist", "/careers/psychiatrist-vs-psychologist-vs-therapist/"),
   ("Look up the concept on Shrinkopedia", "https://shrinkopedia.com")],
  "It explains how a working diagnosis actually forms: from the history a patient gives, the collateral from family or records, the mental status exam, the course over time, and the response to treatment. It's a structured process with criteria behind it, not an impression.",
  "It's why two careful clinicians can land on different working diagnoses early, why follow-up changes the picture, and why a first appointment is a starting hypothesis rather than a verdict. Understanding that makes the pace of psychiatric care make sense.",
  "That the absence of a lab test means the diagnosis is arbitrary. Plenty of medicine runs on pattern, history, and observation. Psychiatry is unusually honest about doing so."),
 ("03", "Documentation", "practice", "The note behind the visit", "room-03",
  "The clinical note is a billing record, a legal document, and a continuity tool all at once. Why it shapes care as much as it records it.",
  [("Why documentation shapes care", "/business/why-documentation-shapes-care/")],
  "It explains what the note actually does. It justifies the billing code, stands as the legal record of what happened, and carries the plan forward to the next visit or the next clinician. Every visit produces one, and the rules for what it must contain are not optional.",
  "Documentation burden is a real force, not a footnote. It drives the after-hours charting clinicians call pajama time, it pulls minutes out of the appointment itself, and it's one of the most cited contributors to burnout. The note shapes the visit, not just the file.",
  "That the note is paperwork done after the fact. In practice it reaches back into the room and changes how long the visit runs and what gets asked."),
 ("04", "Telepsychiatry", "technology practice", "Care through a screen", "room-04",
  "What moved online, what the rules now allow, and which parts of the work the screen genuinely changed.",
  [("What telepsychiatry changes", "/technology/what-telepsychiatry-changes/"),
   ("See the network's telepsychiatry practice, shrinkMD", "https://shrinkmd.com")],
  "It explains what telepsychiatry actually shifted: access for people far from a clinician, the overhead of a physical office, and the geography of who can see whom. It also explains what stayed the same, because the core of a psychiatric visit is a structured conversation that travels well.",
  "Video care reshaped the economics and the reach of psychiatry without gutting the clinical method. Knowing which parts changed, and which didn't, is the difference between hype and an honest read on what virtual care can and can't do.",
  "That video is simply a lesser substitute for in-person care, or the opposite, that everything works equally well remotely. Some problems and some patients need the room. Many don't."),
 ("05", "Ethics", "ethics", "The lines that define the work", "room-05",
  "Confidentiality, capacity, consent, boundaries, and the rare duty to act. The ethical structure underneath ordinary visits.",
  [("Ethics in psychiatry", "/ethics/")],
  "It explains the framework most visits never have to name out loud: who can consent and when, how capacity is assessed, where the boundaries of the relationship sit, what confidentiality protects, and the narrow situations where a clinician may have to act to prevent harm.",
  "These lines decide what a psychiatrist can and cannot do, often invisibly. They're why a clinician asks certain questions, why some information can't be shared even with family, and why the rare exceptions to confidentiality are so tightly defined.",
  "That confidentiality is absolute. It's strong and it's the default, but it has specific, legally defined limits, and good care depends on understanding where they are."),
 ("06", "Medication systems", "practice ethics", "Prescribing and its rules", "room-06",
  "Why controlled substances like stimulants and benzodiazepines come with rules that reshape how a whole practice runs.",
  [("Why controlled substances are different", "/business/why-controlled-substances-are-different/"),
   ("How a specific medication works, on PsychiatryRx", "https://psychiatryrx.org")],
  "It explains how Drug Enforcement Administration scheduling turns a single line on a prescription into a system. Schedule II stimulants and Schedule IV benzodiazepines carry monitoring, refill limits, and telemedicine constraints that ordinary prescriptions don't.",
  "Those rules reshape the whole practice, not just the prescription. They affect how often a patient must be seen, what can be done by video, and how a clinician documents and tracks. The regulation is part of the treatment, whether anyone says so or not.",
  "That prescribing is just picking the right drug. For a large part of psychiatry, it's also navigating a regulatory apparatus that sits on top of the clinical decision."),
 ("07", "Business model", "practice economics", "How practices are built", "room-07",
  "Solo, group, hospital-employed, hybrid. The structures behind psychiatric care, and the tradeoffs baked into each one.",
  [("How private psychiatry practices work", "/business/how-private-psychiatry-practices-work/"),
   ("Cash-pay vs insurance", "/business/cash-pay-vs-insurance/"),
   ("Estimate a practice's revenue", "/tools/private-practice-revenue-estimator/")],
  "It explains the structures care is actually delivered through, and what each one trades away. Solo practice buys autonomy and carries all the overhead. Employment trades control for stability. Group and hybrid models sit in between, each with its own math.",
  "The model quietly sets the things patients feel: how big the panel is, how long a visit runs, whether the practice takes insurance, and who can afford to be seen. The business structure is upstream of the clinical experience.",
  "That a psychiatrist going out of network is simply chasing money. Far more often it's a response to reimbursement rates and administrative load that make in-network solo practice hard to sustain."),
 ("08", "Economics", "economics", "Supply, demand, and access", "room-08",
  "Supply, demand, reimbursement, and the workforce shortage that shapes who can get care and how fast.",
  [("The psychiatrist shortage", "/economics/the-psychiatrist-shortage/")],
  "It explains the economics underneath access: how many psychiatrists there are, where they are, how they're paid, and why demand keeps outrunning supply. Roughly half of the US population lives in a federally designated mental-health workforce shortage area.",
  "Most of the access gap is structural, not a matter of clinicians not caring. Reimbursement, distribution, and the slow pipeline of training all push in the same direction, and they explain waitlists better than individual choices do.",
  "That the shortage is simply about graduating too few psychiatrists. Distribution, pay, and how clinicians are deployed matter at least as much as raw numbers."),
 ("09", "AI and technology", "technology", "What's automating, what isn't", "room-09",
  "Ambient scribes, decision support, and chatbots. A grounded read on what the tools do and where the risks sit.",
  [("AI in psychiatry, an honest read", "/technology/ai-in-psychiatry/")],
  "It explains where technology is actually landing in psychiatry. Ambient documentation tools that draft the note are the nearest-term shift. Decision support and consumer chatbots are noisier, with claims that often run ahead of the evidence.",
  "Sorting the genuine relief from the overstatement matters because the stakes are clinical. A scribe that saves charting time is real and useful. A chatbot presented as a substitute for care is a different thing entirely.",
  "That AI is about to diagnose or replace psychiatrists. The likeliest near-term effect is on the paperwork around the visit, not the judgment inside it."),
 ("10", "Burnout", "wellbeing", "The cost of the work", "room-10",
  "What national surveys show about burnout in psychiatry, where the specialty sits relative to others, and what protects against it.",
  [("Burnout in psychiatry", "/culture/burnout-in-psychiatry/")],
  "It explains what the data on burnout actually says: psychiatry consistently lands in the middle-to-upper range of physician burnout in national surveys, and the drivers are mostly systemic, from documentation load to administrative friction to caseload.",
  "Burnout isn't only a clinician's problem. It feeds turnover and reduced availability, which lands directly on access and quality for patients. The cost of the work becomes a cost of care.",
  "That burnout is personal weakness or a failure of resilience. The strongest evidence points at the system around the clinician, not the clinician's character."),
 ("11", "Patient access", "economics practice", "Why getting seen is hard", "room-11",
  "From network adequacy to geography to cash-pay, the many reasons a first appointment is so hard to get.",
  [("The psychiatrist shortage", "/economics/the-psychiatrist-shortage/"),
   ("Cash-pay vs insurance", "/business/cash-pay-vs-insurance/"),
   ("Get care through shrinkMD", "https://shrinkmd.com")],
  "It explains why access is the bottleneck the rest of the system runs into. Thin insurance networks, uneven geography, the cash-pay shift, and the workforce shortage all stack on top of each other to make a simple appointment surprisingly hard to secure.",
  "Access is where every other room shows up at once. Training pipelines, business models, reimbursement, and technology all converge on one question for a patient: can I actually be seen, and when?",
  "That access is only about cost. Cost is one barrier. Network design, distribution, and sheer supply are often the bigger ones."),
 ("12", "Future of psychiatry", "technology economics", "Where the field is heading", "room-12",
  "Measurement-based care, collaborative care, digital tools, and the shifts that will decide whether access and quality improve together.",
  [("Innovation in psychiatry", "/innovation/"),
   ("AI in psychiatry", "/technology/ai-in-psychiatry/")],
  "It explains the changes most likely to shape the next decade: measurement-based care that tracks outcomes systematically, the collaborative care model that embeds psychiatry into primary care, and the digital tools layering on top of both.",
  "These shifts decide whether access and quality move together or apart. The promising direction integrates psychiatry into the systems people already touch, rather than waiting for a single breakthrough to fix everything.",
  "That the future arrives as one dramatic invention. In practice it looks like changes to how care is organized, paid for, and measured, which are less cinematic and more consequential."),
]

FILTERS = [
 ("all", "All rooms"),
 ("training", "Training & judgment"),
 ("practice", "Practice & operations"),
 ("technology", "Technology & AI"),
 ("economics", "Economics & access"),
 ("ethics", "Ethics"),
 ("wellbeing", "Wellbeing"),
]

def _cards():
    out = []
    for num, title, tags, stage, desc, anchor, deep, what, why, mis in ROOMS:
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
    for i, (num, title, tags, stage, desc, anchor, deep, what, why, mis) in enumerate(ROOMS):
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
         "url": "https://shrinkiatry.com/psychiatry-operating-room/#" + r[5]}
        for i, r in enumerate(ROOMS)
    ],
}

_sources = [
    ("Accreditation Council for Graduate Medical Education, Program Requirements for Psychiatry (residency length and structure).", "https://www.acgme.org/specialties/psychiatry/"),
    ("American Board of Psychiatry and Neurology, certification and continuing certification.", "https://www.abpn.com/"),
    ("American Psychiatric Association, professional practice and the collaborative care model.", "https://www.psychiatry.org/"),
    ("Health Resources and Services Administration, designated Health Professional Shortage Areas for mental health.", "https://data.hrsa.gov/topics/health-workforce/shortage-areas"),
    ("US Drug Enforcement Administration, Diversion Control Division, controlled-substance scheduling and telemedicine prescribing.", "https://www.deadiversion.usdoj.gov/"),
    ("American Medical Association, physician burnout research and resources.", "https://www.ama-assn.org/practice-management/physician-health"),
]

INTRO = """
<p>Patients see the encounter. They don't see the four years of training that shaped the clinician across from them, the documentation that follows every visit, the prescribing rules that govern a single line on the chart, or the economics that decided how long the appointment would last. The Psychiatry Operating Room opens those rooms one at a time.</p>
<p>Think of it as a map of the profession behind the care. Twelve rooms, each one a system that runs underneath an ordinary psychiatric visit. Some are about how a psychiatrist is made and how judgment gets formed. Some are about how a practice is built, paid, and regulated. Some are about where the field is strained, and where it's heading. Together they're the part of psychiatry that's usually kept off the page.</p>
<p>Filter the floor by what you want to understand, then step into a room. Each one explains what it covers, why it matters, the misconception people most often carry into it, and where to read further, both here on shrinkiatry and across The Shrink Network. None of this is medical advice. It's a guide to how the profession actually works.</p>
"""

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
