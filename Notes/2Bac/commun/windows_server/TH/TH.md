# Notes de Windows Server (bonne merde en tt cas)

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

## Bonnes pratiques (halal windows server)

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