# shrinkiatry SEO / GEO Playbook

Edward-Sturm-informed action plan. The on-page and authority work is already built into the site. This file covers the off-site and operational moves that need your hands, plus the 60-to-90-day tactics that only work once you're indexed.

Last updated: June 29, 2026.

---

## 1. Index the site (do this first, this week)

None of the operational SEO tactics work until search engines and LLMs can see the site. This is the Pareto baseline.

**Google Search Console**
1. Go to search.google.com/search-console and add a property for `shrinkiatry.com` (use the Domain property type; verify with the DNS TXT record Cloudflare lets you add under DNS > Records).
2. Submit the sitemap: in GSC, Sitemaps > enter `sitemap.xml` > Submit. Full URL is `https://shrinkiatry.com/sitemap.xml`.
3. Use URL Inspection > "Request indexing" on these key pages so they get crawled first:
   - `https://shrinkiatry.com/`
   - `https://shrinkiatry.com/psychiatry-operating-room/`
   - `https://shrinkiatry.com/decoder/`
   - `https://shrinkiatry.com/state-of-psychiatry/`

**Bing Webmaster Tools** (matters more than people think: it feeds ChatGPT's grounding)
1. Go to bing.com/webmasters, add `shrinkiatry.com`, and import from GSC (fastest) or verify by DNS.
2. Submit the same sitemap.
3. Later, check the AI performance / grounding report to see which queries are surfacing the site in Copilot and ChatGPT.

**Also:** point each network site's GSC at its sitemap too, so the whole network is crawled and the internal links below get discovered.

---

## 2. Internal-network backlink map (your biggest controllable win)

Edward pays for backlinks to specific pages with descriptive anchor text. You own the whole network, so you can do this for free. Add these contextual links from the network sites INTO shrinkiatry, using the exact anchor text shown (descriptive anchors pass topical authority, generic "click here" does not). Place them inside relevant body content, not just footers.

| From (site / page) | To (shrinkiatry page) | Anchor text to use |
|---|---|---|
| Shrinkopedia, antipsychotics / any medication concept | `/psychiatry-operating-room/#room-06` | the systems behind psychiatric prescribing |
| Shrinkopedia, any clinical concept page | `/psychiatry-operating-room/` | how psychiatric practice actually works |
| Shrinktionary, term pages (e.g. biopsychosocial) | `/decoder/` | why psychiatric care works the way it does |
| Shrinktionary, "confidentiality" or similar | `/decoder/why-psychiatrists-ask-certain-questions/` | why psychiatrists ask certain questions |
| PsychiatryRx, stimulant / benzodiazepine pages | `/decoder/why-controlled-substances-have-extra-rules/` | why controlled substances carry extra rules |
| PsychiatryRx, any medication page | `/decoder/why-medication-changes-are-gradual/` | why dose changes are gradual |
| AnxietyResource / DepressionResource, "getting help" pages | `/decoder/why-getting-an-appointment-is-hard/` | why getting a psychiatry appointment is hard |
| AnxietyResource / DepressionResource, cost pages | `/decoder/why-some-psychiatrists-dont-take-insurance/` | why some psychiatrists don't take insurance |
| AnxietyResearch, evidence / methodology pages | `/state-of-psychiatry/` | sourced data on the state of psychiatry |
| shrinkMD, about / how-it-works | `/` | the profession behind the care |
| shrinkMD, telepsychiatry page | `/state-of-psychiatry/telepsychiatry/` | the state of telepsychiatry, with sources |
| shariqrefai.com, bio / writing | `/editorial-team/` | Dr. Refai's editorial role across the network |
| shrinknetwork.com, network map | `/` | shrinkiatry, the profession layer |

Rule of thumb from Edward: build links to the specific page you want to rank, not just the homepage, and vary the surrounding sentence so the language stays natural. Aim to get the homepage ranking for "shrinkiatry" first (the network links above handle that), then funnel into the deeper pages.

---

## 3. People Also Ask expansion (your content pipeline)

You already guessed strong questions for the Decoder. To find the REAL ones Google and LLMs surface:

1. Go to alsoasked.com (free tier) and enter seed terms one at a time: "psychiatrist," "psychiatry appointment," "telepsychiatry," "ADHD medication refill," "psychiatrist vs therapist," "involuntary hold," "psychiatric diagnosis."
2. Export the question tree. Each branch is a real PAA question.
3. For each question, decide: does an existing page answer it (add an H3 question + 100-word answer to that page's FAQ), or does it deserve its own Decoder entry?
4. Paste the export to me and I'll turn the best ones into new Decoder entries or FAQ blocks (with FAQPage schema), in the site's voice and sourced.

Strong candidate new Decoder entries to consider next (all high-intent, plain-English, route to shrinkMD):
- Why does my psychiatrist want to see me so often?
- Why did my psychiatrist change my medication?
- Why can't I just get my prescription refilled?
- What's the difference between a psychiatrist and a psychiatric nurse practitioner?
- Why do I have to fill out so many forms?
- Can a psychiatrist talk to my family?
- Why was I asked about drugs and alcohol?

---

## 4. Operational tactics (start at 60 to 90 days, once you have ranking data)

These need GSC data you won't have until the site is indexed and ranking. Calendar them.

- **Mine GSC for low-hanging fruit.** In GSC, Performance > Pages > click a page > Queries tab. Find keywords where the page sits in positions 3 to 20. Weave those exact phrases into the page naturally and re-request indexing. This is the single highest-ROI ongoing task.
- **Content refreshes to move 2-to-4 up to 1.** Pick pages ranking just off the top. Tighten the above-the-fold answer, update any stale stat, confirm the target phrase is in the title, meta, slug, H1, and first sentence, then re-submit the URL and bump the published date. CTR roughly doubles going from position 3 to 1.
- **Republish stuck pages.** If a page is stuck on page 2 for months, move it to a slightly longer new URL, 301 the old one, and submit both. Google re-evaluates it with your now-stronger topical authority.
- **Rotate internal links.** When a weak page reaches stable ranking, repoint the internal link that was feeding it toward the next target page. Never leave a page with zero internal links.

---

## 5. What's already done (don't re-do)

These map to Edward's checklist and are live in the build:
- Target phrase in title, meta description, URL slug, H1, and an above-the-fold plain-English answer on every key page.
- One page per real question (the Decoder is textbook People-Also-Ask structure), now with a PAA FAQ layer on the hubs.
- FAQPage, MedicalWebPage, ItemList, Person, Organization, and BreadcrumbList schema.
- LLM grounding proof: author identifiers (ORCID, NPI, Wikidata), Person schema with sameAs, sources on every page, review panel, editorial standards, evidence methodology, llms.txt.
- Subfolders (`/decoder/`, `/state-of-psychiatry/`, `/tools/`) linked from the footer, dense descriptive internal linking, no orphan pages.
- A clear care CTA to shrinkMD on the high-intent Decoder pages (the conversion path).
- AI tells removed: contractions throughout, no em or en dashes.

## 6. What we deliberately skipped (and why)

Edward's commercial tactics don't fit an evidence-based authority publication and would weaken the moat:
- Buyer-intent "solution" keyword pages, product/landing pages, and self-promotional "best of" listicles. shrinkiatry's conversion is a soft handoff to shrinkMD, not a checkout.
- Review syndication ("is X legit / a scam") and manufactured social proof. Wrong tone for a psychiatrist-signed publication.
- Note: Edward de-prioritizes schema for normal sites; we keep it because our goal is GEO/AEO authority, where schema and structured proof genuinely help LLMs cite us.
