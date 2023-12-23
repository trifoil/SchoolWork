# Sythèse de théorie de linux

This work is dedicated to our god, Mlord Torvalds.

Par pitié installez votre fcking software in english.
## GNU/linux 

### 

## Administration

## Gestion des fichiers

## Gestion des users et des groupes

## Gestion des systèmes de fichiers

## Archivages, sauvegardes et compression

## Installation de programmes

### Généralités

La licence GPL de la plupart des programmes permet leur utilisation/modification extrêment libres.

La plupart des logiciels libres sont disponibles via :
* Package manager (dnf, apt, ...)
* Github
* Gitlab
* L'hébergement par l'organisme lui-même 

Comme la distribution sur laquelle nous allons travailler cette année sont de la famille Red Hat, nous nous focalisons sur certains gestionnaires de packages.

Nous allons principalement utiliser trois methodes pour installer un programme :
* DNF (Dandified YUM)
* RPM (RedHat Package Manager)
* Compilation

Les deux premiers ont le même but : installer des packages .rpm

Le premier est toujours préférable au second car :
* DNF identifie et installe automatiquement toutes les dépendances nécessaire au programme qu'on installe
* RPM installe seulement le programme, et doit être utilisée plusieurs fois pour rechercher les dépendances et les installer, ce qui est chiant.


### Utilisation de RPM

Il fonctionne :
* de manière graphique lorsqu'on travaille dans un DE (desktop environment), 
* en CLI (command line interface).

Sa nomenclature est très simple :
* Nomn du package
* Version
* Architecture visée 
* Extention .rpm

Commandes les plus courantes :

```
rpm -ivh packagename-1.2.3.i386.rpm
```
L'option :
* -i veut dire installer.
* -v affiche les infos de debugging.
* -h affiche des résultats plus lisibles our un être humain.

Si un package manque, il faut aller le chercher manuellement.

```
rpm -e packagename
```
L'option :

* -e veut dire désinstaller.

```
rpm -Uvh packagename
```
L'option :
* -U veut dire mettre à jour.

```
rpm -q packagename.
```
L'option :
* -q veut dire qu'on demande les détails.
```
rpm -qa
```
Affiche tous les packages et leurs infos (contenues dans le nom)

### Installation d'archives

Une archive est toujours nommée sous cette forme :

```<Nom>-<Version>.<src ou bin>.<(Type de binaire)>.<Type d'archive>.<type de compression>```

* bin veut dire que l'archive contient un fichier binaire prêt à être executé 
* src veut dire que l'archive contient le code source

## Gestion des process



## Gestion des ressources




## Tips



Ne pas oublier de dire à Malaise que NFS est routable, de cette manière, il rira dans sa barbe et mettra secrètement ZERO à la question


# Vieux

# Sythèse de théorie de linux

dans le bashrc config de bash (pour aller modifier)


## Systemes de fichiers

Constitués de secteurs, constitués eux même de blocs = plus petite unité 

```
df -i
```

Ajout de disques via

```
mount
```



### Journalisés 



### Non journalisés


## Processus

### Programmes et processus

* Process IDentification ou PID
* Parent Process Identification ou PPID
* User id ou UID
* Group ID ou GID
* temps CPU


Redirection d'une commande
```
ls > liste.txt
```
Une tache peut être envoyée en tâche de fond si elle n'est pas affichée
