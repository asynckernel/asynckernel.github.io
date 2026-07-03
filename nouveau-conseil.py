#!/usr/bin/env python3
"""
Ajoute un conseil à conseils-informatiques/index.html.

Deux cas :
  - la rubrique (ex. "mots-de-passe") existe déjà -> le conseil est
    ajouté comme nouvel <article> dans la <section> existante
  - la rubrique n'existe pas -> une nouvelle <section> est créée,
    juste avant la fermeture de <main>

Usage : python3 nouveau-conseil.py (depuis la racine du repo, en interactif)
"""

import html as html_lib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PAGE = ROOT / "conseils-informatiques" / "index.html"

ARTICLE_TEMPLATE = """        <article class="product">
          <h3>{title}</h3>
{content}
        </article>"""

SECTION_TEMPLATE = """      <section>
        <p class="section-prompt">ls {category}/</p>

{article}
      </section>
"""


def content_to_html(raw: str) -> str:
    blocks = re.split(r"\n\s*\n", raw.strip())
    out = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if re.match(r"^\d+\.\s", block):
            items = []
            for line in block.split("\n"):
                line = line.strip()
                m = re.match(r"^\d+\.\s(.*)", line)
                if m:
                    items.append(f"          <li>{html_lib.escape(m.group(1))}</li>")
            out.append("        <ol>\n" + "\n".join(items) + "\n        </ol>")
        elif block.lstrip().startswith("- "):
            items = [
                f"          <li>{html_lib.escape(line.strip()[2:].strip())}</li>"
                for line in block.split("\n") if line.strip().startswith("- ")
            ]
            out.append("        <ul>\n" + "\n".join(items) + "\n        </ul>")
        else:
            para = " ".join(line.strip() for line in block.split("\n") if line.strip())
            out.append(f"          <p>{html_lib.escape(para)}</p>")
    return "\n\n".join(out)


def main():
    print(">_ nouveau conseil — conseils-informatiques\n")
    if not PAGE.exists():
        sys.exit(f"Introuvable : {PAGE}")

    category = input("Rubrique (ex. mots-de-passe) : ").strip().lower().replace(" ", "-")
    title = input("Titre du conseil : ").strip()
    print("Contenu (paragraphes séparés par une ligne vide, listes avec '1. ' ou '- ') :")
    print("Termine par une ligne vide puis Ctrl+D.")
    raw_lines = sys.stdin.read()

    content_html = content_to_html(raw_lines)
    article = ARTICLE_TEMPLATE.format(title=title, content=content_html)

    page_html = PAGE.read_text(encoding="utf-8")
    section_marker = f"ls {category}/</p>"

    if section_marker in page_html:
        # Rubrique existante : insère avant le </section> correspondant
        idx = page_html.find(section_marker)
        m = re.search(r"\n([ \t]*)</section>", page_html[idx:])
        if not m:
            sys.exit("</section> introuvable pour cette rubrique — insertion manuelle nécessaire.")
        close_idx = idx + m.start()
        indent = m.group(1)
        updated = (page_html[:close_idx] + "\n" + article + "\n"
                   + indent + "</section>" + page_html[idx + m.end():])
        print(f"✅ Conseil ajouté dans la rubrique existante « ls {category}/ »")
    else:
        # Nouvelle rubrique : insère juste avant la fermeture de <main>
        new_section = SECTION_TEMPLATE.format(category=category, article=article)
        marker = "    </div>\n  </main>"
        if marker not in page_html:
            sys.exit("Marqueur de fin de <main> introuvable — insertion manuelle nécessaire.")
        updated = page_html.replace(marker, f"      {new_section}    </div>\n  </main>", 1)
        print(f"✅ Nouvelle rubrique créée : « ls {category}/ »")

    PAGE.write_text(updated, encoding="utf-8")
    print("\nReste à faire :")
    print(f"  1. Relire {PAGE}")
    print(f"  2. git add . && git commit -m \"feat: conseil — {title}\" && git push")
    print("  (sitemap non affecté : conseils-informatiques/ est une page unique déjà indexée)")


if __name__ == "__main__":
    main()
