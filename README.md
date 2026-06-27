# shrinkiatry.com

The profession layer of The Shrink Network. shrinkiatry explains the profession of psychiatry: careers, business, technology, economics, culture, and ethics. It does not duplicate the patient-education or clinical sites in the network; it links to them.

This repository is a fully prerendered static site. The HTML in the repo root is the deployable site. No build step is required to deploy.

## What's here

```
/                      The deployable static site (HTML in clean-URL folders)
  index.html           Homepage
  careers/ business/ technology/ economics/ culture/ ...   Section hubs
  careers/how-psychiatry-residency-works/ ...              Long-form articles
  psychiatry-operating-room/                               The flagship interactive hub
  tools/ tools/private-practice-revenue-estimator/         Tools
  about/ editorial-standards/ medical-disclaimer/ ...      About + legal pages
  404.html, sitemap.xml, robots.txt, _headers, site.webmanifest
  favicon.svg, favicon.ico, opengraph.jpg
  assets/css/main.css  Design system (slate + muted blue, light + dark themes)
  assets/js/main.js    Nav, theme toggle, Operating Room filters
  assets/img/          Icons (logo, apple-touch, manifest icons)
/src                   The generator that produces the HTML (Python, no dependencies)
_source-materials/     Original brief, palettes, reference docs (git-ignored, not deployed)
```

## Editing content and rebuilding

Content lives in `src/` as plain Python modules (one per area). To regenerate the site after editing:

```bash
python3 src/build.py
```

That rewrites every page in the repo root, plus `sitemap.xml`, `robots.txt`, `404.html`, and `_headers`. Python 3 with the standard library is all you need.

- Articles: `src/content_articles.py`
- Section hubs: `src/content_hubs.py`
- Homepage: `src/content_home.py`
- The Operating Room: `src/content_or.py`
- Tools: `src/content_tools.py`
- Legal and about pages: `src/content_legal.py`
- Layout, nav, footer, schema, and shared components: `src/engine.py`

## Deploying to GitHub + Cloudflare Pages

1. **Create the repo and push.**
   ```bash
   cd "shrinkiatry website"
   git init
   git add .
   git commit -m "shrinkiatry.com initial site"
   git branch -M main
   git remote add origin https://github.com/<you>/shrinkiatry.git
   git push -u origin main
   ```
   `_source-materials/` is git-ignored, so the brief and palettes stay local.

2. **Connect Cloudflare Pages.**
   In the Cloudflare dashboard: Workers & Pages, Create, Pages, Connect to Git, pick the repo.
   - **Framework preset:** None
   - **Build command:** leave empty (the site is prebuilt)
   - **Build output directory:** `/` (the repo root)

3. **Add the custom domain.**
   In the Pages project: Custom domains, add `shrinkiatry.com` and `www.shrinkiatry.com`. Cloudflare sets the DNS automatically if the domain is on your Cloudflare account.

4. **Done.** `_headers` applies long-cache for `/assets/*` and basic security headers. Cloudflare serves `404.html` for not-found routes and clean URLs from the folder structure.

If you prefer to keep the generator out of the deployed site, you can set the Pages build output directory to a subfolder, but the simplest setup is to serve the root as-is.

## Notes and follow-ups

- **Hero image.** The homepage hero photo is generated and currently referenced from the image CDN. For full ownership and best performance, download it into `assets/img/hero.jpg` and change the `<img src>` in `src/content_home.py` to `/assets/img/hero.jpg`, then rebuild. The image has an `onerror` fallback so the hero still looks intentional if the remote image is ever unavailable.
- **Contact form.** `contact/` includes a form wired to a placeholder action. Connect it to a form handler (Cloudflare, Formspree, or similar) by setting the form `action`, or rely on the `support@shrinkiatry.com` mailto link shown on the page.
- **Open Graph image.** `opengraph.jpg` (1200x630) is referenced site-wide. Replace it any time; keep the dimensions.
- **Analytics.** None is included. If you add a privacy-respecting analytics snippet, drop it into the `<head>` template in `src/engine.py`.

## Standards built in

- SEO/AEO/GEO: unique titles, meta descriptions, canonicals, Open Graph and Twitter cards, semantic headings, clean URLs, `sitemap.xml`, and an AI-assistant-friendly `robots.txt`.
- Schema.org JSON-LD: Organization, WebSite, BreadcrumbList, Article, Person (Shariq Refai, MD, MBA), FAQPage, MedicalWebPage where relevant, ItemList for the Operating Room, and SoftwareApplication for the tool.
- Accessibility: built toward WCAG 2.2 AA. Semantic landmarks, skip link, labeled controls, visible focus, reduced-motion support, light and dark themes, and color contrast that passes AA across both themes.
- Voice: every claim is sourced, contractions throughout, no em or en dashes, no hype. Written or reviewed by Shariq Refai, MD, MBA.

&copy; 2026 shrinkMD Publishing, LLC.
