# Commandes liées aux switches Cisco

## Informations

![Image du switch](image/switch_commands/1698421610122.png)

> Un switch (commutateur) est un équipement réseau.

## Commandes en fonction du mode

### Utilisateur standard

### Utilisateur privilégié

### Configuration globale

### Configuration d'une adresse IP pour le switch

Pour passer en mode de configuration de l'adresse IP du switch :
```
(config)# interface vlan 1
```

Pour attribuer une adresse IP et son masque de sous-réseau au switch :
```
(config-if)# ip address {addr} {submask}
```

Pour activer l'interface sans redémarrage :
```
no shutdown
```

### Peu importe le mode

Pour afficher la liste des interfaces du switch avec des informations associées :
```
show ip interface brief
```