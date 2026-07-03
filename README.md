# asynckernel.github.io

Site officiel des éditions **Async Kernel >_**.

Servi à l'adresse https://asynckernel.fr via GitHub Pages.

## Structure

```
.
├── index.html                          ← accueil de la marque
├── trois-carnets/
│   └── index.html                      ← page compagnon du tome 1
├── un-iphone-qui-nepuise-pas/
│   └── index.html                      ← page compagnon du tome 2
├── jegardelecontrolesurmonordi/
│   └── index.html                      ← page compagnon du tome 3
├── conseils-informatiques/
│   └── index.html                      ← astuces transversales, accès libre
├── blog/
│   ├── index.html                      ← généré par generate_blog.py
│   ├── feed.xml                        ← généré par generate_blog.py (RSS 2.0)
│   └── <slug>/index.html               ← un article par dossier, écrit à la main
├── posts.json                          ← source de vérité du blog
├── generate_blog.py                    ← régénère blog/index.html + blog/feed.xml
├── generate_sitemap.py                 ← régénère sitemap.xml (pages statiques + blog)
├── nouveau-livret.py                   ← scaffolding page compagnon + entrée accueil
├── nouveau-conseil.py                  ← ajoute un conseil sur conseils-informatiques/
├── sitemap.xml                         ← généré, à régénérer après tout ajout de page
├── 404.html                            ← page d'erreur
├── assets/
│   ├── css/
│   │   └── style.css                   ← feuille de style commune
│   └── fonts/                          ← polices auto-hébergées (EB Garamond, JetBrains Mono)
├── CNAME                               ← domaine personnalisé pour GitHub Pages
├── .nojekyll                           ← désactive Jekyll (le site est servi tel quel)
├── robots.txt                          ← configuration indexation
└── README.md
```

## Déploiement

Chaque push sur la branche `main` déclenche un déploiement automatique sur GitHub Pages.

## Blog et flux RSS

`posts.json` est la source de vérité unique. `generate_blog.py` régénère `blog/index.html`
et `blog/feed.xml` à partir de ce fichier — ne touche jamais aux pages d'articles
individuelles (`blog/<slug>/index.html`), écrites à la main.

Nouvel article :
1. Dupliquer un dossier `blog/<slug-existant>/` (ou utiliser l'outil local `nouveau-billet.py`,
   voir `~/scripts/asynckernel-blog/`)
2. Ajouter l'entrée dans `posts.json`
3. `python3 generate_blog.py`
4. `python3 generate_sitemap.py`
5. Commit + push, puis vérifier le flux sur [validator.w3.org/feed](https://validator.w3.org/feed/)

## Sitemap

`sitemap.xml` est généré par `generate_sitemap.py` à partir d'une liste de pages statiques
(codée en dur en haut du script — à mettre à jour à chaque nouveau livret) et de `posts.json`
pour les articles de blog. Pas de mise à jour automatique au push : à relancer manuellement
après toute nouvelle page.

## Nouveau livret

`python3 nouveau-livret.py` (interactif) crée `<slug>/index.html` (gabarit avec sections TODO
à remplir) et ajoute automatiquement l'entrée correspondante dans la section
`ls bibliothèque/` de `index.html`. Ne met pas à jour le sitemap ni ce README — rappels
affichés en fin d'exécution.

## Nouveau conseil

`python3 nouveau-conseil.py` (interactif) ajoute un article à `conseils-informatiques/index.html`,
dans une rubrique existante ou une nouvelle rubrique `ls <catégorie>/`.

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
