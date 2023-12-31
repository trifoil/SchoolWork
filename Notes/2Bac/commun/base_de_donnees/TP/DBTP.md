# Notes labo Bases de données ⛁

## Table des matières

1. [Installation](#installation)
2. [Le PHP](#php)
3. [SQL](#sql)
4. [Exam Tips](#tips)

## Softs pour gérer les bases de données et PHP <a name="installation"></a>

Choix selon plateforme

* Laragon
* XAMPP

### Installation de Laragon sous winshit

Telecharger l'executable :

https://laragon.org/download/

Installer 

Clic droit -> Tools -> Quick add -> *phpmyadmin :

![Alt text](image.png)

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


### Utilisation de Laragon sous Windows

Démarrer les services 

![Alt text](image-1.png)

Modifier le code php :

![Alt text](image-2.png)

Accéder à phpmyadmin :

![Alt text](image-3.png)

Accéder au 

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

Les fichiers PHP doivent être placés dans le répertoire /opt/lampp



## Le PHP <a name="php"></a>

### Inclusions / Redirections



### Variables

### Dates

### Structures conditionnelles et itératives

in array 

pour checker une valeur dans 

## SQL <a name="sql"></a>

## Tips exam <a name="tips"></a>

Question d'examen :

```ìnclude``` n'arrête pas le code si erreur

```require``` arrête le code lors d'un problème


## PHP cheatsheet

cd /opt/lampp
./manager-linux-x64.run
              
```
include '';
include_once '';
require '';
require_once '';

header(''); toujours en tout premier
exit; arret d'exécution

header('Location:index.php'); redirection vers index.php

$longueur = 10; est une variable (lettre/chiffre, mais pas apres le $/_)
unset($longueur); détruit la variable 

if (isset($longueur)){check si la variable a une valeur quelconque}
if (empty($longueur)){check si la variable est inexistante, NULL ou 0};

$A = &$B; A a comme référence B donc la valeur de A vaut celle de B

gettype ($var); 

is_<type de la variable : integer int float real double numeric bool string array object resource null> ($x); pour verifier le type de x


```

## PHP exercices

**Exercice 2 : Inclusion de fichiers**

index.php

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Inclusion de fichiers</title>
</head>
<body>
    <?php
    include '_header.php' ;
    include '_nav.php' ;
    include '_footer.php' ;
    ?>
    <h2>Accueil</h2>
</body>
</html>
```

_footer.php

```
<footer>
    <p>
    Dudule la pendule
    </p>
</footer>
```

administration.php

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Administration</title>
</head>
<body>
    <?php
    header('Location:index.php');
    include '_header.php' ;
    include '_nav.php' ;
    include '_footer.php' ;
    ?>
    <h2>Administration</h2>
</body>
</html>
```

contact.php

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Administration</title>
</head>
<body>
    <?php
    include '_header.php' ;
    include '_nav.php' ;
    include '_footer.php' ;
    ?>
    <h2>Contact</h2>
</body>
</html>
```

**Exercice 3 : Opérations sur les variables**