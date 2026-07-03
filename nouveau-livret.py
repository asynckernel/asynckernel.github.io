#!/usr/bin/env python3
"""
Scaffolding pour une nouvelle page compagnon de livret Async Kernel.

Crée <slug>/index.html (gabarit vide à remplir), et insère automatiquement
l'entrée correspondante dans la section "ls bibliothèque/" de index.html.

Usage : python3 nouveau-livret.py (depuis la racine du repo, en interactif)

Ne touche à rien d'autre. Ne met PAS à jour sitemap.xml ni README.md —
rappels affichés en fin d'exécution.
"""

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent
INDEX_HTML = ROOT / "index.html"

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — outils recommandés · Async Kernel &gt;_</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#162842">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <header class="site-header">
    <div class="container">
      <a href="/" class="brand">Async Kernel <span class="prompt">&gt;_</span></a>
    </div>
  </header>

  <main>
    <div class="container">
      <div class="hero">
        <h1>{title_html}</h1>
        <p class="lede">{description}</p>
      </div>

      <!-- TODO : sections "ls xxx/" avec articles .product, sur le modèle
           de trois-carnets/index.html, un-iphone-qui-nepuise-pas/index.html
           ou jegardelecontrolesurmonordi/index.html selon la structure
           la plus pertinente pour ce livret. -->

      <section>
        <p class="section-prompt">ls TODO/</p>

        <article class="product">
          <h3>TODO — premier élément</h3>
          <p>TODO — description.</p>
          <p class="meta">TODO prix · <a href="#TODO">voir →</a></p>
        </article>
      </section>

      <div class="disclosure">
        <p><strong>Note d'usage.</strong> Cette page contient des liens d'affiliation Amazon. Si vous achetez via ces liens, je perçois une petite commission qui contribue à financer le travail éditorial sans rien changer au prix que vous payez. Les références sont sélectionnées sur la base de leur pertinence pour le système décrit dans le guide, pas sur la commission qu'elles génèrent.</p>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>Async Kernel <span class="prompt">&gt;_</span> · <a href="/">accueil</a> · contact@asynckernel.fr</p>
    </div>
  </footer>
</body>
</html>
"""

HOMEPAGE_ARTICLE = """        <article class="product">
          <h3>{title}</h3>
          <p>{description}</p>
          <p class="meta">TODO prix numérique · <a href="#TODO">acheter</a> · TODO prix papier · <a href="#TODO">acheter sur Amazon.</a></p>
          <p>     </p>
          <p class="meta">guide pratique · 2026 · <a href="/{slug}/">outils recommandés →</a></p>
        </article>
"""


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text


def insert_into_homepage(title, description, slug):
    if not INDEX_HTML.exists():
        raise RuntimeError(f"Introuvable : {INDEX_HTML}")
    html = INDEX_HTML.read_text(encoding="utf-8")

    marker = 'ls bibliothèque/</p>'
    idx = html.find(marker)
    if idx == -1:
        raise RuntimeError("Section « ls bibliothèque/ » introuvable dans index.html — insertion manuelle nécessaire.")

    # Cherche le "\n<indentation></section>" qui ferme cette section, en
    # préservant l'indentation exacte pour ne pas casser la mise en forme.
    m = re.search(r"\n([ \t]*)</section>", html[idx:])
    if not m:
        raise RuntimeError("</section> introuvable après « ls bibliothèque/ » — insertion manuelle nécessaire.")
    close_idx = idx + m.start()
    indent = m.group(1)

    new_article = HOMEPAGE_ARTICLE.format(title=title, description=description, slug=slug)
    updated = html[:close_idx] + "\n" + new_article + "\n" + indent + "</section>" + html[idx + m.end():]
    INDEX_HTML.write_text(updated, encoding="utf-8")


def main():
    print(">_ nouveau livret Async Kernel\n")
    title = input("Titre du livre : ").strip()
    if not title:
        sys.exit("Titre requis.")
    description = input("Description courte (1-2 phrases, pour la page et l'accueil) : ").strip()
    slug_input = input(f"Slug [{slugify(title)}] : ").strip()
    slug = slugify(slug_input) if slug_input else slugify(title)

    article_dir = ROOT / slug
    if article_dir.exists():
        sys.exit(f"Le dossier « {slug} » existe déjà.")

    article_dir.mkdir(parents=True)
    page = PAGE_TEMPLATE.format(title=title, title_html=title, description=description)
    (article_dir / "index.html").write_text(page, encoding="utf-8")
    print(f"\n✅ Créé : {article_dir / 'index.html'} (gabarit à remplir, sections TODO)")

    insert_into_homepage(title, description, slug)
    print(f"✅ Entrée ajoutée dans index.html, section « ls bibliothèque/ »")

    print("\nReste à faire manuellement :")
    print(f"  1. Remplir {slug}/index.html (sections réelles, produits, liens)")
    print(f"  2. Ajouter \"/{slug}/\" dans STATIC_PAGES de generate_sitemap.py, puis relancer generate_sitemap.py")
    print(f"  3. Ajouter une ligne dans le tableau « Pages compagnons existantes » du README.md")
    print(f"  4. Vérifier les prix/liens dans index.html (actuellement des TODO)")
    print(f"  5. git add . && git commit -m \"feat: page compagnon — {title}\" && git push")


if __name__ == "__main__":
    main()
