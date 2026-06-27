# -*- coding: utf-8 -*-
"""engine_v3: engine_v2 + Shrink Network links + author identifiers (ORCID/NPI/Wikidata)."""
from engine_v2 import *          # noqa: F401,F403  (card, render_head, SITE, why_trust_box, etc.)
import engine_v2 as _b

SHRINKNET = "https://shrinknetwork.com"
_NEWTAB = ' target="_blank" rel="noopener noreferrer"'

def _jsonld_person():
    p = _b._jsonld_person()
    p["sameAs"] = [
        "https://shariqrefai.com/",
        "https://orcid.org/0009-0009-1090-4373",
        "https://www.wikidata.org/wiki/Q139822307",
        "https://npiregistry.cms.hhs.gov/provider-view/1467680660",
    ]
    p["identifier"] = [
        {"@type": "PropertyValue", "propertyID": "ORCID", "value": "0009-0009-1090-4373",
         "url": "https://orcid.org/0009-0009-1090-4373"},
        {"@type": "PropertyValue", "propertyID": "NPI", "value": "1467680660",
         "url": "https://npiregistry.cms.hhs.gov/provider-view/1467680660"},
        {"@type": "PropertyValue", "propertyID": "Wikidata", "value": "Q139822307",
         "url": "https://www.wikidata.org/wiki/Q139822307"},
    ]
    return p

def render_header(active=None):
    html = _b.render_header(active)
    return html.replace(
        '<span class="brand__sub">Part of The Shrink Network</span>',
        f'<a class="brand__sub" href="{SHRINKNET}"{_NEWTAB}>Part of The Shrink Network</a>')

def render_footer():
    html = _b.render_footer()
    return html.replace(
        '<span class="brandline">Part of The Shrink Network</span>',
        f'<a class="brandline" href="{SHRINKNET}"{_NEWTAB}>Part of The Shrink Network</a>')

def render_document(page):
    return render_head(page) + render_header(page.get("active")) + page["body"] + render_footer()
