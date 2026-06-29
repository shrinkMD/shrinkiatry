# -*- coding: utf-8 -*-
"""SEO/GEO enhancements injected at build time: care CTA on high-intent Decoder
pages, plus People-Also-Ask FAQ layers (with FAQPage schema) on the Decoder and
State of Psychiatry hubs."""

CARE_CTA = (
    '<div class="callout" style="border-left:4px solid var(--accent)">'
    '<strong class="callout__label">Looking for care, not commentary?</strong>'
    "shrinkiatry explains the profession, it doesn't provide treatment, and reading it doesn't create a "
    "doctor-patient relationship. If you want to talk with a psychiatrist, "
    '<a href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">shrinkMD</a> is the network\'s '
    "independent telepsychiatry practice, and it's a good place to start. If you're in crisis, call or text "
    "<strong>988</strong> in the US to reach the Suicide and Crisis Lifeline."
    '<div class="mt-2"><a class="btn btn--primary" href="https://shrinkmd.com" target="_blank" rel="noopener noreferrer">Visit shrinkMD</a></div>'
    "</div>"
)

CTA_SLUGS = {
    "decoder/why-appointments-feel-short",
    "decoder/why-getting-an-appointment-is-hard",
    "decoder/why-some-psychiatrists-dont-take-insurance",
    "decoder/why-controlled-substances-have-extra-rules",
    "decoder/why-medication-changes-are-gradual",
}

DECODER_FAQ = [
    ("What is the Psychiatry Decoder?",
     "It's a plain-English section of shrinkiatry that explains the confusing realities of psychiatric care, like why appointments feel short, why your psychiatrist takes notes, and why getting seen is hard. It explains how care works, not what condition or medication you have."),
    ("Is shrinkiatry medical advice?",
     "No. shrinkiatry is education and professional commentary about the profession of psychiatry. It doesn't diagnose or treat, and reading it doesn't create a doctor-patient relationship. For care, shrinkMD is the network's clinical practice."),
    ("Why is psychiatric care so confusing to navigate?",
     "Because a lot of what shapes your experience happens off-stage: billing codes, documentation rules, prescribing regulations, and a workforce shortage. The Decoder pulls each of those into plain view so the care makes more sense."),
    ("Who writes and reviews the Decoder?",
     "Every page is written or reviewed by Shariq Refai, MD, MBA, a board-certified psychiatrist, and sourced to primary materials like the ACGME, the DEA, HRSA, and the FDA."),
]

STATE_FAQ = [
    ("Is there a psychiatrist shortage in the United States?",
     "Yes. Roughly half of the US population lives in a federally designated mental-health workforce shortage area, and a large share of counties have no practicing psychiatrist. The gap is driven as much by distribution and pay as by raw numbers."),
    ("Is telepsychiatry as effective as in-person care?",
     "For many follow-ups and many patients, research finds remote psychiatric care clinically comparable to in-person, which is partly why psychiatry kept telehealth more than almost any other specialty. Some presentations still need an in-person exam."),
    ("How common is burnout among psychiatrists?",
     "National surveys consistently find a large share of psychiatrists reporting burnout, often roughly a third to nearly half depending on the year and the instrument. Psychiatry usually lands in the middle-to-upper range across specialties, and the drivers are mostly systemic."),
    ("Can AI diagnose or replace psychiatrists?",
     "No AI system is authorized to diagnose or treat psychiatric illness on its own, and a clinician remains responsible. AI's most established role today is drafting documentation, not making clinical decisions."),
]

def faq_section(faq, heading="Common questions"):
    items = "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in faq)
    return (
        '<section class="section section--surface section--tight"><div class="wrap"><div class="maxread flow">'
        f'<h2 id="faq">{heading}</h2>{items}'
        "</div></div></section>"
    )

def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def apply(pages):
    """Mutate the page list in place: inject CTA + hub FAQ. Returns the list."""
    for p in pages:
        slug = p.get("slug", "")
        if slug in CTA_SLUGS and "<hr>" in p["body"]:
            p["body"] = p["body"].replace("<hr>", CARE_CTA + "<hr>", 1)
        if slug == "decoder":
            p["body"] += faq_section(DECODER_FAQ)
            p.setdefault("schema", []).append(faq_schema(DECODER_FAQ))
        if slug == "state-of-psychiatry":
            p["body"] += faq_section(STATE_FAQ)
            p.setdefault("schema", []).append(faq_schema(STATE_FAQ))
    return pages
