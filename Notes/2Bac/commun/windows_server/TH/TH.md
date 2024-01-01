# Notes de Windows Server (bonne merde en tt cas)

## 

On met toujours une adresse IP fixe à un serveur

Différence entre adresse IPv4 et IPv6
* IPv4 -> en décimal
* IPv6 -> en hexadécimal

Unicast = Envoyer de personne à personne en IPv4 ou IPv6

Broadcast = Envoyer de personne à tout le monde en IPv4

Anycast = Envoi à un groupe et celui qui recoit et celui qui est le plus proche

IPv4
* Net_id de longueur variable
* Host_id de longueur variable

IPv6
* 64 premiers bits : le préfixe
* 64 derniers bits : Identifiant de l’interface

Adresse 127.000.1 sert à tester la carte réseau 

Les adresses privées sont aussi appelées non routable car non routable sur internet

Pq microsoft a fait plusieurs versions séparées

Dans les anciennes versions avant 2008, il y avait des failles de securité sur le serveur windows car de base quand on installe le windows serveur tout est installé (le DNS, le dhcp, l'ad, ...) donc si on voulait juste le coté dns on utilisait la parite DNS mais le reste était qd même installé et l'administrateur ne mettait pas à jour le reste comme il ne l'utilisait pas et donc créait des failles de sécurité car le hackeur pouvait rentrer par là.

Donc maintenant on choisit d'installer juste ce qui est nécessaire.

Niveau licence on a trois licences, une client, une serveur, et une pour la com entre les 2

La CAL c'est sur le serveur la possibilité de se connecter au client et le client au serveur. Quand un serveur web, pas besoin de CAL.

Il existe le serveur WDS qui installe automatiquement le client dans ces entreprise.
Avantage : permet à l'administrateur reseaude configurer correctement comment il veut installer son systeme d'exploitation, c'est rapide, il peut faire un déploinment de masse, automatisation et peut faire des récup

Pourquoi en mode core (=sans GUI) pour mettre l'heure on arrive sur une interface graphique pour l'authentification car quand on va se connecter, le jeton de connexion va se connecter sur le serveur va lancer une authentification et quand il  la lance il a un certain temps et le jeton est horodaté et a une durée de vie très courte.

Chaque serveur a une adresse IP fixe.

Renommer l'ordi est la première chose à faire car important pour c'est plus facile de savoir identifier le serveur 

Active directory 

## Bonnes pratiques (Halal windows server)

* Nommer le serveur convenablement.
* Ajouter une adresse IP fixe.
* Config la time zone

## Server manager

* Gestion de l’ensemble du serveur.
* Ajout & suppression de rôles et de fonctionnalités.
* Gestion des PC distants

## Roles et fonctionnalités 

* Rôle :
    > Ensemble de programmes logiciels qui, une fois
installés et correctement configurés, permettent à un ordinateur de <ins>remplir une
fonction spécifique</ins> pour plusieurs utilisateurs ou pour d’autres ordinateurs sur un
réseau.

* Service de rôle (sous-ensemble d’un rôle)
    > Programmes logiciels qui fournissent la fonctionnalité
d’un rôle.
    * Avantage : diminution de la surface d'attaque

* Fonctionnalité :
    > programmes logiciel qui, bien
que ne faisant pas directement partie des rôle, peut prendre en charge ou
augmenter la <ins>fonctionnalité</ins> d’un ou de plusieurs rôles, ou encore améliorer la
fonctionnalité de la totalité du serveur, quels que soient les rôles installés

## Serveur DNS

* DNS :
> Domain Name System

* Whois :
> C'est un protocole utilisé pour interroger une base de
données en ligne afin d'obtenir des informations sur
les noms de domaine, les adresses IP, ...


L'acronyme Whois signifie "Who is responsible for this
domain ?" ICANN (Internet Corporation for Assigned
Names and Numbers) gère les adresses IP et les noms
de domaines de premier niveau (TLD). L’IANA (Internet
Assigned Numbers Authority) est une composante de
l’ICANN qui gère les noms de domaine, les adresses IP,
n° de protocole.

Le protocole Whois permet de rechercher des
informations sur un nom de domaine ou une adresse IP
spécifique, telles que le titulaire du domaine, les
coordonnées de contact, les serveurs de noms
associés, et d'autres données techniques.

### De quoi est composé un DNS ?

* Un espace de noms (Domain Namespace) qui contient
des RR (Ressources Records).
* Un serveur de noms DNS.
* Des clients DNS - DNS Resolvers (DNR).

### Sur quoi est basé le DNS ?
Le DNS est basé sur la demande de résolution de
noms (lookup queries). Il peut mettre en cache les
requêtes réussies ou échouées.

### Quelles sont les entités pour le DNS ?
* L'ICANN (Internet Corporation for Assigned Names and
Numbers) gère les adresses IP et les noms de domaines de
premier niveau (TLD).
* L'IANA qui est une composante de l'ICANN gère les noms
de domaine, les adresses IP et les N° de protocole.

## Réseau 

Serveur DNS
◦ Qu'est-ce qu'un espace de nom DNS ? (Partie 1)
◦ Définition :
◦ Toute zone délimitée dans laquelle un nom peut être résolu.
◦ FQDN (Fully Qualified Domain Name) :
◦ Nom de domaine qui est écrit de manière à fournir l’emplacement précis d’une ressource sur Internet.
C’est une séquence de labels de domaine où chaque label est séparé par un point. Le FQDN commence
par le domaine de plus haut niveau (TLD – Top-Level Domain) à droite, en allant vers le domaine de niveau
le plus bas à gauche.
◦ Exemple : www.exemple.com
◦ « com » est le TLD.
◦ « exemple » est le domaine de second niveau.
◦ « www » est un sous-domaine.

## Serveur DHCP

## Active Directory

