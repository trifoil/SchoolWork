# SchoolWork
Pour unifier notre belle communauté nerdo-anarcho-communiste, nous avons créé ce répo dans lequel vous pouvez créer/ajouter vos synthèses/notes/supports de cours. Avec votre aide, nous pourrions créer une ressource capable d'aider tout le monde pour cette année ou les années à venir.

> Si vous souhaitez devenir contributeur, veuillez contacter @trifoil (Augustin) sur l'un des serveurs Discord de la HEH.

### Organisation des notes

Organisation générale des dossiers :

```
bloc_x      
└── quad_x      
    └── option      
        └── nom_du_cours        
            ├── nom_de_la_personne      
            │   ├── synthèses
            │   │   └── synthèses...
            │   │
            │   ├── questions
            │   │   └── questions...
            │   │   
            │   ├── notes
            |   |   └── note_x...
            │   │
            │   └── projets
            │       └── ...
            │       
            ├── exos        
            │   └── exo-...md       
            │       
            └── supports        
                └── cours     
```
 
- bloc_x (x = 1, 2, 3)
- quad_x (x = 1, 2)
- option (commun, secu, dev)
- nom_du_cours (ex : prog, prog-tp, ioe)
- nom_de_la_personne (nom_prénom)
- synthèses (vos synthèses sans format précis)
- questions (questions type d'interrogation)
- notes/note_x (x = séance du cours)
- exos/exo-...md (un exercice à la fois)
- supports (support de cours)


## Utilisation de git
#### [Tutoriel en français sur git](https://www.atlassian.com/fr/git/tutorials)
#### [Tutoriel en anglais sur git](https://github.com/git-guides/)

<details>
<summary>1. Générer une clé SSH</summary>

- Utilisez la commande : `ssh-key` pour générer une clé SSH
- Copiez la clé qui se trouve dans le dossier `.ssh` dans le fichier `id_rsa.pub`
- [Ajoutez la clé à votre profil Github](https://github.com/settings/keys)
</details>

<details>
<summary>2. Cloner le repo </summary>
    
- Utilisez la commande : `git clone git@github.com:trifoil/SchoolWork.git` , cela va créer le dossier "SchoolWork" dans le répertoire où la commande est exécutée
</details>

<details>
<summary> 3. Modifier le repo </summary>

- Utilisez la commande [`git pull`](https://www.atlassian.com/fr/git/tutorials/syncing/git-pull) pour mettre à jour le repo
- Utilisez les commandes [`git add`](https://www.atlassian.com/fr/git/tutorials/saving-changes/git-add) et [`git commit`](https://www.atlassian.com/fr/git/tutorials/saving-changes/git-commit) pour enregistrer localement vos modifications 
- Puis utilisez la commande [`git push`](https://www.atlassian.com/fr/git/tutorials/syncing/git-push) pour envoyer vos modifications sur le repo
</details>

## Todo
<details>
<summary> Bac 1 </summary>

## Bac 1
### <u> Quad 1 </u>

### **TH**
- [x] Réseau
- [x] Archi
- [x] IOE
- [ ] Elec
- [ ] Tech num
- [x] Prog
### **TP**
- [x] Prog

### <u> Quad 2 </u>

### **TH**
- [ ] Réseau
- [ ] Elec
- [ ] Prog
- [ ] Tech num
### **TP**
- [ ] Prog

</details>

<details>
<summary> Bac 2 </summary>

### Bac 2
---
### **TH**
- [ ] DB
  
### **TP**
- [ ] Windows Server 
- [ ] Linux 
- [ ] PHP
- [ ] Technum

</details>