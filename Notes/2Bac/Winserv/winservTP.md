

### Consignes
1) Nom
2) IP Fixe
3) Serveur et client doivent communiquer ensemble


Test123*


Mettre ip adress 192.168.1.1
Subnet mask 255.255.255.0
Pas de gateways pcq on ne veut pas se connecter hors du réseau local


en haut à droite du dashboard,

Creer nom de domaine Test.lan

forward lookup zone -> Test.len
Nom en ip   
Obligatoire :
Hote -> serv2019 -> 192.168.1.1
Optionnel :
Alias -> www -> Serv 2019 

reverse lookup zone -> 192.168.1.0
ip en nom
Obligatoire :
Ptr -> 192.168.1.1 -> Hote Serv2019

NSLookUP
-> Nom
-> IP

## TP2

Travail avec DNS secondaire (copie du DNS primaire)

FQDN du serveur = nom du serveur + nom de domaine

Delegation de zone dans le cas ou on a bcp de zones, le serveur primaire a toujours autorité sur la azone mais ne s'en occupe plus (serveur secondaire a les droits d'écriture)

## TP4 Oct 16

### DHCP 
DHCP 192.168.1.0/24
SCOPE 50
Soit 192.168.1.1->254
Soit 192.168.1.1->49  +20%

x3

Plage d'exclusion
Reservation d'une adresse IP par rapport à une adresse MAC

Le couillon qui met au dessus de F pour une adresse mac a zero
Si  adresse mac non précisée, on en met une au hasard

### BAIL
Le BAIL est par défaut à 8 jours lors de l'installation du serveur DHCP 
Chose à ne pas faire est de par exemple mettre 1h
Ne pas descendre en dessous de 4h

### CLASS UT

### OP ETENDUE

### AD-DS

On ne supprime jamais un compte pcq il y a une serie de choses liées au compte

-> on le désactive

### Manipulation DHCP

Dans une installation fraîche :

1) IP statique 192.168.0.1
2) Reboot
3) Dans "Manage" -> "Add roles" on selectionne "DHCP Server" -> "Add features"
4) Install
5) Reboot & snapshot
6) Cliquer sur le drapeau avec un point d'exclamation -> Complete DHCP configuration
7) 

### Manipulation AD-DS

1) Dans "Manage" -> "Add roles" on selectionne "Active Directory
Domain Services"
2) Install
3) Cliquer sur le drapeau avec un point d'exclamation -> "Promote this server to a domain controller"
4) "Add a new forest"
5) Ajouter un nom de domaine, par ex. "GHOST.lan"
6) 

8) DNS primaire = adresse du serveur
9) Installer le role AD-DS