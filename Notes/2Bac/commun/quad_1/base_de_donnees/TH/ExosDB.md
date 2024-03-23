1) Réalisez le MCD et le MLD d'une DB pour un restaurant

* La table : numero de table, nombre de place, date
* La table produit : nom de produit, priix, stock
* La table type de produit : nom du type, description, tva
* La table serveur : nom du serveur, salaire

    Une table commande des produits.    
    Une table peut commander plusieurs produits.    
    Un produit appartient toujours à un seul type.  
    Un seul serveur peut gérer plusieurs tables.    
    Une table ne change pas de serveur.     
    Un serveur ne travaille pas tous les jours.     
    Un produit n'appartient qu'à un seul type. 


2) Soit une agence immobilière qui propose la location de tous types d'hébergement (maison, appartement,...). Cette agence souhaite gérer ses logements avec une base de données, cette agence désire connaitre le nom de la commune et le quartier où se trouve chaque type de logement ainsi que les personnes qui ont loué ces logements (les signataires uniquement).   
Le prix pour chaque logement dépend de son type (maison, appartement, studio), 'agence facturera toujours en plus du loyer une charge forfaitaire à ses clients selon le type de bien. Par exemple, por louer un studio alors le prix égale au prix du loyer +30€ de charges par mois.  
Un logement est caractérisé aussi par sa surface, l'adresse ainsi que le loyer. Chaque client client est caractérisé par son nom, prénom, date de naissance et numéro de téléphone. Cette base de données doit connaitre le nombre d'habitantsde chaque commune ainsi que la distance séparant la commune de cette agence.  
La base de données à développer doit aussi gérer l'historique de location de ces logements par les individus. Il doit aussi enregistrer la date de début et la date de fin de chaque location.
Chaque client peut signer plusieurs contrats de location.
