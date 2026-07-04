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

# Dossiers à la racine qui ne sont PAS des pages compagnons (infra, pas contenu)
IGNORE_DIRS = {".git", "__pycache__", "assets", "blog", "node_modules", ".github"}


# Ajustements de priorité pour des pages spécifiques (le reste utilise
# la valeur par défaut 0.8). À compléter si besoin, sans que ça bloque
# la découverte automatique des nouvelles pages.
PRIORITY_OVERRIDES = {
    "conseils-informatiques": "0.6",
}


def discover_static_pages():
    """Scanne la racine du repo : tout dossier contenant un index.html
    (hors dossiers infra) est traité comme une page compagnon (livret,
    conseils-informatiques, etc). Ajouté automatiquement, sans liste à
    maintenir à la main — voir aussi update-readme-structure.py qui suit
    le même principe."""
    pages = [{"path": "/", "priority": "1.0", "changefreq": "monthly"}]
    for entry in sorted(ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in IGNORE_DIRS or entry.name.startswith("."):
            continue
        if (entry / "index.html").exists():
            priority = PRIORITY_OVERRIDES.get(entry.name, "0.8")
            pages.append({"path": f"/{entry.name}/", "priority": priority, "changefreq": "monthly"})
    pages.append({"path": "/blog/", "priority": "0.7", "changefreq": "weekly"})
    return pages


def load_posts():
    if not POSTS_JSON.exists():
        sys.exit(f"Introuvable : {POSTS_JSON}. Lance le script depuis la racine du repo.")
    return json.loads(POSTS_JSON.read_text(encoding="utf-8"))["posts"]


def build_urls():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = []

    for page in discover_static_pages():
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
