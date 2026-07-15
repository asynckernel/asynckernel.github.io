#!/usr/bin/env python3
"""
Génère blog/index.html et blog/feed.xml à partir de posts.json.

Usage : python3 generate_blog.py (depuis la racine du repo)

Ce script ne touche jamais aux pages individuelles des articles
(blog/<slug>/index.html) : celles-ci restent écrites à la main.
Il régénère uniquement la liste et le flux RSS, à partir de la
même source de vérité (posts.json), pour éviter toute désynchronisation.

Le header/footer/head repris ici sont ceux de index.html et
trois-carnets/index.html au 02/07/2026. Si tu modifies le gabarit
commun du site (nav, footer), reporte le changement ici aussi.
"""

import json
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).parent
POSTS_JSON = ROOT / "posts.json"
BLOG_DIR = ROOT / "blog"

HEAD_COMMON = """  <link rel="stylesheet" href="/assets/css/style.css">"""

HEADER = """  <header class="site-header">
    <div class="container">
      <a href="/" class="brand">Async Kernel <span class="prompt">&gt;_</span></a>
    </div>
  </header>"""

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <p>Async Kernel <span class="prompt">&gt;_</span> · <a href="/">accueil</a> · <a href="/blog/">blog</a> · contact@asynckernel.fr</p>
      <p class="meta">En tant que Partenaire Amazon, Async Kernel réalise un bénéfice sur les achats remplissant les conditions requises. Pour vous, cela ne change rien au prix ; pour moi, cela fait vivre le projet.</p>
    </div>
  </footer>"""


def load_posts():
    if not POSTS_JSON.exists():
        sys.exit(f"Introuvable : {POSTS_JSON}. Lance le script depuis la racine du repo.")
    data = json.loads(POSTS_JSON.read_text(encoding="utf-8"))
    data["posts"].sort(key=lambda p: p["date"], reverse=True)
    return data


def render_index(data: dict) -> str:
    site_url = data["site_url"]
    items = []
    for p in data["posts"]:
        url = f"/blog/{p['slug']}/"
        date_h = datetime.strptime(p["date"], "%Y-%m-%d").strftime("%d/%m/%Y")
        items.append(f"""        <article class="product">
          <h3><a href="{url}">{escape(p['title'])}</a></h3>
          <p>{escape(p['excerpt'])}</p>
          <p class="meta">{date_h}</p>
        </article>""")

    posts_html = "\n\n".join(items)

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(data['blog_title'])}</title>
  <meta name="description" content="{escape(data['blog_description'])}">
  <meta name="theme-color" content="#162842">

{HEAD_COMMON}
  <link rel="alternate" type="application/rss+xml" title="{escape(data['blog_title'])}" href="{site_url}/blog/feed.xml">
</head>
<body>
{HEADER}

  <main>
    <div class="container">
      <div class="hero">
        <h1>Blog.</h1>
        <p class="lede">{escape(data['blog_description'])}</p>
        <p class="meta"><a href="/blog/feed.xml" style="color: var(--accent); text-decoration: none; border-bottom: 1px dotted var(--accent); padding-bottom: 2px;">S'abonner au flux RSS →</a></p>
      </div>

      <section>
        <p class="section-prompt">ls blog/</p>

{posts_html}
      </section>
    </div>
  </main>

{FOOTER}
</body>
</html>
"""


def render_feed(data: dict) -> str:
    site_url = data["site_url"]
    now = format_datetime(datetime.now(timezone.utc))

    items = []
    for p in data["posts"]:
        url = f"{site_url}/blog/{p['slug']}/"
        pub_date = format_datetime(
            datetime.strptime(p["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        )
        items.append(f"""    <item>
      <title>{escape(p['title'])}</title>
      <link>{url}</link>
      <guid isPermaLink="true">{url}</guid>
      <pubDate>{pub_date}</pubDate>
      <description>{escape(p['excerpt'])}</description>
    </item>""")

    items_xml = "\n".join(items)

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{escape(data['blog_title'])}</title>
    <link>{site_url}/blog/</link>
    <description>{escape(data['blog_description'])}</description>
    <language>fr</language>
    <lastBuildDate>{now}</lastBuildDate>
{items_xml}
  </channel>
</rss>
"""


def main():
    data = load_posts()
    BLOG_DIR.mkdir(exist_ok=True)

    (BLOG_DIR / "index.html").write_text(render_index(data), encoding="utf-8")
    (BLOG_DIR / "feed.xml").write_text(render_feed(data), encoding="utf-8")

    print(f"Généré : {BLOG_DIR / 'index.html'}")
    print(f"Généré : {BLOG_DIR / 'feed.xml'}")
    print(f"{len(data['posts'])} article(s) dans le flux.")


if __name__ == "__main__":
    main()
