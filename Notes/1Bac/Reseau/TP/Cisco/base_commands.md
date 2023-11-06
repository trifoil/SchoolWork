# Commandes de base de Cisco IOS

## Principes de la console IOS

### La console

```
nom_du_periph>
```

- `nom_du_periph` : c'est le nom d'hôte du périphérique.
- `>` : c'est le mode de configuration.

### L'aide.

- `?` : Affiche la liste des commandes du mode de configuration actuel avec de brèves descriptions.
- `debut_command?` : Affiche les commandes commençant par le texte avant le ?.
- `command ?` : Fournit de l'aide sur ce qui devrait être saisi à cet endroit.

> Le signe "?" fonctionne dans n'importe quel mode de configuration.

## Modes de configurations

Differents mode de configurations:

- `>` : Utilisateur standard
- `#` : Utilisateur privilégié
- `(config)#` : configuration globale
- `(config-int)#` : configuration d'une interface

> Dans 99 % des cas, les commandes IOS doivent être exécutées dans un mode de configuration spécifique.

Passage d'un mode de configuration à un autre.

### `>` --> `#`
```
> enable
#
```

### `#` --> `(config)#`
```
# configure terminal
(config)#
```

### `#` --> `(config-int)#`
```
(config)# interface ...
(config-int)#
```

## Commandes communes dans les peripheriques IOS.

### Utilisateur standard.

### Utilisateur privilégié

Afficher la configuration actuelle.
```
# show running-config
```

Modifier la date, l'heure, les minutes et les secondes.
```
# clock set hh:mm:ss MONTH dd yyyy
```

Sauvegarder la configuration actuelle dans la NVRAM.
```
# copy running-config startup-config
```

### Configuration globale.

Changer le nom de l'appareil.
```
(config)# hostname {name}
```

Changer le mot de passe du mode privilégié.
```
(config)# enable password {password}
```

Changer le mot de passe du mode privilégié en le chiffrant.
```
(config)# enable secret {password}
```

Activer le chiffrement automatique des mots de passe dans le fichier de configuration.
```
(config)# service password-encryption
```

Changer la bannière de connexion.
```
(config)# banner motd "{banner}"
```

### Configuration du port console.

Entrer en mode de configuration du port console.
```
(config)# line console 0
(config-line)#
```

Changer le mot de passe d'accès au switch via le port console.
```
(config-line)# password {password}
```

Activer le système de mot de passe du port console.
```
(config-line)# login
```

### Peu-importe le mode

Obtenir des informations sur le matériel et la version.
```
> show version
```

Afficher la date, l'heure, les minutes et les secondes.
```
> show clock
```