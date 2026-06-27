# -*- coding: utf-8 -*-
"""Cornerstone long-form articles."""
import engine as S

PUB = "2026-06-20"
MOD = "2026-06-27"
UPDATED = "June 27, 2026"

def make_article(a):
    article_type = ["MedicalWebPage", "Article"] if a.get("medical") else "Article"
    schema = [S._jsonld_person(), {
        "@type": article_type,
        "headline": a["title"],
        "description": a["desc"],
        "datePublished": PUB,
        "dateModified": MOD,
        "inLanguage": "en-US",
        "isPartOf": {"@id": "https://shrinkiatry.com/#website"},
        "publisher": {"@id": "https://shrinkiatry.com/#org"},
        "author": {"@id": "https://shrinkiatry.com/#refai"},
        "reviewedBy": {"@id": "https://shrinkiatry.com/#refai"},
        "mainEntityOfPage": "https://shrinkiatry.com/" + a["slug"] + "/",
    }]
    if a.get("faq"):
        schema.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": ans}}
                for q, ans in a["faq"]
            ],
        })
    meta = {
        "kicker": a["kicker"], "title": a["title"], "lede": a["lede"],
        "breadcrumbs": a["breadcrumbs"], "reading_time": a["reading_time"],
        "updated": UPDATED, "quick_answer": a["quick_answer"],
        "takeaways": a["takeaways"], "toc": a["toc"], "body": a["body"],
        "faq": a.get("faq"), "sources": a["sources"], "network": a["network"],
    }
    return {
        "slug": a["slug"], "active": a["active"],
        "title": a["title"] + " | shrinkiatry",
        "desc": a["desc"], "og_type": "article",
        "breadcrumbs": a["breadcrumbs"], "schema": schema,
        "body": S.article_shell(meta),
    }

ART = []

# ============================================================
# 1. How psychiatry residency works
# ============================================================
ART.append({
"slug": "careers/how-psychiatry-residency-works",
"active": "/careers/", "kicker": "Careers / Training",
"title": "How psychiatry residency actually works",
"lede": "Becoming a psychiatrist takes four years of residency after medical school, in a fixed sequence the national accreditor sets. Here's what each year trains, and why the first one barely looks like psychiatry.",
"desc": "A clear, sourced explanation of how psychiatry residency works: four years, the PGY ladder, what each year trains, and the board exam at the end.",
"reading_time": "9 min read",
"breadcrumbs": [("Home", "/"), ("Careers", "/careers/"), ("How residency works", None)],
"quick_answer": "After medical school, a doctor who wants to be a psychiatrist completes a residency that the Accreditation Council for Graduate Medical Education sets at 48 months, usually called PGY-1 through PGY-4. The first year includes months of general medicine and neurology before psychiatry takes over. After residency, most psychiatrists take a board exam to become certified, and some add a one or two year fellowship in a subspecialty.",
"takeaways": [
 "Psychiatry residency is four years long, set at 48 months by the ACGME.",
 "The first year mixes internal medicine, neurology, and psychiatry, so a new psychiatrist is also trained as a physician first.",
 "Residents move from supervised inpatient work toward outpatient care, psychotherapy, and more independence over the four years.",
 "Board certification through the ABPN comes after residency, and subspecialty fellowships add one to two more years.",
],
"toc": [("path","The path in one paragraph"),("year1","PGY-1: still a doctor first"),
 ("year2","PGY-2: psychiatry takes over"),("year3","PGY-3: the outpatient year"),
 ("year4","PGY-4: independence and electives"),("after","After residency: boards and fellowships"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="path">The path in one paragraph</h2>
<p>A psychiatrist is a physician first. The path runs through four years of college, four years of medical school, and then residency, which is paid, supervised training inside a hospital or health system. For psychiatry, the Accreditation Council for Graduate Medical Education (ACGME) requires that residency to be 48 months long. People count those years as PGY-1 through PGY-4, where PGY stands for postgraduate year. Only after all of that does someone practice independently, and most go on to take a board exam to be certified.</p>
<p>The thing that surprises people is how much of the early training isn't psychiatry at all. That's on purpose. Psychiatric patients have bodies, take other medications, and develop medical illnesses that can look like psychiatric ones. A psychiatrist who can't recognize a thyroid problem or a drug interaction isn't fully trained, so the field builds general medicine into the foundation.</p>

<h2 id="year1">PGY-1: still a doctor first</h2>
<p>The first year of psychiatry residency, the intern year, deliberately looks a lot like internal medicine. ACGME rules require a stretch of months in general medical care and in neurology, alongside the first psychiatry rotations. An intern might spend the morning managing blood pressure and diabetes on a medicine ward and the afternoon learning to assess a first psychotic episode.</p>
<p>This is where the habit of ruling out medical causes gets built. By the end of the year, a resident has admitted patients, written orders, handled emergencies, and started to learn psychiatric interviewing under close supervision. They're a licensed doctor doing hospital medicine who happens to be heading toward psychiatry.</p>

<h2 id="year2">PGY-2: psychiatry takes over</h2>
<p>The second year is when psychiatry becomes the center of gravity. Residents rotate through inpatient psychiatric units, the emergency room, consultation services that advise other medical teams, and often addiction and geriatric settings. The volume is high and the supervision is still heavy, because this is where pattern recognition is forged.</p>
<p>A PGY-2 sees a lot of acute illness in a short time: mania, psychosis, severe depression, withdrawal, suicidal crises. They learn to start and adjust medications, to assess risk, and to write the kind of careful note that the rest of the team and the next clinician will rely on. It's demanding work, and it's where many residents say they finally feel like psychiatrists.</p>

<h2 id="year3">PGY-3: the outpatient year</h2>
<p>The third year usually shifts to the clinic. Residents carry their own panel of outpatients over months and sometimes years, which is the first time they see how people actually change with treatment over time. This is also the year psychotherapy training becomes central. ACGME requires residents to demonstrate competence in several forms of psychotherapy, so a PGY-3 might be learning cognitive behavioral therapy, psychodynamic therapy, and supportive therapy at once, each with its own supervisor.</p>
<p>Continuity is the lesson of this year. Medication management looks different when you're the one who prescribed it three months ago and you're watching what happened. The work gets quieter and, in some ways, harder.</p>

<h2 id="year4">PGY-4: independence and electives</h2>
<p>By the fourth year, residents function with much more independence and often take on teaching and leadership roles, supervising junior residents and medical students. The schedule opens up for electives, so a senior resident can go deeper into an interest, whether that's child psychiatry, forensic work, research, addiction, or running a clinic. Many use the year to prepare for whatever comes next, including fellowship applications or job hunting.</p>

<h2 id="after">After residency: boards and fellowships</h2>
<p>Finishing residency makes someone eligible for board certification through the American Board of Psychiatry and Neurology (ABPN). Certification isn't legally required to practice, but it's the standard credential, and many hospitals and insurers expect it. It involves passing an exam and then keeping the certificate active through an ongoing continuing-certification process rather than a single test that lasts forever.</p>
<p>Some psychiatrists then add a fellowship, which is extra subspecialty training that usually runs one to two years. Common ones include child and adolescent psychiatry, consultation-liaison psychiatry (the medical-psychiatric interface), addiction psychiatry, geriatric psychiatry, forensic psychiatry, and sleep medicine. Child and adolescent psychiatry is the largest, and it's a two-year fellowship.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>People often think psychiatrists train mainly in talk therapy, or that they barely train in it at all. Both are wrong. Residency requires real competence in psychotherapy and in medical management, because the job is the combination. People also assume residency is shorter than it is. At four years after medical school, training a psychiatrist takes well over a decade from the start of college, which is part of why the workforce can't expand quickly to meet demand. We cover that supply problem in <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>.</p>
""",
"faq": [
 ("How long is psychiatry residency?", "Psychiatry residency is four years, which the ACGME sets at 48 months, completed after medical school. Subspecialty fellowships add one to two more years."),
 ("Do psychiatrists train in therapy or just medication?", "Both. ACGME requirements include demonstrated competence in several forms of psychotherapy as well as medical and medication management. The job is the combination of the two."),
 ("Is board certification required to practice psychiatry?", "No. A medical license is what's legally required. Board certification through the ABPN is the standard professional credential and is often expected by employers and insurers, but it isn't a legal requirement."),
],
"sources": [
 ("ACGME, Psychiatry program overview and requirements (48-month length).", "https://www.acgme.org/specialties/psychiatry/overview/"),
 ("ACGME Program Requirements for Graduate Medical Education in Psychiatry (2025).", "https://www.acgme.org/globalassets/pfassets/programrequirements/2025-reformatted-requirements/400_psychiatry_2025_reformatted.pdf"),
 ("American Board of Psychiatry and Neurology, becoming certified in psychiatry.", "https://abpn.org/become-certified/taking-a-specialty-exam/psychiatry/"),
 ("American Psychiatric Association, Certification and Licensure.", "https://www.psychiatry.org/psychiatrists/education/certification-and-licensure"),
],
"network": ["shrinkmd","shariqrefai","shrinknetwork"],
})

# ============================================================
# 2. Psychiatrist vs psychologist vs therapist
# ============================================================
ART.append({
"slug": "careers/psychiatrist-vs-psychologist-vs-therapist",
"active": "/careers/", "kicker": "Careers / The profession", "medical": True,
"title": "Psychiatrist, psychologist, therapist: the real differences",
"lede": "They get used as synonyms, but they're different jobs with different training, tools, and scope. Here's what actually separates them, and where they overlap.",
"desc": "Psychiatrist vs psychologist vs therapist: the real differences in training, scope, prescribing, and the work, explained clearly by a board-certified psychiatrist.",
"reading_time": "8 min read",
"breadcrumbs": [("Home", "/"), ("Careers", "/careers/"), ("Psychiatrist vs psychologist vs therapist", None)],
"quick_answer": "A psychiatrist is a medical doctor (MD or DO) who can diagnose mental illness, prescribe medication, and treat the medical side of psychiatric conditions. A psychologist usually holds a doctorate (PhD or PsyD), specializes in assessment and psychotherapy, and generally can't prescribe except in a few states. A therapist is a broader term for licensed counselors, social workers, and marriage and family therapists who provide talk therapy and typically hold a master's degree. The training paths and the legal scope of practice are what really separate them.",
"takeaways": [
 "Psychiatrists are physicians; they can prescribe and treat medical aspects of mental illness.",
 "Psychologists usually hold a doctorate and specialize in testing and therapy, and they generally can't prescribe.",
 "\"Therapist\" is an umbrella term for several master's-level licensed professions that provide talk therapy.",
 "The roles overlap in practice and often work as a team, but their training and legal scope are different.",
],
"toc": [("words","Why the words get confused"),("psychiatrist","The psychiatrist"),
 ("psychologist","The psychologist"),("therapist","The therapist"),
 ("overlap","Where they overlap"),("choose","Who does a person actually need"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="words">Why the words get confused</h2>
<p>In everyday speech, people say they're "seeing their therapist" whether that person is a psychiatrist, a psychologist, or a counselor. That's understandable, because all three can sit across from someone and help. But they trained differently, they're licensed differently, and they can legally do different things. Knowing which is which saves people time, money, and a lot of frustration when they're trying to get the right kind of help.</p>

<h2 id="psychiatrist">The psychiatrist</h2>
<p>A psychiatrist is a medical doctor, holding an MD or a DO, who went to medical school and then completed a four-year psychiatry residency. Because they're physicians, they can order labs and imaging, diagnose and manage medical conditions that affect mental health, prescribe and adjust medication, and provide certain medical treatments. Many also do psychotherapy, and all are trained in it. If a problem might be driven by a thyroid disorder, a medication interaction, or a substance, the psychiatrist is the one trained to catch it. We cover that training in <a href="/careers/how-psychiatry-residency-works/">how residency works</a>.</p>

<h2 id="psychologist">The psychologist</h2>
<p>A clinical psychologist usually holds a doctorate, either a PhD or a PsyD, and completed years of supervised clinical training plus an internship. Their deepest expertise tends to be in two areas: psychological assessment, including the detailed testing used to clarify a diagnosis like ADHD or a learning disorder, and psychotherapy, often at a high level of specialization. In most of the United States, psychologists can't prescribe medication. A small number of states have created a path for specially trained "prescribing psychologists," but that remains the exception rather than the rule.</p>

<h2 id="therapist">The therapist</h2>
<p>"Therapist" or "counselor" usually refers to a master's-level licensed professional. This group includes licensed professional counselors (LPCs), licensed clinical social workers (LCSWs), and licensed marriage and family therapists (LMFTs), among others. They complete a master's degree and a substantial number of supervised hours before licensure, and they provide talk therapy for a wide range of concerns. They don't prescribe, and most don't do formal psychological testing, but they make up the largest part of the mental health workforce and provide much of the therapy people actually receive.</p>

<h2 id="overlap">Where they overlap</h2>
<p>All three can provide psychotherapy, and a skilled member of any of these professions can be excellent at it. All three can be the person who first recognizes that something is wrong and points a patient toward the right next step. In a lot of real care, they work as a team: a therapist provides weekly therapy, a psychiatrist manages medication, and a psychologist does testing when the picture is unclear. The professions are complementary more often than they're competing.</p>

<h2 id="choose">Who does a person actually need</h2>
<p>It depends on the problem. Someone who wants talk therapy for anxiety or a rough life stretch is often well served by a therapist or psychologist. Someone who may need medication, has a complicated medical picture, or has a severe condition like bipolar disorder or psychosis usually needs a psychiatrist in the mix. Someone who needs a diagnosis clarified through formal testing needs a psychologist. Many people end up seeing more than one, and that's normal, not a sign that something went wrong.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>The biggest myth is that psychiatrists "just prescribe pills" and don't do therapy. Psychiatrists train in psychotherapy and many practice it; the difference is that they can also handle the medical and medication side, which the others can't. The second myth is that a psychologist is "almost a psychiatrist." They're both highly trained, but the doctorates are different kinds of doctorate, and the scope of practice, especially around prescribing and medical care, is genuinely different. None of these roles outranks the others. They're built for different parts of the same problem.</p>
""",
"faq": [
 ("Can a psychologist prescribe medication?", "In most of the United States, no. Psychologists specialize in assessment and therapy. A small number of states allow specially trained prescribing psychologists, but that's the exception. Prescribing is generally done by psychiatrists and other medical prescribers."),
 ("Is a psychiatrist better than a therapist?", "Neither is better; they do different jobs. A psychiatrist is a physician who can prescribe and manage medical aspects of mental illness. A therapist provides talk therapy. Many people benefit from both at once."),
 ("What's the difference between a PhD and a PsyD psychologist?", "Both are doctorates in psychology. A PhD typically emphasizes research alongside clinical training, while a PsyD emphasizes clinical practice. In day-to-day care, both are licensed clinical psychologists."),
],
"sources": [
 ("American Psychiatric Association, What is Psychiatry and Certification and Licensure.", "https://www.psychiatry.org/patients-families/what-is-psychiatry"),
 ("American Psychological Association, About clinical psychology and prescriptive authority.", "https://www.apa.org/ed/graduate/specialize/clinical"),
 ("ACGME, Psychiatry program requirements (residency training and psychotherapy competence).", "https://www.acgme.org/specialties/psychiatry/overview/"),
],
"network": ["shrinkopedia","shrinkmd","shrinknetwork"],
})

# ============================================================
# 3. What board certification means
# ============================================================
ART.append({
"slug": "careers/what-board-certification-means",
"active": "/careers/", "kicker": "Careers / Credentials",
"title": "What board certification in psychiatry actually means",
"lede": "Board certified sounds official, and it is, but it doesn't mean what most people assume. Here's what the credential guarantees, what it doesn't, and how it's kept current.",
"desc": "What board certification in psychiatry means: how ABPN certification works, what it guarantees, what it doesn't, and how continuing certification keeps it current.",
"reading_time": "7 min read",
"breadcrumbs": [("Home", "/"), ("Careers", "/careers/"), ("What board certification means", None)],
"quick_answer": "Board certification in psychiatry is a credential from the American Board of Psychiatry and Neurology (ABPN) that a doctor has met a national standard: an accredited residency, an unrestricted medical license, and a passing score on a certifying exam. It isn't legally required to practice, and it isn't a guarantee that any given visit will go well. It signals that a psychiatrist met a recognized bar and keeps meeting it through ongoing continuing certification.",
"takeaways": [
 "Board certification comes from the ABPN, a member of the American Board of Medical Specialties.",
 "It requires completing an accredited residency, holding a full medical license, and passing a certifying exam.",
 "It's the standard credential but isn't legally required to practice; a state medical license is.",
 "Certification is kept active through continuing certification, not a single lifetime test.",
],
"toc": [("what","What the credential is"),("how","How a psychiatrist gets certified"),
 ("keep","Keeping it current"),("guarantee","What it does and doesn't guarantee"),
 ("subspecialty","Subspecialty certification"),("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="what">What the credential is</h2>
<p>Board certification is a voluntary, national standard run by specialty boards, not by the government. For psychiatry, that board is the American Board of Psychiatry and Neurology, usually shortened to ABPN, which is one of the member boards of the American Board of Medical Specialties. When a psychiatrist says they're "board certified," they mean the ABPN has verified that they met the board's requirements and passed its exam.</p>
<p>It's worth being precise here, because the word "board" gets used loosely. The credential isn't a license. A license to practice medicine comes from a state medical board and is the thing that's legally required. Certification sits on top of the license as a profession-set mark of standardized competence.</p>

<h2 id="how">How a psychiatrist gets certified</h2>
<p>The path has a few gates. A psychiatrist has to graduate from medical school, complete an ACGME-accredited psychiatry residency, and hold an active, full, and unrestricted medical license. Then they sit for the ABPN certifying examination in psychiatry. Passing it earns initial certification. Each of those steps is its own bar, and the exam is meant to confirm a shared baseline across everyone who carries the credential.</p>

<h2 id="keep">Keeping it current</h2>
<p>Certification used to be thought of as a one-time achievement, and older psychiatrists who certified long ago sometimes hold time-unlimited certificates. For everyone certifying now, it's an ongoing process the ABPN calls continuing certification. It has a few moving parts: keeping an active license, completing continuing medical education including self-assessment, doing practice-improvement activity, and meeting an assessment requirement.</p>
<p>That last piece has changed recently. Instead of one high-stakes exam every ten years, the ABPN now offers an article-based pathway in which diplomates read and answer questions on a set of journal articles on a rolling basis. Under that pathway, the requirement runs in three-year cycles. The point of the shift is to make staying current feel more like ongoing learning and less like cramming for a test.</p>

<h2 id="guarantee">What it does and doesn't guarantee</h2>
<p>Certification guarantees that a psychiatrist met a recognized national standard and is keeping it up. That's genuinely useful information, and it's reasonable for a patient or a hospital to want it. What it can't guarantee is the quality of any single encounter, the fit between a particular patient and a particular doctor, or that a clinician is current on a narrow new development the week you happen to see them. It's a floor and a signal, not a promise about outcomes.</p>

<h2 id="subspecialty">Subspecialty certification</h2>
<p>Beyond general psychiatry, the ABPN certifies subspecialties for psychiatrists who complete an accredited fellowship and pass an additional exam. These include child and adolescent psychiatry, addiction psychiatry, consultation-liaison psychiatry, geriatric psychiatry, forensic psychiatry, and sleep medicine, among others. A psychiatrist board certified in child and adolescent psychiatry, for example, has done extra training specifically in that area on top of general certification.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>People often assume board certification is legally mandatory. It isn't; the license is. They also assume "board eligible," a phrase sometimes used for someone who finished residency but hasn't yet passed the exam, means the same thing as certified. It doesn't. And many patients think certification is a lifetime stamp. For current psychiatrists, it's an ongoing commitment that has to be maintained, which is arguably the more reassuring version.</p>
""",
"faq": [
 ("Is board certification required to be a psychiatrist?", "No. A state medical license is what's legally required to practice. Board certification through the ABPN is the standard professional credential and is often expected by employers and insurers, but it isn't a legal requirement."),
 ("What does ABPN stand for?", "The American Board of Psychiatry and Neurology, the specialty board that certifies psychiatrists and neurologists in the United States. It's a member board of the American Board of Medical Specialties."),
 ("Do psychiatrists have to retake an exam every ten years?", "Not necessarily. The ABPN now offers an article-based continuing certification pathway, completed on a rolling basis in three-year cycles, as an alternative to a single recertification exam."),
],
"sources": [
 ("American Board of Psychiatry and Neurology, Continuing Certification.", "https://abpn.org/continuing-certification/"),
 ("ABPN, Becoming certified in psychiatry.", "https://abpn.org/become-certified/taking-a-specialty-exam/psychiatry/"),
 ("American Psychiatric Association, Certification and Licensure.", "https://www.psychiatry.org/psychiatrists/education/certification-and-licensure"),
],
"network": ["shrinkmd","shariqrefai","shrinknetwork"],
})

# ============================================================
# 4. How private psychiatry practices work
# ============================================================
ART.append({
"slug": "business/how-private-psychiatry-practices-work",
"active": "/business/", "kicker": "Business / Practice models",
"title": "How private psychiatry practices actually work",
"lede": "An independent psychiatry practice is a small business with unusual rules. Here's how it's structured, where the money goes, and the tradeoffs behind running your own.",
"desc": "How private psychiatry practices work: structure, payer mix, overhead, staffing, and the tradeoffs behind running an independent psychiatric practice.",
"reading_time": "9 min read",
"breadcrumbs": [("Home", "/"), ("Business", "/business/"), ("How private practices work", None)],
"quick_answer": "A private psychiatry practice is a physician-owned small business. The psychiatrist sees patients and also, directly or through staff, handles scheduling, billing, documentation, compliance, and overhead. The big structural choices are whether to take insurance or go cash-pay, whether to practice solo or in a group, and how much to spend on staff and systems. Those choices shape income, access, and how much administrative weight lands on the clinician.",
"takeaways": [
 "A private practice is a small business the psychiatrist owns and runs, not just a place they work.",
 "The central decision is the payer model: insurance, cash-pay, or a hybrid, each with real tradeoffs.",
 "Overhead, no-shows, and documentation time quietly determine whether the model works.",
 "Solo practice offers control; group practice shares cost and risk but dilutes autonomy.",
],
"toc": [("business","A clinic is a business"),("models","Solo, group, and hybrid"),
 ("payers","The payer decision"),("overhead","Where the money goes"),
 ("admin","The administrative weight"),("tradeoffs","The honest tradeoffs"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="business">A clinic is a business</h2>
<p>When a psychiatrist opens a practice, they take on two jobs. One is clinical: seeing patients, making diagnoses, prescribing, and providing therapy. The other is running a company: setting prices, getting paid, hiring, keeping records, following regulations, and covering the bills whether or not the schedule fills. Medical training prepares people thoroughly for the first job and almost not at all for the second. That gap is the reason this section of shrinkiatry exists.</p>
<p>You can model a practice in your browser with our <a href="/tools/private-practice-revenue-estimator/">revenue estimator</a>, which shows how the levers interact. The rest of this article explains those levers.</p>

<h2 id="models">Solo, group, and hybrid</h2>
<p>The simplest structure is solo practice: one psychiatrist, maybe one staff member, full control over every decision. It's the most autonomous and the most exposed, because every fixed cost and every empty slot lands on one person. Group practice spreads the overhead and the risk across several clinicians who share rent, staff, and systems, in exchange for some loss of independence and a share of the revenue going to the group. Hybrid arrangements are common too, where a psychiatrist keeps a small private panel while also working part-time for a hospital or a telepsychiatry company for steady income and benefits.</p>

<h2 id="payers">The payer decision</h2>
<p>The single most consequential choice is how the practice gets paid. A practice that takes insurance reaches far more patients, because most people use their coverage, but it accepts the insurer's contracted rate and the administrative work of claims, prior authorizations, and credentialing. A cash-pay practice, also called out-of-network, sets its own fees and skips much of that paperwork, but it limits the patient pool to people who can pay directly or file for partial reimbursement themselves. Many psychiatrists land in a hybrid: in-network with a few plans, cash-pay for the rest. We unpack this fully in <a href="/business/cash-pay-vs-insurance/">cash-pay vs insurance</a>.</p>

<h2 id="overhead">Where the money goes</h2>
<p>Gross revenue is not take-home pay. Out of every dollar collected, a practice pays rent or its telehealth platform, staff salaries, malpractice insurance, an electronic health record, billing costs, software, and supplies. Overhead in an outpatient psychiatry practice is generally lower than in procedure-heavy specialties, because there's no expensive equipment, but it's far from zero, and it scales with how much staff and infrastructure the practice carries. Two other quiet drains matter a lot: no-shows, since an empty slot earns nothing while the overhead keeps running, and unpaid administrative time spent on notes and forms after hours.</p>

<h2 id="admin">The administrative weight</h2>
<p>The part clinicians underestimate is how much non-clinical work a practice generates. Someone has to verify benefits, post payments, chase denied claims, manage the schedule, handle records requests, and keep up with compliance. In a solo practice, that someone is often the psychiatrist, at night. This is why documentation, billing systems, and increasingly automation tools matter so much to whether a practice is sustainable. The clinical work can be excellent and the practice can still fail on operations. For why the note itself carries so much weight, see <a href="/business/why-documentation-shapes-care/">why documentation shapes care</a>.</p>

<h2 id="tradeoffs">The honest tradeoffs</h2>
<p>Independent practice buys autonomy: control over schedule, panel size, appointment length, and the kind of care you provide. It costs security: there's no salary floor, no employer handling the back office, and no built-in benefits. Cash-pay buys simplicity and time per patient at the cost of reach and the discomfort of pricing people out. Insurance buys access and volume at the cost of paperwork and rate-setting you don't control. There's no model that wins on every axis, which is exactly why different psychiatrists make different choices.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>Patients sometimes assume a cash-pay psychiatrist is simply charging what they can get away with. Often the fee reflects the real cost of running a small practice with long appointments and no insurer subsidizing the overhead. On the other side, people assume insurance-based practices are financially comfortable; thin contracted rates and heavy administrative load can make the economics tighter than they look. The reality is that a psychiatry practice is a narrow-margin small business wearing a white coat.</p>
""",
"faq": [
 ("Why don't more psychiatrists take insurance?", "Contracted insurance rates can be low relative to the time careful psychiatric care takes, and the administrative work of claims and authorizations is heavy. Many psychiatrists go out of network to protect appointment length and reduce paperwork, which is covered in our cash-pay vs insurance article."),
 ("Is private practice more profitable than being employed?", "It can be, because the owner keeps the margin, but it carries more financial risk and administrative work and no built-in benefits. Employed roles trade some income ceiling for stability. The right answer depends on the person."),
 ("What's the biggest hidden cost in a psychiatry practice?", "Two of them: no-shows, because an empty slot still carries overhead, and unpaid administrative time spent on documentation and billing. Both quietly determine whether the model works."),
],
"sources": [
 ("American Psychiatric Association, practice management resources.", "https://www.psychiatry.org/psychiatrists/practice/practice-management"),
 ("American Medical Association, private practice and physician practice resources.", "https://www.ama-assn.org/practice-management/private-practices"),
 ("American Board of Psychiatry and Neurology (training and credentialing context).", "https://abpn.org/"),
],
"network": ["shrinkmd","shariqrefai","shrinknetwork"],
})

# ============================================================
# 5. Cash-pay vs insurance
# ============================================================
ART.append({
"slug": "business/cash-pay-vs-insurance",
"active": "/business/", "kicker": "Business / Payment",
"title": "Cash-pay vs insurance in psychiatry",
"lede": "A striking share of psychiatrists don't take insurance. That isn't greed, and it isn't an accident. It's what the reimbursement system rewards. Here's the real tradeoff.",
"desc": "Cash-pay vs insurance psychiatry: why so many psychiatrists go out of network, what it does to access and income, and the tradeoffs for patients and clinicians.",
"reading_time": "8 min read",
"breadcrumbs": [("Home", "/"), ("Business", "/business/"), ("Cash-pay vs insurance", None)],
"quick_answer": "Many psychiatrists practice cash-pay, meaning they don't bill insurance and patients pay directly. They do it because insurance reimbursement for psychiatric visits is often low relative to the time the work takes, and the administrative burden of claims, authorizations, and credentialing is heavy. Cash-pay buys longer visits, simpler operations, and predictable income, at the cost of reach, since it prices out patients who can't pay out of pocket. It's a tradeoff between access and sustainability, not a simple good or bad.",
"takeaways": [
 "Psychiatry has one of the highest out-of-network rates in medicine.",
 "Low contracted reimbursement and heavy paperwork push psychiatrists out of insurance networks.",
 "Cash-pay improves visit length and operational simplicity but reduces access.",
 "The result is a real equity problem: care is available, but not evenly affordable.",
],
"toc": [("pattern","An unusual pattern"),("why","Why psychiatrists opt out"),
 ("cashside","What cash-pay buys"),("insside","What insurance buys"),
 ("access","The access problem"),("patient","What it means for patients"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="pattern">An unusual pattern</h2>
<p>Psychiatry stands out in American medicine for how often its clinicians don't take insurance. In most specialties, opting out of insurance is rare. In psychiatry, it's common enough that patients often expect to pay out of pocket or to use out-of-network benefits. This pattern is one of the clearest windows into the economics of the field, because it isn't really about individual choices. It's about what the payment system rewards.</p>

<h2 id="why">Why psychiatrists opt out</h2>
<p>Two forces push psychiatrists out of networks. The first is the rate. Insurers reimburse psychiatric visits at amounts that often don't reflect the time good care takes, especially when a visit involves both medication management and meaningful conversation. The second is the overhead of participating: credentialing with each plan, submitting claims, fighting denials, and obtaining prior authorizations for medications. For a solo or small practice, that administrative load can require staff the practice can barely afford. When the rate is low and the paperwork is high, the math pushes toward opting out.</p>

<h2 id="cashside">What cash-pay buys</h2>
<p>A cash-pay practice sets its own fees and collects them directly. That changes the day in concrete ways. Visits can be longer, because the practice isn't trying to make the economics work on short, low-paying appointments. The back office shrinks, because there are no claims to file or denials to appeal. Income becomes more predictable. For the clinician, it often means the ability to practice the way they were trained, with time to listen. None of that is trivial, and it's why so many psychiatrists who care deeply about quality still choose this model.</p>

<h2 id="insside">What insurance buys</h2>
<p>Taking insurance buys reach. Most people have coverage and use it, and an in-network psychiatrist is reachable by ordinary patients without a large out-of-pocket cost. For many conditions and many communities, the in-network psychiatrist is the only realistic option a patient has. Insurance-based practice also smooths demand, because patients aren't filtered by ability to pay up front. The cost is the rate-setting and the paperwork, which is exactly what the cash-pay practice is escaping.</p>

<h2 id="access">The access problem</h2>
<p>Put these together and you get the field's central tension. The cash-pay model can deliver excellent, unhurried care, but mostly to people who can afford it. The insurance model spreads access more widely, but the thin economics contribute to short visits, long waitlists, and burnout. Neither model solves the underlying problem, which is that there aren't enough psychiatrists and the payment system doesn't pay for the time the work needs. We cover the supply side in <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>, and one system-level response in the same article, the Collaborative Care Model, which stretches a single psychiatrist across many more patients.</p>

<h2 id="patient">What it means for patients</h2>
<p>For a patient, the practical takeaways are simple. Ask up front whether a psychiatrist is in-network, out-of-network, or cash-pay. If they're out of network, ask whether your plan offers out-of-network reimbursement, since some of the cost may come back to you. Consider that a nurse practitioner, a collaborative care program through primary care, or a telepsychiatry service may be more affordable in-network options. And know that a high cash fee usually reflects the cost of long visits and low overhead subsidy, not a markup for its own sake.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>The cynical read is that psychiatrists go cash-pay to get rich. The honest read is that the reimbursement system makes careful in-network psychiatry financially difficult, and opting out is often a way to keep doing the work well rather than a way to maximize income. The opposite mistake is to assume insurance solves affordability; thin networks and long waits mean that having coverage and finding a psychiatrist who takes it are two different things.</p>
""",
"faq": [
 ("Why do so many psychiatrists not take insurance?", "Because contracted reimbursement for psychiatric visits is often low relative to the time the work takes, and the administrative burden of claims, credentialing, and prior authorizations is heavy. Many psychiatrists opt out to protect visit length and reduce paperwork."),
 ("Can I get money back for an out-of-network psychiatrist?", "Sometimes. Many insurance plans offer out-of-network benefits that reimburse part of the cost after you pay and submit a claim, often called a superbill. Check your specific plan's out-of-network mental health coverage."),
 ("Is cash-pay psychiatry better care?", "Not inherently. Cash-pay often allows longer visits and simpler operations, which can support quality, but excellent psychiatrists practice in-network too. The model affects access and economics more than it guarantees clinical quality."),
],
"sources": [
 ("American Psychiatric Association, integrated and collaborative care resources.", "https://www.psychiatry.org/psychiatrists/practice/professional-interests/integrated-care/learn"),
 ("AMA, how collaborative care can help close the mental health care gap.", "https://www.ama-assn.org/practice-management/scope-practice/how-collaborative-care-can-help-close-mental-health-care-gap"),
 ("HRSA Bureau of Health Workforce, behavioral health workforce briefs.", "https://bhw.hrsa.gov/data-research/projecting-health-workforce-supply-demand"),
],
"network": ["shrinkmd","psychiatryrx","shrinknetwork"],
})

# ============================================================
# 6. Why documentation shapes care
# ============================================================
ART.append({
"slug": "business/why-documentation-shapes-care",
"active": "/business/", "kicker": "Business / Operations",
"title": "Why documentation shapes psychiatric care",
"lede": "The clinical note looks like paperwork. It's actually one of the most powerful forces on how care is delivered, how long visits run, and how clinicians feel at the end of the day.",
"desc": "Why documentation shapes psychiatric care: how the clinical note drives billing, liability, continuity, time, and burnout, and what ambient AI is changing.",
"reading_time": "8 min read",
"breadcrumbs": [("Home", "/"), ("Business", "/business/"), ("Why documentation shapes care", None)],
"quick_answer": "In psychiatry, the clinical note is far more than a record. It justifies billing, creates the legal account of what happened, carries the plan to the next visit and the next clinician, and protects the patient. Because notes take real time and that time is mostly unpaid, documentation also drives how long visits run and how much work spills into the evening. That's why documentation, and the tools that speed it up, sit at the center of both care quality and burnout.",
"takeaways": [
 "The note serves at least four jobs: billing, legal record, continuity, and patient protection.",
 "Documentation time is largely unpaid and often happens after hours, the so-called pajama time.",
 "Heavy documentation pressure shortens visits and contributes to burnout.",
 "Ambient AI scribes are early evidence that reducing the note burden can help, with caveats.",
],
"toc": [("morethan","More than paperwork"),("jobs","The four jobs of a note"),
 ("time","The time problem"),("care","How it bends the visit"),
 ("ai","What ambient AI is changing"),("good","What a good note actually does"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="morethan">More than paperwork</h2>
<p>Ask a patient what the note is, and they'll usually say it's the doctor typing while they talk. Ask a psychiatrist, and you'll get a more complicated answer, because the note is doing several jobs at once, and some of them have nothing to do with memory. Understanding those jobs explains a surprising amount about why psychiatric care feels the way it does.</p>

<h2 id="jobs">The four jobs of a note</h2>
<p>First, the note justifies billing. The level of service billed has to be supported by what's documented, so the note is also a financial document. Second, it's the legal record. If there's ever a question about what was decided and why, especially around risk and safety, the note is the account that stands. Third, it carries continuity. The plan, the reasoning, the medication history, and the things to watch all travel forward through the note to the next visit and to any other clinician involved. Fourth, it protects the patient, by making the reasoning explicit, flagging risks, and reducing the chance that something important is lost between visits.</p>

<h2 id="time">The time problem</h2>
<p>Here's the catch: all of that takes time, and most of that time isn't separately paid. Across medicine, clinicians spend hours in the electronic health record for every few hours of patient contact, and a meaningful share of documentation happens outside clinic hours, in the evenings and on weekends. Clinicians call it pajama time, and it's one of the most consistent complaints in modern practice. In psychiatry, where the substance of the visit is a nuanced conversation that resists checkboxes, capturing it well can be especially demanding.</p>

<h2 id="care">How it bends the visit</h2>
<p>Because the note has to get written and the time to write it is scarce, documentation quietly shapes the encounter itself. It's one of the pressures behind short appointments, since a longer visit also means a longer note. It can pull a clinician's attention toward the screen and away from the person. And it pushes work into the evening, which is part of why documentation and burnout are so tightly linked. None of this is the patient's imagination. The note is a real force in the room.</p>

<h2 id="ai">What ambient AI is changing</h2>
<p>This is exactly where ambient artificial intelligence scribes are landing first. These tools listen to the visit, with consent, and draft the note for the clinician to review and edit. Early studies have shown reductions in time spent on notes and in after-hours work, and in some settings, measurable drops in burnout over a matter of weeks. The American Medical Association has reported large aggregate time savings from such tools. The caveats matter too: the drafts need careful review, accuracy isn't guaranteed, and recording a psychiatric conversation raises real privacy and consent questions. We go deeper in <a href="/technology/ai-in-psychiatry/">AI in psychiatry</a>.</p>

<h2 id="good">What a good note actually does</h2>
<p>Strip away the bureaucracy and a good psychiatric note is a genuinely clinical act. It states what the patient said and what the clinician observed, lays out the reasoning, documents risk and the plan for it, and leaves a clear path for the next person. Done well, it's not a distraction from care; it's part of care. The problem isn't that notes exist. It's that the system asks for thorough notes without paying for the time they take, and then wonders why clinicians are tired.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>Patients sometimes read note-taking as inattention, when it's often the clinician trying to capture something important accurately. On the other side, it's a mistake to treat documentation as pure bureaucracy that could simply be cut. The billing and legal functions are real, and the continuity function genuinely protects patients. The honest target isn't less documentation for its own sake; it's removing the unpaid time tax, which is what the better tools are starting to do.</p>
""",
"faq": [
 ("Why do psychiatrists spend so much time on notes?", "Because the note does several jobs at once: it supports billing, serves as the legal record, carries the treatment plan forward, and protects the patient. Those functions take time, and much of that time isn't separately reimbursed."),
 ("What is pajama time?", "Pajama time is the documentation and electronic health record work clinicians do outside clinic hours, often in the evening at home. It's a widely used measure of administrative burden and a contributor to burnout."),
 ("Do AI scribes actually help with documentation?", "Early studies suggest ambient AI scribes can reduce time spent on notes and after-hours work, and in some settings reduce burnout, but the drafts require careful review for accuracy and raise privacy and consent considerations."),
],
"sources": [
 ("American Medical Association, AI scribes and the documentation burden.", "https://www.ama-assn.org/practice-management/digital-health/ai-scribes-save-15000-hours-and-restore-human-side-medicine"),
 ("Use of Ambient AI Scribes to Reduce Administrative Burden and Professional Burnout (PMC).", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12492056/"),
 ("American Psychiatric Association, documentation and practice resources.", "https://www.psychiatry.org/psychiatrists/practice"),
],
"network": ["psychiatryrx","shrinkmd","shrinknetwork"],
})

# ============================================================
# 7. Why controlled substances are different
# ============================================================
ART.append({
"slug": "business/why-controlled-substances-are-different",
"active": "/business/", "kicker": "Business / Compliance", "medical": True,
"title": "Why controlled substances are handled differently in psychiatry",
"lede": "Stimulants and benzodiazepines come with rules that touch nothing else in a practice. Those rules change how psychiatrists prescribe, document, and even how they schedule.",
"desc": "Why controlled substances are handled differently in psychiatry: DEA scheduling, prescribing rules, monitoring, and how they reshape practice. Educational, not advice.",
"reading_time": "8 min read",
"breadcrumbs": [("Home", "/"), ("Business", "/business/"), ("Controlled substances", None)],
"quick_answer": "Some psychiatric medications, including stimulants for ADHD and benzodiazepines for anxiety, are controlled substances regulated by the DEA because they carry risk of misuse and dependence. That status brings extra rules: a DEA registration to prescribe, tighter refill and documentation requirements, prescription drug monitoring program checks, and special considerations for prescribing by telemedicine. Those rules reshape how a practice runs, not just what gets prescribed.",
"takeaways": [
 "Controlled substances are scheduled by the DEA based on accepted use and risk of misuse.",
 "Prescribing them requires a DEA registration and triggers extra documentation and monitoring.",
 "Schedule II drugs like many stimulants have stricter refill rules than ordinary prescriptions.",
 "Telemedicine prescribing of controlled substances is governed by federal flexibilities currently extended through 2026.",
],
"toc": [("why","Why some drugs are controlled"),("schedules","What the schedules mean"),
 ("rules","The rules that follow"),("pdmp","Monitoring and the PDMP"),
 ("tele","Telemedicine and the moving target"),("practice","How it reshapes the practice"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="why">Why some drugs are controlled</h2>
<p>A number of effective psychiatric medications also carry a risk of misuse, dependence, or diversion. Stimulants used for ADHD and benzodiazepines used for anxiety and panic are the clearest examples. Because of that risk, the federal government, through the Drug Enforcement Administration, classifies them as controlled substances and regulates how they're prescribed, stored, and tracked. This isn't a judgment that the medications are bad. Many are genuinely helpful. It's a recognition that they need guardrails ordinary medications don't.</p>

<h2 id="schedules">What the schedules mean</h2>
<p>Controlled substances are sorted into schedules from II to V, based roughly on accepted medical use and potential for misuse. Schedule II includes drugs with high misuse potential that still have clear medical uses, and it covers many common stimulants. Schedules III through V carry progressively lower misuse potential and looser rules. The schedule a drug sits in determines a lot: how it can be refilled, how prescriptions are transmitted, and how closely the prescriber has to track it.</p>

<h2 id="rules">The rules that follow</h2>
<p>To prescribe any controlled substance, a clinician needs a DEA registration, which is separate from a medical license. Schedule II medications, including many stimulants, generally can't be refilled the way an ordinary prescription can; a new prescription is required each time, which is why patients on stimulants often have to check in more regularly. Documentation expectations are higher, because the prescriber needs to show a legitimate medical purpose and ongoing monitoring. Even the logistics of how a prescription is sent are more tightly regulated.</p>

<h2 id="pdmp">Monitoring and the PDMP</h2>
<p>Most states run a prescription drug monitoring program, usually shortened to PDMP, a database that records controlled-substance prescriptions. Prescribers are often required, or strongly expected, to check it before prescribing, so they can see whether a patient is receiving similar medications elsewhere. This is a safety tool and a compliance step at once, and it's part of the routine of prescribing controlled substances that patients rarely see.</p>

<h2 id="tele">Telemedicine and the moving target</h2>
<p>Prescribing controlled substances over telemedicine is its own evolving area. During the COVID-19 public health emergency, federal rules were relaxed so clinicians could prescribe controlled medications by video without a prior in-person visit. Those flexibilities have been extended several times. As of the most recent extension, the DEA and the Department of Health and Human Services continued them through the end of 2026 while the agencies work on permanent rules, including a proposed special registration for telemedicine prescribing. For a practice, that means the rules in this corner can change, and staying current is part of the job. We cover the broader picture in <a href="/technology/what-telepsychiatry-changes/">what telepsychiatry changes</a>.</p>

<h2 id="practice">How it reshapes the practice</h2>
<p>All of this changes day-to-day operations. Patients on Schedule II medications generally need more frequent visits, which fills the schedule differently. The practice has to track DEA registration, follow PDMP requirements, and keep tighter records. Some psychiatrists limit how much controlled-substance prescribing they do, not because the medications don't work, but because the regulatory weight is real. The rules are a feature of the whole practice, not just a footnote on a prescription.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>Patients sometimes feel that frequent check-ins for a stimulant or a refusal to call in a benzodiazepine refill means the psychiatrist doesn't trust them. Usually it reflects rules the prescriber is legally bound to follow, plus a genuine duty to monitor medications that carry real risks. The flip side is the assumption that controlled means dangerous or addictive for everyone; for many patients these medications are safe and effective when monitored. The point of the rules is to make that careful monitoring the default.</p>
""",
"faq": [
 ("Why can't a psychiatrist just refill my stimulant like other medications?", "Many stimulants are Schedule II controlled substances, which generally can't be refilled the way ordinary prescriptions can. A new prescription is required each time, and prescribers are expected to monitor regularly, so more frequent check-ins are common."),
 ("What is a PDMP?", "A prescription drug monitoring program is a state database of controlled-substance prescriptions. Prescribers often check it before prescribing to see a patient's controlled-substance history and reduce the risk of harmful combinations or diversion."),
 ("Can controlled substances be prescribed over telehealth?", "Currently, yes, under federal flexibilities that have been extended through the end of 2026 while permanent rules are finalized. This area is evolving, so the specifics can change."),
],
"sources": [
 ("DEA, drug scheduling overview.", "https://www.dea.gov/drug-information/drug-scheduling"),
 ("DEA, extension of telemedicine flexibilities for controlled-substance prescribing (Dec 2025).", "https://www.dea.gov/press-releases/2025/12/31/dea-extends-telemedicine-flexibilities-ensure-continued-access-care"),
 ("HHS, DEA telemedicine extension through 2026.", "https://www.hhs.gov/press-room/dea-telemedicine-extension-2026.html"),
],
"network": ["psychiatryrx","shrinkmd","shrinknetwork"],
})

# ============================================================
# 8. What telepsychiatry changes
# ============================================================
ART.append({
"slug": "technology/what-telepsychiatry-changes",
"active": "/technology/", "kicker": "Technology / Telepsychiatry",
"title": "What telepsychiatry changes, and what it doesn't",
"lede": "Video psychiatry exploded, and a lot of confident claims came with it. The honest picture is narrower: some things genuinely changed, and the core of the work mostly didn't.",
"desc": "What telepsychiatry changes and what it doesn't: access, geography, and overhead shifted, while the exam, the rules, and clinical judgment largely stayed the same.",
"reading_time": "8 min read",
"breadcrumbs": [("Home", "/"), ("Technology", "/technology/"), ("What telepsychiatry changes", None)],
"quick_answer": "Telepsychiatry mainly changes access and logistics. It removes travel, widens geographic reach, lowers overhead, and makes scheduling more flexible, which is a real gain for a field with deep shortages. What it doesn't change is the core of the work: the psychiatric interview, clinical judgment, the duty of care, and most of the rules around prescribing. The research generally finds telepsychiatry comparable to in-person care for many common conditions, with some real limits.",
"takeaways": [
 "Telepsychiatry's biggest effect is on access, geography, and overhead, not on the clinical method.",
 "Evidence generally finds it comparable to in-person care for many common psychiatric conditions.",
 "Prescribing rules, especially for controlled substances, still apply and are evolving.",
 "It isn't right for every patient or every situation, and good practice knows the limits.",
],
"toc": [("rise","Why it scaled so fast"),("changes","What genuinely changed"),
 ("same","What stayed the same"),("evidence","What the evidence shows"),
 ("limits","Where it falls short"),("rules","The rules still apply"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="rise">Why it scaled so fast</h2>
<p>Psychiatry was almost built for video. The core of a visit is a conversation and a careful observation, not a physical exam or a procedure, so moving it to a screen loses less than it would in most specialties. When the pandemic forced the issue and the rules loosened, telepsychiatry went from a niche to a default in a matter of months, and a lot of it stuck. That speed produced both genuine progress and a wave of overstated claims, which is why a clear account is worth having.</p>

<h2 id="changes">What genuinely changed</h2>
<p>The real gains are about access and logistics. A patient in a rural county with no local psychiatrist can see one two states away, within the limits of licensing. People who couldn't take half a day off work to travel can keep an appointment from home. For clinicians, overhead drops, because a telepsychiatry practice may need little or no physical office. Scheduling gets more flexible, no-shows can fall when travel isn't required, and a single psychiatrist can serve a wider area. In a field defined by shortage, widening reach is not a small thing. We cover that shortage in <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>.</p>

<h2 id="same">What stayed the same</h2>
<p>Underneath the format, the work is remarkably similar. The psychiatric interview is the same interview. The clinician is still assessing mood, thought, risk, and history, still forming a diagnosis from what's said and observed, and still responsible for the same standard of care. A good telepsychiatry visit isn't a watered-down version of an office visit; it's the same clinical reasoning conducted over video. The duty to the patient doesn't change with the medium.</p>

<h2 id="evidence">What the evidence shows</h2>
<p>The research on telepsychiatry is, on balance, reassuring. For many common conditions, studies generally find that telepsychiatry produces outcomes and patient satisfaction comparable to in-person care, which is part of why professional bodies have supported its expansion. That's a meaningful finding, but it should be read carefully. Comparable for many conditions is not identical for all patients in all situations, and the strength of the evidence varies by condition and population.</p>

<h2 id="limits">Where it falls short</h2>
<p>Telepsychiatry isn't a fit for everything. Some patients can't get privacy at home, lack a reliable connection, or simply do better in a room with another person. Certain assessments benefit from physical presence. Acute safety situations can be harder to manage remotely. And some people, including those who are very young, very ill, or experiencing certain symptoms, may need in-person care. Good practice treats telepsychiatry as a powerful option, not a universal answer, and knows when to bring someone in.</p>

<h2 id="rules">The rules still apply</h2>
<p>Moving online doesn't dissolve the regulations. Licensing still matters, since a clinician generally has to be licensed where the patient is located. Prescribing rules still apply, and prescribing controlled substances by telemedicine is its own evolving area, currently governed by federal flexibilities extended through 2026. For the details, see <a href="/business/why-controlled-substances-are-different/">why controlled substances are handled differently</a>. The format changed; the legal and ethical structure mostly came along for the ride.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>The hype version says telepsychiatry is always just as good and should replace the office. The cynical version says it's a lesser substitute that cheapens care. The accurate version is in between: for a lot of patients and conditions, it's comparable and dramatically more accessible, and for some it isn't the right choice. Treating it as a tool with clear strengths and real limits, rather than a revolution or a downgrade, is the honest read.</p>
""",
"faq": [
 ("Is telepsychiatry as effective as in-person care?", "For many common psychiatric conditions, research generally finds telepsychiatry comparable to in-person care in outcomes and satisfaction. It isn't the right fit for every patient or situation, and the strength of the evidence varies by condition."),
 ("Can a psychiatrist prescribe medication over telehealth?", "Yes, within licensing and prescribing rules. Prescribing controlled substances by telemedicine is governed by federal flexibilities currently extended through the end of 2026 while permanent rules are finalized."),
 ("Does my psychiatrist need to be licensed in my state for a video visit?", "Generally yes. Licensing usually depends on where the patient is physically located at the time of the visit, which is why telepsychiatry practices pay close attention to state licensure."),
],
"sources": [
 ("American Psychiatric Association, telepsychiatry toolkit and evidence base.", "https://www.psychiatry.org/psychiatrists/practice/telepsychiatry"),
 ("DEA and HHS, telemedicine prescribing flexibilities extended through 2026.", "https://www.hhs.gov/press-room/dea-telemedicine-extension-2026.html"),
 ("HRSA Bureau of Health Workforce, access and workforce context.", "https://bhw.hrsa.gov/data-research"),
],
"network": ["shrinkmd","psychiatryrx","shrinknetwork"],
})

# ============================================================
# 9. AI in psychiatry
# ============================================================
ART.append({
"slug": "technology/ai-in-psychiatry",
"active": "/technology/", "kicker": "Technology / Artificial intelligence",
"title": "AI in psychiatry: a grounded look",
"lede": "Artificial intelligence is arriving in psychiatry through the back office first, not the therapy chair. Here's what's genuinely useful, what's hype, and what to watch.",
"desc": "AI in psychiatry, assessed honestly: ambient scribes, decision support, and chatbots. What the evidence shows, what's overstated, and the real risks.",
"reading_time": "9 min read",
"breadcrumbs": [("Home", "/"), ("Technology", "/technology/"), ("AI in psychiatry", None)],
"quick_answer": "The most real use of AI in psychiatry right now is administrative: ambient scribes that draft clinical notes from a recorded visit. Early studies show meaningful reductions in documentation time and, in some settings, burnout. Other uses, like decision support and triage, are promising but earlier. AI chatbots marketed as therapy are the most overstated and the most risky. The honest summary is that AI is helping with the paperwork faster than it's changing the care.",
"takeaways": [
 "Ambient AI scribes are the clearest current win, mainly by cutting documentation time.",
 "Early research shows reduced note time and after-hours work, and in some settings lower burnout.",
 "Decision support and triage tools are promising but still early and need validation.",
 "AI chatbots sold as therapy are the most hyped and carry real safety and privacy risks.",
],
"toc": [("backoffice","AI arrived through the back office"),("scribes","Ambient scribes: the real win"),
 ("evidence","What the early evidence shows"),("support","Decision support and triage"),
 ("chatbots","The chatbot question"),("risks","The risks that matter"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="backoffice">AI arrived through the back office</h2>
<p>When people imagine AI in psychiatry, they picture a chatbot doing therapy. The reality so far is less dramatic and more useful: AI is landing first in the administrative machinery around care, where it can save time without making clinical decisions. That's the right place for it to start, because the documentation burden is one of the field's biggest, most measurable problems, and it's the kind of problem software is actually good at.</p>

<h2 id="scribes">Ambient scribes: the real win</h2>
<p>The clearest current application is the ambient AI scribe. With the patient's consent, the tool listens to the visit and produces a draft clinical note that the clinician reviews and edits. It doesn't diagnose or decide; it transcribes and organizes. For a field where the note carries enormous weight and eats enormous time, that's a meaningful help. We explain why the note matters so much in <a href="/business/why-documentation-shapes-care/">why documentation shapes care</a>.</p>

<h2 id="evidence">What the early evidence shows</h2>
<p>The early data is encouraging but should be read with care. Studies of ambient documentation tools have found reductions in time spent writing notes and in after-hours work, and some have reported drops in burnout among clinicians using them, in one ambulatory study from roughly half of clinicians burned out to under forty percent over about a month. The American Medical Association has reported large aggregate time savings across organizations adopting these tools. These are real results. They're also early, often from specific settings, and dependent on the clinician still reviewing every draft for accuracy.</p>

<h2 id="support">Decision support and triage</h2>
<p>A step beyond documentation is decision support: software that flags drug interactions, surfaces guideline-based options, or helps triage who needs to be seen sooner. This is promising, and some of it is genuinely helpful, but it's earlier and the bar is higher, because now the tool is influencing clinical choices. The responsible standard is that these systems assist a clinician who remains accountable, rather than replacing judgment. Validation, transparency about how a tool reaches its output, and attention to bias all matter more here than in the back office.</p>

<h2 id="chatbots">The chatbot question</h2>
<p>The most hyped and most fraught application is the AI chatbot marketed as therapy or emotional support. Some tools may help with structured, low-risk tasks like practicing a skill or journaling. But a general-purpose chatbot is not a clinician, can't take responsibility, and can respond unpredictably in exactly the high-stakes moments where it matters most. Treating a chatbot as a substitute for psychiatric care, especially in crisis, is the clearest example of the technology being oversold. If you're in crisis, contact a human service: in the US, call or text 988.</p>

<h2 id="risks">The risks that matter</h2>
<p>Three risks deserve attention. Privacy, because recording and processing a psychiatric conversation involves unusually sensitive data, and consent has to be real and informed. Accuracy, because a confident, fluent draft can be wrong, and an unreviewed AI note can introduce errors into the record. And overreliance, because the more a tool blends into the workflow, the easier it is to stop checking it. None of these means avoiding the technology. They mean using it as an assistant under human oversight, which is how the useful applications are already being deployed.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>The two errors are mirror images. One is breathless: AI will diagnose and treat mental illness and replace psychiatrists. The other is dismissive: it's all hype with nothing real. The grounded view is that a specific, unglamorous application, drafting the note, is already delivering measurable value, while the flashier promises remain unproven or risky. The interesting story in AI and psychiatry is the boring one, and it's worth telling accurately.</p>
""",
"faq": [
 ("Is AI replacing psychiatrists?", "No. The current real-world uses of AI in psychiatry are mostly administrative, such as drafting clinical notes, with the clinician reviewing and remaining accountable. Diagnosis and treatment decisions remain the clinician's responsibility."),
 ("Do AI scribes work in psychiatry?", "Early studies suggest ambient AI scribes reduce documentation time and after-hours work and, in some settings, reduce burnout. The drafts require careful review for accuracy, and recording a psychiatric visit raises privacy and consent considerations."),
 ("Can an AI chatbot replace therapy?", "No. A general-purpose chatbot isn't a clinician and can respond unpredictably in high-stakes moments. It shouldn't be relied on as a substitute for psychiatric care, especially in a crisis. In the US, call or text 988 if you need help now."),
],
"sources": [
 ("American Medical Association, AI scribes save 15,000 hours.", "https://www.ama-assn.org/practice-management/digital-health/ai-scribes-save-15000-hours-and-restore-human-side-medicine"),
 ("Use of Ambient AI Scribes to Reduce Administrative Burden and Professional Burnout (PMC).", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12492056/"),
 ("988 Suicide and Crisis Lifeline.", "https://988lifeline.org/"),
],
"network": ["shrinkopedia","anxietyresearch","shrinknetwork"],
})

# ============================================================
# 10. Burnout in psychiatry
# ============================================================
ART.append({
"slug": "culture/burnout-in-psychiatry",
"active": "/culture/", "kicker": "Culture / The work",
"title": "Burnout in psychiatry",
"lede": "Psychiatry actually reports some of the lower burnout rates in medicine. That's the surprising part. The harder part is understanding why the number isn't lower still.",
"desc": "Burnout in psychiatry: what national data shows, where the specialty sits relative to others, what drives it, and what protects against it. Honest and sourced.",
"reading_time": "8 min read",
"breadcrumbs": [("Home", "/"), ("Culture", "/culture/"), ("Burnout in psychiatry", None)],
"quick_answer": "Burnout among physicians has been high for years, hovering around the low to mid forties percent in recent national data, though it has eased somewhat from its pandemic peak. Psychiatry tends to report rates on the lower end, around the low thirties in recent figures, partly because the work has more control and less of some pressures than other specialties. But the drivers that remain, especially administrative load and emotional weight, are real, and burnout has consequences for both clinicians and patients.",
"takeaways": [
 "Physician burnout has eased from its pandemic peak but remains around the low to mid forties percent nationally.",
 "Psychiatry reports comparatively lower burnout, around the low thirties in recent data.",
 "Administrative burden, especially documentation, is among the most consistent drivers.",
 "Burnout isn't just a personal problem; it affects access, quality, and the workforce.",
],
"toc": [("number","Start with the number"),("compare","Where psychiatry sits"),
 ("why","Why it's lower, and why it isn't lower still"),("drivers","What actually drives it"),
 ("matters","Why it matters beyond the clinician"),("helps","What helps"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="number">Start with the number</h2>
<p>Burnout is a syndrome of emotional exhaustion, depersonalization, and a reduced sense of accomplishment, and in medicine it's been measured for years. National surveys put physician burnout high through the pandemic, near or above half of doctors, and recent data shows it easing somewhat, settling into roughly the low to mid forties percent depending on the survey. It's improving, slowly, and it's still far too common.</p>

<h2 id="compare">Where psychiatry sits</h2>
<p>Against that backdrop, psychiatry tends to look comparatively better. Recent figures have placed psychiatrist burnout in roughly the low thirties percent, among the lower rates across specialties rather than the highest. That surprises people who assume that absorbing other people's suffering all day would make psychiatry one of the worst. The data says otherwise, and the reasons are worth understanding.</p>

<h2 id="why">Why it's lower, and why it isn't lower still</h2>
<p>Several features of psychiatric work seem protective. Psychiatrists often have more control over their schedules, more ability to set appointment length, and a strong path into outpatient and telepsychiatry practice that offers flexibility. The work is relationship-centered, which many find meaningful, and the field is, by training and culture, more comfortable talking about mental health than most. None of that makes psychiatry immune. The same forces that burn out other doctors, especially paperwork and system pressure, still reach into psychiatry, which is why the rate is lower but not low.</p>

<h2 id="drivers">What actually drives it</h2>
<p>When clinicians describe burnout, the cause is rarely the patients. It's the system around the patients. Administrative burden comes up again and again, and documentation is a recurring villain, which is why ambient scribes that cut note time have shown burnout improvements in early studies. Add the emotional weight of risk and responsibility, the moral strain of not being able to give patients the access or time they need, and the economics that push toward volume, and you have the conditions that wear people down. We unpack the documentation piece in <a href="/business/why-documentation-shapes-care/">why documentation shapes care</a>.</p>

<h2 id="matters">Why it matters beyond the clinician</h2>
<p>Burnout isn't only a wellbeing issue for doctors. A burned-out workforce sees fewer patients, leaves practice earlier, and is more prone to error, which makes burnout a driver of the access problem too. In a field already short of clinicians, losing people to exhaustion deepens the shortage we describe in <a href="/economics/the-psychiatrist-shortage/">the psychiatrist shortage</a>. The case for taking burnout seriously isn't sentimental. It's structural.</p>

<h2 id="helps">What helps</h2>
<p>The evidence points more toward fixing systems than toward telling clinicians to be more resilient. Reducing administrative load, including the documentation burden, is one of the most direct levers, and it's part of why technology that genuinely saves time matters. Reasonable schedules, real control over the work, adequate support staff, and a culture that treats clinician wellbeing as an operational priority all help. Individual practices like supervision, peer support, and boundaries matter too, but they work best on top of a system that isn't actively making things worse.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>People assume psychiatry must have the worst burnout because of the emotional content of the work. The data says it's comparatively lower, which is a useful corrective. The opposite mistake is to treat the lower number as proof there's no problem. A third of a profession reporting burnout is a problem, and framing it as a personal failing rather than a system design issue is exactly the framing that keeps it from improving.</p>
""",
"faq": [
 ("Is burnout worse in psychiatry than other specialties?", "No. Recent national data places psychiatrist burnout among the lower rates across specialties, in roughly the low thirties percent, compared with a physician average in the low to mid forties. It's comparatively lower, though still common."),
 ("What causes burnout in psychiatrists?", "The most consistent drivers are system factors, especially administrative and documentation burden, plus the emotional weight of risk and responsibility and the strain of limited access and time. Patients themselves are rarely the cause clinicians cite."),
 ("Does reducing documentation help burnout?", "Early evidence suggests it can. Studies of ambient AI scribes that cut documentation time have reported reductions in burnout in some settings, supporting the idea that administrative load is a major driver."),
],
"sources": [
 ("Medscape Physician Mental Health and Wellbeing Report 2025.", "https://www.medscape.com/sites/public/mental-health/2025"),
 ("American Medical Association, physician burnout trends.", "https://www.ama-assn.org/practice-management/physician-health"),
 ("Use of Ambient AI Scribes to Reduce Administrative Burden and Professional Burnout (PMC).", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12492056/"),
],
"network": ["shrinkopedia","shariqrefai","shrinknetwork"],
})

# ============================================================
# 11. The psychiatrist shortage
# ============================================================
ART.append({
"slug": "economics/the-psychiatrist-shortage",
"active": "/economics/", "kicker": "Economics / Workforce",
"title": "The psychiatrist shortage",
"lede": "Long waits for a psychiatrist aren't a local glitch. They're the visible edge of a national workforce shortage with deep roots and a few real, if partial, fixes.",
"desc": "The psychiatrist shortage explained: how big it is, why it persists, where it concentrates, and what actually expands access, including the Collaborative Care Model.",
"reading_time": "9 min read",
"breadcrumbs": [("Home", "/"), ("Economics", "/economics/"), ("The psychiatrist shortage", None)],
"quick_answer": "The United States doesn't have enough psychiatrists, and federal data shows a large share of the population lives in areas with too few mental health professionals. The shortage comes from a slow training pipeline, an aging workforce, uneven geographic distribution, and payment models that limit supply. There's no quick fix, because training a psychiatrist takes over a decade, but approaches like the Collaborative Care Model can stretch the existing workforce much further.",
"takeaways": [
 "Roughly 137 million Americans live in a federally designated mental health shortage area, per HRSA.",
 "Federal projections estimate a shortage of tens of thousands of adult psychiatrists by 2038.",
 "Causes include a slow pipeline, an aging workforce, geographic maldistribution, and payment limits.",
 "The Collaborative Care Model, backed by more than 80 trials, can extend one psychiatrist across many more patients.",
],
"toc": [("scale","The scale of it"),("future","Where it's heading"),
 ("why","Why it persists"),("geography","The geography problem"),
 ("fixes","What actually helps"),("ccm","The Collaborative Care Model"),
 ("misunderstood","What's commonly misunderstood"),("faq","Common questions")],
"body": """
<h2 id="scale">The scale of it</h2>
<p>If you've waited months for a psychiatry appointment, you've met the shortage in person. It's not a local quirk. The federal Health Resources and Services Administration, HRSA, designates areas with too few mental health professionals, and by recent counts roughly 137 million Americans, around 40 percent of the population, live in one of those mental health professional shortage areas. That's not a statement about one underserved town. It's most of the country.</p>

<h2 id="future">Where it's heading</h2>
<p>The projections don't show the gap closing on its own. HRSA's modeling has estimated a shortage of tens of thousands of adult psychiatrists by 2038 under baseline assumptions, and substantially larger if access improves and more people seek care, which would raise demand further. Child and adolescent psychiatry, already among the thinnest parts of the workforce, is projected to remain deeply inadequate relative to need. The direction is the concern as much as the current number.</p>

<h2 id="why">Why it persists</h2>
<p>Several causes stack up. The training pipeline is slow: it takes well over a decade from the start of college to an independent psychiatrist, so you can't quickly manufacture more, a point we cover in <a href="/careers/how-psychiatry-residency-works/">how residency works</a>. The workforce is aging, with a large share of psychiatrists near retirement. Demand has risen sharply, especially since the pandemic, while supply moves slowly. And the payment system limits supply in subtler ways, since low reimbursement and heavy paperwork push some psychiatrists toward cash-pay or part-time work, which we cover in <a href="/business/cash-pay-vs-insurance/">cash-pay vs insurance</a>.</p>

<h2 id="geography">The geography problem</h2>
<p>The shortage isn't spread evenly. Psychiatrists cluster in cities and around academic centers, while rural and lower-income areas can have almost none. That maldistribution means national averages understate how bad access is in the places that have the least. It's also why telepsychiatry matters so much: by decoupling care from location, it can bring a psychiatrist's time to a county that has no local one. See <a href="/technology/what-telepsychiatry-changes/">what telepsychiatry changes</a>.</p>

<h2 id="fixes">What actually helps</h2>
<p>There's no single fix, but several things move the needle. Expanding residency training slots increases supply over time. Telepsychiatry spreads existing supply across geography. Other prescribers, including psychiatric nurse practitioners and physician assistants, add capacity. Reducing administrative burden keeps existing psychiatrists in practice longer and at fuller capacity. And critically, models that change the ratio of psychiatrists to patients can expand access without waiting a decade for new graduates.</p>

<h2 id="ccm">The Collaborative Care Model</h2>
<p>The most evidence-backed of those models is Collaborative Care. In it, a primary care team includes a behavioral health care manager and a consulting psychiatrist who reviews a caseload and advises rather than seeing most patients directly. The approach grew out of the IMPACT trial and has since been supported by more than 80 randomized trials, making it one of the better-evidenced interventions in the field. Its power is leverage: because the psychiatrist consults on many patients through the primary care team rather than seeing each one, the model can extend a single psychiatrist's reach across a far larger population than a traditional clinic could. It doesn't replace direct care, but it's one of the few approaches that meaningfully addresses the shortage now rather than in 2038.</p>

<h2 id="misunderstood">What's commonly misunderstood</h2>
<p>People often read the shortage as laziness or greed in the profession, as if psychiatrists are simply choosing not to take patients. The deeper causes are structural: a slow pipeline, an aging workforce, geographic concentration, and payment incentives. The other misunderstanding is fatalism, the sense that nothing can be done. Training takes time, true, but telepsychiatry, team-based models like Collaborative Care, and reducing the burdens that drive psychiatrists out of full practice are real levers that are already being pulled.</p>
""",
"faq": [
 ("How many Americans lack adequate access to a psychiatrist?", "By recent HRSA counts, roughly 137 million Americans, about 40 percent of the population, live in a designated mental health professional shortage area, meaning there are too few mental health professionals for the population's needs."),
 ("Why is there a psychiatrist shortage?", "Main causes include a slow training pipeline that takes over a decade, an aging workforce nearing retirement, rising demand for care, uneven geographic distribution, and payment models that limit how many patients psychiatrists can see in-network."),
 ("What is the Collaborative Care Model?", "It's a team-based approach where a primary care team includes a behavioral health care manager and a consulting psychiatrist who advises on a caseload rather than seeing most patients directly. Backed by more than 80 trials, it extends one psychiatrist's reach across many more patients."),
],
"sources": [
 ("HRSA Bureau of Health Workforce, behavioral health workforce brief and projections.", "https://bhw.hrsa.gov/sites/default/files/bureau-health-workforce/data-research/Behavioral-Health-Workforce-Brief-2025.pdf"),
 ("Unutzer et al., the psychiatrist's role in the Collaborative Care Model, American Journal of Psychiatry.", "https://psychiatryonline.org/doi/10.1176/appi.ajp.2015.15010017"),
 ("AMA, how collaborative care can help close the mental health care gap.", "https://www.ama-assn.org/practice-management/scope-practice/how-collaborative-care-can-help-close-mental-health-care-gap"),
],
"network": ["shrinkmd","anxietyresearch","shrinknetwork"],
})

PAGES = [make_article(a) for a in ART]
