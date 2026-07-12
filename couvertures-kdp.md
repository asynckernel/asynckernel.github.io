# Génération des couvertures KDP — Async Kernel >_

> Copie publique de la documentation interne (référence : COUVERTURES.md, dossier outillage kDrive). Rédigée le 12/07/2026.
> Statut des sources : cette procédure est reconstituée depuis les conversations Claude du projet KDP (tomes 1 à 3). **Les scripts eux-mêmes n'ont pas été conservés** : ils ont été générés et exécutés en conversation, à la demande. Les paramètres marqués « à vérifier » doivent être contrôlés sur le calculateur KDP au moment de chaque soumission.

---

## 1. Principe

Les couvertures sont générées par **script Python + Pillow**, jamais par outil graphique en ligne. Raison documentée : Canva AI (et équivalents) ne rend fidèlement ni le glyphe `>_`, ni les couleurs hex exactes, ni les typographies imposées. Le script garantit un rendu au pixel, reproductible d'un tome à l'autre.

Pour un nouveau tome, deux voies :
- relancer une conversation dans le projet Claude KDP en fournissant les paramètres du § 4 — le script est regénéré et exécuté ;
- (recommandé à terme) pérenniser un script `gen_couverture.py` paramétrable dans ce dossier, pour ne plus dépendre de la regénération.

## 2. Livrables par tome

| Livrable | Format | Spécifications |
|---|---|---|
| Couverture Kindle | JPEG | **1600 × 2560 px** (ratio 1,6:1), RGB |
| Couverture print (wraparound) | PDF | **300 DPI**, dimensions totales données par le template officiel KDP (dépendent du format 6×9", de la pagination et du papier) |

## 3. Paramètres de marque (constants)

- Palette : fond `#162842` (navy), texte `#E8E2D0` (cream), prompt `#7DB8A8` (teal), accent `#D8C77E` (gold), filet `#243959`.
- Typographies : **EB Garamond** (titres/corps) + **JetBrains Mono** (éléments structurels, `>_`).
- Source des polices dans le script : fontes **variables** téléchargées depuis le dépôt GitHub de Google Fonts (`raw.githubusercontent.com/google/fonts/...`) — pas de dépendance à un CDN.
- Marque centrale : le prompt terminal `>_`.

## 4. Procédure pour un nouveau tome

1. **Figer les paramètres** : titre, sous-titre, pagination définitive, type de papier (les tomes 1–3 : 6×9", ~45–50 p.).
2. **Télécharger le template officiel KDP** (calculateur de couverture KDP : format + pagination + papier). Il donne les dimensions totales, la largeur de tranche et la position de la zone code-barres.
3. **Tranche** : règle KDP — texte sur la tranche uniquement à partir de **79 pages**. Tous les tomes actuels (45–50 p.) sont en dessous → tranche laissée vierge, couleur de fond unie.
4. **Générer** via le script Pillow : quatrième de couverture (texte de présentation), tranche, première de couverture, aux dimensions du template.
5. **Zone code-barres** : sa position est vérifiée par **analyse de pixels du template officiel** — aucun contenu (texte, filet, motif) ne doit l'empiéter.
6. **Exporter** : PDF 300 DPI pour le print, JPEG 1600×2560 pour Kindle.

## 5. Vérifications avant soumission

- Dimensions du PDF exactement conformes au template (à vérifier : le template change avec la pagination — ne jamais réutiliser celui d'un tome précédent).
- Zone code-barres vierge.
- Fond perdu (bleed) inclus conformément au template KDP (à vérifier sur le calculateur ; ne pas se fier à une valeur mémorisée).
- Aperçu KDP (previewer) sans avertissement avant validation.
- Redevance recalculée sur le calculateur KDP à la soumission (fait pour le tome 3 le 12/07/2026).

## 6. Historique

- Tomes 1, 2, 3 : couvertures produites par ce pipeline. Tome 3 : wraparound PDF + Kindle JPEG générés et vérifiés (tranche vierge, zone code-barres contrôlée).
- Le logo du site a aussi été produit via Pillow (même contrainte de fidélité).

## 7. Limites connues de cette documentation

- Pas de valeurs chiffrées conservées pour : largeur de tranche par tome, coordonnées exactes de mise en page, noms de fichiers des fontes. Ces valeurs sont recalculées à chaque génération à partir du template KDP du moment.
- Si un script est pérennisé un jour, le documenter ici et supprimer ce paragraphe.
