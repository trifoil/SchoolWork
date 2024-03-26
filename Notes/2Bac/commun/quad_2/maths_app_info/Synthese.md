# Synthese de mathématiques appliquées à l'informatique

Graphe de l'évolution du temps de calcul en fonction de la complexité du calcul (appelé n ou encore taille du problème)

l'expression $O(n)$ représente la borne supérieure

On note $f(n)\in O(g(n))$, où $f(n)$ et $g(n)$ peuvent prendre un tas de formes (des fonction mathématiques courantes : logarithmes carrés, etc... )

La formule générale pour la complexité (mesure de l'ordre de grandeur d'une fonction) est :

$$f(n) \in O(g(n))$$

si

$$\exists c > 0, \exists n_0 \geq 1 : f(n) \leq c . g(n) \forall n \geq n_0 $$

Ce qui veut dire que $f(n)$ appartient à $O(g(n))$ s'il existe une constante multiplicative $c$ plus grande que zero, et un nombre (seuil) plus grand ou égal à 1, tels que $f(n)$ est toujours plus petit ou égal à la constante multiplicative fois $g(n)$ pour tout n supérieur ou égal au seuil choisi.     
C'est donc une manière de voir si on dépasse pour des n grands.

Quelques exercices :

> [!IMPORTANT]  
> Log veut dire ici logaritme néperien, et l'un et l'autre sont liés par une constante

1) Vrai ou faux?    
$n \log(n) \in O(n)$     

    * résolution rigoureuse     
    Selon la définition,    
    $f(n) \leq c . g(n) $ 
    $\forall n \geq n_0 $       
    devient     
    $ n \log(n) \leq c . n $ 
    $ \forall n \geq n_0 $       

    * approche intuitive        

