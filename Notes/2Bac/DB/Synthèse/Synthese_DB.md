# Synthèse du cours de bases de données (DB) ⛁

## Definitions

1) Definition :
* Ensemble (potentiellement structuré) organisé de données ayant un objectif commun.

2) SGBD : 
* Système de gestion de base de données.

3) OLTP :
* OnLine Transaction processing.

4) ACID :
* Ensemble de propriétés qui garantissent
qu'une transaction est exécutée de façon fiable 
    - **Atomicité:** Une transaction se fait au complet ou pas du tout
    - **Cohérence:** Assure que chaque transaction amènera le système d'un état valide à un autre état valide
    - **Isolation:** Toute transaction doit s'exécuter comme si elle était la seule sur le système (pas de dépendance)
    - **Durabilité:** Lorsqu'une transaction a été confirmée, elle demeure enregistrée même à la suite d'une panne


5) OLAP : 
* OnLine Analytical Processing

6) On travaille avec des DB relationnelles

## Modelisation 

### Définitions


1) Tuple :
* Collection ordonnée de n objets. 
* Stocké dans une table (entité)

2) Merise :
* Méthode d'analyse, de conception et de gestion de projet (informatique)
    - **Entités**
        * regroupements d'informations communes à un "individu"
        * équivalent d'une "classe" en POO
        * schématisés par un rectangle
    - **Attributs**
        * caractéristiques décrivant les entités
        * vont stocker des valeurs
        * représentés par une liste de mots explicites et concis
    - **Association**
        * Liaison logique entre une ou plusieurs entités
        * Représentée par une ellipse (en MERISE) reliée aux entités concernées
        * Doit être affublée de cardinalités aux extrémités de l'association afin d'en caractériser le type
    - **Degré**
        * Nb d'entités inpliquées dans la relation
    - **Cardinalités**
        * Inversées entre modele UML et ER

### Le schéma conceptuel



### Le schéma logique
### Normalisation
### Le schéma physique