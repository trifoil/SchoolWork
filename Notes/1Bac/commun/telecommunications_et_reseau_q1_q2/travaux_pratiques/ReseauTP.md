# Synthèse TP réseau

## TP0 : Table des matières <a name="0"></a>

0. [TP0 : Table des matières](#0)
1. [TP1 : ]
2. [TP2 : ](#2)
3. [TP3 : ](#3)
4. [TP4 : ]
5. [TP5 : ]


### Normes ISO


* 568 A
* 568 B = le plus souvent

![6d8d55067056c9533110daff369749d6.png](:/979a13606b1e43daa4688a7c93f1ec1b)

### Code couleur

* Orange 
* Orange-Blanc
* Vert
* Vert-Blanc
* Bleu 
* Bleu - Blanc
* Brun 
* Brun - Blanc

### Blindage
* U/UTP
	* Non-blindé
* F/UTP
	* Film d'alu autour du cable
* F/FTP
	* Film d'alu autour de chaque paire
* S/FTP
	* Blindage et film d'alu

### Cablage structuré



### Pratique 
* Pince à sertir
	* RJ45
	* Patch panel
* Testeur

## TP2 : Installation de packet tracer <a name="2"></a>

## TP3 : Logical and physical Mode Exploration

## TP4 : Network representation

## TP5 : Navigate the IOS

### Découverte IOS

Le point d'interrogation liste l'ensemble des commandes disponibles ou la suite d'une commande.
```
S1>?
```

Liste des commandes commençant par la lettre t :

```
S1>t?
```

Autocomplétion de commande avec la touche tab (comme dans linux).

### Mode d'exécution privilégié

Si on utilise la commande ```enable```, on active le mode d'éxécution privilégié.

Le symbole doit changer en dièse

```
S1>enable
S1#
```

### Mode de configuration globale

Si on utilise la commande ```configure``` après être passé en mode d'exécution privilégié, on passe en mode de configuration globale. La console affiche donc :

```
S1#configure
S1(config)#
```

Les commandes ```end```, ```exit``` ou Ctrl+Z permettent de quitter le mode de configuration globale. 

### Réglage de l'horloge

La commande ```show clock``` montre l'heure. Si elle n'est pas correcte, on peut la définir :

```
S1#clock set 15:00:00 2 JAN 2035
```

Bien évidemment donc, Heure, minute seconde, jour, mois et année.

## TP6 : Connectivité initiale de la console

La commande ```show version``` affiche a version du firmware.

## TP7 : Configuration initiale des switches

Pour afficher la config initiale, on utilise la commande ```startup-config```

Pour activer 

```
S1# config t
S1(config)# enable secret itsasecret
S1(config)# exit
S1#
```

![Alt text](image.png)
## TPX : Synthèse des commandes

## TPZ : Tips pour l'examen

Mettre d'office :

* Bannière 
* MDP pour accéder à la console 
* MDP pour accéder au mode privilégié

