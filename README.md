# asynckernel.github.io

Site officiel des éditions **Async Kernel >_**.

Servi à l'adresse https://asynckernel.fr via GitHub Pages.

## Livres publiés

| Titre | Numérique | Papier | Page outils |
|---|---|---|---|
| Trois carnets pour reprendre pied | [Amazon](https://amzn.to/3QvR60D) ~6,99 € | [Amazon](https://amzn.to/4ez51fH) ~11,98 € | `/trois-carnets/` |
| Un iPhone qui n'épuise pas | [Amazon](https://amzn.to/4oJAZJu) ~6,99 € | [Amazon](https://amzn.to/4b7EIe7) ~11,98 € | `/un-iphone-qui-nepuise-pas/` |

## Structure

```
.
├── index.html                          ← accueil de la marque (ls bibliothèque/)
├── trois-carnets/
│   └── index.html                      ← page outils du livre 1
├── un-iphone-qui-nepuise-pas/
│   └── index.html                      ← page outils du livre 2
├── 404.html                            ← page d'erreur
├── assets/
│   └── css/
│       └── style.css                   ← feuille de style commune
├── CNAME                               ← domaine personnalisé pour GitHub Pages
├── .nojekyll                           ← désactive Jekyll (le site est servi tel quel)
├── robots.txt                          ← configuration indexation
└── README.md
```

## Déploiement

Chaque push sur la branche `main` déclenche un déploiement automatique sur GitHub Pages.

## Ajouter un produit recommandé sur une page outils

1. Éditer `<slug-du-livre>/index.html`
2. Copier un bloc `<article class="product">…</article>` existant
3. Adapter titre, description, prix et lien d'affiliation
4. Commit + push

## Ajouter un nouveau livre

1. Créer un nouveau dossier à la racine, par exemple `nouveau-titre/`
2. Y placer un `index.html` qui suit la structure de `un-iphone-qui-nepuise-pas/index.html`
3. Ajouter un `<article class="product">` dans la section `ls bibliothèque/` de `index.html` (racine)
4. Commit + push

## Polices

JetBrains Mono et EB Garamond sont auto-hébergées dans `assets/fonts/` (subsets `latin` et `latin-ext`, format `.woff2`). Les `@font-face` sont déclarés en tête de `assets/css/style.css`. Aucune requête externe au chargement des pages.

## Licence

Code source (HTML/CSS) sous licence libre à définir (CC0 ou MIT envisageables).
Contenu éditorial © Async Kernel >_, tous droits réservés.
