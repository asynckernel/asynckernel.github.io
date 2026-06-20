# asynckernel.github.io

Site officiel des éditions **Async Kernel >_**.

Servi à l'adresse https://asynckernel.fr via GitHub Pages.

## Structure

```
.
├── index.html              ← accueil de la marque
├── trois-carnets/
│   └── index.html          ← page compagnon du livre
├── 404.html                ← page d'erreur
├── assets/
│   └── css/
│       └── style.css       ← feuille de style commune
├── CNAME                   ← domaine personnalisé pour GitHub Pages
├── .nojekyll               ← désactive Jekyll (le site est servi tel quel)
├── robots.txt              ← configuration indexation
└── README.md
```

## Déploiement

Chaque push sur la branche `main` déclenche un déploiement automatique sur GitHub Pages.

## Ajouter un produit recommandé

1. Éditer `trois-carnets/index.html`
2. Copier un bloc `<article class="product">…</article>` existant
3. Adapter titre, description, prix et lien d'affiliation
4. Commit + push

## Ajouter un nouveau livre

1. Créer un nouveau dossier à la racine, par exemple `nouveau-titre/`
2. Y placer un `index.html` qui suit la structure de `trois-carnets/index.html`
3. Ajouter une référence dans la section `ls bibliothèque/` du `index.html` racine
4. Commit + push

## Polices

Les polices sont actuellement chargées depuis Google Fonts (JetBrains Mono + EB Garamond).

**TODO :** héberger localement les polices pour respect des données personnelles européennes et chargement plus rapide. Voir [google-webfonts-helper](https://gwfh.mranftl.com/fonts) pour générer les fichiers `.woff2` et les `@font-face` correspondants.

## Licence

Code source (HTML/CSS) sous licence libre à définir (CC0 ou MIT envisageables).
Contenu éditorial © Async Kernel >_, tous droits réservés.
