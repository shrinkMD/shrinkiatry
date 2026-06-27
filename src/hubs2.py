# -*- coding: utf-8 -*-
"""Pillar section hubs (deep, sourced) rendered through core.article_shell."""
import core as S

PUB = "June 2026"
UPD = "June 27, 2026"

def _schema(title, desc, slug, faq=None, medical=False):
    atype = ["MedicalWebPage", "Article"] if medical else "Article"
    out = [S._jsonld_person(), {
        "@type": atype, "headline": title, "description": desc,
        "datePublished": "2026-06-20", "dateModified": "2026-06-27", "inLanguage": "en-US",
        "isPartOf": {"@id": "https://shrinkiatry.com/#website"},
        "publisher": {"@id": "https://shrinkiatry.com/#org"},
        "author": {"@id": "https://shrinkiatry.com/#refai"},
        "reviewedBy": {"@id": "https://shrinkiatry.com/#refai"},
        "mainEntityOfPage": "https://shrinkiatry.com/" + slug + "/",
    }]
    if faq:
        out.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    return out

def hub(slug, active, kicker, title, lede, desc, keywords, quick, takeaways, toc,
        body, cards_html, faq, sources, related, network, evidence, reading="10 min read", medical=False):
    full_body = body + ('<h2 id="read-next">Read next in this section</h2>' + cards_html if cards_html else "")
    meta = {
        "kicker": kicker, "title": title, "lede": lede, "breadcrumbs": [("Home", "/"), (title, None)],
        "reading_time": reading, "updated": UPD, "published": PUB, "evidence": evidence,
        "quick_answer": quick, "takeaways": takeaways, "toc": toc, "body": full_body,
        "faq": faq, "sources": sources, "related": related, "network": network,
    }
    return {
        "slug": slug, "active": active, "title": f"{title} | shrinkiatry", "desc": desc,
        "keywords": keywords, "og_type": "article",
        "breadcrumbs": [("Home", "/"), (title, None)],
        "schema": _schema(title, desc, slug, faq, medical),
        "body": S.article_shell(meta),
    }

PAGES = []

# ============================== CAREERS ==============================
PAGES.append(hub(
    "careers", "/careers/", "Careers in psychiatry", "Careers in psychiatry: how psychiatrists are trained and what the work becomes",
    "Becoming a psychiatrist takes four years of medical school, a four-year residency, and board certification, then a career that can bend in many directions. This is the full map.",
    "How psychiatrists are trained and certified, and the many shapes a psychiatry career can take: residency, fellowships, board certification, compensation, and practice paths.",
    "psychiatry careers, psychiatry residency, how to become a psychiatrist, psychiatry fellowships, board certification",
    "Becoming a psychiatrist means medical school, then a residency the Accreditation Council for Graduate Medical Education (ACGME) sets at 48 months, then board certification through the American Board of Psychiatry and Neurology (ABPN). After that, the work can take many shapes: private practice, hospital systems, academia, consultation, the military and the VA, sports, industry, and telepsychiatry. This page maps the whole path and links to deeper guides on each stage.",
    ["A psychiatrist is a physician first: four years of medical school precede any psychiatric specialization.",
     "Residency is four years (48 months per the ACGME), and board certification through the ABPN is the standard credential.",
     "Subspecialty fellowships add one to two years; child and adolescent psychiatry is the largest.",
     "The same training opens many careers, from solo practice to academia to telepsychiatry, each with real tradeoffs."],
    [("path", "The path, end to end"), ("residency", "What residency actually trains"),
     ("certification", "Board certification and licensure"), ("subspecialties", "Subspecialties and fellowships"),
     ("paths", "Where a career can go"), ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="path">The path, end to end</h2>
<p>The pipeline is long and specific. It runs through four years of college, four years of medical school, and then residency, which is paid, supervised training inside a hospital or health system. For psychiatry, the <a href="https://www.acgme.org/specialties/psychiatry/overview/" target="_blank" rel="noopener noreferrer">ACGME</a> requires that residency to be 48 months. Only after residency does a psychiatrist practice independently, and most then become board certified. From the start of college, training a psychiatrist takes well over a decade, which is one reason the workforce can't expand quickly to meet demand. We cover that supply problem in <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>.</p>

<h2 id="residency">What residency actually trains</h2>
<p>The surprising part of psychiatry residency is how much of the early training isn't psychiatry. The first year, the intern year, deliberately includes months of general medicine and neurology alongside the first psychiatry rotations, because psychiatric patients have bodies, take other medications, and develop medical illnesses that can mimic psychiatric ones. Over the four years, residents move from supervised inpatient work toward outpatient clinics, psychotherapy training, and growing independence. ACGME requirements include demonstrated competence in several forms of psychotherapy as well as medical and medication management, so the job is the combination of the two. The full year-by-year picture is in <a href="/careers/how-psychiatry-residency-works/">how psychiatry residency actually works</a>.</p>

<h2 id="certification">Board certification and licensure</h2>
<p>Two credentials get confused. A medical license, granted by a state medical board, is what's legally required to practice. Board certification through the <a href="https://abpn.org/become-certified/taking-a-specialty-exam/psychiatry/" target="_blank" rel="noopener noreferrer">ABPN</a> sits on top of the license as the profession's standardized mark of competence, earned by completing an accredited residency, holding a full license, and passing a certifying exam. Certification is now maintained through ongoing continuing certification rather than a single lifetime test. We unpack what the credential does and doesn't guarantee in <a href="/careers/what-board-certification-means/">what board certification actually means</a>.</p>

<h2 id="subspecialties">Subspecialties and fellowships</h2>
<p>After residency, some psychiatrists complete a fellowship: one to two years of subspecialty training. Common ones include child and adolescent psychiatry (the largest, a two-year fellowship), consultation-liaison psychiatry, addiction psychiatry, geriatric psychiatry, forensic psychiatry, and sleep medicine. A fellowship plus an additional ABPN exam leads to subspecialty certification. For people deciding between roles, it helps to be clear on what separates a psychiatrist from a psychologist or therapist; see <a href="/careers/psychiatrist-vs-psychologist-vs-therapist/">psychiatrist vs psychologist vs therapist</a>.</p>

<h2 id="paths">Where a career can go</h2>
<p>The same training opens very different lives. Some psychiatrists own independent practices and carry the business as well as the clinical work, which we cover in <a href="/business/how-private-psychiatry-practices-work/">how private practices work</a>. Others are employed by hospitals or health systems for steady income and benefits. Academic psychiatrists teach and do research. Telepsychiatry has opened location-independent careers, explored in <a href="/technology/what-telepsychiatry-changes/">what telepsychiatry changes</a>. And because demand outruns supply, the job market is unusually strong, which shapes compensation and leverage across all of these paths.</p>
""",
    S.card_grid([
        S.card("How psychiatry residency actually works", "Four years, the PGY ladder, what each year trains, and the boards at the end.", "/careers/how-psychiatry-residency-works/", tag="Training", tagclass="tag--blue"),
        S.card("Psychiatrist vs psychologist vs therapist", "Different training, different tools, different scope, and where they overlap.", "/careers/psychiatrist-vs-psychologist-vs-therapist/", tag="The profession", tagclass="tag--blue"),
        S.card("What board certification actually means", "ABPN certification, continuing certification, and what it does and doesn't guarantee.", "/careers/what-board-certification-means/", tag="Credentials", tagclass="tag--blue"),
    ], 3),
    [("How long does it take to become a psychiatrist?", "Counting four years of college, four years of medical school, and a four-year (48-month) residency, it takes about twelve years after high school, plus one to two more for a subspecialty fellowship."),
     ("Do psychiatrists do therapy or just prescribe?", "Both. ACGME residency requirements include demonstrated competence in several forms of psychotherapy as well as medical and medication management. Many psychiatrists practice therapy; all are trained in it."),
     ("Is board certification required to practice?", "No. A state medical license is what's legally required. ABPN board certification is the standard professional credential and is often expected by employers and insurers.")],
    [("ACGME, Psychiatry program requirements (48-month residency).", "https://www.acgme.org/specialties/psychiatry/overview/"),
     ("American Board of Psychiatry and Neurology, certification in psychiatry.", "https://abpn.org/become-certified/taking-a-specialty-exam/psychiatry/"),
     ("American Psychiatric Association, Certification and Licensure.", "https://www.psychiatry.org/psychiatrists/education/certification-and-licensure")],
    [("How residency works", "/careers/how-psychiatry-residency-works/"), ("Board certification", "/careers/what-board-certification-means/"),
     ("Psychiatrist vs psychologist", "/careers/psychiatrist-vs-psychologist-vs-therapist/"), ("The shortage", "/economics/the-psychiatrist-shortage/"),
     ("Private practice", "/business/how-private-psychiatry-practices-work/"), ("Burnout", "/culture/burnout-in-psychiatry/")],
    ["shrinkmd", "shariqrefai", "shrinknetwork"],
    "ACGME program requirements, ABPN certification standards, and American Psychiatric Association guidance",
))

# ============================== BUSINESS ==============================
PAGES.append(hub(
    "business", "/business/", "The business of psychiatry", "The business of psychiatry: how practices are built, paid, and run",
    "A psychiatry practice is a small business with unusual rules: time-limited visits, payment models that don't always match the work, and controlled-substance regulations no other part of the business has to think about.",
    "How psychiatric practices are built, paid, and run: cash-pay vs insurance, practice models, documentation, controlled-substance rules, and the economics of independent practice.",
    "psychiatry business, private practice psychiatry, cash-pay psychiatry, psychiatry practice management, controlled substances",
    "Running a psychiatry practice means doing two jobs: the clinical work, and operating a small business that sets prices, gets paid, hires, documents, and follows regulations. The biggest decision is the payment model, cash-pay, insurance, or a hybrid, and it shapes income, access, and how much administrative weight lands on the clinician. Documentation and controlled-substance rules add constraints unique to the field. This page maps how the business works and links to deeper guides.",
    ["A practice is a small business the psychiatrist owns and runs, not just a place they work.",
     "The central choice is the payment model: cash-pay, insurance, or hybrid, each with real tradeoffs.",
     "Documentation drives billing, liability, continuity, and time, so it shapes care as much as it records it.",
     "Controlled substances bring DEA rules that reshape scheduling, monitoring, and compliance."],
    [("business", "A clinic is a business"), ("payers", "The payment decision"), ("documentation", "Why documentation shapes care"),
     ("controlled", "Controlled substances and compliance"), ("models", "Practice models and scaling"),
     ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="business">A clinic is a business</h2>
<p>When a psychiatrist opens a practice, they take on operations they were never taught in medical training: pricing, billing, credentialing, hiring, compliance, and covering fixed costs whether or not the schedule fills. Outpatient psychiatry has lower overhead than procedure-heavy specialties, because there's no expensive equipment, but it's far from zero, and two quiet drains matter a lot: no-shows, since an empty slot earns nothing while overhead runs, and unpaid administrative time spent on notes after hours. You can model the math in our <a href="/tools/private-practice-revenue-estimator/">revenue estimator</a>.</p>

<h2 id="payers">The payment decision</h2>
<p>The single most consequential choice is how the practice gets paid. Psychiatry stands out in American medicine for how often clinicians don't take insurance, because contracted reimbursement often doesn't reflect the time careful work takes, and the administrative burden of claims, credentialing, and prior authorizations is heavy. Cash-pay buys longer visits and simpler operations at the cost of reach; insurance buys access and volume at the cost of rate-setting and paperwork. The full tradeoff, and what it does to access, is in <a href="/business/cash-pay-vs-insurance/">cash-pay vs insurance</a>.</p>

<h2 id="documentation">Why documentation shapes care</h2>
<p>The clinical note looks like paperwork, but it does at least four jobs: it justifies billing, creates the legal record, carries the plan to the next visit, and protects the patient. Because notes take real, largely unpaid time, documentation quietly shapes appointment length and contributes to burnout. It's also where ambient AI tools are landing first. We explain the whole picture in <a href="/business/why-documentation-shapes-care/">why documentation shapes care</a>.</p>

<h2 id="controlled">Controlled substances and compliance</h2>
<p>Some psychiatric medications, including stimulants and benzodiazepines, are controlled substances regulated by the <a href="https://www.dea.gov/drug-information/drug-scheduling" target="_blank" rel="noopener noreferrer">DEA</a>. That status brings rules that reshape the whole practice: a separate DEA registration, tighter refill and documentation requirements, prescription drug monitoring program checks, and evolving telemedicine rules. The details, and why they change how a practice runs, are in <a href="/business/why-controlled-substances-are-different/">why controlled substances are handled differently</a>.</p>

<h2 id="models">Practice models and scaling</h2>
<p>Solo practice offers the most control and the most exposure, since every fixed cost lands on one person. Group practice spreads overhead and risk across several clinicians in exchange for some autonomy and a share of revenue. Hybrid arrangements, a small private panel plus part-time employed or telepsychiatry work, are common for stability. Growth raises new questions about hiring, credentialing, and whether to bring on other prescribers. The structures and tradeoffs are detailed in <a href="/business/how-private-psychiatry-practices-work/">how private psychiatry practices work</a>.</p>
""",
    S.card_grid([
        S.card("How private psychiatry practices work", "Structure, payer mix, overhead, and the tradeoffs behind an independent practice.", "/business/how-private-psychiatry-practices-work/", tag="Practice models", tagclass="tag--blue"),
        S.card("Cash-pay vs insurance", "Why so many psychiatrists go out of network, and what that does to access and income.", "/business/cash-pay-vs-insurance/", tag="Payment", tagclass="tag--blue"),
        S.card("Why documentation shapes care", "The note drives billing, liability, continuity, and time.", "/business/why-documentation-shapes-care/", tag="Operations", tagclass="tag--blue"),
    ], 3),
    [("Why don't more psychiatrists take insurance?", "Contracted rates are often low relative to the time careful psychiatric care takes, and the administrative burden of claims and authorizations is heavy. Many psychiatrists go out of network to protect visit length and reduce paperwork."),
     ("Do you need a special license to prescribe stimulants?", "You need a DEA registration to prescribe any controlled substance, which is separate from a medical license. Schedule II medications like many stimulants also carry stricter refill and monitoring rules."),
     ("Is private practice profitable?", "It can be, because the owner keeps the margin, but it carries more financial risk, more administrative work, and no built-in benefits. The right model depends on the person.")],
    [("American Psychiatric Association, practice management resources.", "https://www.psychiatry.org/psychiatrists/practice/practice-management"),
     ("DEA, drug scheduling overview.", "https://www.dea.gov/drug-information/drug-scheduling"),
     ("AMA, private practice resources.", "https://www.ama-assn.org/practice-management/private-practices")],
    [("Private practice", "/business/how-private-psychiatry-practices-work/"), ("Cash-pay vs insurance", "/business/cash-pay-vs-insurance/"),
     ("Documentation", "/business/why-documentation-shapes-care/"), ("Controlled substances", "/business/why-controlled-substances-are-different/"),
     ("Revenue estimator", "/tools/private-practice-revenue-estimator/"), ("The shortage", "/economics/the-psychiatrist-shortage/")],
    ["psychiatryrx", "shrinkmd", "shrinknetwork"],
    "APA and AMA practice-management resources, DEA scheduling rules, and federal reimbursement context",
))

# ============================== TECHNOLOGY ==============================
PAGES.append(hub(
    "technology", "/technology/", "Technology in psychiatry", "Technology in psychiatry: telepsychiatry, records, and AI, judged honestly",
    "Psychiatry may be the specialty most exposed to technology change, because its core encounter is a conversation. That makes it portable to video, easy to transcribe, and tempting to automate. Here's what actually changes.",
    "Telepsychiatry, EHRs, ambient documentation, and AI in psychiatric practice, assessed on what they actually change and what the evidence shows.",
    "AI in psychiatry, telepsychiatry, ambient documentation, psychiatry technology, ambient AI scribe",
    "Technology is reshaping how psychiatric care is delivered and documented, but unevenly. Telepsychiatry changed access and logistics more than the clinical method. Ambient AI scribes are the clearest current win, mainly by cutting documentation time. Decision support is promising but earlier, and chatbots sold as therapy are the most overstated and the most risky. This page covers the technology of practice with the same standard as any honest review: what it changes, what it doesn't, and what the evidence shows.",
    ["Telepsychiatry mainly changed access and overhead, not the core clinical method.",
     "Ambient AI scribes show real, measured reductions in documentation time and, in some settings, burnout.",
     "Decision-support tools are promising but earlier, and need validation and human oversight.",
     "Chatbots marketed as therapy are the most hyped and carry real safety and privacy risks."],
    [("exposed", "Why psychiatry is exposed to tech"), ("tele", "Telepsychiatry: access, not a new method"),
     ("ai", "AI: the back office first"), ("risks", "The risks that matter"), ("future", "Where it's heading"),
     ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="exposed">Why psychiatry is exposed to tech</h2>
<p>The core of a psychiatric visit is a conversation and a careful observation, not a procedure. That makes it unusually portable to video, unusually easy to record and transcribe, and unusually tempting to automate. It's why telepsychiatry scaled so fast, why ambient documentation tools landed in psychiatry early, and why every claim about artificial intelligence in mental health deserves a careful read.</p>

<h2 id="tele">Telepsychiatry: access, not a new method</h2>
<p>Telepsychiatry's biggest effect is on access and logistics: it removes travel, widens geographic reach, lowers overhead, and makes scheduling more flexible. What it doesn't change is the clinical method, the interview, the judgment, and most of the duty of care. Research generally finds telepsychiatry comparable to in-person care for many common conditions, which is why professional bodies have supported its expansion, though it isn't right for every patient or situation. The full picture is in <a href="/technology/what-telepsychiatry-changes/">what telepsychiatry changes</a>.</p>

<h2 id="ai">AI: the back office first</h2>
<p>People imagine AI doing therapy. The real-world use so far is administrative: ambient scribes that listen to a visit, with consent, and draft the clinical note for the clinician to review. Early studies and reporting from the <a href="https://www.ama-assn.org/practice-management/digital-health/ai-scribes-save-15000-hours-and-restore-human-side-medicine" target="_blank" rel="noopener noreferrer">American Medical Association</a> show meaningful reductions in documentation time and after-hours work, and in some settings, lower burnout. That's the clearest current win. A grounded read on what helps and what's hype is in <a href="/technology/ai-in-psychiatry/">AI in psychiatry</a>.</p>

<h2 id="risks">The risks that matter</h2>
<p>Three risks deserve attention. Privacy, because recording and processing a psychiatric conversation involves unusually sensitive data and consent has to be real. Accuracy, because a fluent AI draft can be wrong and an unreviewed note can introduce errors into the record. And overreliance, especially with chatbots marketed as therapy, which aren't clinicians and can respond unpredictably in exactly the high-stakes moments that matter most. The responsible standard is that these tools assist a clinician who remains accountable.</p>

<h2 id="future">Where it's heading</h2>
<p>The near future is less dramatic than the headlines: better documentation tools, measurement-based care supported by simple tracking, and decision support that surfaces guideline-based options without replacing judgment. As telemedicine prescribing rules settle, remote care will keep maturing. We track the genuinely new in <a href="/innovation/">innovation</a> and the regulatory edge in <a href="/business/why-controlled-substances-are-different/">controlled substances</a>.</p>
""",
    S.card_grid([
        S.card("What telepsychiatry changes, and what it doesn't", "Access and overhead changed. The exam, the rules, and the judgment mostly didn't.", "/technology/what-telepsychiatry-changes/", tag="Telepsychiatry", tagclass="tag--blue"),
        S.card("AI in psychiatry: a grounded look", "Ambient scribes, decision support, and chatbots. What helps and what's hype.", "/technology/ai-in-psychiatry/", tag="Artificial intelligence", tagclass="tag--blue"),
        S.card("Why documentation shapes care", "Before AI can fix the note, it helps to understand what the note is for.", "/business/why-documentation-shapes-care/", tag="Documentation", tagclass="tag--olive"),
    ], 3),
    [("Is telepsychiatry as good as in-person care?", "For many common conditions, research generally finds telepsychiatry comparable in outcomes and satisfaction. It isn't the right fit for every patient or situation, and the strength of the evidence varies by condition."),
     ("Do AI scribes work in psychiatry?", "Early studies suggest ambient AI scribes reduce documentation time and after-hours work and, in some settings, burnout. Drafts require careful review for accuracy, and recording a visit raises privacy and consent considerations."),
     ("Can an AI chatbot replace a therapist?", "No. A general-purpose chatbot isn't a clinician and can respond unpredictably in high-stakes moments. It shouldn't be relied on as a substitute for care, especially in a crisis.")],
    [("AMA, AI scribes and the documentation burden.", "https://www.ama-assn.org/practice-management/digital-health/ai-scribes-save-15000-hours-and-restore-human-side-medicine"),
     ("APA, telepsychiatry toolkit and evidence base.", "https://www.psychiatry.org/psychiatrists/practice/telepsychiatry"),
     ("Use of Ambient AI Scribes to Reduce Administrative Burden and Professional Burnout (PMC).", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12492056/")],
    [("Telepsychiatry", "/technology/what-telepsychiatry-changes/"), ("AI in psychiatry", "/technology/ai-in-psychiatry/"),
     ("Documentation", "/business/why-documentation-shapes-care/"), ("Innovation", "/innovation/"),
     ("Controlled substances", "/business/why-controlled-substances-are-different/")],
    ["psychiatryrx", "shrinkmd", "shrinknetwork"],
    "AMA reporting, APA telepsychiatry resources, and peer-reviewed studies of ambient documentation",
))

# ============================== ECONOMICS ==============================
PAGES.append(hub(
    "economics", "/economics/", "The economics of psychiatry", "The economics of psychiatry: workforce, reimbursement, and access",
    "Almost every frustration patients have with psychiatry, long waits, short visits, out-of-network bills, traces back to economics. This is the money and the math underneath the care.",
    "The workforce shortage, reimbursement, supply and demand, and the economics that shape access to psychiatric care, explained with sources.",
    "psychiatrist shortage, psychiatry workforce, mental health access, psychiatry reimbursement, collaborative care model",
    "You can't understand the experience of psychiatric care without the economics underneath it. Waitlists exist because demand outruns a constrained workforce. Out-of-network billing exists because reimbursement often doesn't cover careful work. Short appointments exist because the payment model rewards volume. By recent federal counts, roughly 137 million Americans live in a designated mental health shortage area. This page explains the workforce, the money, and the approaches that actually expand access.",
    ["About 137 million Americans live in a federally designated mental health professional shortage area (HRSA).",
     "Federal projections estimate a shortage of tens of thousands of adult psychiatrists by 2038.",
     "Causes include a slow training pipeline, an aging workforce, geographic maldistribution, and payment limits.",
     "The Collaborative Care Model, backed by more than 80 trials, can stretch one psychiatrist across many more patients."],
    [("scale", "The scale of the shortage"), ("why", "Why it persists"), ("reimbursement", "Reimbursement and incentives"),
     ("ccm", "What actually expands access"), ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="scale">The scale of the shortage</h2>
<p>If you've waited months for a psychiatry appointment, you've met the economics in person. The federal <a href="https://bhw.hrsa.gov/data-research" target="_blank" rel="noopener noreferrer">Health Resources and Services Administration</a> designates areas with too few mental health professionals, and by recent counts roughly 137 million Americans, around 40 percent of the population, live in one. HRSA's modeling has estimated a shortage of tens of thousands of adult psychiatrists by 2038 under baseline assumptions, and larger if access improves and more people seek care. Child and adolescent psychiatry is among the thinnest parts of the workforce. The standing brief is <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>.</p>

<h2 id="why">Why it persists</h2>
<p>Several causes stack up. The training pipeline is slow, taking well over a decade per psychiatrist, so supply can't expand quickly; we cover that in <a href="/careers/how-psychiatry-residency-works/">how residency works</a>. The workforce is aging, with a large share near retirement. Demand has risen sharply since the pandemic while supply moves slowly. And payment limits supply in subtler ways, pushing some psychiatrists toward cash-pay or part-time work.</p>

<h2 id="reimbursement">Reimbursement and incentives</h2>
<p>The payment system shapes behavior. Insurers reimburse psychiatric visits at rates that often don't reflect the time good care takes, and participating means credentialing, claims, denials, and prior authorizations. The result is one of the highest out-of-network rates in medicine, which improves quality and time for those who can pay while reducing access for those who can't. The full reimbursement story is in <a href="/business/cash-pay-vs-insurance/">cash-pay vs insurance</a>.</p>

<h2 id="ccm">What actually expands access</h2>
<p>There's no single fix, but several things help: more residency slots over time, telepsychiatry to spread existing supply across geography, other prescribers like psychiatric nurse practitioners, and reducing the burdens that drive psychiatrists out of full practice. The most evidence-backed approach is the Collaborative Care Model, in which a consulting psychiatrist advises a primary care team and a behavioral health care manager rather than seeing most patients directly. Grown from the IMPACT trial and supported by more than 80 randomized trials, it can extend one psychiatrist's reach across a far larger population, addressing the shortage now rather than in 2038.</p>
""",
    S.card_grid([
        S.card("The psychiatrist shortage", "How big it is, why it persists, where it concentrates, and what moves the needle.", "/economics/the-psychiatrist-shortage/", tag="Workforce", tagclass="tag--blue"),
        S.card("Cash-pay vs insurance", "The reimbursement story behind out-of-network psychiatry.", "/business/cash-pay-vs-insurance/", tag="Reimbursement", tagclass="tag--blue"),
        S.card("Estimate practice revenue", "See how payer mix and pricing change the math.", "/tools/private-practice-revenue-estimator/", tag="Tool", tagclass="tag--olive"),
    ], 3),
    [("How many Americans lack access to a psychiatrist?", "By recent HRSA counts, roughly 137 million Americans, about 40 percent of the population, live in a designated mental health professional shortage area, meaning there are too few mental health professionals for the population's needs."),
     ("Why are psychiatry appointments so short?", "Payment models reward volume, and reimbursement often doesn't cover the time careful work takes. Documentation time, which is largely unpaid, adds further pressure toward shorter visits."),
     ("What is the Collaborative Care Model?", "A team-based approach where a consulting psychiatrist advises a primary care team and a behavioral health care manager rather than seeing most patients directly. Backed by more than 80 trials, it extends one psychiatrist's reach across many more patients.")],
    [("HRSA Bureau of Health Workforce, behavioral health workforce brief and projections.", "https://bhw.hrsa.gov/sites/default/files/bureau-health-workforce/data-research/Behavioral-Health-Workforce-Brief-2025.pdf"),
     ("Unutzer et al., the psychiatrist's role in the Collaborative Care Model, American Journal of Psychiatry.", "https://psychiatryonline.org/doi/10.1176/appi.ajp.2015.15010017"),
     ("AMA, how collaborative care can help close the mental health care gap.", "https://www.ama-assn.org/practice-management/scope-practice/how-collaborative-care-can-help-close-mental-health-care-gap")],
    [("The shortage", "/economics/the-psychiatrist-shortage/"), ("Cash-pay vs insurance", "/business/cash-pay-vs-insurance/"),
     ("How residency works", "/careers/how-psychiatry-residency-works/"), ("Telepsychiatry", "/technology/what-telepsychiatry-changes/"),
     ("Revenue estimator", "/tools/private-practice-revenue-estimator/")],
    ["anxietyresearch", "shrinkmd", "shrinknetwork"],
    "HRSA workforce projections, the IMPACT trial and Collaborative Care literature, and AMA policy analysis",
))

# ============================== CULTURE ==============================
PAGES.append(hub(
    "culture", "/culture/", "The culture of psychiatry", "The culture of psychiatry: history, ethics, identity, and perception",
    "Psychiatry carries more cultural weight than most specialties. It sits at the intersection of medicine, the law, the family, and the self, with a public image shaped as much by film and history as by the clinic.",
    "History, ethics, professional identity, and public perception of psychiatry: the reflective, behind-the-scenes layer of the profession.",
    "psychiatry culture, history of psychiatry, psychiatry ethics, psychiatry stigma, professional identity",
    "Psychiatry's culture, its history, its ethics, its sense of identity, and the myths attached to it, affects how patients arrive, what they expect, and whether they trust the clinician across from them. This is the reflective layer of shrinkiatry: the experience of doing the work, the lines that define responsible practice, and the gap between what psychiatry is and what people think it is. It's commentary, clearly labeled, and it stays evidence-based even when the subject is perception rather than data.",
    ["Psychiatry's public image is shaped heavily by film, history, and stigma, not just by clinical reality.",
     "The work carries an emotional and ethical weight that isn't visible in the appointment.",
     "Burnout in psychiatry is comparatively lower than in many specialties, but still common.",
     "Understanding the culture explains how patients arrive and why trust is hard-won."],
    [("weight", "Why psychiatry carries cultural weight"), ("identity", "Professional identity and the work"),
     ("ethics", "Ethics as structure, not side topic"), ("perception", "Perception, myth, and stigma"),
     ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="weight">Why psychiatry carries cultural weight</h2>
<p>Few specialties are as loaded with meaning. Psychiatry touches autonomy, the law, family, and identity, and its public image has been shaped by a long, complicated history and by decades of film and television. That inheritance shows up in the room: patients arrive with expectations and fears formed long before the first appointment. Taking the culture seriously is part of taking the care seriously.</p>

<h2 id="identity">Professional identity and the work</h2>
<p>The day-to-day experience of psychiatry is heavier than it looks from outside. Clinicians carry risk, responsibility, and the emotional content of other people's suffering, while also managing documentation, economics, and time pressure. That weight is one reason burnout matters in the field, even though, as the data shows, psychiatry reports comparatively lower burnout than many specialties. We cover that honestly in <a href="/culture/burnout-in-psychiatry/">burnout in psychiatry</a>.</p>

<h2 id="ethics">Ethics as structure, not side topic</h2>
<p>Ethics isn't a footnote in psychiatry; it's structural. Confidentiality, capacity, consent, boundaries, and the rare duty to act shape ordinary decisions in ordinary visits. The field's ethical framework, drawn from the American Psychiatric Association's principles of medical ethics, is its own subject, covered in <a href="/ethics/">ethics in psychiatric care</a>. Even documentation is partly an ethical act, since honest, careful records protect patients as much as clinicians.</p>

<h2 id="perception">Perception, myth, and stigma</h2>
<p>Much of what the public believes about psychiatry is myth: that medications are chemical restraints, that seeing a psychiatrist means you're broken, that the work is mostly couches and dream analysis. These beliefs affect whether people seek care and how they feel when they do. One of the most common confusions, the difference between a psychiatrist, a psychologist, and a therapist, is untangled in <a href="/careers/psychiatrist-vs-psychologist-vs-therapist/">that guide</a>. Naming the myths plainly is part of the work this section does.</p>
""",
    S.card_grid([
        S.card("Burnout in psychiatry", "What national data shows about the cost of the work, and what protects against it.", "/culture/burnout-in-psychiatry/", tag="The work", tagclass="tag--blue"),
        S.card("Ethics in psychiatric care", "Boundaries, confidentiality, capacity, and the lines that define responsible practice.", "/ethics/", tag="Ethics", tagclass="tag--blue"),
        S.card("Psychiatrist, psychologist, therapist", "Untangling the most common public confusion about the field.", "/careers/psychiatrist-vs-psychologist-vs-therapist/", tag="Identity", tagclass="tag--olive"),
    ], 3),
    [("Is psychiatry burnout the worst in medicine?", "No. Recent national data places psychiatrist burnout among the lower rates across specialties, in roughly the low thirties percent, compared with a physician average in the low to mid forties. It's comparatively lower, though still common."),
     ("Why is there so much stigma around psychiatry?", "Stigma is shaped by history, by cultural portrayals in film and media, and by misunderstanding of what treatment involves. Naming the myths plainly, and explaining the reality, is one way the field works to reduce it."),
     ("Is psychiatry mostly talk therapy?", "Not exactly. Psychiatrists train in psychotherapy and many practice it, but they also handle medical assessment and medication management, which the public image often leaves out.")],
    [("American Psychiatric Association, Principles of Medical Ethics.", "https://www.psychiatry.org/psychiatrists/practice/ethics"),
     ("Medscape Physician Mental Health and Wellbeing Report 2025.", "https://www.medscape.com/sites/public/mental-health/2025"),
     ("American Psychiatric Association, What is Psychiatry.", "https://www.psychiatry.org/patients-families/what-is-psychiatry")],
    [("Burnout", "/culture/burnout-in-psychiatry/"), ("Ethics", "/ethics/"),
     ("Psychiatrist vs psychologist", "/careers/psychiatrist-vs-psychologist-vs-therapist/"), ("Documentation", "/business/why-documentation-shapes-care/"),
     ("The Operating Room", "/psychiatry-operating-room/")],
    ["shrinkopedia", "shariqrefai", "shrinknetwork"],
    "APA principles of medical ethics, national physician wellbeing surveys, and professional-identity literature",
))

# ============================== ETHICS ==============================
PAGES.append(hub(
    "ethics", "/ethics/", "Ethics in psychiatry", "Ethics in psychiatry: the boundaries and duties behind responsible care",
    "Ethics isn't a side topic in psychiatry. It's structural. The field deals with confidentiality, capacity, consent, coercion, dual relationships, and the rare but real duty to act when someone is in danger.",
    "Boundaries, confidentiality, capacity, consent, and conflicts of interest in psychiatry: the ethical framework behind responsible practice, explained.",
    "psychiatry ethics, confidentiality, informed consent, capacity, boundaries in psychiatry, duty to warn",
    "Psychiatric ethics shape ordinary decisions in ordinary visits. The framework draws on the American Psychiatric Association's principles of medical ethics and on the everyday situations where those principles get tested: who can consent, what stays confidential and when it can't, where boundaries lie, and what a clinician owes when risk is high. This page explains how responsible practice is defined. It's educational commentary, not legal advice and not a substitute for a clinician's judgment or an ethics board.",
    ["Ethics is built into psychiatry's everyday decisions, not reserved for rare dilemmas.",
     "Confidentiality is central but not absolute; specific situations can require disclosure.",
     "Capacity and informed consent govern whether and how treatment proceeds.",
     "Boundaries and disclosed conflicts of interest protect the trust the work depends on."],
    [("framework", "The ethical framework"), ("confidentiality", "Confidentiality and its limits"),
     ("consent", "Capacity and informed consent"), ("boundaries", "Boundaries and conflicts of interest"),
     ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="framework">The ethical framework</h2>
<p>Medical ethics in psychiatry rests on familiar principles, respect for autonomy, beneficence, non-maleficence, and justice, adapted to a field where judgment, risk, and the patient's own decision-making capacity are often part of the clinical picture. The American Psychiatric Association publishes <a href="https://www.psychiatry.org/psychiatrists/practice/ethics" target="_blank" rel="noopener noreferrer">principles of medical ethics with annotations for psychiatry</a>, which translate general medical ethics into the specialty's specific situations.</p>

<h2 id="confidentiality">Confidentiality and its limits</h2>
<p>Confidentiality is foundational; people can't speak freely without it. But it isn't absolute. Specific, limited situations, such as a serious and imminent risk of harm, can require a clinician to act, and the law in many places shapes a duty to protect or warn. Good practice is transparent with patients about these limits up front, so trust is built on an honest account of how confidentiality actually works.</p>

<h2 id="consent">Capacity and informed consent</h2>
<p>Treatment generally proceeds with a patient's informed consent, which depends on capacity: the ability to understand the relevant information, appreciate the situation, reason through options, and communicate a choice. Capacity is decision-specific and can change over time. When it's impaired, ethics and law provide structured paths, which is one of the places psychiatry's responsibilities are heaviest and most carefully governed.</p>

<h2 id="boundaries">Boundaries and conflicts of interest</h2>
<p>Clear professional boundaries protect patients and the relationship the work depends on. So does transparency about conflicts of interest. shrinkiatry holds itself to the same standard it describes: where the editor has a financial interest, such as shrinkMD, it's <a href="/disclosures/">disclosed plainly</a>. Even documentation has an ethical dimension, since honest records protect patients, a point we make in <a href="/business/why-documentation-shapes-care/">why documentation shapes care</a>.</p>
""",
    S.card_grid([
        S.card("Why documentation is an ethical act", "Honest, careful records protect patients as much as clinicians.", "/business/why-documentation-shapes-care/", tag="Records", tagclass="tag--blue"),
        S.card("Controlled substances and the duty of care", "Prescribing rules exist for ethical reasons, not just legal ones.", "/business/why-controlled-substances-are-different/", tag="Prescribing", tagclass="tag--blue"),
        S.card("How shrinkiatry discloses interests", "The financial interests behind the network, stated plainly.", "/disclosures/", tag="Transparency", tagclass="tag--olive"),
    ], 3),
    [("Is what I tell a psychiatrist always confidential?", "Confidentiality is central but not absolute. Specific, limited situations, such as a serious and imminent risk of harm, can require disclosure, and laws vary by place. Good practice explains these limits up front."),
     ("What is decision-making capacity?", "Capacity is the ability to understand relevant information, appreciate one's situation, reason through options, and communicate a choice. It is specific to a decision and can change over time."),
     ("Is this page legal advice?", "No. It's educational commentary about how psychiatric ethics are defined. It isn't legal advice and isn't a substitute for a clinician's judgment, an ethics consultation, or a lawyer.")],
    [("American Psychiatric Association, Principles of Medical Ethics with Annotations for Psychiatry.", "https://www.psychiatry.org/psychiatrists/practice/ethics"),
     ("American Medical Association, Code of Medical Ethics.", "https://www.ama-assn.org/delivering-care/ethics/code-medical-ethics-overview"),
     ("American Psychiatric Association, resource documents on confidentiality and consent.", "https://www.psychiatry.org/psychiatrists/practice")],
    [("Documentation", "/business/why-documentation-shapes-care/"), ("Controlled substances", "/business/why-controlled-substances-are-different/"),
     ("Telepsychiatry", "/technology/what-telepsychiatry-changes/"), ("Disclosures", "/disclosures/"), ("Culture", "/culture/")],
    ["shrinkopedia", "shrinkmd", "shrinknetwork"],
    "APA principles of medical ethics, the AMA Code of Medical Ethics, and APA resource documents",
    medical=True,
))

# ============================== LEADERSHIP ==============================
PAGES.append(hub(
    "leadership", "/leadership/", "Leadership in psychiatry", "Leadership in psychiatry: running teams, practices, and systems",
    "Psychiatrists end up leading more than they're trained to: group practices, departments, service lines, residents, and the committees that decide how care gets delivered.",
    "How psychiatrists lead practices, departments, and care teams: clinical leadership, supervision, and systems thinking in psychiatry.",
    "psychiatry leadership, clinical leadership, medical supervision, mentorship, healthcare leadership",
    "Leadership is a real skill set psychiatry needs, not a soft extra. Psychiatrists run group practices, chair departments, supervise residents, and sit on the committees that shape care, yet leadership, communication, and conflict management are rarely formal parts of training. This page treats clinical leadership seriously and connects it to the business, systems, and culture of the field.",
    ["Psychiatrists lead practices, departments, and teams, often without formal leadership training.",
     "Running a practice is itself a leadership job: hiring, supervising, and setting the standard.",
     "Systems-level models like Collaborative Care ask psychiatrists to lead and consult, not just treat.",
     "Mentorship and supervision are how the next cohort is trained."],
    [("gap", "The leadership gap"), ("practice", "Leading a practice"), ("systems", "Leading at the systems level"),
     ("teaching", "Mentorship and supervision"), ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="gap">The leadership gap</h2>
<p>The profession asks psychiatrists to lead in ways training rarely prepares them for. They supervise, hire, chair, and direct, and they do it while carrying clinical responsibility. Naming that gap is the first step to closing it, and it connects directly to the business and culture sections of shrinkiatry.</p>

<h2 id="practice">Leading a practice</h2>
<p>Owning a practice is a leadership job before it's a financial one: setting the clinical standard, hiring and supervising staff, and building the systems that let good care happen consistently. The operational side is covered in <a href="/business/how-private-psychiatry-practices-work/">how private practices work</a>.</p>

<h2 id="systems">Leading at the systems level</h2>
<p>Some of the most consequential leadership is at the systems level. In the Collaborative Care Model, a consulting psychiatrist guides a primary care team's approach to a whole caseload rather than treating each patient directly, a role that is as much leadership and teaching as it is clinical. The model and its evidence are covered in <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>.</p>

<h2 id="teaching">Mentorship and supervision</h2>
<p>Teaching the next cohort is part of the work. Supervision of residents and students is woven through training, described in <a href="/careers/how-psychiatry-residency-works/">how residency works</a>, and it's where clinical judgment is transmitted from one generation to the next.</p>
""",
    S.card_grid([
        S.card("Running a practice is a leadership job", "Hiring, supervising, and setting the standard inside an independent practice.", "/business/how-private-psychiatry-practices-work/", tag="Practice", tagclass="tag--blue"),
        S.card("The Collaborative Care Model", "How one psychiatrist can guide care across a whole primary care population.", "/economics/the-psychiatrist-shortage/", tag="Systems", tagclass="tag--blue"),
    ], 2),
    [("Do psychiatrists get leadership training?", "Rarely as a formal part of residency. Leadership, communication, and conflict management are usually learned on the job, which is part of why the profession needs to treat them as real skills."),
     ("What is a consulting psychiatrist?", "In team-based models like Collaborative Care, a consulting psychiatrist advises a primary care team and a care manager on a caseload rather than seeing most patients directly, extending their reach and acting as a clinical leader.")],
    [("APA, integrated and collaborative care leadership resources.", "https://www.psychiatry.org/psychiatrists/practice/professional-interests/integrated-care/learn"),
     ("AMA, physician leadership resources.", "https://www.ama-assn.org/")],
    [("Private practice", "/business/how-private-psychiatry-practices-work/"), ("The shortage", "/economics/the-psychiatrist-shortage/"),
     ("How residency works", "/careers/how-psychiatry-residency-works/"), ("Culture", "/culture/")],
    ["shariqrefai", "shrinkmd", "shrinknetwork"],
    "APA integrated-care resources and clinical-leadership literature",
    reading="6 min read",
))

# ============================== INNOVATION ==============================
PAGES.append(hub(
    "innovation", "/innovation/", "Innovation in psychiatry", "Innovation in psychiatry: what's genuinely changing the field",
    "Psychiatry attracts big claims about the future, from genetic tests that promise to pick your medication to apps that promise to replace your therapist. The job here is to tell the difference between real progress and marketing.",
    "The future of psychiatry: measurement-based care, digital therapeutics, precision approaches, and AI, with an honest read on the evidence.",
    "future of psychiatry, measurement-based care, digital therapeutics, precision psychiatry, psychiatry innovation",
    "Innovation at shrinkiatry means tracking what's genuinely changing in how psychiatric care is measured, delivered, and improved, while keeping the same honest standard about evidence that runs through the rest of the network. Some claims are real and gaining support; some are marketing wearing a lab coat. This page separates the two and links to deeper coverage.",
    ["Not every 'breakthrough' in psychiatry is supported; the job is to weigh the evidence.",
     "Measurement-based care, tracking outcomes with simple scales, is an underrated, evidence-backed shift.",
     "AI's most real near-term impact is administrative, not diagnostic.",
     "Digital therapeutics and precision approaches are promising but uneven in evidence."],
    [("standard", "The standard for 'innovation'"), ("mbc", "Measurement-based care"),
     ("ai", "AI and automation"), ("frontier", "The frontier, read honestly"),
     ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="standard">The standard for 'innovation'</h2>
<p>When something works, we'll say so. When the data is thin, we'll say that too. That standard matters most in a field where confident claims outpace evidence. The goal is to track genuine change without getting swept up in hype, the same discipline we apply in <a href="/technology/ai-in-psychiatry/">AI in psychiatry</a>.</p>

<h2 id="mbc">Measurement-based care</h2>
<p>One of the most underrated shifts is also one of the least flashy: measurement-based care, the practice of tracking outcomes with simple validated scales and adjusting treatment accordingly. It's a quiet, evidence-supported improvement in how care is delivered, and it pairs well with the data tools covered in <a href="/technology/">technology</a>.</p>

<h2 id="ai">AI and automation</h2>
<p>The most consequential current technology is artificial intelligence, and its real near-term impact is administrative rather than diagnostic. Ambient documentation tools are already saving clinician time; broader clinical AI is earlier and needs validation. The grounded account is in <a href="/technology/ai-in-psychiatry/">AI in psychiatry</a>.</p>

<h2 id="frontier">The frontier, read honestly</h2>
<p>Further out sit digital therapeutics, precision-psychiatry approaches like pharmacogenomic testing, and other tools that promise to personalize care. Some have real, if narrow, evidence; others are oversold. As the field matures and telemedicine rules settle, covered in <a href="/technology/what-telepsychiatry-changes/">telepsychiatry</a>, the honest read on each is what this section will keep providing.</p>
""",
    S.card_grid([
        S.card("AI in psychiatry", "The most consequential technology story in the field right now, assessed honestly.", "/technology/ai-in-psychiatry/", tag="Technology", tagclass="tag--blue"),
        S.card("The future of telepsychiatry", "What changes as the rules settle and remote care becomes ordinary.", "/technology/what-telepsychiatry-changes/", tag="Access", tagclass="tag--blue"),
    ], 2),
    [("Does pharmacogenomic testing pick the right medication?", "The evidence is mixed and narrower than marketing suggests. Some tests offer limited guidance for specific situations, but they don't reliably predict the best medication for a given person. Treat strong claims with caution."),
     ("Is measurement-based care actually new?", "The tools aren't new, but consistent use is. Routinely tracking outcomes with validated scales and adjusting treatment is an evidence-supported practice that many settings are only now adopting widely.")],
    [("APA, integrated care and measurement-based care resources.", "https://www.psychiatry.org/psychiatrists/practice/professional-interests/integrated-care/learn"),
     ("AnxietyResearch, evidence summaries on emerging treatments.", "https://anxietyresearch.org")],
    [("AI in psychiatry", "/technology/ai-in-psychiatry/"), ("Telepsychiatry", "/technology/what-telepsychiatry-changes/"),
     ("Technology", "/technology/"), ("Research Digest", "/research-digest/")],
    ["anxietyresearch", "shrinkopedia", "shrinknetwork"],
    "APA measurement-based care resources and peer-reviewed evidence summaries",
    reading="6 min read",
))

# ============================== RESEARCH DIGEST ==============================
PAGES.append(hub(
    "research-digest", "/research-digest/", "Research Digest", "Research Digest: practice-relevant psychiatry research, summarized honestly",
    "Psychiatrists, residents, and the people who write about them can't read everything, and most coverage overstates what a single study shows. The Research Digest summarizes practice-relevant papers the way a careful colleague would.",
    "Practice-relevant psychiatric research, guidelines, and policy changes, summarized honestly with the limits of the evidence stated plainly.",
    "psychiatry research, evidence-based psychiatry, clinical guidelines, research summaries",
    "The Research Digest summarizes practice-relevant papers, guidelines, and policy changes, including the part where we say what a study doesn't prove. Every entry follows the same discipline as the rest of the network: claims tied to primary sources, the limits of the evidence stated plainly, and no breathless takes. When the field's standard references update, this is where shrinkiatry tracks what changed and why it matters.",
    ["Most coverage of psychiatric research overstates what one study shows; the Digest corrects for that.",
     "Every summary ties claims to primary sources and states the limits of the evidence.",
     "Strong, replicated findings, like the Collaborative Care evidence base, are flagged clearly.",
     "How evidence is weighed is documented in the evidence methodology."],
    [("why", "Why a digest"), ("discipline", "The discipline"), ("examples", "What strong evidence looks like"),
     ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="why">Why a digest</h2>
<p>The Research Digest exists because no one can read everything, and because most coverage of psychiatric research treats a single study as a settled fact. This section summarizes papers, guidelines, and policy changes for busy readers, with sourcing and honesty about limits.</p>

<h2 id="discipline">The discipline</h2>
<p>Every entry ties claims to primary sources and conveys the strength and limits of the evidence: how large or replicated a finding is, what population it applies to, and what it doesn't prove. The standard each entry is held to is documented in <a href="/evidence-methodology/">how we evaluate evidence</a>.</p>

<h2 id="examples">What strong evidence looks like</h2>
<p>Some findings are genuinely robust. The Collaborative Care Model, supported by more than 80 randomized trials, is one of psychiatry's strongest access-expanding findings, covered in <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>. Early evidence on ambient AI documentation is promising but newer, covered in <a href="/technology/ai-in-psychiatry/">AI in psychiatry</a>. Distinguishing the two is the point of this section.</p>
""",
    S.card_grid([
        S.card("The evidence behind Collaborative Care", "More than 80 trials, one of psychiatry's strongest access-expanding findings.", "/economics/the-psychiatrist-shortage/", tag="Evidence", tagclass="tag--blue"),
        S.card("What ambient AI documentation studies show", "Early data on time saved, burnout, and the catches.", "/technology/ai-in-psychiatry/", tag="Technology", tagclass="tag--blue"),
        S.card("How we evaluate evidence", "The standard every digest entry is held to.", "/evidence-methodology/", tag="Method", tagclass="tag--olive"),
    ], 3),
    [("How is research chosen for the Digest?", "We prioritize research that's relevant to how the profession actually works, guidelines, landmark trials, and policy changes, and we summarize it with sourcing and explicit limits rather than chasing headlines."),
     ("Does one study prove a treatment works?", "Rarely. A single study is a data point, not a settled fact. Strength comes from replication, sample size, and consistency across populations, which is what our evidence methodology weighs.")],
    [("AnxietyResearch, sourced research summaries.", "https://anxietyresearch.org"),
     ("Unutzer et al., Collaborative Care Model, American Journal of Psychiatry.", "https://psychiatryonline.org/doi/10.1176/appi.ajp.2015.15010017")],
    [("How we evaluate evidence", "/evidence-methodology/"), ("The shortage", "/economics/the-psychiatrist-shortage/"),
     ("AI in psychiatry", "/technology/ai-in-psychiatry/"), ("Reports", "/reports/")],
    ["anxietyresearch", "shrinkopedia", "shrinknetwork"],
    "Peer-reviewed literature, clinical guidelines, and documented evidence methodology",
    reading="5 min read",
))

# ============================== REPORTS ==============================
PAGES.append(hub(
    "reports", "/reports/", "Reports", "Reports: data-driven briefs on the state of the profession",
    "Reports are shrinkiatry's deeper, data-driven pieces: longer briefs that pull together public datasets and primary sources to describe the state of the profession, with the sources shown and the methodology described.",
    "Data-driven briefs on the state of psychiatry, built from public sources: workforce, telepsychiatry, burnout, technology adoption, and compensation.",
    "psychiatry reports, psychiatry workforce report, telepsychiatry report, psychiatry burnout report",
    "Where an article explains one idea, a report assembles the numbers behind a whole topic. These are built from public data anyone could find, including HRSA workforce projections, ACGME training data, federal surveys, and peer-reviewed research, organized so the picture is legible. Each report states what the data can and can't tell you. Planned reports cover the workforce, telepsychiatry, burnout, technology adoption, and compensation.",
    ["Reports assemble public data into a legible picture of the profession.",
     "Sources are shown and methodology described, so claims can be checked.",
     "Each report states what the data can and can't tell you.",
     "Standing reports are kept current as the underlying data updates."],
    [("what", "What a report is"), ("sources", "Built from public data"), ("standing", "Standing reports"),
     ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="what">What a report is</h2>
<p>A report is a longer, data-driven brief that pulls together public datasets and primary sources to describe a whole topic, with the sources shown and the methodology described. It's the format for questions that need numbers, not just explanation.</p>

<h2 id="sources">Built from public data</h2>
<p>Reports use data anyone could find, including <a href="https://bhw.hrsa.gov/data-research" target="_blank" rel="noopener noreferrer">HRSA workforce projections</a>, ACGME training data, federal surveys, and peer-reviewed research, organized so the picture is legible. Each report states what the data can and can't support, consistent with our <a href="/evidence-methodology/">evidence methodology</a>.</p>

<h2 id="standing">Standing reports</h2>
<p>Some topics get standing reports kept current as the data updates: the workforce (<a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>), burnout (<a href="/culture/burnout-in-psychiatry/">burnout in psychiatry</a>), and telepsychiatry (<a href="/technology/what-telepsychiatry-changes/">what telepsychiatry changes</a>). Compensation and technology-adoption reports are planned.</p>
""",
    S.card_grid([
        S.card("The Psychiatrist Shortage", "Our standing brief on workforce supply, demand, and access.", "/economics/the-psychiatrist-shortage/", tag="Workforce report", tagclass="tag--blue"),
        S.card("Burnout in Psychiatry", "What national surveys show about burnout in the specialty, in context.", "/culture/burnout-in-psychiatry/", tag="Burnout report", tagclass="tag--blue"),
        S.card("Telepsychiatry, after the cliff", "How remote prescribing rules and practice patterns are settling.", "/technology/what-telepsychiatry-changes/", tag="Telepsychiatry report", tagclass="tag--olive"),
    ], 3),
    [("Where does the data come from?", "From public sources such as HRSA workforce projections, ACGME training data, federal surveys, and peer-reviewed research, all cited so the figures can be checked."),
     ("Are these reports predictions?", "Some include projections from sources like HRSA, which we describe as projections rather than fixed forecasts. Each report states what the data can and can't tell you.")],
    [("HRSA Bureau of Health Workforce, projections and briefs.", "https://bhw.hrsa.gov/data-research"),
     ("ACGME data resources.", "https://www.acgme.org/about/publications-and-resources/graduate-medical-education-data-resource-book/")],
    [("The shortage", "/economics/the-psychiatrist-shortage/"), ("Burnout", "/culture/burnout-in-psychiatry/"),
     ("Telepsychiatry", "/technology/what-telepsychiatry-changes/"), ("Research Digest", "/research-digest/")],
    ["anxietyresearch", "shrinkmd", "shrinknetwork"],
    "HRSA workforce data, ACGME training data, and federal surveys",
    reading="5 min read",
))

# ============================== INTERVIEWS ==============================
PAGES.append(hub(
    "interviews", "/interviews/", "Interviews", "Interviews: conversations with the people who build and study psychiatry",
    "Some of what's worth knowing about the profession only comes out in conversation. This section talks with psychiatrists, researchers, founders, and leaders about how the work actually gets done.",
    "Conversations with psychiatrists, researchers, founders, and leaders about how the profession works and where it's heading.",
    "psychiatry interviews, psychiatrist interviews, mental health founders, psychiatry leaders",
    "The Interviews section is where shrinkiatry talks with psychiatrists, researchers, founders, department chairs, authors, and the technologists building tools for the field, about how the work actually gets done and where it's heading. Interviews are edited for clarity and length, clearly distinguished from reported articles and opinion. The people we talk with speak for themselves; their views aren't the network's. This section is being built.",
    ["Interviews surface knowledge that only comes out in conversation.",
     "They're edited for clarity and clearly separated from reported articles and opinion.",
     "Interviewees speak for themselves; their views aren't the network's.",
     "The first conversations are in progress."],
    [("why", "Why interviews"), ("standard", "How they're handled"), ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="why">Why interviews</h2>
<p>Reported articles and digests stick to what's established. Conversations add something different: how the work feels from inside, what a founder learned building a practice, what a researcher thinks the data misses. That's what this section is for.</p>

<h2 id="standard">How they're handled</h2>
<p>Interviews are edited for clarity and length, and clearly distinguished from reported articles and from <a href="/opinion/">opinion</a>. Interviewees speak for themselves; their views aren't the network's. For the founder's-eye view of building independent telepsychiatry, see <a href="https://shariqrefai.com" target="_blank" rel="noopener noreferrer">Shariq Refai</a>.</p>
""",
    S.card_grid([
        S.card("A founder's view of telepsychiatry", "From the network's own founder, on building independent telepsychiatry.", "https://shariqrefai.com", tag="Founder", tagclass="tag--blue", more="Visit"),
        S.card("Suggest an interview", "Know someone whose work belongs here? Tell us.", "/contact/", tag="Get in touch", tagclass="tag--olive", more="Contact"),
    ], 2),
    [("Who do you interview?", "Psychiatrists, residents, researchers, founders, department chairs, authors, and technologists building tools for the field, anyone whose work helps explain how the profession operates and where it's heading."),
     ("Do interviewees' views represent shrinkiatry?", "No. Interviews are edited for clarity, and interviewees speak for themselves. Their views aren't the network's, and interviews are clearly separated from reported articles and opinion.")],
    [("shrinkiatry editorial standards.", "https://shrinkiatry.com/editorial-standards/")],
    [("Opinion", "/opinion/"), ("Research Digest", "/research-digest/"), ("Culture", "/culture/"), ("Contact", "/contact/")],
    ["shariqrefai", "shrinkmd", "shrinknetwork"],
    "Edited primary interviews, clearly distinguished from reported and opinion content",
    reading="4 min read",
))

# ============================== OPINION ==============================
PAGES.append(hub(
    "opinion", "/opinion/", "Opinion", "Opinion: clearly labeled arguments about the direction of psychiatry",
    "Opinion is where shrinkiatry makes arguments rather than just describing the field, and it's always labeled as such. The line between reporting and arguing is kept bright on purpose.",
    "Clearly labeled editorials and arguments about psychiatry: ethics, policy, technology, and the direction of the profession.",
    "psychiatry opinion, psychiatry editorials, mental health policy, psychiatry commentary",
    "Reported articles and digests stick to what's established; this section is for thought pieces about ethics, policy, technology, and the choices the profession faces. Opinions published here are reasoned and sourced where claims are factual, but they're positions, not consensus, and they're meant to be argued with. Keeping the line between describing the profession and arguing about it visible is part of the editorial standard.",
    ["Opinion is for arguments, always clearly labeled and separated from reporting.",
     "Pieces are reasoned and sourced where claims are factual.",
     "Positions are meant to be argued with, not treated as consensus.",
     "The bright line between reporting and opinion is an editorial commitment."],
    [("why", "Why label opinion"), ("standard", "The standard for opinion"), ("read-next", "Read next"), ("faq", "Common questions")],
    """
<h2 id="why">Why label opinion</h2>
<p>Trust depends on readers knowing what they're reading. shrinkiatry keeps a bright line between reported, sourced explanation and argument. Opinion is where the site takes positions; everything here is marked as such, consistent with our <a href="/editorial-standards/">editorial standards</a>.</p>

<h2 id="standard">The standard for opinion</h2>
<p>Opinions here are reasoned, and factual claims within them are sourced, but the conclusions are positions, not consensus. They're meant to be argued with. If you think a piece gets it wrong, that's the point of running it under a clear label, and our <a href="/corrections/">corrections policy</a> still applies to any factual error.</p>
""",
    S.card_grid([
        S.card("The case for treating documentation as care", "Why the note deserves more respect than the system gives it.", "/business/why-documentation-shapes-care/", tag="Editorial", tagclass="tag--clay"),
        S.card("On hype in mental health technology", "How to read big claims about AI and apps without cynicism or credulity.", "/technology/ai-in-psychiatry/", tag="Editorial", tagclass="tag--clay"),
    ], 2),
    [("Is opinion content sourced?", "Factual claims within opinion pieces are sourced, but the conclusions are positions, not consensus. Opinion is clearly labeled and kept separate from reported articles."),
     ("What if an opinion piece has a factual error?", "Our corrections policy applies to factual errors anywhere on the site, including opinion. The argument is the author's; the facts still have to be right.")],
    [("shrinkiatry editorial standards.", "https://shrinkiatry.com/editorial-standards/"),
     ("shrinkiatry corrections policy.", "https://shrinkiatry.com/corrections/")],
    [("Editorial standards", "/editorial-standards/"), ("AI in psychiatry", "/technology/ai-in-psychiatry/"),
     ("Documentation", "/business/why-documentation-shapes-care/"), ("Interviews", "/interviews/")],
    ["shariqrefai", "anxietyresearch", "shrinknetwork"],
    "Reasoned argument with sourced factual claims, clearly labeled as opinion",
    reading="4 min read",
))

# ============================== START HERE ==============================
def _start_cards():
    rows = [
        ("Understand the profession", "Start with the map of how psychiatry is organized.", "/psychiatry-operating-room/", "Profession", "tag--blue"),
        ("Understand training", "How psychiatrists are educated, from medical school to board certification.", "/careers/", "Training", "tag--blue"),
        ("Understand the business", "How practices are built, paid, and run.", "/business/", "Business", "tag--blue"),
        ("Understand telepsychiatry", "What virtual care changed, and what it didn't.", "/technology/what-telepsychiatry-changes/", "Technology", "tag--olive"),
        ("Understand the economics", "Why access is hard and appointments are short.", "/economics/the-psychiatrist-shortage/", "Economics", "tag--olive"),
        ("Understand the ethics", "The boundaries and duties behind responsible care.", "/ethics/", "Ethics", "tag--olive"),
        ("Read behind-the-scenes commentary", "The culture and identity of the profession.", "/culture/", "Culture", "tag--clay"),
        ("Find clinical care", "If you need a psychiatrist, this is the network's practice.", "https://shrinkmd.com", "shrinkMD", "tag--clay"),
    ]
    return S.card_grid([S.card(t, d, h, tag=tn, tagclass=tc, more="Go") for t, d, h, tn, tc in rows], 4)

_sh_hero = """<section class="section section--slate section--tight"><div class="wrap">
<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">Start Here</span></nav>
<span class="eyebrow">Start here</span><h1 class="mt-1">What part of psychiatry are you trying to understand?</h1>
<p class="hero__sub mt-2" style="max-width:60ch">shrinkiatry covers the whole profession, so it helps to start from a question. Pick the one closest to yours.</p>
</div></section>"""

PAGES.append({
    "slug": "start-here", "active": "/start-here/",
    "title": "Start Here | shrinkiatry",
    "desc": "New to shrinkiatry? Start here. Tell us what part of psychiatry you're trying to understand, and we'll point you somewhere useful.",
    "keywords": "psychiatry profession, understand psychiatry, psychiatry guide, shrinkiatry start here",
    "breadcrumbs": [("Home", "/"), ("Start Here", None)],
    "body": (
        _sh_hero
        + '<section class="section section--surface"><div class="wrap"><div class="maxread flow">'
        + S.why_trust_box()
        + '<p class="mt-3">shrinkiatry is the profession layer of The Shrink Network. It explains how psychiatry is trained, paid, regulated, and practiced, rather than explaining specific conditions or medications, which other sites in the network do well. If you came here looking for the encyclopedia of mental health, that\'s <a href="https://shrinkopedia.com" target="_blank" rel="noopener noreferrer">Shrinkopedia</a>. If you want medication guides, that\'s <a href="https://psychiatryrx.org" target="_blank" rel="noopener noreferrer">PsychiatryRx</a>. If you need care, that\'s <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a>. If you want to understand the profession itself, you\'re in the right place.</p></div></div></section>'
        + f'<section class="section section--tint"><div class="wrap">{_start_cards()}</div></section>'
        + f'<section class="section section--surface"><div class="wrap"><div class="maxread">{S.network_continue(["shrinkopedia","psychiatryrx","shrinkmd","shrinknetwork"])}</div></div></section>'
    ),
})
