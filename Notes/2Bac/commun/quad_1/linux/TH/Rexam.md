**Logiciel libre:**
- **Définition:** Un logiciel libre est un logiciel dont l'utilisation, la modification et la distribution sont autorisées, sans restriction de droits. Cela signifie que les utilisateurs ont la liberté d'étudier, de modifier et de partager le code source du logiciel.

- **Licences de logiciel libre:**
  - GNU General Public License (GPL)
  - Apache License
  - MIT License
  - BSD License
  - Creative Commons

- **Logiciel open source:** Un logiciel open source est un type de logiciel libre dont le code source est accessible au public. Les licences open source garantissent également la liberté de modifier et de distribuer le logiciel.

**Distro Linux:**
- Une "distro Linux" (distribution Linux) est une version spécifique du système d'exploitation Linux, regroupant le noyau Linux, des utilitaires système et souvent des logiciels applicatifs. Elle est conçue pour répondre à des besoins spécifiques des utilisateurs.

**Exemples de distros Linux:**
- Ubuntu
- Fedora
- Debian
- CentOS
- Arch Linux

**Shell:**
- Un shell est une interface en ligne de commande permettant à l'utilisateur d'interagir avec le système d'exploitation. Il prend les commandes de l'utilisateur et les transmet au noyau pour exécution.

**Différence entre console et terminal:**
- Une console est l'écran et le clavier physiques, tandis qu'un terminal est une interface logicielle qui permet d'interagir avec le système d'exploitation via la ligne de commande.

**Les commandes:**
- Les commandes Linux sont des instructions données via le terminal pour effectuer des tâches spécifiques. Exemples : `ls` (list), `cp` (copy), `mv` (move), `mkdir` (make directory).

**Rôle de l'administrateur système:**
- L'administrateur système est responsable de la gestion, de la configuration et de la maintenance d'un système informatique. Il peut avoir des rôles spécifiques tels que l'administration réseau, la gestion des utilisateurs, etc.

**Linux - Tout est fichier:**
- En Linux, tout est traité comme un fichier, y compris les périphériques matériels, les sockets réseau, etc.

**Arborescence Linux:**
- Exemples de dossiers dans l'arborescence: `/etc` (configuration), `/home` (répertoires personnels), `/bin` (binaires essentiels), `/var` (données variables).

**Types de fichiers:**
- Fichiers texte, binaires, exécutables, liens symboliques, etc.

**Extensions de fichiers (qui servent à rien):**
- Les extensions de fichiers n'ont pas toujours de signification précise sous Linux, car le système se base sur les permissions pour déterminer le type de fichier.

**Liens symboliques:**
- Les liens symboliques sont des raccourcis vers d'autres fichiers ou répertoires. Ils permettent de créer des alias.

**Droits:**
- Les droits sur les fichiers et répertoires définissent qui peut faire quoi. Les droits sont généralement séparés en lecture (r), écriture (w) et exécution (x).

**Umask:**
- Umask est une commande qui détermine les droits par défaut lors de la création de fichiers. Il masque les droits que vous ne voulez pas attribuer par défaut.

**Risques liés aux droits d'endossement:**
- Les droits d'endossement peuvent donner à un utilisateur les mêmes droits qu'un autre, posant ainsi des risques de sécurité.

**Changer les options de montage pour contrer:**
- En modifiant les options de montage, vous pouvez limiter les droits accordés lors du montage d'un système de fichiers.

**Sticky bit:**
- Le sticky bit sur un répertoire permet à un utilisateur d'effacer uniquement ses propres fichiers dans ce répertoire, même s'il a les droits d'écriture.

**Utilisateur physique / logique:**
- Un utilisateur physique utilise directement le système, tandis qu'un utilisateur logique se connecte au système à distance.

**Groupes:**
- Les groupes permettent de regrouper les utilisateurs pour définir des permissions communes.

**UPG - Risque de sécurité:**
- UPG (User Private Groups) est un modèle de gestion des groupes qui peut présenter des risques si mal configuré.

**Authentification:**
- Processus permettant de vérifier l'identité d'un utilisateur. Les informations sont généralement stockées dans `/etc/passwd` et `/etc/shadow`.

**Mot de passe sécurisé:**
- Un bon mot de passe doit être complexe, avec des combinaisons de lettres majuscules et minuscules, des chiffres et des caractères spéciaux.

**Filesystems:**
- Les systèmes de fichiers organisent la manière dont les données sont stockées et récupérées. Exemples : ext4, XFS, Btrfs.

**Disque dur - Plateaux, etc.:**
- Un disque dur contient des plateaux magnétiques où les données sont stockées. Les têtes de lecture/écriture accèdent aux données.

**Structure d'un type de fichiers ext:**
- Ext4, par exemple, utilise une structure de blocs pour stocker les données, avec des inodes pour représenter les fichiers.

**Inodes:**
- Les inodes contiennent des métadonnées sur les fichiers, telles que les propriétaires, les droits, etc.

**Gestion soi-même d'un système de fichiers:**
- Gérer son système de fichiers permet un contrôle fin sur les autorisations, la configuration et la gestion des données.

**Système de fichiers journalisé:**
- Un système de fichiers journalisé enregistre les modifications avant de les appliquer, ce qui améliore la récupération après une panne. Exemples : ext4, XFS.

**Archivage:**
- Archiver consiste à regrouper des fichiers dans un format compressé (tar) pour faciliter le stockage et la distribution.

**Plan de sauvegarde:**
- Un plan de sauvegarde définit les procédures et la fréquence des sauvegardes pour assurer la récupération des données en cas de problème.

**Bon support de sauvegarde:**
- Un support de sauvegarde doit être fiable, rapide et avoir une capacité de stockage suffisante.

**Commande tar:**
- La commande `tar` est utilisée pour créer des archives et extraire des fichiers à partir de ces archives.


**Types de stockages (avantages et inconvénients) :**
- Stockage local (disques durs, SSD) : Rapide, mais limité en capacité.
- Stockage en réseau (NFS, CIFS) : Permet le partage de données entre systèmes, mais dépend de la connectivité réseau.
- Stockage cloud : Évolutif, mais dépend de la connexion Internet.

**Installer un programme :**
- Compiler : Source code transformé en exécutable, nécessite des dépendances.
- Télécharger la version précompilée (paquet) : Installation simplifiée, gestion des dépendances.

**Cekoi un paquet :**
- Un paquet est un ensemble de fichiers associés à un programme, incluant les exécutables, bibliothèques et fichiers de configuration.

**Processus puces (ppid) :**
- ppid (Parent Process ID) représente l'ID du processus parent.

**Modes d'exécution :**
- Utilisateur (user mode) : Restreint, accès aux ressources limité.
   - Noyau (kernel mode) : Accès complet aux ressources du système.

**Héritage des processus :**
- Les processus peuvent créer d'autres processus, héritant de certains attributs du processus parent.

**Conditions pour envoyer un processus en arrière-plan :**
- Utiliser `&` à la fin de la commande.
- Ou utiliser `Ctrl + Z`, puis `bg` pour le mettre en arrière-plan.

**Cekoi un signal :**
- Un signal est une notification envoyée à un processus ou au système d'exploitation pour indiquer un événement ou une action.
**Priorité des processus :**
- La priorité est déterminée par la nice value, allant de -20 (priorité élevée) à 19 (priorité basse).

**Crontab :**
- Un outil pour planifier des tâches récurrentes.

**Quotas :**
- Limiter l'utilisation de ressources (espace disque, inodes) par utilisateur.

**Principales ressources à surveiller :**
- CPU, mémoire, espace disque, utilisation réseau.

**Avantages à gérer son système de fichier :**
- Organisation, sécurité, maintenance facilitée.

**Noyau Linux :**
- Partie centrale du système d'exploitation, gérant les ressources et les interactions entre le matériel et les logiciels.

**LVM (Logical Volume Manager) :**
- Avantages : Flexibilité dans la gestion des volumes.
- Inconvénients : Complexité.

**Démarrage de Linux (phases) :**
- BIOS/UEFI, Bootloader (GRUB), Noyau, Init (systemd).

**GRUB :**
- Bootloader permettant de charger le noyau Linux.

**systemd :**
- Système d'initialisation et de gestion de services.

**Fichiers utilisateurs et logs :**
- `/etc/passwd`, `/etc/shadow`, `/var/log` pour les logs système.

**NFS (Network File System) :**
- Protocole de partage de fichiers sur un réseau.

**Portmap et RPC :**
- Portmap attribue des ports pour les services RPC (Remote Procedure Call).

**Scripting :**
- Automatisation de tâches via des scripts (bash, Python).

**SNMP et MIB :**
- Protocole de gestion réseau, MIB (Management Information Base) définit la structure des informations.

**Sécurité :**
- Menaces : Virus, malware, attaques par force brute.
- DRP (Disaster Recovery Plan) : Plan de reprise après sinistre.

**Options de montage, logiciels :**
- Sécuriser le système via des options de montage, utilisation d'outils de sécurité.

**Firewall :**
- Types : Stateful, Stateless.
- Avantages : Filtrage du trafic, protection contre les attaques.
- Paramètres : Règles, NAT.

**Proxy :**
- Interception des requêtes entre client et serveur, améliore la sécurité et la performance.

**Table, shelf, cibles :**
- Descripteurs utilisés dans le contexte du stockage ou du réseau.

**Politique par défaut d'une chaîne :**
- Les règles appliquées si aucune autre règle ne correspond.

**/etc/nologin :**
- Empêche les connexions sauf pour les utilisateurs spécifiés.

**usermod -G, chgrp :**
- Ajouter un utilisateur à un groupe, changer le groupe d'un fichier.
