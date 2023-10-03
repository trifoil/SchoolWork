- slide 14 importante 

- slide 19-27 chaque fois avancer vers le sommet(ovale) le plus petit (somme des précédent) et mettre jour pour le prochain a chaque fois jusqu'a la fin pour avoir le plus petit poids (somme des trajets)
- slide 28 
- slide 29 
- ex 1![[Pasted image 20230302110910.png]]
- ex 2 ![[Pasted image 20230302110920.png]]
- ex3![[Pasted image 20230302110930.png]]
- ex 4 ( a insérer )

# examen !
Algo de Djikstra et Krustal  

ex voir excel ! 






### Cours 9/03

Compression des données : 
Processus permettant de réduire la taille des données pour économiser de l’espace de stockage et améliorer les performances de transmission

Méthodes : 
- **compression sans pertes** :
	- Aucune perte des données d’origine, réécriture de façon concise. Pas de solution universelle
- **compression avec perte** : 
	- Utilisée pour les données sonores ou visuelles où la perte d’informations est imperceptible pour l’œil humain
- Possibilités de décompresser les données pour revenir à l’origine
- exemples : 
	- Compression de fichiers textes
	- Compression d’archives
	- Compression de fichiers de configuration
- Basé sur la redondance, l’entropie
- Implémenté de manière statique ou sur base d’un dictionnaire
- Quelques algorithmes :
	- Lempel-Ziv-Welch (LZW)
	- Huffman 
	- Run Legnth Encoding (RLE)

### LZW
- Très souvent utilisé avec les .GIF, les .PDF et les .TIFF
- Regroupement de symboles en chaînes
- Convertir chaînes en codes
- Codes moins de places que les chaînes
- Choix fréquents d’entrée possibles : 4096
- 0 à 255 bloqués pour les caractères uniques du fichier d’entrée
- Identification des séquences répétées dans les données et ajout à la table de codage


### Codage de Huffman statique :
- Attribution de code en fonction de la fréquence d’apparition
	- Les symboles avec une basse fréquence sont codés sur beaucoup de bits et inversement pour les symboles à haute fréquence
- Génération d’un arbre binaire avec les branches étiquetées de 0 et de 1
- L’arbre et le message compressé doivent être envoyé pour pouvoir être décodé



### exercices : 
![[Pasted image 20230309093235.png]]
-  101000101110100001000010011
	- eetenstets-erreur !!
- 001001101111000
	- telnet
- 0010010000
	- test
- 00100
	- te-erreur
![[Pasted image 20230309094056.png]] 
- 010 00 110 00 10 010
- 111 0111 00 10 010


Arbre  d'huffman 

E : 102
A : 64
C : 35
G :12
S : 48
T : 35 
H : 9

---
cours 27/04

![[Pasted image 20230427085257.png]]
truc noir :Enigma machine de chiffrement utilisée durant la guerre 
baton : baton de chiffrement ou on  ecrivait un message le long du fill       enroulé sur le baton et fallait le même baton pour lire 
roulette : cesar décalage des lettres 

---
### méthodes

- #### Substitution 
	- cesar
	
- #### Transposition

- #### Par bloc 
	- DES, AES

- #### Par flux 
	- RC4

---
### différents algo :
- Vigenère : on prends 2 mots on répète le 2 ieme pour qu'il fasse la taille du premier ensuite on prends les intersections des 2 lettres 
- Playfair : ![[Pasted image 20230427090853.png]]
	prends l'opposé on croise si en ligne on prends le premier a droite si en collonne prends le premier en bas (ex : st donne tl et lu donne um)
---
## Algorithmes 
-  DES (Data Encryption Standard)
	![[Pasted image 20230427092702.png]]
	détail : 
	![[Pasted image 20230427092720.png]]
	rentre le message découpé --> fais une permuttation et découpe en 2 partie --> 16 tours dans le chiffrement suivant un clé la meme des 2 cotés --> regroupe les 2 cotés et repermute -->sortie 

- 3 DES  = 3 fois le DES 

- AES pas rentenir  

----
## Chiffrement asymétrique 

### Algorithmes 
- RSA 
	- basé sur la difficulté de factoriser de grands nombres entiers en facteur premier
	- Définition RSA ![[Pasted image 20230511083600.png]]
	 - pour générer une clé RSA ![[Pasted image 20230511083636.png]]
	 -  Pourquoi compliqué a casser ? ![[Pasted image 20230511084314.png]]
	 - attaques possibles : 
		 - Brute force sur p & q
		 - Attaque de Wiener
		 - Attaque de Hastad
		 - Time attack
		 - Adaptative chose cyphertext attack	   
- Chiffrement El Gamal
- Chiffrement de Merkle-Hellman

### RegEx 
- Une expression régulière est une chaîne de caractères qui décrit un ensemble de chaînes de caractères.
- exemple : 
	- Vérifier si c'est une adresse mail ![[Pasted image 20230511090103.png]]
 - syntaxe : 
	 - ![[Pasted image 20230511085543.png]]
	 - Les caractères littéraux
	 - Les classes de caractères
	 - Les quantificateurs
	 - Les métacaractères
	 - Les goupes de capture 
- Ressources 
	- Regex101.com
	- Regexr.com
	- Rexegg.com



