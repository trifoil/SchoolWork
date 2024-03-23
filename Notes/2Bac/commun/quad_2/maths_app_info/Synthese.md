# Synthese de mathématiques appliquées à l'informatique

Graphe de l'évolution du temps de calcul en fonction de la complexité du calcul (appelé n ou encore taille du problème)

l'expression $O(n)$ représente la borne supérieure

On note $f(n)\in O(g(n))$, où $f(n)$ et $g(n)$ peuvent prendre un tas de formes (des fonction mathématiques courantes : logarithmes carrés, etc... )

La formule générale pour la complexité (mesure de l'ordre de grandeur d'une fonction) est :

$$f(n) \in O(g(n))$$

si

$$\exists c > 0, \exists n_0 \geq 1 : f(n) \geq c . g(n) \forall n \geq n_0 $$

"$f(n)$ appartient à $O(g(n))$ s'il existe une constante multiplicative $c$ plus grande que zero, et une  