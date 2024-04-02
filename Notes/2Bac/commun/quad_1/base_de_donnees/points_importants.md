## Points importants :

- SELECT
- WHERE
- ORDER BY
- AND
- OR
- INSERT INTO
- UPDATE
- DELETE
- MIN MAX
- COUNT (SUPER IMPORTANT)
- SUM
- AVG
- LIKE (IMPORTANT)

tous les join sauf le self
group by 
having

formulaires get et post

requete
requete preparée

regex


## Synthèse sur les requêtes SQL

### SELECT

Pour sélectionner toute la table "Customers" (* veut dire all):
```
SELECT * FROM joueurs;
```
![Alt text](image.png)

Pour sélectionner le colonne equipe dans la table joueurs :
```
SELECT equipe FROM joueurs;
```
![Alt text](image-1.png)

Rigoureusement, on précise que l'on sélectionne la colonne qui vient d'une table précise (pas de conflits quand on importe plusieurs tables) :

```
SELECT joueurs.equipe FROM joueurs
```

![Alt text](image-3.png)

### WHERE

Pour sélectionner les lignes auxquelles la colonne possède la valeur :

```
SELECT joueurs.equipe FROM joueurs WHERE joueurs.equipe = 'RUS';
```

![Alt text](image-4.png)