# -*- coding: utf-8 -*-
"""Author media features: an 'In the media' block on the editorial-team page plus
subjectOf schema for the interview. Strengthens E-E-A-T and GEO author credibility."""

NEWTAB = ' target="_blank" rel="noopener noreferrer"'

# (title, publisher, url, year)  -- verified quotes/interview except EatingWell (owner-supplied)
FEATURES = [
    ("Mental Health Does Not Discriminate: An Interview with Dr. Shariq Refai", "Top Doctor Magazine",
     "https://topdoctormagazine.com/mental-health/mental-health-does-not-discriminate-an-interview-with-dr-shariq-refai/", "2024"),
    ("10 Research-Backed, Natural Ways to Counter Depression", "The Epoch Times",
     "https://www.theepochtimes.com/health/research-backed-natural-ways-to-treat-depression-5873396", "2025"),
    ("Survivors in Isolation: Abusers Separate Victims from Everyone for Power and Control", "DomesticShelters.org",
     "https://www.domesticshelters.org/articles/identifying-abuse/survivors-in-isolation-abusers-separate-victims-from-everyone-for-power-and-control", "2025"),
    ("Why Does Stress Make You Poop?", "EatingWell",
     "https://www.eatingwell.com/why-does-stress-make-you-poop-11776377", "2025"),
]

_li = "".join(
    f'<li><a href="{u}"{NEWTAB}>{t}</a>, {pub} ({yr})</li>' for t, pub, u, yr in FEATURES
)
MEDIA_SECTION = (
    '<h2>In the media</h2>'
    "<p>Dr. Refai's clinical perspective has been featured and quoted in national health and consumer "
    "publications, where he comments on psychiatry, depression, lifestyle, and mental health. A selection:</p>"
    f"<ul>{_li}</ul>"
)

# Only the Top Doctor piece is an article ABOUT him, so only it is a valid schema subjectOf.
SUBJECT_OF = [{
    "@type": "Article",
    "headline": "Mental Health Does Not Discriminate: An Interview with Dr. Shariq Refai",
    "url": "https://topdoctormagazine.com/mental-health/mental-health-does-not-discriminate-an-interview-with-dr-shariq-refai/",
    "publisher": {"@type": "Organization", "name": "Top Doctor Magazine"},
    "datePublished": "2024-07-01",
}]

MARKER = '<a href="/editorial-standards/">editorial standards</a>.</p>'

def apply(pages):
    for p in pages:
        if p.get("slug") == "editorial-team":
            if MARKER in p["body"]:
                p["body"] = p["body"].replace(MARKER, MARKER + MEDIA_SECTION, 1)
            if p.get("schema"):
                p["schema"][0]["subjectOf"] = SUBJECT_OF
    return pages
