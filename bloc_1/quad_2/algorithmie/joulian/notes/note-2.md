# Prise de note - algorithmie - N02

## Tri par tas

Utilise:
    - Liste
    - arbres

Etapes:
    1. Cree un arbre binaire a une liste, l'element = (index + valeur)
    2. swap: on echange l'element racine avec l'element le plus en bas a droite possible + on le change de place aussi dans la liste
    3. remove: on retire l'element de l'arbre car il est bien mis.
    3. heapify: Repositionne l'element le plus grand a la racine

Complexite:

| Type          | Complexite  |
| ------------- | ----------- |
| Meilleur Temp | O(n log(n)) |
| Moyenne Temp  | O(n log(n)) |
| Pire Temp     | O(n log(n)) |
| Spatiale      | O(1)        |

- Stable? Non

## Tables de hachage
- Structure de donnees
- Utilise les tableaux

Position de l'element depend de lui meme.

Particularite:
    - On peut faire: `Value -> Hash`, mais on peut pas `Hash -> Value`
    - Collisions: Il est possible que deux valeurs differentes peuvent faire un meme Hash !! (A EVITER)
    - Tous les `Hash` ont la meme taille independement de la `Value`

> TABLE DE HACHAGE N'EST PAS POUR STOCKER DES PASSWORDS

Salage:
    - Ajout un element a une donnees pour modifier sa signature
    - Plus securise
    - Moins de chances de collisions

Salage static:
    - Meme salage pour tout le monde.

Salage dynamique:
    - Depend d'elements recuperables.

Algorithms:
    - MD5 (Collisions: pas fou, Securite: pas fou, 128bits)
    - SHA-1 (Collisions: ok, 160bits)
    - SHA-2 (CHAD+++, 224-512bits) -> SHA-256 / SHA-512

Solutions au collisions:
    - Si deux elements ont meme Hash -> Liste chainees dans le meme index.
    - Hashage ouvert

Complexite:
| Type          | List | Search | Insert | Delete |
| ------------- | ---- | ------ | ------ | ------ |
| Meilleur Temp | O(n) | O(1)   | O(1)   | O(1)   |
| Pire Temp     | O(n) | O(n)   | O(n)   | O(n)   |

## SHA-256
1. Pretraitement:
    - Padding: ajout d'elements pour atteindre la taille minimum pour le hashage (512bits)
2. Initialisations Constantes:
    - huits constantes a partir des 32 premiers bits + huits permiers nombres premiers
3. Division en blocs
4. Traitement
    - Recursif
    - Individuel
    - Transformation (Permutation, rotation, modulo, ...)
    

## Notice

> Ces notes ne sont pas forcement correctes (voir syntheses).