# Sythèse de théorie de télécommunications et réseaux 🖧
## Chapitre 0 : Table des matières <a name="1"></a>

0. [Chapitre 0 : Table des matières](#1)
1. [Installation](#installation)
2. [Le PHP](#php)
3. [SQL](#sql)
4. [Exam Tips](#tips)

## Chapitre 1 : Introduction et généralités <a name="deux"></a>

### Rôles de l'administrateur

L'admin gère :
* Les besoins, budget et priorités
* Les ordinateurs et périphériques
* Les performances des systèmes
* Les utilisateurs
* Les fichiers et disques
* Les services
* Les problèmes
* Les sauvegardes et stockage des données
* Le réseau
* La sécurité

### Methodologie de l'administrateur

### Conversion de nombres dans d'autres bases

1) 10 en base 2    
  
      | 2^x | 2^10 | 2^9 | 2^8 | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
      | ---  | ---- | --- |---  | ---- | --- |---  | ---- | --- |---  | ---- | --- |
      | Base 10 | 1024 | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
  
    * Si le nombre à convertir est plus petit que la valeur du tableau, on note un zero sous la case
    * Si le nombre à convertir est plus grand que la valeur du tableau, on note un un, on soustrait la valeur au nombre à convertir et on continue le processus.
  
2) 2 en base 10
  
      | 2^x | 2^10 | 2^9 | 2^8 | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
      | ---  | ---- | --- |---  | ---- | --- |---  | ---- | --- |---  | ---- | --- |
      | Base 10 | 1024 | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
      | Base 2 |  |  |  |  |  |  |  |  |  |  |  |

    * On note le nombre en base 2 en partant de la droite, puis on additionne les nombres en base 10 qui sont face à un 1
      
4) 2 en base 8
5) 2 en base 16
6) 8 en base 2
7) 10 en base 8 ou 16

### Les réseaux 

>un réseau est un ensemble d'équipements et de logiciels qui permettent d'acheminer de l'information d'un émetteur jusqu'à un ou plusieurs récepteurs

Deux critères pour les catégoriser :
* Etendue du réseau
    * PAN (personal area network) ex : bluetooth
    * LAN (local area network)
    * MAN (metropolitan area network)
    * WAN (wide area network)
* Technologie du réseau     
    Topologie physique
    * Diffusion (support de transmission partagé par tous les équipements). On y retrouve BUS et ANNEAU.
        * Dans le cas ou le message est destiné à tous les équipements on a une diffusion générale (broadcast).

    * Point à point (un seul support de transmission reliant une paire d'équipements seulement). On y retrouve POINT A POINT, ETOILE, MAILLÉE
        * Le point à point entre un expediteur et un destinataire est une diffusion individuelle (unicast).

    En général la topologie représente la disposition physique des composants, mais il existe aussi la topologie logique qui est la manière dont les stations se partagent le support et dépend de la methode d'accès au réseau.

    On retrouve dans les topologies logiques :
    * Ethernet
        * Repose sur une topologie de type bus linéaire
        * protocole CSMA/CD (Carrier Sense Multiple Access
with Collision Detection)
    * Token ring
        * Seul le poste ayant le jeton peut transmettre sur le réseau
        * Si un poste veut émettre, il doit attendre jusqu'à ce qu'il ait le jeton
        * Topologie en anneau
    * FDDI (fiber distributed data interface)
        * Fibre optique
        * Anneaux primaire et secondaire (pour rattrapage d'erreurs)

### Modes de fonctionnement 

> Tous les ordinateurs connectés à un réseau et qui participent directement aux communications
réseau s’appellent des hôtes ou des périphériques finaux


## Chapitre 2 : Communication et protocoles réseaux

### Protocoles

>Un protocole est une suite de règles qui visent à ce qu'un message soit correctement transmis et compris

### Codage d'un message 

Un message est d'abord codé en bits puis converti en en impulsions électriques ou ondes lumineuses

### Encapsulation 

## Chapitre 3 : Accès réseau

## Chapitre 4 : Ethernet

### Ethernet

Technologie #1 dans le monde

## Chapitre 5 : Système d'exploitation réseau


## Chapitre 6 : Couche réseau


## Chapitre 7 : Couche transport


## Chapitre 8 : Adressage IP


## Chapitre 9 : Découpage réseau


## Chapitre 10 : Couche Application

