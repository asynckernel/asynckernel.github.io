#!/usr/bin/env python3
"""
Régénère le bloc de structure (arborescence) du README.md, entre les
marqueurs <!-- STRUCTURE:START --> et <!-- STRUCTURE:END -->.

Scanne le repo réel : la structure est toujours exacte. Les commentaires
(" ← accueil de la marque", etc.) sont conservés pour les chemins connus
via COMMENTS ci-dessous ; à compléter à la main quand tu ajoutes un
nouveau fichier significatif. Un chemin absent de COMMENTS apparaît
simplement sans commentaire — rien ne casse, mais rien n'est deviné.

Usage : python3 update-readme-structure.py (depuis la racine du repo)
"""

import sys
from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"

START_MARKER = "<!-- STRUCTURE:START"
END_MARKER = "<!-- STRUCTURE:END -->"

# Dossiers/fichiers ignorés dans le scan (infra, pas contenu éditorial)
IGNORE = {".git", "__pycache__", ".DS_Store"}

# Commentaires connus, par chemin relatif à la racine (sans slash final
# pour les dossiers). À compléter à la main si tu veux qu'un nouveau
# fichier apparaisse commenté.
COMMENTS = {
    "index.html": "accueil de la marque",
    "trois-carnets": "page compagnon du tome 1",
    "un-iphone-qui-nepuise-pas": "page compagnon du tome 2",
    "jegardelecontrolesurmonordi": "page compagnon du tome 3",
    "conseils-informatiques": "astuces transversales, accès libre",
    "blog": "notes de veille, RSS",
    "blog/index.html": "généré par generate_blog.py",
    "blog/feed.xml": "généré par generate_blog.py (RSS 2.0)",
    "posts.json": "source de vérité du blog",
    "generate_blog.py": "régénère blog/index.html + blog/feed.xml",
    "generate_sitemap.py": "régénère sitemap.xml (pages statiques + blog)",
    "update-readme-structure.py": "régénère ce bloc de structure",
    "nouveau-livret.py": "scaffolding page compagnon + entrée accueil",
    "nouveau-conseil.py": "ajoute un conseil sur conseils-informatiques/",
    "sitemap.xml": "généré, à régénérer après tout ajout de page",
    "404.html": "page d'erreur",
    "assets": None,
    "assets/css": None,
    "assets/css/style.css": "feuille de style commune",
    "assets/fonts": "polices auto-hébergées (EB Garamond, JetBrains Mono)",
    "CNAME": "domaine personnalisé pour GitHub Pages",
    ".nojekyll": "désactive Jekyll (le site est servi tel quel)",
    "robots.txt": "configuration indexation",
    "README.md": None,
}


def scan(dir_path: Path, prefix: str, rel_prefix: str, lines: list):
    entries = sorted(
        [e for e in dir_path.iterdir() if e.name not in IGNORE],
        key=lambda e: (e.is_file(), e.name.lower())
    )
    # dossiers d'abord, alphabétique ; fichiers ensuite, alphabétique
    dirs = [e for e in entries if e.is_dir()]
    files = [e for e in entries if e.is_file()]
    entries = dirs + files

    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "
        rel_path = f"{rel_prefix}{entry.name}" if not rel_prefix else f"{rel_prefix}/{entry.name}"
        # Chemin utilisé pour la table COMMENTS : sans slash final pour les dossiers
        lookup_key = rel_path

        display_name = entry.name + ("/" if entry.is_dir() else "")
        comment = COMMENTS.get(lookup_key)
        line = f"{prefix}{connector}{display_name}"
        if comment:
            pad = max(1, 40 - len(prefix) - len(connector) - len(display_name))
            line += " " * pad + f"← {comment}"
        lines.append(line)

        if entry.is_dir():
            extension = "    " if is_last else "│   "
            # Ne descend pas dans assets/fonts (contenu non éditorial, nombreux fichiers)
            if lookup_key == "assets/fonts":
                continue
            scan(entry, prefix + extension, rel_path, lines)


def build_tree() -> str:
    lines = ["."]
    scan(ROOT, "", "", lines)
    return "\n".join(lines)


def main():
    if not README.exists():
        sys.exit(f"Introuvable : {README}")
    content = README.read_text(encoding="utf-8")

    start_idx = content.find(START_MARKER)
    end_idx = content.find(END_MARKER)
    if start_idx == -1 or end_idx == -1:
        sys.exit(
            "Marqueurs STRUCTURE:START / STRUCTURE:END introuvables dans README.md.\n"
            "Ajoute-les manuellement une fois autour du bloc ```...``` de structure."
        )

    # Trouve la fin de la ligne START_MARKER (fin du commentaire HTML)
    marker_line_end = content.find("\n", start_idx) + 1
    tree = build_tree()
    new_block = f"```\n{tree}\n```\n"

    updated = content[:marker_line_end] + new_block + content[end_idx:]
    README.write_text(updated, encoding="utf-8")
    print(f"Structure régénérée dans {README}")


if __name__ == "__main__":
    main()
