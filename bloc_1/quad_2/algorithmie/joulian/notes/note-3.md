# Prise de note - algorithmie - N03

# Tris
> Doit savoir comparer tous les tris pour la fin d'annee !!!

# Graphes (+Pathfinding)
- G = (V, E)
    - V == Sommets (noeuds, points, vertex)
    - E == Aretes (liens, lignes)

- Il y a differents type de graphes. (orientation, conexe)

- Structure de donnees abstraite

Algorithmes:
    - Dijkstra (< Bellman-Dord)
    - Floyd-Warshall
    - A* (proba)
    - Kruskal (Utile pour les spanning-tree)
    - Prim (evolution Dijkstra)
    - Boruvka

## Operations

- Ajacents avec x et y
- Voisins avec x
- Ajouter... Sommets/Arete
- Supprimer... Sommets/Arete
- SetValues
- GetValues

## Parcours

en largeur:
    - Utilisation d'une file pour les noeuds voisins.

en profondeur:
    - Marquage des sommets visistes

## Representations

- Liste d'adjacence: sommet == liste avec sommets adjacents
- Matrice d'adjacence: lignes == sommets de depart + colonnes == sommets d'arrivee
- Matrice d'incidence: lignes == sommets + colonnes == aretes (pas important)

## Notice

> Ces notes ne sont pas forcement correctes (voir syntheses).