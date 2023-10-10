# Notes labo Bases de données

Table des matières

1. [Installation](#installation)
2. [Le PHP](#php)
3. [SQL](#sql)

## Softs pour gérer les bases de données et PHP <a name="installation"></a>

Choix selon plateforme

* Laragon
* XAMPP

### Installation de XAMPP sous linux (fedora)

XAMPP a besoin de libnsl pour fonctionner sous fedora linux :

```
sudo dnf install libnsl
```

Pour installer XAMPP, aller sur le site et télécharger le .run de la bonne version :

https://www.apachefriends.org/index.html

Ensuite il faut ouvrir un terminal dans le dossier ou le package a été téléchargé, et entrer la commande suivante afin de rendre le fichier exécutable :
```
chmod +x xampp-linux-x64-7.2.9-0-installer.run
```

Puis on l'installe via :

```
sudo ./xampp-linux-x64-7.2.9-0-installer.run
```

Il faut suivre les instructions et cocher la case "launch xampp"


### Utilisation de XAMPP sous linux

Il faut se rendre dans le repertoire contenant les fichiers du programme :

```
cd /opt/lampp
```

Puis on lance l'exécutable (le nom dépend de la version!!!):

```
./manager-linux-x64.run
```

Comme ci-dessous :

![Alt text](<assets/images/Screenshot from 2023-10-10 15-15-13.png>)

Le menu ressembleà ceci :

![Alt text](<assets/images/Screenshot from 2023-10-10 15-15-22.png>)

## Le PHP <a name="php"></a>

### Redirections

### Variables

## Tips exam

Question d'examen :

```ìnclude``` n'arrête pas le code si erreur

```require``` arrête le code lors d'un problème

## SQL <a name="sql"></a>