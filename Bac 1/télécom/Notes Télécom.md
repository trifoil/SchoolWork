## Ex 1(slide6):

réseau : 10.192.224.0/19

##### Par service :
- 505 employés 10.192.224.0/23 car 2^9= 512
	- Adresse réseau suivant : 20.192.226.0
- 28 personnes vente : 10.192.226.0/27
	- adresse réseau suivant  20.192.224.32
- 17 personnes marketing :10.192.226.32/27
	- adresse réseau suivant : 10.192.226.64
- 8 personnes direction : 10.192.226.64/28
	- adresse réseau suivant : 10.192.226.80 
- 6 personnes réception : 10.192.226.80/29
	- adresse réseau suivant : 10.192.226.88
- 6 personnes finciers : 10.192.226.88/29
	-  adresse réseau suivant : 10.192.226.96
- 5 personnes ressources humaines : 10.192.226.96/29
	- adresse réseau suivant : 10.192.226.104
- 2 personnes informatique : 10.192.226.104/30
	- adresse réseau suivant : 10.192.226.108

##### Par étage : 
- 1er étage 513 personnes : 10.192.224.0/22
	- Adresse réseau suivant : 10.192.228.0
- 2ieme étage 45 personnes : 10.192.228.0/26
	- Adresse réseau suivant :10.192.228.64
- 3ieme étage 11 personnes 10.192.228.64/28
	- Adresse réseau suivant : 10.192.228.80
- 4ieme étage 8 personnes : 10.192.228.80/28
	- Adresse réseau suivante : 10.192.228.96
-----
![[Pasted image 20230421110415.png]]
**Réponse** : transfère le packet, le router va analyser ligne par ligne, 1er adresse est bien dans le réseau donc suis la ligne et transfère via le port 
![[Pasted image 20230421111009.png]]
**Réponse**: abandon du packet car connais pas réseaux et pas de route par défault 
*autres explications* : ![[Pasted image 20230421111144.png]]


---
