#!/usr/bin/env python3
"""
Génère sitemap.xml à la racine du repo.

Combine :
  - une liste de pages statiques (à tenir à jour manuellement ci-dessous
    quand tu crées une nouvelle page compagnon ou un nouveau livret)
  - les articles de blog, lus automatiquement depuis posts.json

Usage : python3 generate_sitemap.py (depuis la racine du repo)

N'écrase que sitemap.xml. Ne touche à rien d'autre.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).parent
POSTS_JSON = ROOT / "posts.json"
SITEMAP = ROOT / "sitemap.xml"
SITE_URL = "https://asynckernel.fr"

# Pages statiques du site. Ajoute une ligne ici à chaque nouvelle page
# compagnon ou nouveau livret créé (le script nouveau-livret.py te le
# rappellera aussi au moment de la création).
STATIC_PAGES = [
    {"path": "/", "priority": "1.0", "changefreq": "monthly"},
    {"path": "/trois-carnets/", "priority": "0.8", "changefreq": "monthly"},
    {"path": "/un-iphone-qui-nepuise-pas/", "priority": "0.8", "changefreq": "monthly"},
    {"path": "/jegardelecontrolesurmonordi/", "priority": "0.8", "changefreq": "monthly"},
    {"path": "/conseils-informatiques/", "priority": "0.6", "changefreq": "monthly"},
    {"path": "/blog/", "priority": "0.7", "changefreq": "weekly"},
]


def load_posts():
    if not POSTS_JSON.exists():
        sys.exit(f"Introuvable : {POSTS_JSON}. Lance le script depuis la racine du repo.")
    return json.loads(POSTS_JSON.read_text(encoding="utf-8"))["posts"]


def build_urls():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = []

    for page in STATIC_PAGES:
        urls.append({
            "loc": f"{SITE_URL}{page['path']}",
            "lastmod": today,
            "changefreq": page["changefreq"],
            "priority": page["priority"],
        })

    for post in load_posts():
        urls.append({
            "loc": f"{SITE_URL}/blog/{post['slug']}/",
            "lastmod": post["date"],
            "changefreq": "yearly",
            "priority": "0.5",
        })

    return urls


def render_sitemap(urls) -> str:
    items = []
    for u in urls:
        items.append(f"""  <url>
    <loc>{escape(u['loc'])}</loc>
    <lastmod>{u['lastmod']}</lastmod>
    <changefreq>{u['changefreq']}</changefreq>
    <priority>{u['priority']}</priority>
  </url>""")
    body = "\n".join(items)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""


def main():
    urls = build_urls()
    SITEMAP.write_text(render_sitemap(urls), encoding="utf-8")
    print(f"Généré : {SITEMAP}")
    print(f"{len(urls)} URL(s) dans le sitemap.")


if __name__ == "__main__":
    main()
