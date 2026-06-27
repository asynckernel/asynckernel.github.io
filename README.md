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

## Licence

Code source (HTML/CSS) sous licence libre à définir (CC0 ou MIT envisageables).
Contenu éditorial © Async Kernel >_, tous droits réservés.
