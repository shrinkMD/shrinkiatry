# -*- coding: utf-8 -*-
"""Post-build patches (v2). Run AFTER any build from the repo root:
   python3 src/postbuild2.py
Supersedes postbuild.py. Adds shortened descriptions for the Decoder and
State of Psychiatry sections. Idempotent. Kept as a fresh filename because the
shell mount serves stale reads of edited files.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_VER = "10"

NEWTAB = ' target="_blank" rel="noopener noreferrer"'
BRAND_OLD = ('<a class="brand" href="/">shrinkiatry<span class="dot">.</span>'
             '<a class="brand__sub" href="https://shrinknetwork.com"' + NEWTAB + '>Part of The Shrink Network</a></a>')
BRAND_NEW = ('<span class="brandwrap"><a class="brand" href="/">shrinkiatry<span class="dot">.</span></a>'
             '<a class="brand__sub" href="https://shrinknetwork.com"' + NEWTAB + '>Part of The Shrink Network</a></span>')

IDENTS = ('<p class="idents">Professional identifiers: '
          '<a href="https://orcid.org/0009-0009-1090-4373"' + NEWTAB + '>ORCID 0009-0009-1090-4373</a> &middot; '
          '<a href="https://npiregistry.cms.hhs.gov/provider-view/1467680660"' + NEWTAB + '>NPI 1467680660</a> &middot; '
          '<a href="https://www.wikidata.org/wiki/Q139822307"' + NEWTAB + '>Wikidata Q139822307</a>.</p>')

TITLES = {
 "careers": "Careers in Psychiatry | shrinkiatry", "business": "The Business of Psychiatry | shrinkiatry",
 "technology": "Technology in Psychiatry | shrinkiatry", "economics": "The Economics of Psychiatry | shrinkiatry",
 "culture": "The Culture of Psychiatry | shrinkiatry", "ethics": "Ethics in Psychiatry | shrinkiatry",
 "innovation": "Innovation in Psychiatry | shrinkiatry", "leadership": "Leadership in Psychiatry | shrinkiatry",
 "research-digest": "Psychiatry Research Digest | shrinkiatry", "reports": "Psychiatry Reports | shrinkiatry",
 "interviews": "Psychiatry Interviews | shrinkiatry", "opinion": "Psychiatry Opinion | shrinkiatry",
 "careers/psychiatrist-vs-psychologist-vs-therapist": "Psychiatrist vs Psychologist vs Therapist | shrinkiatry",
 "careers/what-board-certification-means": "What Board Certification Means | shrinkiatry",
 "careers/how-psychiatry-residency-works": "How Psychiatry Residency Works | shrinkiatry",
 "business/how-private-psychiatry-practices-work": "How Private Psychiatry Practices Work | shrinkiatry",
 "business/why-controlled-substances-are-different": "Why Controlled Substances Are Different | shrinkiatry",
 "business/why-documentation-shapes-care": "Why Documentation Shapes Care | shrinkiatry",
 "technology/what-telepsychiatry-changes": "What Telepsychiatry Changes | shrinkiatry",
}
DESCS = {
 "careers": "How psychiatrists are trained and certified: residency, board certification, fellowships, and the many shapes a psychiatry career can take.",
 "business": "How psychiatric practices are built, paid, and run: cash-pay vs insurance, practice models, documentation, and controlled-substance rules.",
 "technology": "Telepsychiatry, electronic records, ambient documentation, and AI in psychiatry, judged on what they change and what the evidence shows.",
 "economics": "The workforce shortage, reimbursement, supply and demand, and the economics that shape access to psychiatric care, explained with sources.",
 "culture": "History, ethics, professional identity, and public perception of psychiatry: the reflective, behind-the-scenes layer of the profession.",
 "ethics": "Confidentiality, capacity, consent, boundaries, and conflicts of interest: the ethical framework behind responsible psychiatric practice.",
 "innovation": "Measurement-based care, digital therapeutics, precision approaches, and AI in psychiatry, with an honest read on the evidence.",
 "leadership": "How psychiatrists lead practices, departments, and care teams: clinical leadership, supervision, and systems thinking in psychiatry.",
 "research-digest": "Practice-relevant psychiatry research, guidelines, and policy changes, summarized honestly with the limits of the evidence stated plainly.",
 "reports": "Data-driven briefs on the state of psychiatry from public sources: workforce, telepsychiatry, burnout, technology adoption, and compensation.",
 "interviews": "Conversations with psychiatrists, researchers, founders, and leaders about how the profession works and where it's heading.",
 "opinion": "Clearly labeled editorials and arguments about psychiatry: ethics, policy, technology, and the direction of the profession.",
 "business/cash-pay-vs-insurance": "Why so many psychiatrists go out of network, what cash-pay buys, and what it does to access and income, explained with sources.",
 "business/why-controlled-substances-are-different": "Why controlled substances are handled differently in psychiatry: DEA scheduling, prescribing rules, and how they reshape practice. Educational only.",
 "careers/psychiatrist-vs-psychologist-vs-therapist": "Psychiatrist vs psychologist vs therapist: the real differences in training, scope, and prescribing, explained by a board-certified psychiatrist.",
 "careers/what-board-certification-means": "What board certification in psychiatry means: how ABPN certification works, what it guarantees, what it doesn't, and how it is kept current.",
 "economics/the-psychiatrist-shortage": "The psychiatrist shortage explained: how big it is, why it persists, where it concentrates, and what actually expands access to care.",
 "psychiatry-operating-room": "The behind-the-scenes map of psychiatric practice: training, judgment, documentation, telepsychiatry, ethics, medication rules, AI, and access.",
 "technology/what-telepsychiatry-changes": "What telepsychiatry changes and what it doesn't: access and overhead shifted, while the exam, the rules, and clinical judgment mostly stayed.",
 "tools": "Educational tools for understanding the profession of psychiatry, starting with a private-practice revenue estimator. More in development.",
 "tools/private-practice-revenue-estimator": "A free, educational calculator estimating net and gross annual revenue for an independent psychiatry practice from volume, pricing, and overhead.",
 "decoder/why-appointments-feel-short": "Why psychiatric appointments feel short: medication-management visits, billing codes, documentation, and the workforce shortage all compress the time.",
 "decoder/why-your-psychiatrist-takes-notes": "Why your psychiatrist takes notes: the note is a legal record, a billing document, and the thread that carries your plan between visits.",
 "decoder/why-medication-changes-are-gradual": "Why psychiatric medication changes are gradual: many drugs take weeks to work, side effects peak early, and slow changes keep the signal clean.",
 "decoder/why-psychiatrists-ask-certain-questions": "Why psychiatrists ask about sleep, appetite, and family history: the questions map directly to how a diagnosis is built and to safety.",
 "decoder/why-a-diagnosis-can-change": "Why a psychiatric diagnosis can change: the first one is a working hypothesis, and updating it as the picture clarifies is careful medicine.",
 "decoder/why-getting-an-appointment-is-hard": "Why getting a psychiatry appointment is hard: a real workforce shortage, thin insurance networks, and uneven geography, all at once.",
 "decoder/why-some-psychiatrists-dont-take-insurance": "Why some psychiatrists don't take insurance: low reimbursement, heavy administration, and hard-to-join networks push many to cash-pay.",
 "decoder/why-controlled-substances-have-extra-rules": "Why controlled substances carry extra rules: stimulants and benzodiazepines are federally scheduled, which drives refills, visits, and telehealth limits.",
 "state-of-psychiatry/psychiatrist-shortage": "The state of the psychiatrist shortage: how deep the workforce gap runs, where it concentrates, and what the projections actually show.",
 "state-of-psychiatry/telepsychiatry": "The state of telepsychiatry: psychiatry kept virtual care more than any specialty, reshaping access and overhead. The numbers and the limits.",
 "state-of-psychiatry/burnout": "The state of burnout in psychiatry: what national surveys show, where the specialty ranks, and why the drivers are mostly systemic.",
 "state-of-psychiatry/ai": "The state of AI in psychiatry: ambient note tools are real, decision support and chatbots are unproven, and no AI is cleared to diagnose.",
}

def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")

def main():
    os.chdir(ROOT)
    files = glob.glob("**/*.html", recursive=True)
    for p in files:
        s = open(p, encoding="utf-8").read()
        slug = os.path.dirname(p)
        s = s.replace(BRAND_OLD, BRAND_NEW)
        s = re.sub(r"main\.(css|js)\?v=[0-9]+", r"main.\1?v=" + ASSET_VER, s)
        if slug in TITLES:
            t = esc(TITLES[slug])
            s = re.sub(r"<title>[^<]*</title>", "<title>" + t + "</title>", s, count=1)
            s = re.sub(r'(<meta property="og:title" content=")[^"]*(">)', r"\g<1>" + t + r"\g<2>", s, count=1)
            s = re.sub(r'(<meta name="twitter:title" content=")[^"]*(">)', r"\g<1>" + t + r"\g<2>", s, count=1)
        if slug in DESCS:
            dd = esc(DESCS[slug])
            for pat in (r'(<meta name="description" content=")[^"]*(">)',
                        r'(<meta property="og:description" content=")[^"]*(">)',
                        r'(<meta name="twitter:description" content=")[^"]*(">)'):
                s = re.sub(pat, r"\g<1>" + dd + r"\g<2>", s, count=1)
        open(p, "w", encoding="utf-8").write(s)
    home = "index.html"
    if os.path.exists(home):
        s = open(home, encoding="utf-8").read()
        s = s.replace('<span class="eyebrow">Part of The Shrink Network</span>',
                      '<span class="eyebrow"><a href="https://shrinknetwork.com"' + NEWTAB + '>Part of The Shrink Network</a></span>')
        open(home, "w", encoding="utf-8").write(s)
    et = os.path.join("editorial-team", "index.html")
    if os.path.exists(et):
        s = open(et, encoding="utf-8").read()
        mark = "shariqrefai.com</a>.</p>"
        if mark in s and "idents" not in s:
            s = s.replace(mark, mark + IDENTS, 1)
            open(et, "w", encoding="utf-8").write(s)
    print("post-build v2 applied to", len(files), "pages; asset version v" + ASSET_VER)

if __name__ == "__main__":
    main()
