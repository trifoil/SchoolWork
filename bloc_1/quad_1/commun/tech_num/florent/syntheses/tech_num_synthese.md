---
title: "Techniques numériques"
output:
  pdf_document:
    toc: yes
  html_document:
    toc: yes
    number_sections: yes
date: "Q1 2023"
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

# Logique mathématique

-   Formule

-   Prédicat

-   Une valeur de vérité est une valeur attribuée à chaque proposition logique.

-   Un connecteur logique est un opérateur booléen utilisé dans le calcul des propositions.

# Algèbre de Boole

## Principe

On travaille avec des variables comprises dans l'ensemble $B = \{0, 1\}$.

Sur cet ensemble, on définit 3 opérateurs de base.

1.  ET
    -   x . y

|  x  |  y  | F(x . y) |
|:---:|:---:|:--------:|
|  0  |  0  |    0     |
|  0  |  1  |    0     |
|  1  |  0  |    0     |
|  1  |  1  |    1     |

------------------------------------------------------------------------

2.  OU
    -   x + y

|  x  |  y  | F(x . y) |
|:---:|:---:|:--------:|
|  0  |  0  |    0     |
|  0  |  1  |    0     |
|  1  |  0  |    0     |
|  1  |  1  |    1     |

------------------------------------------------------------------------

3.  NON
    -   !x

|  x  | F(!x) |
|:---:|:-----:|
|  0  |   0   |
|  0  |   0   |

------------------------------------------------------------------------

## Les fonctions binaires

Les fonctions binaires prennent des valeurs binaires en entrée et renvoient des booléens en sorties.

Par exemple, les opérateurs ET, OU, NON sont des fonctions binaires qui prennent des valeurs de 0 à 3 et qui renvoient 1(Vrai) ou 0(Faux).

## Expressions canoniques

### Somme de produits

### Produit de sommes

-   Toutes les fonctions binaires peuvent être exprimées avec AND, OR, NOT.

# Portes logiques

# Table de Karnaugh
