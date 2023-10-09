

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