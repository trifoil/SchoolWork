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
        * Selon la définition,    
    $f(n) \leq c . g(n)$    
    $\forall n \geq n_0 $       
        * devient     
    $n \log(n) \leq c . n$  
    $\forall n \geq n_0 $  
        * Il faut chercher $n_0$ et c pour que l'équation soit vraie  
    Avec    
    $n \log(n) \leq 1000 n$  
    par définition, $n \neq 0$     
    $\forall n \geq n_0 $   
        * Isoler $n$  
    $n \log(n) \leq 1000 n$     
    $\log(n) \leq 1000$   
    $n \leq \exp(1000)$    



    * approche intuitive        

2) Vrai ou faux?   
$10^{12} \in O(1)$

    * résolution rigoureuse     
        * Selon la définition,   
        $10^{12} \leq C .1$     
        $\forall n \geq n_0 $  
        * On prend un $c$ arbitraire    
        $10^{12} \leq 10^{12} .1$       

        * Ici, le $n_0$ n'influence rien donc il est choisi arbitrairement, On va donc prendre :         
        $\forall n \geq 1 $ 
        * Il faut juste vérifier que ceci est vrai :    
        $10^{12} \leq 10^{12} .1$            
        $\forall n \geq 1 $ 
        * -> Vrai
   


3) Vrai ou faux?   