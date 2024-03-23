## Examen 
- trois façon d'avoir zéro des le début :
	- Ne pas changer le nom du serveur
	- Ne pas avoir une ip fixe 
	- Pas de communication SRV <--> Client

Mise en place 
windows-server 2019 STD
- prendre la desktop exp standard 
- modif name (restart)
- config ip

- pour tester le reverse lookup ```nslookup [ip]```
- pour tester l'alias ```nslookup www.test.lan```


## Erreurs
- Soucis DNS --> config ipv4 add ip dns
- 

## Mise en place 
windows-server 2019 STD
- prendre la desktop exp standard 
- modif name 
	- Controll panel > sytem and security > system > advanced system settings > computer name > change  
	 ![[Pasted image 20231002194955.png]]
	 - **Ensuite restart** 
	 
- config ip
	- Control panel > network and internet > network and sharing center > ethernet > properties >ipv4 >properties  
	 ![[Pasted image 20231002194553.png]]

- Modifier le pare-feu 
	- control panel > windows defender firewall > advanced settings > trier par protocol > inbound rules  > activer tout les ipv4 (sauf file and printing mais pas obligé)
	 ![[Pasted image 20231002195831.png]]

-  tester la connection serveur <--> client avec ```Ping [ip]```

- Configure DNS (sur le serveur)
	- Server manager > manage > add roles and features > next > select based role or feature installation > next > next > cocher DNS server (dans server roles) > next .. >install  
	- Tools > DNS > clic droit sur forward lookup > new zone >primary zone > nom de zone > next ... 
	- clic droit sur le nom crée > ajouter hôte > nom dhote + ip address + cochez PTR 
	- (clic droit sur le nom crée > ajouter alias > www et sélectionner via le browse ) pas obligé
	- Reverse lookup > next > next > addresse du reseau

- tester avec ```nslookup [ip / nomdedomaine]``` sur le client et le serveur 

- Si IPV6 dans la réponse désactivez les ipv6 dans le config ip voir ci-dessus 
- Si domain : Unknown entrer l'ip du DNS dans cofig ipv4 voir ci dessus
- pour tester l'alias ```nslookup www.nomdomaine``` 

_____
## DNS 

-  ip
	- mettre des ip et masque fixe pour serveur primaire et secondaire 
	- mettre lp dns 

- time zone
	- mettre la meme time zone sur les 2 serveur (bruxelles)


- Setup dns  SRV1 (primaire)
	- installation du role : Manage > add roles > cocher dns
	-  mise en place : tools > 
		- forward lookup : clic droit > new zone > cocher primary > entrer zone name > next > finish
		- reverse lookup : new zone > primary > ipv4 > entrez addresse réseau > next > finish
		- ajouter un host : forward zone >clic droit > add host > nom serv, ip et cocher create pointer  > finish
		- ajouter un alias : forward zone >clic droit > add alias > nom alias, chemin via browse
	- tester via nslookup 

-  Setup dns SRV2 (secondaire)
	- installation du role : Manage > add roles > cocher dns
	- mise en place : tools > 
		- forward lookup : clic droit > new zone > cocher secondary > entrer zone name > entrer ip SRV1 > finish
		- Transfert de zone (**sur le SRV1**) :  forward zone >clic droit > add host > nom sSRV2, ipSRV2 et cocher create pointer  > finish. Ensuite forward zone > properties > name server > add > SRV2 , resolve > ok > apply 
		- tester transfer de zone (dans le cmd): nslookup IP_de_votre_serveur_principal >nslookup > ls –d votre_nom_de_zone
		- reverse lookup zone : new zone > secondary > ipv4 > adresse du reseau > ip SRV1 > next > finish ensuite properties > name server > add > SRV2 , resolve > ok >apply
	- Délégation de zone :  
		- new zone : forward zone > new zone > delegue.nom > next > finish
		- ajouter un host : forward zone >clic droit > add host > nom serv, ip et cocher create pointer  > finish
		- ajouter une délégation (**SUR SRV1**) > new delegation > delegue > SRV2, resolve
		- ajouter un alias : forward zone >clic droit > add alias > nom alias, chemin via browse (bien mettre pour le delegue.test.lan)
	- Test final ``nslookup www.delegue.test.lan`` 
- G²


___
## DHCP

- adressage ip 
	- ip fixe pour le SRVDHCP + DNS a lui même 
	- ip automatique pour client + dns automatique 
- configuration DHCP
	- installer le rôle DHCP > cocher DHCP > finish
	- ajouter un scope 
		- tools > DHCP > SRV1 > IPV4 > add scope > entrer la range d'ip > entrez la range d'exclusion  > entrez la durée de vie (en fonction du la demande minimum 4 h ) > no > finish
	- configuration des options étendues 
		- scope crée > scope option  > configure options > cocher router, ajouter une ip du range d'exclusion 
	-  Création d'une classe utilisateur 
		- IPV4 > define user classes > add > nom (description facultative), test 
		![[Pasted image 20231030161046.png]]
		- policies > new policies > nom >add > creteria : User class , operator : Equals , value : nom d'au dessus > ok > next  > no  >  cocher 003 router ajouter une ip du scope d'exclusion, 006 DNS server ajouter l'ip du serveur , 015 DNS domain name test   > finish 
- Configurer le client : 
	- ouvrir un cmd en admin et entrez les commande : 
		- ``netsh interface ipv4 show interfaces``
		- ``ipconfig /setclassid "nom de la carte réseau" "Identifiant"``
		- ``ipconfig/all``
		- 
____
## AD 





### AGDLP
methode de partage préconisé par google
