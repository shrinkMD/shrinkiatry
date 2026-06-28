# -*- coding: utf-8 -*-
"""Deeper rewrites of the thin trust/standards pages. Keyed by slug; buildv7 swaps them in."""
import engine as S
import content_legal as CL
import content_tools as CT

OVERRIDES = {}

def put(slug, kicker, title, lede, body, desc, network=None, schema=None):
    OVERRIDES[slug] = CL.page(slug, kicker, title, lede, body, desc, network, schema)

# ---------------- About ----------------
put(
    "about", "About", "About shrinkiatry",
    "The publication about the profession of psychiatry, and where it sits in The Shrink Network.",
    """
<p>shrinkiatry is a publication about the profession of psychiatry. Not the conditions, not the medications, not the clinical care itself, but the profession that delivers all of it: how psychiatrists are trained, how practices are built and paid, how technology is changing the work, how the economics shape access, and what the public rarely sees behind the clinical encounter.</p>
<p>It exists because that layer is real and underexplained. People can find good information about anxiety, depression, or a specific medication. It's much harder to find a clear, honest, non-promotional account of how the profession actually works, written to a standard a psychiatrist would stand behind. That's the gap shrinkiatry fills, and it's why we describe the site as the profession-intelligence layer of The Shrink Network.</p>
<h2>Who it's for</h2>
<p>We write for a wider room than most psychiatry sites. A medical student weighing the specialty, a resident learning the parts of the job nobody taught in class, a journalist who needs the real shape of the workforce shortage, a policymaker, a founder thinking about private practice, and a curious patient who just wants to understand why their care works the way it does. The aim is that all of them can read the same page and come away with an accurate picture, without being talked down to or sold anything.</p>
<h2>How the site is organized</h2>
<p>Three things make shrinkiatry hard to copy, and they're the best places to start. <a href="/psychiatry-operating-room/">The Psychiatry Operating Room</a> is a map of the systems running underneath an ordinary visit, from training to documentation to access. The <a href="/decoder/">Psychiatry Decoder</a> answers the confusing realities of care in plain English, like why appointments feel short or why a dose changes so slowly. <a href="/state-of-psychiatry/">The State of Psychiatry</a> tracks the profession's pressure points with sourced data. Around those sit the section hubs: <a href="/careers/">careers</a>, <a href="/business/">business</a>, <a href="/technology/">technology</a>, <a href="/economics/">economics</a>, culture, ethics, and more.</p>
<h2>Where it fits in The Shrink Network</h2>
<p>shrinkiatry is the profession layer of <a href="https://shrinknetwork.com" target="_blank" rel="noopener noreferrer">The Shrink Network</a>, a coordinated group of independent mental health properties. Each one does a different job. <a href="https://shrinkopedia.com" target="_blank" rel="noopener noreferrer">Shrinkopedia</a> explains concepts, and <a href="https://shrinktionary.com" target="_blank" rel="noopener noreferrer">Shrinktionary</a> defines the terms. <a href="https://psychiatryrx.org" target="_blank" rel="noopener noreferrer">PsychiatryRx</a> explains medications. <a href="https://anxietyresource.org" target="_blank" rel="noopener noreferrer">AnxietyResource</a> and <a href="https://depressionresource.org" target="_blank" rel="noopener noreferrer">DepressionResource</a> explain specific conditions. <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> provides clinical care. shrinkiatry explains the profession behind all of it, and links out to the others rather than duplicating them.</p>
<h2>What shrinkiatry is not</h2>
<p>It isn't a clinic, and it doesn't provide medical advice or care. It isn't a patient-education site about conditions or drugs; the network has those. It isn't a marketing site for any practice. And it isn't anti-psychiatry or boosterism either. The tone is inside-baseball but accessible: clear, direct, professional, and evidence-based, with opinion clearly labeled as opinion. If you're looking for clinical care rather than commentary, <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the care layer of the network.</p>
<h2>The standard behind it</h2>
<p>Every page is written or reviewed by <a href="/editorial-team/">Shariq Refai, MD, MBA</a>, a board-certified psychiatrist and the founder of shrinkMD, and published by shrinkMD Publishing, LLC. Factual claims are tied to primary sources and listed on the page, the site runs no advertising and sells nothing, and where there's a financial interest, such as shrinkMD, it's <a href="/disclosures/">disclosed plainly</a>. You can read the full <a href="/editorial-standards/">editorial standards</a> and <a href="/how-we-build-content/">how we build content</a>.</p>
""",
    "About shrinkiatry: the publication about the profession of psychiatry and the profession-intelligence layer of The Shrink Network.",
    ["shrinkmd", "shariqrefai", "shrinknetwork"],
)

# ---------------- Editorial team ----------------
put(
    "editorial-team", "About", "Editorial team",
    "Who writes and reviews shrinkiatry, and the standard they're held to.",
    """
<h2>Shariq Refai, MD, MBA</h2>
<p><strong>Board-certified psychiatrist. Founder of shrinkMD. Editor of shrinkiatry.</strong></p>
<p>Shariq Refai is a board-certified psychiatrist based in Jacksonville, Florida, and the founder of shrinkMD, an independent multistate telepsychiatry practice. He holds an MBA from Duke University, trained at St. George's University School of Medicine, and completed residency at the University of Hawaii and John Peter Smith Hospital. Before medical school, he worked nights as a psychiatric technician while studying at the University of North Florida, an experience he credits with teaching him early that mental illness doesn't sort people by income, status, or background.</p>
<p>Across The Shrink Network, he serves as the medical editor and reviewer, setting the clinical line for what claims are made and how. On shrinkiatry, his role is both author and reviewer: the content reflects how the profession actually works, written to a standard he'll put his name to. He's also the author of three forthcoming books that translate psychiatry into plain language, published by shrinkMD Publishing.</p>
<h2>Why a psychiatrist signs off on every page</h2>
<p>shrinkiatry covers a profession where small inaccuracies do real damage: a misstated rule, an overstated study, a tidy answer where the truth is messy. Having a board-certified psychiatrist write or review every page is the difference between commentary that sounds informed and commentary that is. The credential matters here because the subject is the practice of medicine itself, and the reviewer has lived the training, the documentation, the prescribing rules, and the business decisions the site describes.</p>
<h2>What review actually checks</h2>
<p>Review isn't a rubber stamp. It checks that claims match their sources, that nuance survived the edit, that nothing was rounded up to a cleaner answer than the evidence supports, and that opinion is labeled as opinion. It also checks tone: that the page respects the reader, avoids fearmongering, and doesn't drift into giving individualized medical advice. Where the evidence is genuinely mixed, the reviewer's job is to make sure the page says so.</p>
<h2>Independence and disclosure</h2>
<p>The editor has financial interests, most notably in shrinkMD, and the only honest way to handle that is to state it. His interest in shrinkMD, his books, and the Unstuck app is <a href="/disclosures/">disclosed plainly</a>, and the site takes no advertising, sells nothing, and accepts no affiliate or referral commissions. References to shrinkMD are made because it's the network's clinical practice, not as paid placement. You can read more about his background and writing at <a href="https://shariqrefai.com" target="_blank" rel="noopener noreferrer">shariqrefai.com</a>.</p>
<h2>How review works</h2>
<p>Every article on shrinkiatry is written or reviewed by Dr. Refai before it's published, and carries a last-reviewed date. Articles are sourced from primary materials, including accreditation and certification bodies, federal data, professional associations, and peer-reviewed research. We say plainly when evidence is mixed or limited. Pages are revisited when the facts change. The full process is described in <a href="/how-we-build-content/">how we build content</a> and <a href="/editorial-standards/">editorial standards</a>.</p>
""",
    "The shrinkiatry editorial team: Shariq Refai, MD, MBA, a board-certified psychiatrist, and the review standard behind the publication.",
    ["shariqrefai", "shrinkmd", "shrinknetwork"],
    schema=[S._jsonld_person()],
)

# ---------------- Editorial standards ----------------
put(
    "editorial-standards", "Standards", "Editorial standards",
    "The rules shrinkiatry holds itself to, so you know what you're reading and why you can trust it.",
    """
<p>shrinkiatry is built to be trusted on a subject where trust is easy to lose: the inner workings of a profession. These are the standards every page is held to, and we publish them because a site that asks for your trust should show its work.</p>
<h2>Accuracy first</h2>
<p>Content is written to be accurate first and engaging second. Factual claims are tied to real, citable sources, and those sources are listed on the page. When the evidence is mixed, thin, or limited to a specific context, we say so rather than rounding up to a clean answer. We'd rather a page admit uncertainty than pretend to a precision it doesn't have.</p>
<h2>Reviewed by a psychiatrist</h2>
<p>Every article is written or reviewed by <a href="/editorial-team/">Shariq Refai, MD, MBA</a>, a board-certified psychiatrist, before publication, and carries a last-reviewed date. Pages are revisited when the facts change, for example when regulations, guidelines, or workforce data update.</p>
<h2>Sourcing and citation</h2>
<p>For rules and structures, we cite the body that sets the rule, such as the ACGME, the ABPN, the DEA, or HRSA. For clinical and scientific claims, we prefer peer-reviewed research, systematic reviews, and guidelines over secondary coverage, and we attribute statistics to their source with a date where it matters. How we weigh competing evidence is described in <a href="/evidence-methodology/">evidence methodology</a>.</p>
<h2>Independent and ad-free</h2>
<p>shrinkiatry runs no advertising, sells nothing, and takes no affiliate or referral commissions. What an article says is decided by the evidence, not by a commercial interest. Where the editor has a financial interest, such as shrinkMD, it's <a href="/disclosures/">disclosed plainly</a> on the pages where it's relevant, and references to shrinkMD are made because it's the network's clinical practice, not as paid placement.</p>
<h2>Commentary is labeled</h2>
<p>We distinguish reported, sourced explanation from opinion. Opinion and editorial content are clearly marked as such, because the line between describing the profession and arguing about it should always be visible to the reader.</p>
<h2>Careful, respectful language</h2>
<p>We write about people at their most vulnerable, so language matters. We avoid stigmatizing framing, we don't sensationalize, and we describe conditions and the people who have them with care. We also avoid the kind of false balance that treats a fringe claim as equal to a settled one.</p>
<h2>Not medical advice</h2>
<p>shrinkiatry explains the profession. It doesn't diagnose, treat, or give individualized medical advice, and reading it doesn't create a doctor-patient relationship. If you need care, <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network's clinical practice. See the full <a href="/medical-disclaimer/">medical disclaimer</a>.</p>
<h2>Voice</h2>
<p>The writing is plain, direct, and human. We use contractions, keep sentences clear, avoid hype and scare quotes, and write so that a psychiatrist, a resident, a journalist, and a curious patient can all read the same page and come away with an accurate picture.</p>
<h2>Telling us we got it wrong</h2>
<p>If something is inaccurate, we want to fix it openly. See our <a href="/corrections/">corrections policy</a> or email <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a>.</p>
""",
    "shrinkiatry editorial standards: accuracy first, psychiatrist review, careful sourcing, independence, labeled opinion, and open corrections.",
    ["shrinknetwork", "shrinkmd"],
)

# ---------------- How we build content ----------------
put(
    "how-we-build-content", "Standards", "How we build content",
    "The process behind a shrinkiatry article, from question to published page.",
    """
<p>Every shrinkiatry article follows the same path, so the quality is consistent and the reasoning is visible. We publish the process for the same reason we publish our sources: a site about a profession should be transparent about its own.</p>
<h2>1. Start from a real question</h2>
<p>We write to answer questions people actually have about the profession, like how residency works, why so many psychiatrists don't take insurance, or what telepsychiatry really changed. The goal is a page that fully answers the question, not a thin post built around a keyword. If a topic is already covered well elsewhere in the network, we link to it instead of duplicating it.</p>
<h2>2. Research from primary sources</h2>
<p>We work from primary materials: accreditation bodies like the ACGME, certification boards like the ABPN, federal agencies like HRSA and the DEA, professional associations like the American Psychiatric Association, and peer-reviewed research. We avoid building claims on top of other websites, because errors compound when sites cite each other instead of the original source.</p>
<h2>3. Draft in plain language</h2>
<p>Drafts are written to be clear and direct, with contractions and short sentences, no hype, and no jargon left undefined. Where a concept lives elsewhere in the network, we link to it rather than re-explaining it. We try to write the version of the page we'd want to hand to a smart friend who asked the question.</p>
<h2>4. Review by a psychiatrist</h2>
<p>Every article is reviewed by <a href="/editorial-team/">Shariq Refai, MD, MBA</a> for clinical and professional accuracy before it's published. He sets the line on what's claimed, what nuance stays in, and what gets cut as oversimplified. A claim that can't be supported doesn't run, and a tidy answer that misrepresents a messy reality gets rewritten.</p>
<h2>5. Source, date, and structure</h2>
<p>Each article ships with its sources listed, a last-reviewed date, key takeaways, an on-this-page outline, related links into the network, and structured data so search engines and AI systems can recognize it as reviewed, sourced content. How we weigh evidence is described in <a href="/evidence-methodology/">evidence methodology</a>.</p>
<h2>What a finished page includes</h2>
<p>A finished shrinkiatry page is more than prose. It carries a why-trust summary, a plain-English answer up top for readers and AI assistants in a hurry, key takeaways, a clear heading structure, a sources list, a review panel with the reviewer and last-reviewed date, and routing into the rest of the network. The structure is part of the standard, not decoration.</p>
<h2>6. Keep it current</h2>
<p>Pages are revisited when the facts change. Regulations, guidelines, and workforce data move, and the page should move with them. Corrections are handled openly under our <a href="/corrections/">corrections policy</a>, and we distinguish a correction, where something was wrong, from an update, where the facts themselves changed.</p>
""",
    "How shrinkiatry builds content: real questions, primary sources, plain-language drafting, psychiatrist review, full sourcing, and ongoing updates.",
    ["shrinknetwork", "anxietyresearch"],
)

# ---------------- Evidence methodology ----------------
put(
    "evidence-methodology", "Standards", "How we evaluate evidence",
    "How shrinkiatry weighs sources and states the limits of what's known.",
    """
<p>shrinkiatry covers a profession, so a lot of what we report is institutional fact: how long residency is, what a board requires, what a regulation says. For those, we go to the body that sets the rule. But we also report on research and trends, and there the discipline of weighing evidence matters. This page explains how we do it.</p>
<h2>Institutional facts versus research claims</h2>
<p>We treat two kinds of statements differently. An institutional fact, like the length of residency or the schedule of a controlled substance, has a single authoritative source: the organization that sets it. A research claim, like how effective a treatment is or how common burnout is, lives on a spectrum of evidence and needs to be handled with more care. Confusing the two, treating a contested finding as if it were a fixed rule, is a common way that health writing goes wrong.</p>
<h2>We prefer primary and authoritative sources</h2>
<p>For rules and structures, we cite the source of the rule, such as the ACGME, the ABPN, the DEA, or HRSA. For clinical and scientific claims, we prefer peer-reviewed research, systematic reviews, and guidelines from recognized bodies over secondary coverage. A systematic review or a professional guideline generally carries more weight than a single study, and a single study carries more weight than an expert's unsupported assertion.</p>
<h2>We separate what's shown from what's claimed</h2>
<p>A single study is not a settled fact. When we describe research, we try to convey the strength and the limits of the evidence, including how large or replicated a finding is, what population it applies to, and what it doesn't prove. Early or single-setting results are labeled as such. An association is not a cause, and we try not to let careful research get reported as more certain than it is.</p>
<h2>How we handle conflicting evidence</h2>
<p>When good studies disagree, we don't pick the one we like. We say the evidence is mixed, describe the shape of the disagreement, and lean on the weight of the better-designed and better-replicated work. Where a question is genuinely unresolved, the honest answer on the page is that it's unresolved.</p>
<h2>We state uncertainty plainly</h2>
<p>When evidence is mixed, thin, or evolving, we say so. That's especially true for fast-moving areas like artificial intelligence and telemedicine regulation, where today's accurate statement may need updating tomorrow. We'd rather a reader leave with an accurate sense of uncertainty than a false sense of resolution.</p>
<h2>We attribute and date numbers</h2>
<p>Statistics are tied to their source and dated where it matters. If a figure is an estimate or a projection, we describe it that way rather than presenting it as a fixed count, and we prefer ranges to false precision when the underlying data is itself a range.</p>
<h2>We update</h2>
<p>When better evidence or newer data appears, the page changes, and significant changes are noted under our <a href="/corrections/">corrections policy</a>, consistent with our <a href="/editorial-standards/">editorial standards</a>.</p>
""",
    "How shrinkiatry evaluates evidence: primary and authoritative sources, separating what's shown from what's claimed, and stating uncertainty plainly.",
    ["anxietyresearch", "shrinknetwork"],
)

# ---------------- Medical disclaimer ----------------
put(
    "medical-disclaimer", "Legal", "Medical disclaimer",
    "What shrinkiatry is, what it isn't, and why none of it is medical advice.",
    """
<p><strong>shrinkiatry provides education and professional commentary about the profession of psychiatry. It does not provide medical advice.</strong></p>
<p>The content on this site is for general educational and informational purposes only. It explains how psychiatry is trained, organized, paid, regulated, and practiced. It is not a substitute for professional medical advice, diagnosis, or treatment, and it does not address any individual's specific situation.</p>
<h2>Why we draw this line clearly</h2>
<p>Psychiatry is a clinical field, and clinical decisions depend on the specifics of one person: their history, their other conditions, their medications, their context. A general-audience site can't know any of that, so anything it said as if it were advice would be guesswork at best and harmful at worst. Drawing a bright line between explaining the profession and advising an individual protects you, and it keeps the writing honest about what it can and can't do.</p>
<p>Reading shrinkiatry does not create a doctor-patient relationship between you and Shariq Refai, MD, MBA, shrinkMD, or anyone associated with the site. No content here should be used to diagnose or treat a health problem or disease, or to start, stop, or change any treatment.</p>
<h2>What to do instead</h2>
<p>Always seek the advice of a licensed clinician who knows your situation with any questions about a medical or mental health condition, and never disregard professional advice or delay seeking it because of something you read here. If you're looking for psychiatric care, <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network's clinical practice. For understanding a specific condition or medication, the network's education sites, <a href="https://shrinkopedia.com" target="_blank" rel="noopener noreferrer">Shrinkopedia</a> and <a href="https://psychiatryrx.org" target="_blank" rel="noopener noreferrer">PsychiatryRx</a>, go deeper than we do.</p>
<h2>If you're in crisis</h2>
<p>If you may be in danger or are thinking about suicide, call or text <strong>988</strong> in the US to reach the Suicide and Crisis Lifeline, available 24 hours a day. Call <strong>911</strong> if someone is in immediate danger. You can also text HOME to 741741 to reach the Crisis Text Line. If you're outside the US, contact your local emergency number or a local crisis line.</p>
<h2>Accuracy and currency</h2>
<p>We work to keep content accurate and current, but medicine, regulation, and data change. shrinkiatry makes no warranty that all information is complete or up to date at the moment you read it, and is not liable for decisions made based on the content. When you act on anything you read here, confirm it against a primary source or a qualified professional.</p>
""",
    "shrinkiatry medical disclaimer: educational and professional commentary only, not medical advice, and not a substitute for a licensed clinician.",
    ["shrinkmd", "shrinknetwork"],
)

# ---------------- AI use ----------------
put(
    "ai-use", "Legal", "AI use",
    "How shrinkiatry does and doesn't use artificial intelligence in making this site.",
    """
<p>We write about AI, so we should be clear about how we use it ourselves. The short version: people direct the work, a psychiatrist reviews it, and facts are verified by a human before anything is published.</p>
<h2>Human judgment, psychiatrist review</h2>
<p>shrinkiatry's content is directed by people and reviewed by a board-certified psychiatrist. AI tools may assist with parts of the process, such as drafting, research organization, or editing, but the substance, the claims, and the final word are set by human editorial judgment and by <a href="/editorial-team/">Dr. Refai's</a> review. Nothing is published just because a model produced it, and the reviewer is accountable for every page regardless of how a draft started.</p>
<h2>Where AI helps, and where it doesn't</h2>
<p>AI is useful for the mechanical parts of writing: organizing notes, suggesting structure, tightening a sentence. It is not trustworthy for facts, citations, or clinical nuance, which is exactly where the stakes are highest on a site like this. So we use it where it helps and keep it well away from the parts where being confidently wrong does damage.</p>
<h2>Sourcing is verified by people</h2>
<p>Facts and citations are checked against primary sources by a person, not accepted on a model's say-so. We don't publish AI-generated statistics or references without verifying them against the original source, because models are known to produce plausible citations that don't exist.</p>
<h2>No AI medical advice</h2>
<p>shrinkiatry doesn't use AI to give medical advice, and you shouldn't either. As we explain in <a href="/technology/ai-in-psychiatry/">AI in psychiatry</a> and in the <a href="/decoder/">Decoder</a>, a general-purpose chatbot isn't a clinician and shouldn't be relied on for care, especially in a crisis.</p>
<h2>How AI systems may use this site</h2>
<p>We welcome AI search and assistant systems reading and citing shrinkiatry, and we publish structured data and a plain-language summary on each page to make our content legible to them. We ask that they cite the source and attribute claims to the specific page. Republishing substantial content or using it to train commercial models without permission isn't permitted; see <a href="/copyright/">copyright</a>.</p>
""",
    "How shrinkiatry uses AI: human-directed, psychiatrist-reviewed, with all facts and sources verified by people, and no AI medical advice.",
    ["shrinknetwork", "anxietyresearch"],
)

# ---------------- Disclosures ----------------
put(
    "disclosures", "Legal", "Disclosures",
    "The financial interests behind shrinkiatry, stated plainly.",
    """
<p>Trust depends on knowing who benefits. Here are the relevant interests, disclosed plainly, because a site that covers the business of psychiatry has no business hiding its own.</p>
<h2>Why disclosure matters here</h2>
<p>shrinkiatry writes about practice models, cash-pay psychiatry, and clinical care, and the editor has a financial stake in a telepsychiatry practice. That's a real potential conflict, and the right response isn't to pretend it away but to state it clearly so you can weigh what you read with full information. Disclosure doesn't remove an interest; it just makes it visible, which is the honest minimum.</p>
<h2>The editor's interests</h2>
<p>shrinkiatry is written or reviewed by Shariq Refai, MD, MBA, who has financial interests in several things this site may mention:</p>
<ul>
<li><strong>shrinkMD</strong>, an independent multistate telepsychiatry practice he founded. When shrinkiatry refers to shrinkMD as the network's clinical practice, understand that the editor has a financial interest in it.</li>
<li><strong>Books</strong> published by shrinkMD Publishing, LLC, the imprint behind this site.</li>
<li><strong>The Unstuck app</strong> and the shrinQ program, wellness tools he created.</li>
</ul>
<h2>How we keep coverage honest despite the interest</h2>
<p>The safeguards are concrete. shrinkiatry runs no advertising, sells nothing on the site, and takes no affiliate or referral commissions from anything it links to. Claims are tied to primary sources rather than to whatever would help the business. References to shrinkMD are made because it's the network's clinical practice and the natural place to route someone who needs care, not as paid placement, and we point readers to non-network resources where those are the better fit. Where a financial interest is relevant on a page, we note it.</p>
<h2>What we don't take</h2>
<p>No ad networks, no sponsored posts, no affiliate links, no pay-for-placement. If that ever changes, this page changes first, and any paid relationship would be labeled on the pages it touches.</p>
<h2>The network</h2>
<p>shrinkiatry is part of <a href="https://shrinknetwork.com" target="_blank" rel="noopener noreferrer">The Shrink Network</a>, a group of independent properties created or reviewed by Dr. Refai. The network links its sites to one another openly. You can read the network's own <a href="https://shrinknetwork.com/disclosures/" target="_blank" rel="noopener noreferrer">disclosures</a> as well.</p>
""",
    "shrinkiatry disclosures: the editor's financial interests in shrinkMD, books, and apps, stated plainly. No ads, no affiliate commissions, no paid placement.",
    ["shrinkmd", "shariqrefai", "shrinknetwork"],
)

# ---------------- Tools (custom: reuse the tool cards) ----------------
def _tools_page():
    intro = (
        "<p>shrinkiatry's tools are meant to make the structure of the profession legible: what a practice earns, where the workforce is thin, how programs compare. They're educational. None of them is medical, legal, or financial advice, and none of them replaces a professional who knows your specific situation.</p>"
        "<h2>What makes a tool worth building</h2>"
        "<p>We build tools that teach, not gimmicks that perform. A good educational tool here does three things: it runs on transparent assumptions you can see and change, it's honest about what it ignores, and it leaves you understanding the system better than a static page could. The revenue estimator, for instance, isn't there to predict your income. It's there to let you feel how the levers, visit volume, pricing, payer mix, and overhead, push against each other.</p>"
        "<h2>What's live</h2>"
        "<p>The <a href=\"/tools/private-practice-revenue-estimator/\">private practice revenue estimator</a> models the gross and net annual revenue of an independent psychiatry practice from a handful of inputs. It runs entirely in your browser, sends nothing anywhere, and shows its math. It's built to pair with the business section, especially <a href=\"/business/how-private-psychiatry-practices-work/\">how private practices work</a> and <a href=\"/business/cash-pay-vs-insurance/\">cash-pay versus insurance</a>, so the numbers have context.</p>"
        "<h2>What's in development</h2>"
        "<p>Several more are planned: a psychiatry workforce map built from HRSA shortage-area data, a residency program explorer, and a compensation explorer by practice type and setting. We'd rather ship these accurate and well-sourced than fast, so they land as the underlying data and design are ready. If there's a tool you'd find useful, tell us through <a href=\"/contact/\">contact</a>.</p>"
        "<h2>A word of caution</h2>"
        "<p>Every tool here is a model, and a model is a simplification. The outputs are a way to build intuition, not a forecast for any specific person or practice, and they should never stand in for advice from a professional who knows your circumstances. We label that on each tool, and we mean it.</p>"
    )
    body = (
        '<section class="section section--slate section--tight"><div class="wrap">'
        '<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">Tools</span></nav>'
        '<span class="eyebrow">Tools</span><h1 class="mt-1">Tools for understanding the profession</h1>'
        '<p class="hero__sub mt-2" style="max-width:54ch">Useful, educational tools rather than gimmicks. Built to be bookmarked, sourced where they use data, and clear about what they are and aren\'t.</p>'
        '</div></section>'
        f'<section class="section section--surface"><div class="wrap"><div class="maxread flow">{intro}</div><div class="mt-4">{CT._tool_cards()}</div></div></section>'
        f'<section class="section section--tint"><div class="wrap"><div class="maxread">{S.network_continue(["shrinkmd","anxietyresearch","shrinknetwork"])}</div></div></section>'
    )
    return {
        "slug": "tools", "active": "/tools/",
        "title": "Tools | shrinkiatry",
        "desc": "Educational tools for understanding the profession of psychiatry, starting with a private-practice revenue estimator. More in development.",
        "breadcrumbs": [("Home", "/"), ("Tools", None)],
        "body": body,
    }

OVERRIDES["tools"] = _tools_page()
