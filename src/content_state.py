# -*- coding: utf-8 -*-
"""The State of Psychiatry: data-driven briefs on the profession's pressure points."""
import engine as S

PAGES = []

def _brief_schema(title, desc, slug):
    return {"@type": "MedicalWebPage", "name": title, "description": desc,
            "url": "https://shrinkiatry.com/state-of-psychiatry/" + slug + "/",
            "isPartOf": {"@id": "https://shrinkiatry.com/#website"},
            "author": {"@id": "https://shrinkiatry.com/#refai"},
            "reviewedBy": {"@id": "https://shrinkiatry.com/#refai"},
            "lastReviewed": "2026-06-27"}

def _faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def brief(slug, kicker, title, lede, desc, quick, body, takeaways, toc, faq, sources, related, network, keywords):
    meta = {
        "breadcrumbs": [("Home", "/"), ("State of Psychiatry", "/state-of-psychiatry/"), (title, None)],
        "kicker": kicker, "title": title, "lede": lede, "quick_answer": quick,
        "takeaways": takeaways, "toc": toc, "body": body, "faq": faq,
        "related": related, "sources": sources, "network": network,
        "updated": "June 27, 2026", "reading_time": "6 min read",
    }
    schema = [_brief_schema(title, desc, slug)]
    if faq:
        schema.append(_faq_schema(faq))
    PAGES.append({
        "slug": "state-of-psychiatry/" + slug, "active": "/state-of-psychiatry/",
        "title": title + " | shrinkiatry", "desc": desc, "keywords": keywords,
        "breadcrumbs": meta["breadcrumbs"], "schema": schema, "og_type": "article",
        "body": S.article_shell(meta),
    })

# ---------------- Hub ----------------
def _hub():
    cards = S.card_grid([
        S.card("The psychiatrist shortage", "How deep the workforce gap runs, where it concentrates, and what the projections say.", "/state-of-psychiatry/psychiatrist-shortage/", tag="Workforce", tagclass="tag--blue"),
        S.card("Telepsychiatry", "The fastest structural change in modern psychiatry, by the numbers, and what stuck after the surge.", "/state-of-psychiatry/telepsychiatry/", tag="Access", tagclass="tag--blue"),
        S.card("Burnout", "What national surveys actually show about burnout in psychiatry, and why it's a systems problem.", "/state-of-psychiatry/burnout/", tag="Workforce", tagclass="tag--olive"),
        S.card("AI in psychiatry", "Where artificial intelligence is genuinely landing in the field, and where the claims outrun the evidence.", "/state-of-psychiatry/ai/", tag="Technology", tagclass="tag--olive"),
    ], 2)
    intro = (
        "<p>The State of Psychiatry is shrinkiatry's running read on the pressure points shaping the profession: the workforce shortage, the telepsychiatry shift, burnout, and the arrival of artificial intelligence. Each brief gathers the most credible public data, states plainly what it does and doesn't show, and links to the explainer pieces that go deeper.</p>"
        "<p>These aren't opinion pieces, and they aren't patient education. They're the profession-intelligence layer: the numbers a journalist, a policymaker, a trainee, or a curious patient would want, sourced and dated, written and reviewed by a board-certified psychiatrist. Where the evidence is thin or contested, we say so rather than rounding up to a clean headline.</p>"
        "<p>Data changes, so these briefs carry a last-reviewed date and get revisited as new figures land. This is education and commentary, not medical advice. For care, the network's clinical practice is <a href=\"https://shrinkmd.com\" target=\"_blank\" rel=\"noopener noreferrer\">shrinkMD</a>.</p>"
    )
    body = (
        '<section class="section section--slate section--tight"><div class="wrap">'
        '<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">State of Psychiatry</span></nav>'
        '<span class="eyebrow">The State of Psychiatry</span><h1 class="mt-1">The State of Psychiatry</h1>'
        '<p class="hero__sub mt-2" style="max-width:60ch">A sourced, regularly updated read on the forces reshaping the profession: the workforce shortage, telepsychiatry, burnout, and AI. The numbers, the trend, and the honest limits of the evidence.</p>'
        '</div></section>'
        f'<section class="section section--surface"><div class="wrap"><div class="maxread flow">{intro}</div></div></section>'
        f'<section class="section section--tint"><div class="wrap">{cards}</div></section>'
        f'<section class="section section--surface section--tight"><div class="wrap"><div class="maxread flow">{S.why_trust_box()}</div></div></section>'
        f'<section class="section section--tint"><div class="wrap"><div class="maxread">{S.network_continue(["shrinkopedia","psychiatryrx","shrinkmd","shariqrefai","shrinknetwork"])}<div class="mt-3">{S.disclaimer_box()}</div></div></div></section>'
    )
    _itemlist = {"@type": "ItemList", "name": "The State of Psychiatry", "numberOfItems": 4,
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": "https://shrinkiatry.com/state-of-psychiatry/" + s + "/"}
                 for i, (n, s) in enumerate([
                     ("The psychiatrist shortage", "psychiatrist-shortage"),
                     ("Telepsychiatry", "telepsychiatry"),
                     ("Burnout", "burnout"),
                     ("AI in psychiatry", "ai")])]}
    PAGES.append({
        "slug": "state-of-psychiatry", "active": "/state-of-psychiatry/",
        "title": "The State of Psychiatry | shrinkiatry",
        "desc": "A sourced, regularly updated read on the forces reshaping psychiatry: the workforce shortage, telepsychiatry, burnout, and AI.",
        "keywords": "state of psychiatry, psychiatry workforce, psychiatry trends, psychiatry statistics",
        "breadcrumbs": [("Home", "/"), ("State of Psychiatry", None)],
        "schema": [_itemlist], "body": body,
    })

_hub()

# ---------------- Shortage brief ----------------
brief(
    "psychiatrist-shortage", "Workforce", "The psychiatrist shortage",
    "The gap between how many psychiatrists the country has and how many it needs is one of the defining facts of American mental-health care. Here's what the public data shows, and what it doesn't.",
    "How bad is the psychiatrist shortage? Roughly half of the US population lives in a federally designated mental-health workforce shortage area, a large share of counties have no practicing psychiatrist, and the workforce is aging. Projections point to a continued shortfall, driven as much by distribution and pay as by raw numbers.",
    "Roughly half of Americans live in a designated mental-health shortage area, many counties have no psychiatrist, and the workforce is aging. Distribution and pay matter as much as headcount.",
    "<h2 id=\"scale\">The scale</h2>"
    "<p>The federal government designates Health Professional Shortage Areas where the supply of mental-health providers falls short of need. Roughly half of the United States population lives in one. The Health Resources and Services Administration tracks these designations, and they cover a large and persistent share of the country rather than a few isolated pockets.</p>"
    "<h2 id=\"distribution\">It's a distribution problem, not just a headcount</h2>"
    "<p>Psychiatrists cluster in metropolitan areas and around academic medical centers. A large share of US counties have no practicing psychiatrist at all, which means the national average understates how thin coverage is in rural and lower-income areas. Adding clinicians helps only if they practice where the need is, which is why distribution sits at the center of the problem.</p>"
    "<h2 id=\"aging\">An aging workforce</h2>"
    "<p>The psychiatric workforce skews older than many specialties, with a substantial portion at or near retirement age. As those clinicians retire, the pipeline of new psychiatrists has to run fast just to hold steady. Residency slots, the rate-limiting step in producing psychiatrists, have grown but not at a pace that closes the gap quickly.</p>"
    "<h2 id=\"projections\">What the projections say</h2>"
    "<p>Workforce analyses, including those summarized by the Association of American Medical Colleges and federal projections, point to a continued psychiatrist shortfall for years to come. The exact numbers vary by model and by assumptions about demand, telehealth, and team-based care, so treat any single figure with caution. The direction, though, is consistent across sources.</p>"
    "<h2 id=\"levers\">The levers that actually move it</h2>"
    "<p>Because the problem is partly distribution and pay, the fixes aren't only about training more psychiatrists. Telepsychiatry extends a clinician's reach across a whole state. The collaborative care model lets one psychiatrist support many primary-care patients. Loan forgiveness and incentives aim clinicians toward underserved areas. Each stretches a scarce workforce further, which in the near term matters more than the slow work of growing the pipeline.</p>",
    ["Roughly half of the US population lives in a federally designated mental-health shortage area.",
     "A large share of counties have no practicing psychiatrist, so the shortage is heavily about distribution.",
     "The workforce is aging, and residency slots haven't grown fast enough to close the gap quickly.",
     "Telepsychiatry, collaborative care, and targeted incentives stretch the existing workforce in the near term."],
    [("scale", "The scale"), ("distribution", "A distribution problem"),
     ("aging", "An aging workforce"), ("projections", "What projections say"), ("levers", "The levers that move it")],
    [("Is the psychiatrist shortage getting better or worse?", "Most workforce analyses project a continued shortfall for years, though exact figures vary by model. The workforce is aging and demand is rising, so the near-term pressure is more likely to grow than ease."),
     ("Would training more psychiatrists fix it?", "Only partly. Because the shortage is heavily about where psychiatrists practice and how care is paid for, distribution and team-based models matter alongside the slow work of expanding residency slots.")],
    [("Health Resources and Services Administration, mental-health shortage areas.", "https://data.hrsa.gov/topics/health-workforce/shortage-areas"),
     ("Association of American Medical Colleges, physician workforce projections.", "https://www.aamc.org/data-reports/workforce/report/physician-workforce-projections"),
     ("American Psychiatric Association, the Collaborative Care Model.", "https://www.psychiatry.org/psychiatrists/practice/professional-interests/integrated-care/learn")],
    [("The psychiatrist shortage, explained", "/economics/the-psychiatrist-shortage/"),
     ("Why getting an appointment is so hard", "/decoder/why-getting-an-appointment-is-hard/"),
     ("The Operating Room: Economics", "/psychiatry-operating-room/#room-08")],
    ["shrinkmd", "shrinkopedia", "shrinknetwork"],
    "psychiatrist shortage statistics, mental health workforce shortage, psychiatry workforce data",
)

# ---------------- Telepsychiatry brief ----------------
brief(
    "telepsychiatry", "Access", "Telepsychiatry: the state of virtual care",
    "Telepsychiatry went from a niche service to a default channel in the span of a few years. It's the fastest structural change modern psychiatry has seen, and the data on what stuck is now clear enough to read.",
    "How big is telepsychiatry now? After a massive pandemic-era surge, psychiatry retained virtual care more than almost any other specialty. A large and durable share of psychiatric visits are now delivered by video or phone, reshaping access, overhead, and geography while the core clinical interview stayed largely intact.",
    "Psychiatry kept telehealth more than any other specialty after the pandemic surge. A durable share of visits are now virtual, reshaping access and overhead while the interview itself stayed intact.",
    "<h2 id=\"surge\">The surge and what remained</h2>"
    "<p>Before 2020, telepsychiatry was a small slice of care. During the pandemic it became, briefly, the dominant way psychiatric visits happened. What makes psychiatry distinct is how much of that shift stuck. Across analyses of telehealth use, mental-health and psychiatric care retained virtual delivery at far higher rates than other specialties, because the core encounter is a conversation that travels well over video.</p>"
    "<h2 id=\"why-psychiatry\">Why psychiatry fit telehealth so well</h2>"
    "<p>Most specialties depend on a physical exam or a procedure. Psychiatry's central tool is the clinical interview, plus observation that a camera can carry reasonably well. That's why the field absorbed video care faster and kept it longer. For many follow-ups and many patients, the remote visit is clinically comparable to the in-person one, which is what the retention data reflects.</p>"
    "<h2 id=\"access\">What it changed about access</h2>"
    "<p>Telepsychiatry widened the pool of clinicians a patient can reach to anyone licensed in their state, which matters most for rural and underserved areas with few local psychiatrists. It also cut the overhead of a physical office, lowering one barrier to independent practice. Both effects push, modestly, against the access problem, though state licensing still limits how far a single clinician's reach extends.</p>"
    "<h2 id=\"limits\">The limits and the open questions</h2>"
    "<p>Virtual care isn't universal. Some presentations need an in-person exam, some patients lack private space or reliable connectivity, and the digital divide can widen gaps as easily as close them. The rules for prescribing controlled substances by telemedicine remain in flux, governed by federal flexibilities that have been repeatedly extended while a permanent framework is settled. That uncertainty is the biggest open question hanging over the field's virtual future.</p>",
    ["Psychiatry retained telehealth at higher rates than almost any other specialty after the pandemic surge.",
     "The fit is structural: psychiatry's core tool is the clinical interview, which travels well over video.",
     "Telepsychiatry widens access by state and cuts office overhead, though licensing still bounds a clinician's reach.",
     "Controlled-substance prescribing by telemedicine remains governed by changeable federal rules, the field's biggest open question."],
    [("surge", "The surge and what remained"), ("why-psychiatry", "Why psychiatry fit"),
     ("access", "What it changed about access"), ("limits", "Limits and open questions")],
    [("Is telepsychiatry as effective as in-person care?", "For many follow-ups and many patients, research finds remote psychiatric care clinically comparable to in-person, which is partly why it was retained. Some presentations still need an in-person exam."),
     ("Can I get a controlled substance through telepsychiatry?", "Sometimes, but the rules are stricter and changeable. Federal flexibilities that allow some telemedicine prescribing of controlled substances have been repeatedly extended while a permanent rule is finalized.")],
    [("Kaiser Family Foundation, telehealth use and trends.", "https://www.kff.org/mental-health/"),
     ("U.S. Department of Health and Human Services, telehealth policy.", "https://telehealth.hhs.gov/"),
     ("U.S. Drug Enforcement Administration, telemedicine and controlled substances.", "https://www.deadiversion.usdoj.gov/")],
    [("What telepsychiatry changes", "/technology/what-telepsychiatry-changes/"),
     ("Why telepsychiatry works for some things and not others", "/decoder/why-getting-an-appointment-is-hard/"),
     ("The Operating Room: Telepsychiatry", "/psychiatry-operating-room/#room-04")],
    ["shrinkmd", "psychiatryrx", "shrinknetwork"],
    "telepsychiatry statistics, telehealth psychiatry data, virtual psychiatric care trends",
)

# ---------------- Burnout brief ----------------
brief(
    "burnout", "Workforce", "Burnout in psychiatry",
    "Burnout is one of the most measured problems in medicine, and psychiatry sits squarely inside it. The honest read of the data is that this is a systems problem with workforce consequences, not a personal failing.",
    "How common is burnout in psychiatry? National physician surveys consistently find a large share of psychiatrists reporting burnout, often roughly a third to nearly half depending on the year and the instrument. Psychiatry tends to land in the middle-to-upper range across specialties, and the drivers are mostly systemic.",
    "Surveys consistently find a large share of psychiatrists, often a third to nearly half, reporting burnout. Psychiatry lands mid-to-upper across specialties, and the drivers are systemic.",
    "<h2 id=\"numbers\">What the surveys show</h2>"
    "<p>Burnout is tracked annually by large physician surveys, including those run by Medscape and research summarized by the American Medical Association. Year to year, a large share of psychiatrists report burnout symptoms, commonly in the range of roughly a third to nearly half, depending on the survey and how burnout is measured. Psychiatry typically lands in the middle-to-upper band across specialties rather than at either extreme.</p>"
    "<h2 id=\"drivers\">The drivers are mostly systemic</h2>"
    "<p>The strongest evidence points at the system, not the person. Documentation load and electronic-record friction, administrative tasks like prior authorizations, high caseloads driven by the shortage, and limited control over schedules are recurring culprits. The emotional weight of the work matters too, but the modifiable drivers are largely structural, which is where interventions that actually work tend to focus.</p>"
    "<h2 id=\"consequences\">Why it's a workforce issue</h2>"
    "<p>Burnout isn't only a clinician-wellbeing concern. It feeds reduced hours, earlier retirement, and turnover, each of which subtracts from an already strained workforce. In a field with a structural shortage, burnout and access are linked: the cost of the work becomes a cost of care that patients ultimately feel as fewer available appointments.</p>"
    "<h2 id=\"what-helps\">What the evidence says helps</h2>"
    "<p>Because the drivers are structural, the interventions with the best evidence are too: reducing documentation burden, streamlining administrative tasks, improving electronic-record usability, and giving clinicians more control over their schedules. Individual resilience training has a role but a limited one. Framing burnout as a personal weakness misreads the data and points at the wrong solution.</p>",
    ["A large share of psychiatrists report burnout in national surveys, often a third to nearly half depending on the year.",
     "Psychiatry tends to fall in the middle-to-upper range across specialties.",
     "The strongest evidence points at systemic drivers: documentation, administration, caseload, and lack of control.",
     "Burnout subtracts from a strained workforce, linking it directly to patient access."],
    [("numbers", "What the surveys show"), ("drivers", "The drivers are systemic"),
     ("consequences", "Why it's a workforce issue"), ("what-helps", "What the evidence says helps")],
    [("Is psychiatry the most burned-out specialty?", "No. Psychiatry usually lands in the middle-to-upper range across specialties in national surveys, not at the very top. A large share of psychiatrists report burnout, but it's not an outlier among medical fields."),
     ("Is burnout a personal resilience problem?", "The evidence says mostly not. The strongest, most modifiable drivers are systemic, such as documentation load and administrative burden. Individual resilience training helps only modestly.")],
    [("Medscape, Physician Burnout and Depression Report.", "https://www.medscape.com/"),
     ("American Medical Association, physician burnout research and resources.", "https://www.ama-assn.org/practice-management/physician-health")],
    [("Burnout in psychiatry, explained", "/culture/burnout-in-psychiatry/"),
     ("Why documentation shapes care", "/business/why-documentation-shapes-care/"),
     ("The Operating Room: Burnout", "/psychiatry-operating-room/#room-10")],
    ["shrinkmd", "shrinkopedia", "shrinknetwork"],
    "psychiatrist burnout statistics, physician burnout psychiatry, psychiatry burnout data",
)

# ---------------- AI brief ----------------
brief(
    "ai", "Technology", "AI in psychiatry: the state of play",
    "Artificial intelligence is the loudest topic in the field and one of the easiest to overstate. The honest read separates what's actually deployed today from what's still a claim.",
    "Where does AI actually stand in psychiatry? Ambient documentation tools that draft clinical notes are the most real, fastest-spreading use. Decision support and consumer chatbots are far less proven, and no AI is cleared to diagnose or treat psychiatric illness on its own. The near-term effect is on paperwork, not clinical judgment.",
    "Ambient note-drafting tools are the real, fast-spreading use. Decision support and chatbots are unproven, and no AI is cleared to diagnose psychiatric illness on its own. The near-term effect is on paperwork.",
    "<h2 id=\"deployed\">What's actually deployed</h2>"
    "<p>The most real use of AI in psychiatry today is ambient documentation: tools that listen to a visit and draft the clinical note, letting the clinician look up more and type less. Adoption is spreading quickly because it targets the documentation burden that drives burnout, and because the stakes of a draft note, which a clinician reviews and signs, are lower than a clinical decision. This is the near-term story.</p>"
    "<h2 id=\"unproven\">What's promising but unproven</h2>"
    "<p>Beyond documentation, the claims get louder and the evidence thinner. AI-based decision support, risk prediction, and analysis of speech or behavior are active research areas with real promise and, so far, limited validated clinical use. Consumer mental-health chatbots are widely available and largely unregulated, and the evidence for them ranges from modest to absent. Treat bold claims here with skepticism.</p>"
    "<h2 id=\"regulation\">What regulators have and haven't cleared</h2>"
    "<p>The Food and Drug Administration has cleared a small number of digital mental-health tools, including some prescription digital therapeutics, but no AI system is authorized to autonomously diagnose or treat psychiatric illness. A human clinician remains responsible for diagnosis and treatment. The gap between what's marketed and what's actually cleared is wide, which is exactly where careful reading matters.</p>"
    "<h2 id=\"risks\">The risks worth naming</h2>"
    "<p>The real risks aren't science-fiction ones. They're privacy of sensitive mental-health data, bias in models trained on unrepresentative populations, automation bias where clinicians over-trust a tool, and consumer products that present themselves as care without the evidence or accountability of care. The promising direction keeps a clinician in the loop and uses AI to remove friction, not to replace judgment.</p>",
    ["Ambient note-drafting tools are the most real and fastest-spreading use of AI in psychiatry.",
     "Decision support, risk prediction, and chatbots are far less proven, and many consumer tools are unregulated.",
     "No AI is cleared to diagnose or treat psychiatric illness autonomously; a clinician remains responsible.",
     "The real risks are privacy, bias, automation bias, and unproven consumer products posing as care."],
    [("deployed", "What's actually deployed"), ("unproven", "Promising but unproven"),
     ("regulation", "What regulators have cleared"), ("risks", "The risks worth naming")],
    [("Can AI diagnose mental illness?", "No AI system is authorized to diagnose or treat psychiatric illness on its own. A human clinician remains responsible. AI's most established role today is drafting documentation, not making clinical decisions."),
     ("Are mental-health chatbots safe to rely on?", "Be cautious. Most consumer mental-health chatbots are largely unregulated, and the evidence for them ranges from modest to absent. They aren't a substitute for evaluation by a licensed clinician.")],
    [("U.S. Food and Drug Administration, digital health and software as a medical device.", "https://www.fda.gov/medical-devices/digital-health-center-excellence"),
     ("American Psychiatric Association, on AI and mental health.", "https://www.psychiatry.org/")],
    [("AI in psychiatry, an honest read", "/technology/ai-in-psychiatry/"),
     ("Why your psychiatrist takes notes", "/decoder/why-your-psychiatrist-takes-notes/"),
     ("The Operating Room: AI and technology", "/psychiatry-operating-room/#room-09")],
    ["psychiatryrx", "shrinkmd", "shrinknetwork"],
    "AI in psychiatry, mental health AI, ambient scribe psychiatry, AI mental health regulation",
)
