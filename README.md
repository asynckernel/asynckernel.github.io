# asynckernel.github.io

Site officiel des éditions **Async Kernel >_**.

Servi à l'adresse https://asynckernel.fr via GitHub Pages.

## Structure

<!-- STRUCTURE:START (généré par update-readme-structure.py, ne pas éditer à la main entre ces marqueurs) -->
```
.
├── assets/
│   ├── css/
│   │   └── style.css                   ← feuille de style commune
│   └── fonts/                          ← polices auto-hébergées (EB Garamond, JetBrains Mono)
├── blog/                               ← notes de veille, RSS
│   ├── agenda-memoire-morte/
│   │   └── index.html
│   ├── fermer-onglet-mental/
│   │   └── index.html
│   ├── ranger-un-tiroir-pour-repartir/
│   │   └── index.html
│   ├── rappels-natif/
│   │   └── index.html
│   ├── sortir-sans-rien-dans-les-oreilles/
│   │   └── index.html
│   ├── telephone-passif-randonnee/
│   │   └── index.html
│   ├── vacances-banc-essai/
│   │   └── index.html
│   ├── feed.xml                        ← généré par generate_blog.py (RSS 2.0)
│   └── index.html                      ← généré par generate_blog.py
├── conseils-informatiques/             ← astuces transversales, accès libre
│   └── index.html
├── jegardelecontrolesurmonordi/        ← page compagnon du tome 3
│   └── index.html
├── trois-carnets/                      ← page compagnon du tome 1
│   └── index.html
├── un-iphone-qui-nepuise-pas/          ← page compagnon du tome 2
│   └── index.html
├── .gitignore
├── .nojekyll                           ← désactive Jekyll (le site est servi tel quel)
├── 404.html                            ← page d'erreur
├── CNAME                               ← domaine personnalisé pour GitHub Pages
├── couvertures-kdp.md
├── ETAT-PROJET.md
├── generate_blog.py                    ← régénère blog/index.html + blog/feed.xml
├── generate_sitemap.py                 ← régénère sitemap.xml (pages statiques + blog)
├── index.html                          ← accueil de la marque
├── posts.json                          ← source de vérité du blog
├── README.md
├── robots.txt                          ← configuration indexation
├── sitemap.xml                         ← généré, à régénérer après tout ajout de page
└── update-readme-structure.py          ← régénère ce bloc de structure
```
<!-- STRUCTURE:END -->

## Déploiement

Chaque push sur la branche `main` déclenche un déploiement automatique sur GitHub Pages.

## Blog et flux RSS

`posts.json` est la source de vérité unique. `generate_blog.py` régénère `blog/index.html`
et `blog/feed.xml` à partir de ce fichier — ne touche jamais aux pages d'articles
individuelles (`blog/<slug>/index.html`), écrites à la main.

## Blog, livret, conseil — interface locale

`~/scripts/asynckernel-blog/admin.py` (hors de ce repo, volontairement — voir plus bas)
est l'interface unique pour créer un billet, une page compagnon (« livret ») ou un conseil.
Lancer `python3 admin.py`, ou double-clic sur le raccourci bureau. Mode d'emploi intégré
dans la page. Aucune de ces actions ne fait git add/commit/push ni ne met à jour le sitemap
ou la structure du README — étape de relecture volontairement conservée, rappel affiché
après chaque création.

## Blog et flux RSS

`posts.json` est la source de vérité unique. `generate_blog.py` régénère `blog/index.html`
et `blog/feed.xml` à partir de ce fichier — ne touche jamais aux pages d'articles
individuelles (`blog/<slug>/index.html`), écrites à la main. Appelé automatiquement par
`admin.py` à la création d'un billet.

## Sitemap

`sitemap.xml` est généré par `generate_sitemap.py` à partir d'une liste de pages statiques
(codée en dur en haut du script — à mettre à jour à chaque nouveau livret) et de `posts.json`
pour les articles de blog. Pas de mise à jour automatique au push : à relancer manuellement
(onglet Maintenance de `admin.py`, ou `python3 generate_sitemap.py`).

## Structure du README

Le bloc de structure ci-dessus, entre les marqueurs `STRUCTURE:START`/`STRUCTURE:END`, est
généré par `update-readme-structure.py` (scan réel du repo). À relancer après tout ajout de
fichier (onglet Maintenance de `admin.py`, ou `python3 update-readme-structure.py`). Les
commentaires (« ← accueil de la marque », etc.) viennent d'une table dans le script — à
compléter à la main pour qu'un nouveau fichier apparaisse commenté.

## Pourquoi admin.py est hors du repo

Ce repo est publié tel quel sur GitHub Pages : tout fichier ici est servi publiquement sur
asynckernel.fr. `admin.py`, `nouveau-livret.py` et `nouveau-conseil.py` (obsolètes,
remplacés par `admin.py`) n'ont pas leur place ici — outil d'administration local uniquement.

## Ajouter un produit recommandé

1. Éditer le `index.html` du livre concerné (ex. `jegardelecontrolesurmonordi/index.html`)
2. Copier un bloc `<article class="product">…</article>` existant
3. Adapter titre, description, prix et lien d'affiliation ou lien officiel
4. Commit + push

## Ajouter un nouveau livre

1. Créer un nouveau dossier à la racine, par exemple `nouveau-titre/`
2. Y placer un `index.html` qui suit la structure d'une page compagnon existante (ex. `jegardelecontrolesurmonordi/index.html`)
3. Ajouter une entrée dans la section `ls bibliothèque/` du `index.html` racine
4. Commit + push

## Pages compagnons existantes

| Tome | Titre | Page compagnon | Structure |
|---|---|---|---|
| 1 | Trois carnets pour reprendre pied | `/trois-carnets/` | par catégorie de matériel papier |
| 2 | Un iPhone qui n'épuise pas | `/un-iphone-qui-nepuise-pas/` | par catégorie d'usage (apps, casques, etc.) |
| 3 | Je garde le contrôle de mon ordi | `/jegardelecontrolesurmonordi/` | par système d'exploitation (Windows 11, macOS, Linux Mint) + section transversale |

Chaque page compagnon suit le principe éditorial du livre correspondant. Pour le tome 3 : natif d'abord, logiciel libre ensuite, propriétaire en dernier recours — seuls les éléments demandant une installation ou un achat séparé figurent sur la page ; les leviers strictement natifs sont mentionnés pour mémoire sans nécessiter de lien.

## Polices

Les polices sont auto-hébergées dans `assets/fonts/` (EB Garamond + JetBrains Mono, fichiers `.woff2` générés depuis Google Fonts pour respect des données personnelles européennes et chargement plus rapide).

Toutes les pages, y compris celles générées par `generate_blog.py`, chargent uniquement
`/assets/css/style.css` — aucun lien vers le CDN Google Fonts nulle part sur le site
(corrigé le 03/07/2026, `generate_blog.py` chargeait encore le CDN en redondance).

## Licence

Code source (HTML/CSS) sous licence libre à définir (CC0 ou MIT envisageables).
Contenu éditorial © Async Kernel >_, tous droits réservés.
