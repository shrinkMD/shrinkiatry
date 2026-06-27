# -*- coding: utf-8 -*-
"""Section hub pages."""
import engine as S

def page_hero(kicker, title, lede):
    return f"""<section class="section section--slate section--tight"><div class="wrap">
<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">{title}</span></nav>
<span class="eyebrow">{kicker}</span>
<h1 class="mt-1">{title}</h1>
<p class="hero__sub mt-2" style="max-width:54ch">{lede}</p>
</div></section>"""

def hub(slug, active, kicker, title, lede, intro_html, cards_html, network_keys,
        extra_html="", meta_title=None, desc=None):
    body = (page_hero(kicker, title, lede)
            + f'<section class="section section--surface"><div class="wrap"><div class="maxread flow">{intro_html}</div></div></section>'
            + f'<section class="section section--tint"><div class="wrap">{cards_html}</div></section>'
            + (f'<section class="section section--surface"><div class="wrap">{extra_html}</div></section>' if extra_html else "")
            + f'<section class="section section--tint"><div class="wrap"><div class="maxread">{S.network_continue(network_keys)}</div></div></section>')
    return {
        "slug": slug, "active": active,
        "title": meta_title or f"{title} | shrinkiatry",
        "desc": desc or lede[:155],
        "breadcrumbs": [("Home", "/"), (title, None)],
        "body": body,
    }

PAGES = []

# ---------------- Careers ----------------
PAGES.append(hub(
    "careers", "/careers/", "Careers in psychiatry", "Careers",
    "How a psychiatrist is made, and the many shapes a career in the field can take.",
    "<p>Becoming a psychiatrist is a long, specific path: four years of medical school, then a residency that the Accreditation Council for Graduate Medical Education sets at 48 months, then board certification, then a career that can bend toward private practice, hospital systems, academia, consultation, the military, sports, industry, or telepsychiatry. shrinkiatry's Careers section explains each of those stages plainly, for people inside the pipeline and for anyone trying to understand it.</p>"
    "<p>We don't sell a coaching program or a residency-prep course. The aim is to describe how the profession actually trains and credentials its members, what the work looks like at each stage, and what the choices really involve, so that a medical student, a resident, a journalist, or a curious patient can all read the same page and come away with an accurate picture.</p>",
    S.card_grid([
        S.card("How psychiatry residency actually works", "Four years, the PGY ladder, what each year trains, and the boards at the end.", "/careers/how-psychiatry-residency-works/", tag="Training", tagclass="tag--blue"),
        S.card("Psychiatrist vs psychologist vs therapist", "Different training, different tools, different scope. What separates the roles, and where they overlap.", "/careers/psychiatrist-vs-psychologist-vs-therapist/", tag="The profession", tagclass="tag--blue"),
        S.card("What board certification actually means", "ABPN certification, continuing certification, and what the credential does and doesn't guarantee.", "/careers/what-board-certification-means/", tag="Credentials", tagclass="tag--blue"),
        S.card("The shortage and the job market", "Why demand for psychiatrists outruns supply, and what that means for careers.", "/economics/the-psychiatrist-shortage/", tag="Economics", tagclass="tag--olive"),
        S.card("Private practice as a career", "What it takes to own the practice, not just work in it.", "/business/how-private-psychiatry-practices-work/", tag="Business", tagclass="tag--olive"),
        S.card("Burnout and the shape of a sustainable career", "What the data says about psychiatry's burnout rates, and what protects against it.", "/culture/burnout-in-psychiatry/", tag="Culture", tagclass="tag--olive"),
    ], 3),
    ["shrinkmd", "shariqrefai", "shrinknetwork"],
    desc="How psychiatrists are trained and certified, and the many shapes a psychiatry career can take. Residency, fellowships, board certification, and practice paths, explained.",
))

# ---------------- Business ----------------
PAGES.append(hub(
    "business", "/business/", "The business of psychiatry", "Business",
    "How psychiatric practices are built, paid, and run, without the clinical part getting lost.",
    "<p>A psychiatry practice is a small business with unusual constraints. Visits are time-limited and reimbursed in ways that don't always match the work. Documentation is both a clinical tool and a legal record. Controlled substances bring rules that no other part of the business has to think about. And the founder is usually a physician who was never taught operations, billing, or hiring.</p>"
    "<p>This section explains how the business of psychiatry actually works: cash-pay versus insurance, how private practices are structured, why documentation shapes care as much as it records it, and how the economics push clinicians toward some models and away from others. It's educational, not legal or financial advice, and it's written to be useful to a clinician thinking about going out on their own and to anyone trying to understand why psychiatric care is delivered the way it is.</p>",
    S.card_grid([
        S.card("How private psychiatry practices work", "Structure, payer mix, overhead, and the tradeoffs behind an independent practice.", "/business/how-private-psychiatry-practices-work/", tag="Practice models", tagclass="tag--blue"),
        S.card("Cash-pay vs insurance", "Why so many psychiatrists go out of network, and what that does to access and income.", "/business/cash-pay-vs-insurance/", tag="Payment", tagclass="tag--blue"),
        S.card("Why documentation shapes care", "The note isn't an afterthought. It drives billing, liability, continuity, and time.", "/business/why-documentation-shapes-care/", tag="Operations", tagclass="tag--blue"),
        S.card("Why controlled substances are handled differently", "Stimulants and benzodiazepines come with rules that change how the practice runs.", "/business/why-controlled-substances-are-different/", tag="Compliance", tagclass="tag--olive"),
        S.card("Estimate a practice's revenue", "An educational calculator for visit volume, pricing, and payer mix.", "/tools/private-practice-revenue-estimator/", tag="Tool", tagclass="tag--olive"),
        S.card("Telepsychiatry and the practice model", "How virtual care reshaped overhead, geography, and scheduling.", "/technology/what-telepsychiatry-changes/", tag="Technology", tagclass="tag--olive"),
    ], 3),
    ["psychiatryrx", "shrinkmd", "shrinknetwork"],
    desc="How psychiatric practices are built, paid, and run: cash-pay vs insurance, practice models, documentation, controlled-substance rules, and the economics of independent practice.",
))

# ---------------- Technology ----------------
PAGES.append(hub(
    "technology", "/technology/", "Technology in psychiatry", "Technology",
    "Telepsychiatry, electronic records, ambient documentation, and artificial intelligence, judged on what they actually do.",
    "<p>Psychiatry is, in some ways, the specialty most exposed to technology change. The core encounter is a conversation, which makes it unusually portable to video, unusually easy to record and transcribe, and unusually tempting to automate. That's why telepsychiatry scaled so fast, why ambient documentation tools landed in psychiatry early, and why every claim about artificial intelligence in mental health deserves a careful read.</p>"
    "<p>This section covers the technology of psychiatric practice with the same standard we'd want from any review: what the tool changes, what it doesn't, what the evidence shows, and where the risks sit. No hype, no doom. Just a clear account of how the work is shifting, and what stays the same underneath.</p>",
    S.card_grid([
        S.card("What telepsychiatry changes, and what it doesn't", "Access, geography, and overhead changed. The exam, the rules, and the judgment mostly didn't.", "/technology/what-telepsychiatry-changes/", tag="Telepsychiatry", tagclass="tag--blue"),
        S.card("AI in psychiatry: a grounded look", "Ambient scribes, decision support, and chatbots. What helps, what's hype, and what to watch.", "/technology/ai-in-psychiatry/", tag="Artificial intelligence", tagclass="tag--blue"),
        S.card("Why documentation shapes care", "Before AI can fix the note, it helps to understand what the note is for.", "/business/why-documentation-shapes-care/", tag="Documentation", tagclass="tag--olive"),
        S.card("The future of telepsychiatry", "Where remote care is heading as the rules settle and the tools mature.", "/innovation/", tag="Innovation", tagclass="tag--olive"),
    ], 2),
    ["psychiatryrx", "shrinkmd", "shrinknetwork"],
    desc="Telepsychiatry, EHRs, ambient documentation, and AI in psychiatric practice, assessed on what they actually change and what the evidence shows.",
))

# ---------------- Economics ----------------
PAGES.append(hub(
    "economics", "/economics/", "The economics of psychiatry", "Economics",
    "Workforce, reimbursement, supply and demand, and the money that shapes who can get care.",
    "<p>Almost every frustration patients have with psychiatry traces back to economics. Waitlists exist because demand outruns a constrained workforce. Out-of-network billing exists because reimbursement often doesn't cover the cost of careful work. Short appointments exist because the payment model rewards volume. You can't understand the experience of psychiatric care without understanding the money underneath it.</p>"
    "<p>This section explains the economics plainly and with sources: how many psychiatrists there are and aren't, where the shortages concentrate, how reimbursement works, and why the incentives push the field the way they do. The goal is an honest map of the system, not a complaint about it.</p>",
    S.card_grid([
        S.card("The psychiatrist shortage", "How big it is, why it persists, where it concentrates, and what actually moves the needle.", "/economics/the-psychiatrist-shortage/", tag="Workforce", tagclass="tag--blue"),
        S.card("Cash-pay vs insurance", "The reimbursement story behind out-of-network psychiatry.", "/business/cash-pay-vs-insurance/", tag="Reimbursement", tagclass="tag--blue"),
        S.card("Why appointments can feel short", "The economics that shape the length of a psychiatric visit.", "/business/why-documentation-shapes-care/", tag="Access", tagclass="tag--olive"),
        S.card("Estimate practice revenue", "See how payer mix and pricing change the math, with an educational tool.", "/tools/private-practice-revenue-estimator/", tag="Tool", tagclass="tag--olive"),
    ], 2),
    ["anxietyresearch", "shrinkmd", "shrinknetwork"],
    desc="The workforce shortage, reimbursement, supply and demand, and the economics that shape access to psychiatric care, explained with sources.",
))

# ---------------- Culture ----------------
PAGES.append(hub(
    "culture", "/culture/", "The culture of psychiatry", "Culture",
    "History, ethics, identity, and public perception, the parts of the profession that don't fit on a billing sheet.",
    "<p>Psychiatry carries more cultural weight than most specialties. It sits at the intersection of medicine, the law, the family, and the self, and it has a public image shaped as much by film and history as by the clinic. The profession's culture, its ethics, its sense of identity, and the myths attached to it all affect how patients arrive, what they expect, and whether they trust the person across from them.</p>"
    "<p>This section is the reflective layer of shrinkiatry: the history of the field, the ethical lines that define responsible practice, the experience of doing the work, and the gap between what psychiatry is and what people think it is. It's commentary, clearly labeled as such, and it stays evidence-based even when the subject is perception rather than data.</p>",
    S.card_grid([
        S.card("Burnout in psychiatry", "What the data shows about the cost of the work, and what protects against it.", "/culture/burnout-in-psychiatry/", tag="The work", tagclass="tag--blue"),
        S.card("Ethics in psychiatric care", "Boundaries, confidentiality, capacity, and the lines that define responsible practice.", "/ethics/", tag="Ethics", tagclass="tag--blue"),
        S.card("What patients don't see behind the scenes", "The judgment, documentation, and systems that surround the visit.", "/business/why-documentation-shapes-care/", tag="Behind the scenes", tagclass="tag--olive"),
        S.card("Psychiatrist, psychologist, therapist", "Untangling the most common public confusion about the field.", "/careers/psychiatrist-vs-psychologist-vs-therapist/", tag="Identity", tagclass="tag--olive"),
    ], 2),
    ["shrinkopedia", "shariqrefai", "shrinknetwork"],
    desc="History, ethics, professional identity, and public perception of psychiatry. The reflective, behind-the-scenes layer of the profession.",
))

# ---------------- Leadership ----------------
PAGES.append(hub(
    "leadership", "/leadership/", "Leadership", "Leadership",
    "How psychiatrists lead teams, departments, practices, and the systems they work inside.",
    "<p>Psychiatrists end up leading more than they're trained to. They run group practices, chair departments, direct service lines, supervise residents, and sit on the committees that decide how care gets delivered. Yet leadership, communication, conflict management, and team building are rarely formal parts of psychiatric training.</p>"
    "<p>This section treats leadership as a real skill set the profession needs, not a soft extra. It draws on what's known about clinical leadership, supervision, and running mental health teams, and it connects to the business and culture sections where the lines blur. Like the rest of shrinkiatry, it's commentary and education, not a management-consulting pitch.</p>",
    S.card_grid([
        S.card("Running a practice is a leadership job", "Hiring, supervising, and setting the standard inside an independent practice.", "/business/how-private-psychiatry-practices-work/", tag="Practice", tagclass="tag--blue"),
        S.card("The Collaborative Care Model", "How one psychiatrist can extend reach across a whole primary care population, and what it asks of them as a leader.", "/economics/the-psychiatrist-shortage/", tag="Systems", tagclass="tag--blue"),
        S.card("Mentorship and supervision", "Teaching the next cohort is part of the work. Where it shows up in training.", "/careers/how-psychiatry-residency-works/", tag="Teaching", tagclass="tag--olive"),
    ], 3),
    ["shariqrefai", "shrinkmd", "shrinknetwork"],
    desc="How psychiatrists lead practices, departments, and care teams. Clinical leadership, supervision, and systems thinking in psychiatry.",
))

# ---------------- Innovation ----------------
PAGES.append(hub(
    "innovation", "/innovation/", "Innovation", "Innovation",
    "Where psychiatry is heading: measurement-based care, digital therapeutics, precision approaches, and the claims worth watching.",
    "<p>Psychiatry attracts big claims about the future, from genetic tests that promise to pick your medication to apps that promise to replace your therapist. Some of it is real and gaining evidence. Some of it is marketing wearing a lab coat. The job of this section is to tell the difference.</p>"
    "<p>Innovation at shrinkiatry means tracking what's genuinely changing in how psychiatric care is measured, delivered, and improved, while keeping the same honest standard about evidence that runs through the rest of the network. When something works, we'll say so. When the data is thin, we'll say that too.</p>",
    S.card_grid([
        S.card("AI in psychiatry", "The most consequential technology story in the field right now, assessed honestly.", "/technology/ai-in-psychiatry/", tag="Technology", tagclass="tag--blue"),
        S.card("The future of telepsychiatry", "What changes as the rules settle and remote care becomes ordinary.", "/technology/what-telepsychiatry-changes/", tag="Access", tagclass="tag--blue"),
        S.card("Measurement-based care", "Why tracking outcomes with simple scales is one of the field's most underrated shifts.", "/economics/the-psychiatrist-shortage/", tag="Quality", tagclass="tag--olive"),
    ], 3),
    ["anxietyresearch", "shrinkopedia", "shrinknetwork"],
    desc="The future of psychiatry: measurement-based care, digital therapeutics, precision approaches, and AI, with an honest read on the evidence.",
))

# ---------------- Ethics ----------------
PAGES.append(hub(
    "ethics", "/ethics/", "Ethics", "Ethics",
    "The boundaries, duties, and hard calls that define responsible psychiatric practice.",
    "<p>Ethics isn't a side topic in psychiatry. It's structural. The field deals with confidentiality, capacity, consent, coercion, dual relationships, and the rare but real duty to act when someone is in danger. These aren't abstractions; they shape ordinary decisions in ordinary visits, and they're part of why the work is heavier than it looks.</p>"
    "<p>This section explains the ethical framework psychiatry actually uses, drawing on the American Psychiatric Association's principles of medical ethics and the everyday situations where those principles get tested. It's educational commentary about how responsible practice is defined, not legal advice and not a substitute for a clinician's own judgment or an ethics board.</p>",
    S.card_grid([
        S.card("Why documentation is an ethical act", "Honest, careful records protect patients as much as clinicians.", "/business/why-documentation-shapes-care/", tag="Records", tagclass="tag--blue"),
        S.card("Controlled substances and the duty of care", "Prescribing rules exist for ethical reasons, not just legal ones.", "/business/why-controlled-substances-are-different/", tag="Prescribing", tagclass="tag--blue"),
        S.card("Boundaries in telepsychiatry", "What moving care onto a screen does, and doesn't, change about the duties owed.", "/technology/what-telepsychiatry-changes/", tag="Telepsychiatry", tagclass="tag--olive"),
        S.card("Disclosure and conflicts of interest", "How the network handles financial interests, plainly.", "/disclosures/", tag="Transparency", tagclass="tag--olive"),
    ], 2),
    ["shrinkopedia", "shrinkmd", "shrinknetwork"],
    desc="Boundaries, confidentiality, capacity, consent, and conflicts of interest in psychiatry. The ethical framework behind responsible practice.",
))

# ---------------- Research Digest ----------------
PAGES.append(hub(
    "research-digest", "/research-digest/", "Research Digest", "Research Digest",
    "Practice-relevant research, summarized honestly for people who don't have time to read every paper.",
    "<p>The Research Digest exists for a simple reason: psychiatrists, residents, and the people who write about them can't read everything, and most coverage of psychiatric research overstates what a single study shows. This section summarizes practice-relevant papers, guidelines, and policy changes the way a careful colleague would, including the part where we say what a study doesn't prove.</p>"
    "<p>Every digest entry follows the same discipline as the rest of the network: claims tied to primary sources, the limits of the evidence stated plainly, and no breathless takes. When the field's standard references update, such as the DSM, major clinical guidelines, or landmark trials, this is where shrinkiatry tracks what changed and why it matters.</p>",
    S.card_grid([
        S.card("The evidence behind Collaborative Care", "More than 80 trials, one of psychiatry's strongest access-expanding findings.", "/economics/the-psychiatrist-shortage/", tag="Evidence", tagclass="tag--blue"),
        S.card("What ambient AI documentation studies show", "Early data on time saved, burnout, and the catches.", "/technology/ai-in-psychiatry/", tag="Technology", tagclass="tag--blue"),
        S.card("How we evaluate evidence", "The standard every digest entry is held to.", "/evidence-methodology/", tag="Method", tagclass="tag--olive"),
    ], 3),
    ["anxietyresearch", "shrinkopedia", "shrinknetwork"],
    desc="Practice-relevant psychiatric research, guidelines, and policy changes, summarized honestly with the limits of the evidence stated plainly.",
))

# ---------------- Reports ----------------
PAGES.append(hub(
    "reports", "/reports/", "Reports", "Reports",
    "Longer, data-driven briefs on the state of the profession, built from public sources.",
    "<p>Reports are shrinkiatry's deeper, data-driven pieces: longer briefs that pull together public datasets and primary sources to describe the state of the profession. Where an article explains one idea, a report assembles the numbers behind a whole topic, with the sources shown and the methodology described.</p>"
    "<p>These are built from the same public data anyone could find, including HRSA workforce projections, ACGME training data, federal surveys, and peer-reviewed research, organized so the picture is legible. Each report states what the data can and can't tell you. Planned reports cover the workforce, telepsychiatry, burnout, technology adoption, and compensation.</p>",
    S.card_grid([
        S.card("The Psychiatrist Shortage", "Our standing brief on workforce supply, demand, and access, kept current as the data updates.", "/economics/the-psychiatrist-shortage/", tag="Workforce report", tagclass="tag--blue"),
        S.card("Burnout in Psychiatry", "What national surveys show about burnout in the specialty, in context.", "/culture/burnout-in-psychiatry/", tag="Burnout report", tagclass="tag--blue"),
        S.card("Telepsychiatry, after the cliff", "How remote prescribing rules and practice patterns are settling.", "/technology/what-telepsychiatry-changes/", tag="Telepsychiatry report", tagclass="tag--olive"),
    ], 3),
    ["anxietyresearch", "shrinkmd", "shrinknetwork"],
    desc="Data-driven briefs on the state of psychiatry, built from public sources: workforce, telepsychiatry, burnout, technology adoption, and compensation.",
))

# ---------------- Interviews ----------------
PAGES.append(hub(
    "interviews", "/interviews/", "Interviews", "Interviews",
    "Conversations with the people who build, study, and lead in psychiatry.",
    "<p>Some of what's worth knowing about the profession only comes out in conversation. The Interviews section is where shrinkiatry talks with psychiatrists, researchers, founders, department chairs, authors, and the technologists building tools for the field, about how the work actually gets done and where it's heading.</p>"
    "<p>Interviews are edited for clarity and length, and they're clearly distinguished from reported articles and from opinion. The people we talk with speak for themselves; their views aren't the network's. This section is being built, and the first conversations are in progress.</p>",
    S.card_grid([
        S.card("A founder's view of telepsychiatry", "From the network's own founder, on building independent telepsychiatry. See his perspective.", "https://shariqrefai.com", tag="Founder", tagclass="tag--blue", more="Visit"),
        S.card("Suggest an interview", "Know someone whose work belongs here? Tell us.", "/contact/", tag="Get in touch", tagclass="tag--olive", more="Contact"),
    ], 2),
    ["shariqrefai", "shrinkmd", "shrinknetwork"],
    desc="Conversations with psychiatrists, researchers, founders, and leaders about how the profession works and where it's heading.",
))

# ---------------- Opinion ----------------
PAGES.append(hub(
    "opinion", "/opinion/", "Opinion", "Opinion",
    "Clearly labeled editorials and arguments about the direction of the profession.",
    "<p>Opinion is where shrinkiatry makes arguments rather than just describing the field, and it's always labeled as such. Reported articles and digests stick to what's established; this section is for thought pieces about ethics, policy, technology, and the choices the profession faces. The line between the two is kept bright on purpose.</p>"
    "<p>Opinions published here are reasoned and sourced where claims are factual, but they're positions, not consensus. They're meant to be argued with. If you think a piece gets it wrong, that's the point of running them under a clear label.</p>",
    S.card_grid([
        S.card("The case for treating documentation as care", "Why the note deserves more respect than the system gives it.", "/business/why-documentation-shapes-care/", tag="Editorial", tagclass="tag--clay"),
        S.card("On hype in mental health technology", "How to read big claims about AI and apps without cynicism or credulity.", "/technology/ai-in-psychiatry/", tag="Editorial", tagclass="tag--clay"),
    ], 2),
    ["shariqrefai", "anxietyresearch", "shrinknetwork"],
    desc="Clearly labeled editorials and arguments about psychiatry: ethics, policy, technology, and the direction of the profession.",
))

# ---------------- Start Here ----------------
def _start_cards():
    rows = [
        ("Understand the profession", "Start with the overview of what psychiatry is and how it's organized.", "/psychiatry-operating-room/", "Profession", "tag--blue"),
        ("Understand training", "How psychiatrists are educated, from medical school to board certification.", "/careers/", "Training", "tag--blue"),
        ("Understand the business", "How practices are built, paid, and run.", "/business/", "Business", "tag--blue"),
        ("Understand telepsychiatry", "What virtual care changed, and what it didn't.", "/technology/what-telepsychiatry-changes/", "Technology", "tag--olive"),
        ("Understand the economics", "Why access is hard and appointments are short.", "/economics/the-psychiatrist-shortage/", "Economics", "tag--olive"),
        ("Understand the ethics", "The boundaries and duties behind responsible care.", "/ethics/", "Ethics", "tag--olive"),
        ("Read behind-the-scenes commentary", "The culture and identity of the profession.", "/culture/", "Culture", "tag--clay"),
        ("Find clinical care", "If you need a psychiatrist, this is the network's practice.", "https://shrinkmd.com", "shrinkMD", "tag--clay"),
    ]
    return S.card_grid([S.card(t, d, h, tag=tn, tagclass=tc, more="Go") for t, d, h, tn, tc in rows], 4)

PAGES.append({
    "slug": "start-here", "active": "/start-here/",
    "title": "Start Here | shrinkiatry",
    "desc": "New to shrinkiatry? Start here. Tell us what part of psychiatry you're trying to understand, and we'll point you somewhere useful.",
    "breadcrumbs": [("Home", "/"), ("Start Here", None)],
    "body": (
        page_hero("Start here", "What part of psychiatry are you trying to understand?",
                  "shrinkiatry covers the whole profession, so it helps to start from a question. Pick the one closest to yours.")
        + f'<section class="section section--surface"><div class="wrap"><div class="maxread flow"><p>shrinkiatry is the profession layer of The Shrink Network. It explains how psychiatry is trained, paid, regulated, and practiced, rather than explaining specific conditions or medications, which other sites in the network do well. If you came here looking for the encyclopedia of mental health, that\'s <a href="https://shrinkopedia.com" target="_blank" rel="noopener noreferrer">Shrinkopedia</a>. If you want medication guides, that\'s <a href="https://psychiatryrx.org" target="_blank" rel="noopener noreferrer">PsychiatryRx</a>. If you need care, that\'s <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a>. If you want to understand the profession itself, you\'re in the right place.</p></div></div></section>'
        + f'<section class="section section--tint"><div class="wrap">{_start_cards()}</div></section>'
        + f'<section class="section section--surface"><div class="wrap"><div class="maxread">{S.network_continue(["shrinkopedia","psychiatryrx","shrinkmd","shrinknetwork"])}</div></div></section>'
    ),
})
