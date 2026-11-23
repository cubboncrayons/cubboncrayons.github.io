#!/usr/bin/env python3
"""Zero-dependency structural checks for Cubbon Crayons commerce pages.

No payment actions, analytics collection or external requests.
Run: python3 scripts/site_quality.py
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "activities.html", "parent-corner.html",
         "parent-corner-kannada.html", "business.html", "terms.html",
         "refunds.html", "privacy.html", "tithigalu.html", "purochi.html"]
ERRORS = []
WARNINGS = []

class Elements(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.assets = []
        self.images_without_alt = []
        self.sections = 0
        self.section_ends = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            if a["id"] in self.ids:
                ERRORS.append("duplicate id: " + a["id"] + " on " + str(self.page))
            self.ids.add(a["id"])
        if tag == "section":
            self.sections += 1
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("img", "script", "link", "audio", "source"):
            address = a.get("src") or (a.get("href") if tag == "link" else None)
            if address:
                self.assets.append(address)
        if tag == "img" and "alt" not in a:
            self.images_without_alt.append(a.get("src", "(unknown)"))

    def handle_endtag(self, tag):
        if tag == "section":
            self.section_ends += 1

def local_path(page, link):
    p = urlsplit(link)
    if p.scheme or p.netloc or link.startswith(("mailto:", "tel:", "data:", "javascript:")):
        return None
    path = unquote(p.path)
    if not path:
        return page
    if path.startswith("/"):
        return ROOT / path.lstrip("/") if path != "/" else ROOT / "index.html"
    target = page.parent / path
    if path.endswith("/"):
        return target / "index.html"
    return target

def inspect(page_name):
    file = ROOT / page_name
    if not file.is_file():
        ERRORS.append("missing page " + page_name)
        return
    src = file.read_text(encoding="utf-8")
    p = Elements()
    p.page = file.relative_to(ROOT)
    p.feed(src)
    if p.sections != p.section_ends:
        ERRORS.append(f"{page_name}: unbalanced section tags {p.sections}/{p.section_ends}")
    for name in p.images_without_alt:
        ERRORS.append(f"{page_name}: missing alt attribute on {name}")
    for item in p.assets:
        path = local_path(file, item)
        if path is not None and not path.is_file():
            ERRORS.append(f"{page_name}: missing required asset {item}")
    for address in p.links:
        if not address.startswith("#") or address == "#":
            continue
        anchor = unquote(urlsplit(address).fragment)
        if anchor and anchor not in p.ids:
            WARNINGS.append(f"{page_name}: unresolved same-page anchor {address}")
    return src, p

pages = {name: inspect(name) for name in PAGES}
home = pages.get("index.html")
if home:
    html, parsed = home
    ids = ("stories", "previews", "choose-by-moment", "before-you-buy",
           "story-collections", "faq")
    for id_ in ids:
        if id_ not in parsed.ids:
            ERRORS.append("homepage missing key section: " + id_)
    products = {
        "umbrella": ("I2Azi", "10 pages"),
        "idli": ("aXgsm", "9 pages"),
        "amma": ("bTf0x", "8 pages"),
        "ajja": ("HI9zh", "8 pages"),
        "park": ("MGgfX", "11 pages"),
    }
    for slug, (payhip, count) in products.items():
        match = re.search(r'<article class="card" id="story-' +
                          re.escape(slug) + r'".*?</article>', html, re.S)
        if not match:
            ERRORS.append("homepage missing product card " + slug)
            continue
        card = match.group(0)
        if count not in card:
            ERRORS.append(f"{slug}: page count must be confirmed against Payhip: {count}")
        if "payhip.com/b/" + payhip not in card:
            ERRORS.append(slug + ": incorrect Payhip product link")
        if "Buy story" not in card:
            ERRORS.append(slug + ": purchase CTA missing")
    if "There is no bundle checkout or discount currently available" not in html:
        ERRORS.append("bundle claim needs verification or explicit unavailable message")
    if "href=\"/commerce-upgrades.css" not in html:
        ERRORS.append("missing external commerce stylesheet")

# Only inspect local JS syntax; never execute site code during this audit.
js_files = ["book-viewer.js", "reading-room.js", "motion.js",
            "site-navigation.js", "activities.js", "purochi.js"]
for name in js_files:
    if (ROOT / name).exists():
        try:
            p = subprocess.run(["node", "--check", str(ROOT / name)],
                               capture_output=True, text=True)
            if p.returncode:
                ERRORS.append("JS syntax " + name + ": " + p.stderr.strip()[:220])
        except FileNotFoundError:
            WARNINGS.append("Node not installed; JavaScript syntax not checked")
            break

# Explicit launch dependencies that cannot be inferred from source code.
WARNINGS += [
    "MANUAL: verify checkout and file delivery with a real Payhip test order",
    "MANUAL: update age range and downloaded file counts on Payhip",
    "MANUAL: verify seller/contact/grievance disclosures, including applicable tax rules",
    "MANUAL: verify responsive layout and interactions in real browsers",
    "MANUAL: connect analytics only after privacy/CSP review",
]
print("Cubbon Crayons · Quality Gate")
print(f"Pages inspected: {len(PAGES)}")
print(f"Errors: {len(ERRORS)}, warnings: {len(WARNINGS)}")
for line in ERRORS:
    print("ERROR:", line)
for line in WARNINGS:
    print("WARN:", line)
sys.exit(1 if ERRORS else 0)
