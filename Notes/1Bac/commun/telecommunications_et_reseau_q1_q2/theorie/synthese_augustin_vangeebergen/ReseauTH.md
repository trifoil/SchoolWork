# Sythèse de théorie de télécommunications et réseaux 🖧
## Chapitre 0 : Table des matières <a name="0"></a>

0. [Chapitre 0 : Table des matières](#0)
1. [Introduction et généralités](#1)
2. [Communication et protocoles réseaux](#2)
3. [Accès réseau](#3)
4. [Ethernet](#4)
5. [Système d'exploitation de réseau](#5)
5. [Couche réseau](#6)
5. [Couche transport](#7)
5. [Adressage IP](#8)
5. [Découpage réseau](#9)
5. [La couche application](#10)

## Chapitre 1 : Introduction et généralités <a name="1"></a>

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


## Chapitre 2 : Communication et protocoles réseaux <a name="2"></a>

### Protocoles

>Un protocole est une suite de règles qui visent à ce qu'un message soit correctement transmis et compris.

Organisé en couches

### Codage d'un message 

>Un codage est le processus de conversion des informations vers un autre format acceptable, à des fins de transmission.

Un message est :
1) Codé en bits 
2) Converti en en impulsions électriques / ondes lumineuses

### Encapsulation / désencapsulation

>L'encapsulation est un processus permettant d'encapsuler un message dans une trame.

La trame contient :
* L'adresse source
* L'adresse de destination
* Les données encapsulées

<img src="assets/Diagrammes/Pasted image.png" alt="drawing" width="800"/>

Désencapsuler c'est extraire ces données.

### Taille

Si le message est grand, on le découpe en plusieurs trames.

### Synchronisation

* Methode d'accès
  >moment où un individu peut envoyer un message.

* Contrôle de flux
  >négocier une synchronisation correcte en vue d'établir une communication.

* Délai d'attente de la réponse
  >Les hôtes du réseau sont également soumis à des règles qui spécifient le délai d'attente des réponses et l'action à entreprendre en cas de dépassement du délai d'attente.

Options de remise des messages

* Monodiffusion
  * un émetteur, un récepteur
* Diffusion
  * un émetteur à tous les récepteurs
* Multidiffusion
  * un émetteur à un groupe de récepteurs

### Acronymes

<ins>Couche application</ins>

* DNS (Domain Name System)  
  * Nom de domaine -> Adresse IP
* DHCP (Dynamic Host Configuration Protocol)    
  * Attribution dynamique d'addresses IP aux stations clientes au démarrage
* SMTP (Simple Mail Transfer Protocol)  
  Permet aux terminaux d’envoyer un mail à un serveur de messagerie
* POP (Post Office Protocol)  
  * Permet aux clients de récupérer ou de télécharger des emails d’un serveur de messagerie
* IMAP (Internet Message Access Protocol)   
  * Permet aux clients d’accéder aux emails stockés sur un serveur de messagerie
* FTP (File Transfert Protocol) 
  * Permet à un hôte d’accéder à des fichiers sur un autre hôte du réseau
  * Transférer des fichiers vers un autre hôte du réseau
* TFTP (Trivial File Transfert Protocol)
  * Version simplifiée de FTP, pas d’authentification
* HTTP (HyperText Transfert Protocol)   
  * Permet d’échanger du texte ou des fichiers multimédia sur le web

<ins>Couche transport</ins>
   
* UDP (User Datagram Protocol)
  * Permet à un processus exécuté sur un hôte d’envoyer des paquets à un processus exécuté sur un autre hôte
  * Sans connexion  au préalable 
  * Sans confirmation de la transmission de datagrammes
* TCP (Transmission Control Protocol)
  * Au contraire d’UDP, permet une connexion fiable entre les processus s’exécutant sur des hôtes distincts

<ins>Couche internet</ins>

* IP (Internet Protocol)
  * Permet de recevoir des segments de message de la couche transport. 
  * Il regroupe les messages en paquets et indique leur adresse pour permettre leur acheminement de bout en bout sur un interréseau
* NAT (Network Address Translation)
  * Permet de convertir les adresses IP d’un réseau privé en adresses IP globales et publiques
* ICMP (Internet Control Message Protocol)
  * Permet à l’hôte de destination de signaler à l’hôte source des erreurs liées aux transmissions de paquets
* OSPF (Open Shortest Path First)
  * Protocole de routage à états de liens permettant de faire du routage dynamique
* EIGRP (Enhanced Interior Gateway Routing Protocol)
  * Protocole de routage dynamique propriétaire de Cisco

<ins>Protocoles de la couche réseau</ins>

* ARP (Address Resolution Protocol)
  * Fournit un mappage dynamique entre une adresse logique (IP) et une adresse physique (MAC)
* PPP (Point to Point Protocol)
  * Permet d’encapsuler des paquets pour les transmettre via une connexion en série

### Modèles de référence 

Le modèle OSI est un modèle en 7 couches :

* 2 couches basses : dédiées à l’infrastructure des réseaux
* 2 couches moyennes : servant au contrôle du transport de l’information
* 3 couches hautes : liées à la gestion de l’application

<img src="assets/Diagrammes/Pasted image 3.png" alt="drawing" width="800"/>

>PDU = Protocol Data Unit (ou unités de données)

## Chapitre 3 : Accès réseau <a name="3"></a>



## Chapitre 4 : Ethernet <a name="4"></a>

### Ethernet

* Au niveau de la couche liaison de donnée et couche physique
* Norme IEE 802.2 / 802.3 
* 10 Mb/s -> 10 Gb/s

### Couche liaison de donnée

* Sous-couche LLC Ethernet

    Gère la communication entre les couches supérieures et inférieures.
* Sous-couche MAC Ethernet

    Elle encapsule les données et contrôle l'accès au support

### Adresse MAC

## Chapitre 5 : Système d'exploitation réseau <a name="5"></a>



## Chapitre 6 : Couche réseau (OSI3) <a name="6"></a>

### La couche réseau

> Elle fournit des services permettant aux périphériques finaux d'échanger des données sur le réseau.

Elle compte 4 processus de base :

1) Adressage
    * Identification de manière unique du périphérique présent sur le réseau, pour acheminer les données via IPv4 ou IPv6

2) Encapsulation
    * La couche 3 recoit l'unité de données de protocole (segment/datagramme) de la couche 4
    * Ajout d'une en-tête de de couche 3
    * l'unité de données de protocole de la couche 3 est un paquet

3) Routage
    * Les paquets doivent circuler à travers des periphériques intermédiaires
    * Periphériques intermédiaires = "routeurs"
    * Chemin emprunté par un paquet entre deux périphériques consécutifs = "un saut"

4) Désencapsulation
    * Valable si le paquet a atteint le périphérique cible
    * Desencapsulation
    * Transmission de l'unité de donnée de protocole à la couche 4 Transport

### Caractéristiques du protocole IP 

Il a été conçu pour ne pas surcharger les réseaux. Il fournit uniquement les fonctions requises pour transférer un paquet d’une source à une destination en passant par un système interconnecté de réseaux.

* Aucune connexion n'est établie avant l'envoi de paquets de données
* Acheminement non fiable: aucune surchage n'est utilisée pour garantir la transmission des paquets
* Indépendant du support: fonctionne indépendamment du support transportant les
données
* Il est qualifié de protocole "non fiable" car il ne sait pas gérer les paquets
endommagés ou non remis
* Il n'y a pas de champs requis pour la transmission fiable dans l'en-tête d'un
paquet IP mais cela offre moins de surcharge
* On ne sait donc pas si le destinataire est sur le réseau, si le paquet est bien arrivé
à destination et si le destinataire peut lire le paquet
* Le destinataire ne sait pas quand le paquet arrive

:warning: La taille maximale d'unité de données de protocole que chaque support peut
transporter est déterminé au niveau de la couche de liaison
de données et est transmise à la couche réseau. Donc la taille de création des
paquets est déterminée.

### IPv4

Un paquet IPv4 comporte deux parties
1) En-tête IP -> indique les caractéristiques du paquet
2) Données utiles -> contient les info. du segment de couche 4 et les données en elles-mêmes

> "Time To Live" = valeur pour limiter la durée de vie d'un paquet. Elle est indiquée en secondes mais généralement appelée "nombre de
sauts". Si cette valeur est dépassée, le routeur rejette le paquet et envoie un message de dépassement de délai ICMP à la source.

### IPv6

Les problèmes de l'IPv4 ont conduit au développement de l'IPv6
Espace d'adressage plus important (beaucoup beaucoup + d'adresses IP,
environs 67 milliards par cm^2 de surface terrestre, ui c bcp)
* Traitement des paquets plus efficace => l'en-tête IPv6 a été simplifiée et comporte moins de champs
* Traduction d'adresses réseau non nécessaire => comme y'a beaucoup d'IP, plus besoin de NAT
* Sécurité intégrée => prend en charge les fonctions d'authentification et de confidentialité (pas comme l'IPv4)

### Routeur

Equipement intermédiaire opérant au niveau de la couche 3 du modèle OSI, il envoie
et recevoir des paquets IP qui lui sont destinés
Chaque interface du routeur est un membre ou un hôté d'un réseau IP différent
/!\ Deux interfaces actives ne peuvent pas appartenir au même réseau
Ils nécessitent:
* Un OS
* Un processeur 
* De la mémoire vive => contient l'IOS, fichier de config « running-config », table de
routage IP, Cache ARP, Mémoire tampon
/ !\ Mémoire volatile, perd son contenu lors mise hors tension.
* De la mémoire morte => instructions de démarrage, le POST (Power On Self
Test, pour savoir si tout va bien), une version limitée (de merde) de l'IOS


La mémoire vive non volatile est utilisé par IOS comme stockage permanent pour le
fichier startup-config
La mémoire Flash est une mémoire non volative utilisée comme stockage permanent
pour l'IOS et d'autres fichier associés au système, il y est copié de la mémoire
Flash vers la mémoire vive lors du démarrage

![Alt text](image-2.png)

Etapes lors du démarrage:
● Exécution du POST et chargement du bootstrap (ROM)
● Localisation et chargement de l'IOS (Flash ou TFTP)
● Localisation et chargemetn du fichier de config initiale (NVRAM, TFTP ou Console)

![Alt text](image-3.png)

### Connexion et interfaces d'un routeur
Les connexions sur un routeur Cisco peuvent être regroupées en deux catégories:
● Ports de gestion: ports console et aux utilisés pour configurer, gérer et dépanner
le routeur (pas de transfert de paquets)
● Interfaces de routeur: configurée via l'adressage IP pour transporter le trafic.
On peut y accéder avec le port console, telnet ou ssh, le port AUX (comme le
switch)
### Le routage
Le rôle principal du routeur c'est d'effectuer la fonction de routage, c'est à dire de diriger les paquets entre les hôtes
Un hôte peut envoyer un paquet à:
* Lui (via 127.0.0.1 qui est une interface de bouclage, à des fins de test)
* Un hôte local
* Un hôte distant => le routeur sera une "passerelle par défaut"
La passerelle par défaut, dans un réseau domestique, est souvent utilisée pour connecter un réseau local à internet.
### La table de routage
Fichier de donnée stocké dans la mémoire vive qui contient des informations de route sur le réseau connecté ainsi que les entrées de réseaux distants que le périphérique a découvertes. Le routeur utilise ces infos pour trouver le meilleur chemin.  

Les routes possèdent trois caractéristiques principales:
* Le réseau de destination
* Le tronçon suivant ou la passerelle permettant d'atteindre le réseau de
destination
* La métrique associée au réseau de destination

Fonctionnement
1) Le routeur lit l'adresse de destination dans l'en-tête IP et regarde dans sa table de routage s'il connait une route à cette adresse
2) Il transfère le paquet au prochain routeur en fonction du tronçon suivant spécifié par cette route.

Un routeur peut être configuré pour posséder une route par défaut. Il s'agit d'une
route qui correspond à tous les réseaux de destination.
Dans les réseaux IPv4 l'adresse 0.0.0.0 avec le masque 0.0.0.0 est utilisée à cet
effet. La route par défaut est utilisée pour transférer
Les paquets pour lesquels aucune entrée ne figure dans la table de routage pour le
réseau de destination.

Fonctionnement route statique

![Alt text](image-4.png)

Quand un routeur reçoit des info. sur des nouvelles routes ou des routes modifiées, il
met à jour sa propre table de routage et transmet ces infos aux autres routeurs.


C'est donc du routage dynamique et l'inconvénient est que l'échange d'info. afin
d'avoir les routes correctement à jour impose une surcharge de la bande passante.
Les protocoles de routage sont:
● RIP (Routing Information Protocol)
Chaque route est associée à une métrique (nombre de sauts limité à 15)
Chaque routeur envoie à ses voisins ses info. de routage (toutes les 30 sec)
Il va calculer les meilleures routes et déduire sa table de routage selon la métrique
calculée
EIGRP (Enhanced Interior Gateway Routing Protocol)
Calcule les métriques sur base d'une formule composée du délai, de la bande
passante, de la fiabilité et de la charge.
Au niveau du réseau, chaque routeur envoie un paquet "Hello" à ses voisins toutes
les 5sec afin de dire qu'il est actif et que ses routes sont correctes.
Au niveau de l'échange d'info. Une mise à jour concernant une table de routage n'est
envoyée que lorsque celle-ci est modifiée. Cette màj contiendra que les
routes modifiées et sera envoyée qu'aux routeurs concernés
●
30OSPF (Open Shortest Path First)
Permet d'avoir des routes de plus de 15 sauts
Utilise une métrique plus compliquée (prenant compte des débits)
Améliore le temps de convergence. (Temps nécessaire aux routeurs pour recalculer
les nouvelles routes suites à un changement dans le résau)

## Chapitre 7 : Couche transport <a name="7"></a>

Chapitre 7: Couche transport
Introduction
La couche transport est chargée de l'établissement d'une session de communication
temporaire entre deux applications et de l'acheminement des données entre elles.
La plupart de ses protocoles ont des fonctions essentielles communes:
* Segmentation et reconstitution => diviser un bloc de données en des sous-blocs
plus petit et va les reconstituer à la réception
* Multiplexage de conversions => à l'aide du port de l'application ou du service, la
couche transport va déterminer à qui les données se rapportent
Dans le cadre du TCP/IP la segmentation et la réorganisation peuvent être fait à
l'aide des protocoles TCP et UDP
Objectifs de la couche transport
Effectuer un suivi des communications individuelles entre les applications résidant
sur les hôtes source et de destination
* Segmenter les données et gérer chaque bloc individuel
* Réassembler les segments en flux de données d'application
* Identifier les différentes applications en leur affectant un numéro de port

### Fiabilité de la couche transport
Elle est basée sur 3 opérations de base:
● Effectuer le suivi des données transmises
● Accuser la réception des données
● Retransmettre toute donnée n'ayant pas fait l'objet d'un accusé de réception
### Les protocoles TCP et UDP
TCP (Transmission Control Protocol)
Protocole de couche transport fiable et complet, qui garantit que toutes les données
arrivent à destination.
Il segmente un message en partie numérotées à une destination, si il ne reçoit pas
d'accusé de réception, il renvoie tout en supposant que ça a été perdu.
é
En-tête TCP = 20 octets
31UDP (User Datagram Protocol)
Protocole de couche transport très simple qui ne permet pas de garantir la fiabilité
Il fournit des fonction de base permettant d'acheminer des segments entre les
applications appropriées avec peu de surcharge.
En-tête UDP = 8 octets
Donc TCP > UDP
### Les numéros de port classé par l'IANA
* Ports réservés (0 à 1023)   
  Ils sont réservés à des services ou applications
* Ports inscrits (1024 à 49151)   
  Affecté à des processus ou applications d'utilisateurs
* Ports privés ou dynamiques (49152 à 65535)    
  Appelés port éphémères, affectés de façon dynamique à des applications clientes lors d'une connexion

![Alt text](image-5.png)

L’ensemble formé par le numéro de port et l’adresse ip s’appelle un SOCKET.
### Etablissement d'une connexion TCP
1) Le client demande l'établissement d'une session client-serveur avec le serveur
Envoi d'une demande de synchronisation avec numéro de séquence
SYN avec un numéro de séquence (SEQ. Ex 100).
Champs de contrôle = SYN
2) Le serveur accuse réception de la session et demande l'établissement d'une
session serveur-client
Réponse du serveur avec ACK égal au numéro d'ordre reçu +1 (ex : 101) et son
numéro d'ordre de synchronisation (ex SEQ 300)
CTL = SYN
3) Le client accuse réception de la session serveur-client
Connexion établie, le client répond avec un ACK égal au numéro d'ordre reçu + 1.
SEQ = 101 ACK 301 CTL = ACK

![Alt text](image-6.png)

### Fermeture d'une connexion TCP
1) Le client n'a plus rien à envoyer, il envoie un segment pour demander la fin de la
connexion (FIN)
2) Le serveur envoie un ACK disant qu'il a bien reçu le segment FIN, afin de fermer
la session client-serveur
3) Le serveur envoie un segment FIN au client pour mettre fin à la session serveur-
client
4) Le client envoie un ACK pour dire qu'il a bien reçu le segment FIN


### Fiabilité de la connexion

![Alt text](image-8.png)

### La taille de fenêtre

La quantité de données qu'une source peut transmettre avant qu'un accusé de
réception soit reçu est la "taille de fenêtre"
Cette taille est définie lors du démarrage de la session
Le procotole TCP peut réduire la taille de la fenêtre afin de mieux contrôler le flux de
données (envoie d'ACK plus fréquent, évite les pertes)

![Alt text](image-9.png)

### Gestion des pertes de segments du TCP
Quand le protocole TCP source envoie des segments de données, il va : 
* placer une copie du segment dans une file d'attente de retransmission
* va déclencher en même temps un timer
* Si il ne reçoit pas d'ACK avant la fin du timer, il va retransmettre à partir du dernier numéro d'accusé de réception.

Il existe également des SACK (ACK sélectifs) permettant, si les 2 hôtes sont
compatibles, une retransmission partielle des octets manquants.

![Alt text](image-10.png)

### Protocole de la couche application utilisant UDP

UDP c'est quand même pas de la merde, c'est utile pour certains protocoles
* DNS
* DHCP
* TFTP
* RIP
* VoIP

Il n'y a pas de numéro d'ordre dans le protocole UDP, donc il ne sait pas réordonner
les datagrammes => Il les réassemble dans l'ordre qu'il les a reçu

## Chapitre 8 : Adressage IP <a name="8"></a>

### Adressage IPv4

Une IP est le numéro qui identifie chaque ordinateur connecté à Internet, ou plus précisément, l'interface avec le réseau de tout matériel informatique connecte à Internet.

Elle a un format de 4 octets (32 bits) présentable en binaire ou en décimal

Elle contient deux parties:
* ID de réseau  
Adresse réseau logique du sous réseau auquel l'ordinateur se rattache
* ID d'hôte   
Adresse logique du périphérique logique identifiant chaque ordinateur sur un sous réseau

### Les ≠ classes d'adresses

A: 8 bits partie réseau, 24 partie hôte 
B: 16 bits réseau, 16 bits hôtes  
C: 24 bits réseau, 8 hôtes  
D: Réservées pour le multicast, TOUJOURS UNE ADRESSE DE DESTINATION   
E: Réservées à la recherche ou à des usages futurs  

Les adresses du bloc 168.254.0.0/16 sont des adresses link-local (c'est du réseau local APIPA)

Les adresses TEST-NET du bloc 192.0.2.0/24 sont réservées à des fins
pédagogiques

Les adresses expérimentales du bloc 240.0.0.0 à 255.255.255.254 sont réservées pour une utilisation future

### Solution pour palier aux problèmes de l'IPv4

Le CIDR (Classless Inter-Domain Routing)

Permet une diffusion plus efficace de l'espace d'adressage IPv4 et retarde la croissance des tables de routages donc la pénurie d'adresses
Utilisation du NAT
Permet à un ensemble d'hôtes présents sur un réseau local, d'avoir accès à internet en utilisant une adresse IP unique => retarde la pénurie d'adresses
Technique calcul IP réseau/diffusion/hôtes

### Coexistence IPv4 et IPv6

Techniques de migration vers l'IPv6
* Double pile   
Permet à l'IPv4 et à l'IPv6 de coexister sur le même réseau. Les périphériques exécutent les piles de protocoles IPv4 et v6 simultanément

* Tunneling   
Méthode de transport des paquets IPv6 via un réseau IPv4. Les paquets I Pv6 sont
encapsulés dans les paquets IPv4

* Traduction    
Un paquet IPv6 est traduit en paquet IPv4 et inversement

### Adressage IPv6

Une adresse IPv6 est longue de 128 bits (16 octets)
La notation décimale a été abandonée au profit d'une notation hexa
décimale où les 8 groupes de deux octets sont séparés par un signe ":"
Règles
● On peut supprimer les 0 de gauche: 01AB devient 1AB et 00CD devient CD mais
/!\ 0000 devient 0 !
● Une (ou plusieurs) suite de groupe de quatre 0 peut être compressée en "::" (une
seule fois)
ex: 2001:DB8:0:1111::200 => 2001:0DB8:0000:1111:0000:0000:0000:0200
La longueur de préfixe est utilisée pour indiquer la partie réseau d'une adresse IPv6,
elle peut aller de 0 à 128
Si elle vaut 64, il y a 64 bits réseau et 64 bits hôtes
Adresse anycast
Adresse de monodiffusion IPv6 qui peut être attribuée à plusieurs périphériques
Le périphérique le plus proche reçoit le paquet
Il n'y a pas d'adresse de diffusion en IPv6 mais on peut faire un multi-diffusion à tout
les noeuds dont ça revient au même
Adresse de monodiffusion
Il existe 6 types mais voici les plus importants:
●
Adresse de monodiffusion globale: idem que IPv4, un hôte à un destinataire
Adresse link-local: utilisées pour communiquer avec d'autres périphériques sur la
même liaison locale, uniquement utilisable en local plage FE80 ::/10

## Chapitre 9 : Découpage réseau <a name="9"></a>


## Chapitre 10 : Couche Application <a name="10"></a>

![Alt text](image-7.png)