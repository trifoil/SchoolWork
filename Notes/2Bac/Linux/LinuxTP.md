# Sythèse de TP de linux

## TP1 : commandes fondamentales

### Commande cd 

Pour accéder au root directory :

```
cd /
```
Pour accéder au user directory :

```
cd
```

Pour remonter d'un directory :

```
cd ..
```

### Commande ls

```
ls
```

Pour lister les permissions :

```
ls -l
```

### Commande cat

Permet de montrer/écrire des fichiers

```
cat [OPTIONS] [FILE_NAMES]
```

Pour voir les users, on peut taper 

```
cat /etc/passwd
```

### Commande man 

La commande man donne tout simplement le manuel
```
man date
```
Nous donnera le manuel du package date

### Commande useradd

Permet d'ajouter un utilisateur,par exemple appelé toto :

```
useradd toto
```

### Commande passwd

Pour changer le mdp de l'utilisateur actuel :

```
passwd 
```

Pour changer le mdp de l'utilisateur toto :

```
passwd toto
```

### Commande usermod

Permet de modifier un utilisateur

### Commande userdel

Permet de supprimer un utilisateur, par exemple toto :

```
userdel toto
```

Pour supprimer l'utilisateur, son home directory, et son mail utilisateur :

```
userdel toto -r
```
### Commande pwd

Indique le chemin complet du directory ou on se trouve

```
pwd
```

Pour éviter les liens symboliques et avoir l'addresse physique du directory
```
pwd -P
```

### Commande whoami

Pour connaitre son username actuel

```
whoami
```

## TP2 : Gestion des fichiers

## TP3 : 

### Droits d'exécution

Pour afficher les droits :

```
ls -l 
```

En sortie on a :

```
r pour read
w pour write
x pour execute (peut etre même sur des non-executables)
```

On va voir les permissions associées aux fichiers systemd, inittab, skel :

```
drwxr-xr-x.  5 root root   4096 Sep 17 20:00 systemd
-rw-r--r--.  1 root root    490 Sep 17 20:00 inittab
drwxr-xr-x.  2 root root     62 Sep 15 09:12 skel
```


## TP4 : 

mount -l 