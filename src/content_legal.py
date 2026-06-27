# -*- coding: utf-8 -*-
"""Legal and utility pages."""
import engine as S

def hero(kicker, title, lede):
    return f"""<section class="section section--slate section--tight"><div class="wrap">
<nav class="breadcrumb" aria-label="Breadcrumb" style="color:#aeb6bd"><a href="/" style="color:#cdd6dd">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">{title}</span></nav>
<span class="eyebrow">{kicker}</span><h1 class="mt-1">{title}</h1>
<p class="hero__sub mt-2" style="max-width:56ch">{lede}</p></div></section>"""

def page(slug, kicker, title, lede, body_html, desc, network=None, schema=None):
    net = ""
    if network:
        net = f'<section class="section section--tint"><div class="wrap"><div class="maxread">{S.network_continue(network)}</div></div></section>'
    body = (hero(kicker, title, lede)
            + f'<section class="section section--surface"><div class="wrap"><div class="maxread flow">{body_html}</div></div></section>'
            + net)
    p = {"slug": slug, "active": None, "title": f"{title} | shrinkiatry",
         "desc": desc, "breadcrumbs": [("Home", "/"), (title, None)], "body": body}
    if schema:
        p["schema"] = schema
    return p

PAGES = []

# ---------------- About ----------------
PAGES.append(page(
    "about", "About", "About shrinkiatry",
    "The publication about the profession of psychiatry, and where it sits in The Shrink Network.",
    """
<p>shrinkiatry is a publication about the profession of psychiatry. Not the conditions, not the medications, not the clinical care itself, but the profession that delivers all of it: how psychiatrists are trained, how practices are built and paid, how technology is changing the work, how the economics shape access, and what the public rarely sees behind the clinical encounter.</p>
<p>It exists because that layer is real and underexplained. People can find good information about anxiety, depression, or a specific medication. It's much harder to find a clear, honest, non-promotional account of how the profession actually works, written to a standard a psychiatrist would stand behind. That's the gap shrinkiatry fills.</p>
<h2>Where it fits in The Shrink Network</h2>
<p>shrinkiatry is the profession layer of <a href="https://shrinknetwork.com" target="_blank" rel="noopener noreferrer">The Shrink Network</a>, a coordinated group of independent mental health properties. Each one does a different job. <a href="https://shrinkopedia.com" target="_blank" rel="noopener noreferrer">Shrinkopedia</a> explains concepts. <a href="https://psychiatryrx.org" target="_blank" rel="noopener noreferrer">PsychiatryRx</a> explains medications. <a href="https://anxietyresource.org" target="_blank" rel="noopener noreferrer">AnxietyResource</a> and <a href="https://depressionresource.org" target="_blank" rel="noopener noreferrer">DepressionResource</a> explain specific conditions. <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> provides clinical care. shrinkiatry explains the profession behind all of it, and links out to the others rather than duplicating them.</p>
<h2>What shrinkiatry is not</h2>
<p>It isn't a clinic, and it doesn't provide medical advice or care. It isn't a patient-education site about conditions or drugs; the network has those. It isn't a marketing site for any practice. And it isn't anti-psychiatry or boosterism either. The tone is inside-baseball but accessible: clear, direct, professional, and evidence-based, with opinion clearly labeled as opinion.</p>
<h2>Who's behind it</h2>
<p>shrinkiatry is written or reviewed by <a href="/editorial-team/">Shariq Refai, MD, MBA</a>, a board-certified psychiatrist and the founder of shrinkMD, and published by shrinkMD Publishing, LLC. Where there's a financial interest, such as shrinkMD, it's <a href="/disclosures/">disclosed plainly</a>.</p>
""",
    "About shrinkiatry: the publication about the profession of psychiatry and the profession layer of The Shrink Network.",
    ["shrinkmd", "shariqrefai", "shrinknetwork"],
))

# ---------------- Editorial team ----------------
PAGES.append(page(
    "editorial-team", "About", "Editorial team",
    "Who writes and reviews shrinkiatry, and the standard they're held to.",
    """
<h2>Shariq Refai, MD, MBA</h2>
<p><strong>Board-certified psychiatrist. Founder of shrinkMD. Editor of shrinkiatry.</strong></p>
<p>Shariq Refai is a board-certified psychiatrist based in Jacksonville, Florida, and the founder of shrinkMD, an independent multistate telepsychiatry practice. He holds an MBA from Duke University, trained at St. George's University School of Medicine, and completed residency at the University of Hawaii and John Peter Smith Hospital. Before medical school, he worked nights as a psychiatric technician while studying at the University of North Florida, an experience he credits with teaching him early that mental illness doesn't sort people by income, status, or background.</p>
<p>Across The Shrink Network, he serves as the medical editor and reviewer, setting the clinical line for what claims are made and how. On shrinkiatry, his role is both author and reviewer: the content reflects how the profession actually works, written to a standard he'll put his name to. He's also the author of three forthcoming books that translate psychiatry into plain language, published by shrinkMD Publishing.</p>
<p>His financial interest in shrinkMD, his books, and the Unstuck app is <a href="/disclosures/">disclosed plainly</a>. You can read more about his background and writing at <a href="https://shariqrefai.com" target="_blank" rel="noopener noreferrer">shariqrefai.com</a>.</p>
<h2>How review works</h2>
<p>Every article on shrinkiatry is written or reviewed by Dr. Refai before it's published, and carries a last-reviewed date. Articles are sourced from primary materials, including accreditation and certification bodies, federal data, professional associations, and peer-reviewed research. We say plainly when evidence is mixed or limited. The full process is described in <a href="/how-we-build-content/">how we build content</a> and <a href="/editorial-standards/">editorial standards</a>.</p>
""",
    "The shrinkiatry editorial team: Shariq Refai, MD, MBA, a board-certified psychiatrist, and the review standard behind the publication.",
    ["shariqrefai", "shrinkmd", "shrinknetwork"],
    schema=[S._jsonld_person()],
))

# ---------------- Editorial standards ----------------
PAGES.append(page(
    "editorial-standards", "Standards", "Editorial standards",
    "The rules shrinkiatry holds itself to, so you know what you're reading and why you can trust it.",
    """
<p>shrinkiatry is built to be trusted on a subject where trust is easy to lose: the inner workings of a profession. These are the standards every page is held to.</p>
<h2>Accuracy first</h2>
<p>Content is written to be accurate first and engaging second. Factual claims are tied to real, citable sources, and those sources are listed on the page. When the evidence is mixed, thin, or limited to a specific context, we say so rather than rounding up to a clean answer.</p>
<h2>Reviewed by a psychiatrist</h2>
<p>Every article is written or reviewed by <a href="/editorial-team/">Shariq Refai, MD, MBA</a>, a board-certified psychiatrist, before publication, and carries a last-reviewed date. Pages are revisited when the facts change, for example when regulations, guidelines, or workforce data update.</p>
<h2>Independent and ad-free</h2>
<p>shrinkiatry runs no advertising, sells nothing, and takes no affiliate or referral commissions. What an article says is decided by the evidence, not by a commercial interest. Where the editor has a financial interest, such as shrinkMD, it's <a href="/disclosures/">disclosed plainly</a> on the pages where it's relevant.</p>
<h2>Commentary is labeled</h2>
<p>We distinguish reported, sourced explanation from opinion. Opinion and editorial content are clearly marked as such, because the line between describing the profession and arguing about it should always be visible.</p>
<h2>Not medical advice</h2>
<p>shrinkiatry explains the profession. It doesn't diagnose, treat, or give individualized medical advice, and reading it doesn't create a doctor-patient relationship. If you need care, <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network's clinical practice. See the full <a href="/medical-disclaimer/">medical disclaimer</a>.</p>
<h2>Voice</h2>
<p>The writing is plain, direct, and human. We use contractions, keep sentences clear, avoid hype and scare quotes, and write so that a psychiatrist, a resident, a journalist, and a curious patient can all read the same page and come away with an accurate picture.</p>
<h2>Telling us we got it wrong</h2>
<p>If something is inaccurate, we want to fix it. See our <a href="/corrections/">corrections policy</a> or email <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a>.</p>
""",
    "shrinkiatry editorial standards: accuracy first, psychiatrist review, independence, labeled opinion, and clear sourcing.",
    ["shrinknetwork", "shrinkmd"],
))

# ---------------- How we build content ----------------
PAGES.append(page(
    "how-we-build-content", "Standards", "How we build content",
    "The process behind a shrinkiatry article, from question to published page.",
    """
<p>Every shrinkiatry article follows the same path, so the quality is consistent and the reasoning is visible.</p>
<h2>1. Start from a real question</h2>
<p>We write to answer questions people actually have about the profession, like how residency works, why so many psychiatrists don't take insurance, or what telepsychiatry really changed. The goal is a page that fully answers the question, not a thin post built around a keyword.</p>
<h2>2. Research from primary sources</h2>
<p>We work from primary materials: accreditation bodies like the ACGME, certification boards like the ABPN, federal agencies like HRSA and the DEA, professional associations like the American Psychiatric Association, and peer-reviewed research. We avoid building claims on top of other websites.</p>
<h2>3. Draft in plain language</h2>
<p>Drafts are written to be clear and direct, with contractions and short sentences, no hype, and no jargon left undefined. Where a concept lives elsewhere in the network, we link to it rather than re-explaining it.</p>
<h2>4. Review by a psychiatrist</h2>
<p>Every article is reviewed by <a href="/editorial-team/">Shariq Refai, MD, MBA</a> for clinical and professional accuracy before it's published. He sets the line on what's claimed, what nuance stays in, and what gets cut as oversimplified.</p>
<h2>5. Source, date, and structure</h2>
<p>Each article ships with its sources listed, a last-reviewed date, key takeaways, an on-this-page outline, related links into the network, and structured data so search engines and AI systems can recognize it as reviewed, sourced content. How we weigh evidence is described in <a href="/evidence-methodology/">evidence methodology</a>.</p>
<h2>6. Keep it current</h2>
<p>Pages are revisited when the facts change. Regulations, guidelines, and workforce data move, and the page should move with them. Corrections are handled openly under our <a href="/corrections/">corrections policy</a>.</p>
""",
    "How shrinkiatry builds content: real questions, primary sources, plain-language drafting, psychiatrist review, sourcing, and ongoing updates.",
    ["shrinknetwork", "anxietyresearch"],
))

# ---------------- Evidence methodology ----------------
PAGES.append(page(
    "evidence-methodology", "Standards", "How we evaluate evidence",
    "How shrinkiatry weighs sources and states the limits of what's known.",
    """
<p>shrinkiatry covers a profession, so a lot of what we report is institutional fact: how long residency is, what a board requires, what a regulation says. For those, we go to the body that sets the rule. But we also report on research and trends, and there the discipline of weighing evidence matters.</p>
<h2>We prefer primary and authoritative sources</h2>
<p>For rules and structures, we cite the source of the rule, such as the ACGME, the ABPN, the DEA, or HRSA. For clinical and scientific claims, we prefer peer-reviewed research, systematic reviews, and guidelines from recognized bodies over secondary coverage.</p>
<h2>We separate what's shown from what's claimed</h2>
<p>A single study is not a settled fact. When we describe research, we try to convey the strength and the limits of the evidence, including how large or replicated a finding is, what population it applies to, and what it doesn't prove. Early or single-setting results are labeled as such.</p>
<h2>We state uncertainty plainly</h2>
<p>When evidence is mixed, thin, or evolving, we say so. That's especially true for fast-moving areas like artificial intelligence and telemedicine regulation, where today's accurate statement may need updating tomorrow.</p>
<h2>We attribute numbers</h2>
<p>Statistics are tied to their source and dated where it matters. If a figure is an estimate or a projection, we describe it that way rather than presenting it as a fixed count.</p>
<h2>We update</h2>
<p>When better evidence or newer data appears, the page changes, and significant changes are noted under our <a href="/corrections/">corrections policy</a>.</p>
""",
    "How shrinkiatry evaluates evidence: primary and authoritative sources, separating what's shown from what's claimed, and stating uncertainty plainly.",
    ["anxietyresearch", "shrinknetwork"],
))

# ---------------- Contact ----------------
PAGES.append(page(
    "contact", "Contact", "Contact",
    "Questions, corrections, interview suggestions, or feedback. Here's how to reach us.",
    """
<p>The fastest way to reach shrinkiatry is by email at <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a>. We read everything, including corrections, interview suggestions, and feedback on the writing.</p>
<p>For a correction, please point to the page and what you believe is inaccurate, and we'll follow our <a href="/corrections/">corrections policy</a>. For clinical care, shrinkiatry can't help directly; <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network's psychiatric practice. If you're in crisis, call or text <strong>988</strong> in the US.</p>
<form class="tool__panel mt-3" action="https://formspree.io/f/your-form-id" method="POST" aria-label="Contact form">
<div class="field"><label for="c-name">Your name</label><input id="c-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="c-topic">Topic</label>
<select id="c-topic" name="topic">
<option>General feedback</option><option>Correction</option><option>Interview suggestion</option><option>Press or media</option><option>Something else</option>
</select></div>
<div class="field"><label for="c-msg">Message</label><textarea id="c-msg" name="message" rows="6" required></textarea></div>
<div class="field"><button class="btn btn--primary" type="submit">Send message</button></div>
<p class="small muted">This form is set up to be connected to a form handler (such as Formspree, Cloudflare, or another service). Until it's connected, please email <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a> directly.</p>
</form>
""",
    "Contact shrinkiatry: email support@shrinkiatry.com for questions, corrections, interview suggestions, or feedback.",
    ["shrinkmd", "shrinknetwork"],
))

# ---------------- Medical disclaimer ----------------
PAGES.append(page(
    "medical-disclaimer", "Legal", "Medical disclaimer",
    "What shrinkiatry is, what it isn't, and why none of it is medical advice.",
    """
<p><strong>shrinkiatry provides education and professional commentary about the profession of psychiatry. It does not provide medical advice.</strong></p>
<p>The content on this site is for general educational and informational purposes only. It explains how psychiatry is trained, organized, paid, regulated, and practiced. It is not a substitute for professional medical advice, diagnosis, or treatment, and it does not address any individual's specific situation.</p>
<p>Reading shrinkiatry does not create a doctor-patient relationship between you and Shariq Refai, MD, MBA, shrinkMD, or anyone associated with the site. No content here should be used to diagnose or treat a health problem or disease, or to start, stop, or change any treatment.</p>
<p>Always seek the advice of a licensed clinician who knows your situation with any questions about a medical or mental health condition. If you're looking for psychiatric care, <a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network's clinical practice.</p>
<h2>If you're in crisis</h2>
<p>If you may be in danger or are thinking about suicide, call or text <strong>988</strong> in the US to reach the Suicide and Crisis Lifeline, available 24 hours a day. Call <strong>911</strong> if someone is in immediate danger. You can also text HOME to 741741 to reach the Crisis Text Line.</p>
<h2>Accuracy and currency</h2>
<p>We work to keep content accurate and current, but medicine, regulation, and data change. shrinkiatry makes no warranty that all information is complete or up to date at the moment you read it, and is not liable for decisions made based on the content. When you act on anything you read here, confirm it against a primary source or a qualified professional.</p>
""",
    "shrinkiatry medical disclaimer: educational and professional commentary only, not medical advice, and not a substitute for a licensed clinician.",
    ["shrinkmd", "shrinknetwork"],
))

# ---------------- Privacy ----------------
PAGES.append(page(
    "privacy", "Legal", "Privacy policy",
    "What we collect, what we don't, and how your data is handled. The short version: very little.",
    """
<p>shrinkiatry is an educational publication, not a clinic or a store. We collect as little as possible.</p>
<h2>What we collect</h2>
<p>If you email us or use the contact form, we receive what you send: your name, email address, and message. We use that only to respond to you. We may use a privacy-respecting, aggregate analytics measure to understand which pages are read, without building profiles of individuals or selling data.</p>
<h2>What we don't do</h2>
<p>We don't sell or rent your personal information. We don't run advertising or ad-tracking networks. We don't require you to create an account to read anything. We don't collect health information about you, and you should not send us any.</p>
<h2>Cookies</h2>
<p>The site works without tracking cookies. Your theme preference (light or dark) is stored locally in your own browser and never leaves your device. Any analytics we use is designed to avoid cross-site tracking.</p>
<h2>Third parties</h2>
<p>Fonts may be served from a content delivery network, and a contact form, if connected, is processed by a form provider that receives what you submit. Links to other sites in The Shrink Network and elsewhere are governed by those sites' own privacy policies.</p>
<h2>Your choices and contact</h2>
<p>You can email <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a> to ask what we hold from any message you sent us, or to ask us to delete it. Because we collect so little, there's usually very little to manage.</p>
<p class="small muted">This policy is provided for transparency and general information. It isn't legal advice. The publisher may update it; material changes will be reflected here.</p>
""",
    "shrinkiatry privacy policy: minimal data collection, no ads, no data sales, no tracking cookies, and a local-only theme preference.",
    ["shrinknetwork"],
))

# ---------------- Terms of use ----------------
PAGES.append(page(
    "terms-of-use", "Legal", "Terms of use",
    "The basic terms for using shrinkiatry.",
    """
<p>By using shrinkiatry, you agree to these terms. If you don't agree, please don't use the site.</p>
<h2>Educational use only</h2>
<p>The content is for general education and professional commentary. It isn't medical, legal, or financial advice, and it doesn't create any professional relationship. See the <a href="/medical-disclaimer/">medical disclaimer</a>.</p>
<h2>No warranties</h2>
<p>The site is provided as is. We work to keep it accurate and current but make no warranty that it's complete, error-free, or up to date. To the fullest extent allowed by law, the publisher isn't liable for any loss arising from your use of the site or reliance on its content.</p>
<h2>Intellectual property</h2>
<p>The content, design, and branding of shrinkiatry are owned by shrinkMD Publishing, LLC, or used with permission. You may read, share, and link to pages freely. You may not republish substantial content as your own or use it to train commercial models without permission. See <a href="/copyright/">copyright</a>.</p>
<h2>External links</h2>
<p>shrinkiatry links to other sites in The Shrink Network and to outside sources. We aren't responsible for the content of external sites, which have their own terms and policies.</p>
<h2>Changes</h2>
<p>We may update these terms. Continued use after a change means you accept the updated terms. Questions go to <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a>.</p>
<p class="small muted">These terms are provided for general information and aren't legal advice.</p>
""",
    "shrinkiatry terms of use: educational use only, no warranties, intellectual property, external links, and updates.",
    ["shrinknetwork"],
))

# ---------------- Accessibility ----------------
PAGES.append(page(
    "accessibility", "Legal", "Accessibility",
    "Our commitment to making shrinkiatry usable by everyone, and how to tell us when it falls short.",
    """
<p>shrinkiatry is built to be usable by as many people as possible, including people who use screen readers, keyboard navigation, magnification, or other assistive technology.</p>
<h2>The standard we aim for</h2>
<p>We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at Level AA, the standard commonly used to satisfy accessibility expectations under laws such as the Americans with Disabilities Act. Accessibility is an ongoing effort, not a one-time check, and we treat it as part of building each page.</p>
<h2>What we do</h2>
<p>We use semantic HTML and clear heading structure, provide a skip-to-content link, label interactive controls, maintain visible keyboard focus, respect reduced-motion preferences, offer a light and dark theme, write descriptive alternative text for meaningful images, and check color contrast against the WCAG AA thresholds. The site works without JavaScript for reading content, and navigation is operable by keyboard.</p>
<h2>Known limits</h2>
<p>Some interactive tools and any embedded third-party content may not yet meet every criterion. Where we know of a gap, we work to fix it.</p>
<h2>Tell us</h2>
<p>If you hit a barrier on shrinkiatry, please tell us at <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a>, with the page and what happened, and we'll work to fix it and, where we can, help you get the information you needed in another way.</p>
""",
    "shrinkiatry accessibility statement: we aim for WCAG 2.2 Level AA, support assistive technology, and welcome reports of barriers.",
    ["shrinknetwork"],
))

# ---------------- AI use ----------------
PAGES.append(page(
    "ai-use", "Legal", "AI use",
    "How shrinkiatry does and doesn't use artificial intelligence in making this site.",
    """
<p>We write about AI, so we should be clear about how we use it ourselves.</p>
<h2>Human judgment, psychiatrist review</h2>
<p>shrinkiatry's content is directed by people and reviewed by a board-certified psychiatrist. AI tools may assist with parts of the process, such as drafting, research organization, or editing, but the substance, the claims, and the final word are set by human editorial judgment and by <a href="/editorial-team/">Dr. Refai's</a> review. Nothing is published just because a model produced it.</p>
<h2>Sourcing is verified by people</h2>
<p>Facts and citations are checked against primary sources by a person, not accepted on a model's say-so. We don't publish AI-generated statistics or references without verifying them.</p>
<h2>No AI medical advice</h2>
<p>shrinkiatry doesn't use AI to give medical advice, and you shouldn't either. As we explain in <a href="/technology/ai-in-psychiatry/">AI in psychiatry</a>, a general-purpose chatbot isn't a clinician and shouldn't be relied on for care, especially in a crisis.</p>
<h2>How AI systems may use this site</h2>
<p>We welcome AI search and assistant systems reading and citing shrinkiatry, and we publish structured data to make our content legible to them. We ask that they cite the source. Republishing substantial content or using it to train commercial models without permission isn't permitted; see <a href="/copyright/">copyright</a>.</p>
""",
    "How shrinkiatry uses AI: human-directed, psychiatrist-reviewed, with all facts and sources verified by people, and no AI medical advice.",
    ["shrinknetwork", "anxietyresearch"],
))

# ---------------- Disclosures ----------------
PAGES.append(page(
    "disclosures", "Legal", "Disclosures",
    "The financial interests behind shrinkiatry, stated plainly.",
    """
<p>Trust depends on knowing who benefits. Here are the relevant interests, disclosed plainly.</p>
<h2>The editor's interests</h2>
<p>shrinkiatry is written or reviewed by Shariq Refai, MD, MBA, who has financial interests in several things this site may mention:</p>
<ul>
<li><strong>shrinkMD</strong>, an independent multistate telepsychiatry practice he founded. When shrinkiatry refers to shrinkMD as the network's clinical practice, understand that the editor has a financial interest in it.</li>
<li><strong>Books</strong> published by shrinkMD Publishing, LLC, the imprint behind this site.</li>
<li><strong>The Unstuck app</strong> and the shrinQ program, wellness tools he created.</li>
</ul>
<h2>How we handle it</h2>
<p>shrinkiatry runs no advertising, sells nothing on the site, and takes no affiliate or referral commissions from anything it links to. Where a financial interest is relevant on a page, we note it. References to shrinkMD are made because it's the network's clinical practice, not as paid placement.</p>
<h2>The network</h2>
<p>shrinkiatry is part of <a href="https://shrinknetwork.com" target="_blank" rel="noopener noreferrer">The Shrink Network</a>, a group of independent properties created or reviewed by Dr. Refai. The network links its sites to one another openly. You can read the network's own <a href="https://shrinknetwork.com/disclosures/" target="_blank" rel="noopener noreferrer">disclosures</a> as well.</p>
""",
    "shrinkiatry disclosures: the editor's financial interests in shrinkMD, books, and apps, stated plainly. No ads, no affiliate commissions.",
    ["shrinkmd", "shariqrefai", "shrinknetwork"],
))

# ---------------- Corrections ----------------
PAGES.append(page(
    "corrections", "Legal", "Corrections",
    "How we handle mistakes, because a site about accuracy has to get this right.",
    """
<p>We try hard to be accurate, and we still get things wrong sometimes. When we do, we want to know and we want to fix it openly.</p>
<h2>How to report something</h2>
<p>Email <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a> with the page, the specific claim you think is inaccurate, and, if you have it, a source. We read every correction request.</p>
<h2>How we respond</h2>
<p>We review the claim against primary sources. If it's wrong, we fix it. For a significant factual correction, we update the page and note that a correction was made, so the record is honest rather than quietly edited. For small fixes like typos or broken links, we simply correct them.</p>
<h2>Updates versus corrections</h2>
<p>Some changes are corrections, meaning something was inaccurate. Others are updates, meaning the facts themselves changed, such as a new regulation or new data. We treat both seriously and revisit pages when the world moves, consistent with our <a href="/editorial-standards/">editorial standards</a>.</p>
""",
    "shrinkiatry corrections policy: how to report a mistake, how we verify and fix it openly, and how corrections differ from updates.",
    ["shrinknetwork"],
))

# ---------------- Copyright ----------------
PAGES.append(page(
    "copyright", "Legal", "Copyright",
    "Who owns what on shrinkiatry, and what you can do with it.",
    """
<p>The content, design, and branding of shrinkiatry are copyright shrinkMD Publishing, LLC, unless otherwise noted, and the shrinkiatry name and marks belong to the publisher.</p>
<h2>What you can do</h2>
<p>You're welcome to read, link to, and share shrinkiatry pages, and to quote short passages with attribution and a link back. We want the work to be useful and cited.</p>
<h2>What needs permission</h2>
<p>Republishing whole articles or substantial portions, presenting our content as your own, or using shrinkiatry content to train commercial AI models, requires written permission. Educational and journalistic use within normal fair-use limits is fine.</p>
<h2>Requests and complaints</h2>
<p>For permission requests, or to report content you believe infringes a copyright, email <a href="mailto:support@shrinkiatry.com">support@shrinkiatry.com</a> with the details and we'll respond.</p>
<p class="small muted">&copy; 2026 shrinkMD Publishing, LLC. All rights reserved.</p>
""",
    "shrinkiatry copyright: content and branding owned by shrinkMD Publishing, LLC. Read, link, and quote with attribution; republishing needs permission.",
    ["shrinknetwork"],
))
