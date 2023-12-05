# Architecture des ordinateurs

Date de création: 21 septembre 2023 16:53
Supports: https://ecampus.heh.be/pluginfile.php/205875/mod_resource/content/1/cours_Architecture.pdf
Relue ?: No

```jsx
Savoir faire conversion binaire, octale , hexadécimale, décimal (pas opération (+; -; ..) mais bien de revoir)
pas fonction logique
comment augmenter le débit
shéma cpu
architecture big/little (page 18)
pas fabrication processeur
finesse de gravure
savoir cpu lier au socket
qu'est ce que la fréquence (p28)
Connaitre TDP
refroidissement (pas caloduc ni chambre a vapeur)
connaitre ipc et parrallélisme (p52 ; 54)
pas connaitre undervolting
connaitre cpu superscalaire (p55)
pipeline sert juste a augmenté l'IPC
hyperthreading (savoir l'expliquer avec des mots
Savoir comment calculer les FLOPS
Qu'est ce qu'un jeu d'instruction (avec un exemple au moins (p72))
Benchmark synthétique et applicatif
************RAM************
a quoi sert la RAM
Mémoire vive, volatile, RAM et barrette de RAM (p3)
DRAM et SRAM (l'une pour cpu l'autre mémoire vive pc (p4))
Les caractéristique de la ram et leur explication (p5 ou 6)
DDR (optimisé pour les latence cpu) (p11)
comment connaitre la latence a partir du timing (p21)
c'est surtout le débit qui s'améliore dans les RAM mtn pas la fréquence
pas UDIMM et RDIMM
Canaux (multi canaux) (p23)
Mémoire ECC
************************************DISQUE DUR************************************ 
Hdd
Pq vitesse est importante
savoir qu'il existe 3 pouce ,5 et 2 pouce , 5
Caractéristique technique 
Half duplex et full duplex différence (l'un lis et ecris l'autre fais l'un ou l'autre pas en meme temps
savoir calculer le temps d'acces 
fragmentation
IOPS (intput/output per second) (juste ca)
savoir qu'un hdd n'efface jamais vrmt la donnée
******ssd******
caractéristique
type de nand
c quoi un ssd
ssd vs hdd (p26) /!\
c'est quoi le raid et les différents raid (pas important l'abréviation)
Raid logiciel, pseudo-matériel et matériel
**********************CARTE MERE**********************
C'est quoi ?
Le BIOS (mots en gras en gros)
pas connaitre les images des connecteurs (pg7-8-9 pas sur page)
A quoi sert le chipset (p13)
Connaitre son emplacement et que le procésseur sert a qq chose (p14)
pas ventilateur ni alimentation
connaitre VRM (p18)
facteur de forme (juste ATX)
choix d'une carte mère en résumé (p21) 
********************************Le bloc d'alimentation********************************
Ca fait quoi (mots en gras en gros (p2))
pas pcf actif passif
Connaitre l'alimentation ( wattage a avoir) avec une config donnée (p16)
connaitre norme 80 plus 
savoir qu'on peut prendre modulaire non modulaire
Comment choisir son alim
********GPU********
a quoi ca sert ?
Format de GPU
connaitre comment est composé le gpu (p4)
les critère pour jeu vidéo ou calcul scientifique (dans l'ordre les truc en gras)
caractéristique du gpu 
puissance de calcul gpu
Si jeu vidéo en 32 sinon en 64 (p10)
pas texturing memory unit 
pas Ray tracing
pas tensor core
pourquoi la mémoire graphique important ou pq pas
bande passante (p18) et comment la calculer (p20)
l'interface (p24-25) pci 1 -> 0,25 puis le 2 on double le 3 on double encore ..
savoir TDP; TGP; TBP (p26)
pas API
****************Boitier****************
RIEN (juste airflow en sah)
************Ecran************
c quoi la taille d'un ecran et la def (p2)
****************ecran lcd (tft,led)**************** 
pas p4-6
********************************Caractéristique de base (p7)
pas rétroéclairage
**********OLED**********
Def OLED
OLED VRAI NOIR comparé au reste c pas un vrai noir
shéma résumé (p36) pas la partie pixel coupé
```

**Débit** : ex : 4/s

**Latence** : temps d’arriver d’un paquet

**fréquence** : nombre de données envoyée (influence pas la latence) mais peut envoyer + en - de temps

 

**Augmenter canaux** —> permet d’envoyer plus de données en même temps

**CPU (central processing unit) :** 

- Fait calcul
- Orchestre le déplacement de données

Circuit intégré composé de : 

- **Transistors** (Pour faire les calculs)
- **Mémoires** (Pour fournir les données aux transistors et stocker le résultat)
- **Bus de données** (Pour entrer et sortir les données du CPU)

****************************Transistor :**************************** interrupteur à commande électrique 

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled.png)

![2023-09-25_17h40_07.png](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/2023-09-25_17h40_07.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%201.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%202.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%203.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%204.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%205.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%206.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%207.png)

**L’enveloppe thermique, ou TDP (Thermal Design Power)**
Transfert thermique vers l'extérieur dont doit pouvoir bénéficier ce composant pour
fonctionner correctement.

**TDP = k . V² . f**

k = constante (fonction du processeur)
V = tension électrique
f = fréquence
TDP watts (W)
Il est donc nécessaire d’apposer un dispositif de refroidissement adapté au TDP du CPU

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%208.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%209.png)

**Les caloducs :**

- Utilisé pour déplacer rapidement la chaleur du CPU vers son dissipateur

************************WATERCOOLING************************

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2010.png)

**Les surfaces du CPU et du dissipateur ne sont pas parfaitement plates :**
• L'air est un isolant -> mauvais transfert de chaleur
• Solution -> utilisation de pâte thermique ou d'un pad thermique pour
combler les vides

**La tension appliquée au CPU varie en permanence** : si elle est trop basse, la machine plante (UNDERVOLTING)

**IPC** —> instruction par cycle

**but parallélisme :**

- augmenter nombre d’instructions par cycle
    - Dédoubler certaines unitées de calcul
        - calcul indépendant et donc calculer simultanément
    - Pipelines
        - **IF (Instruction Fetch)** : charge l'instruction à exécuter dans le pipeline.
        **ID (Instruction Decode)** : décode l'instruction et adresse les registres.
        **EX (Execute)** : exécute l'instruction
        **MEM (Memory)** : accès mémoire
        **WB (Write Back)** : stocke le résultat
            
            ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2011.png)
            
        
    - Unités vectorielles
        - Utilise l’unité vectorielle pour appliquer un même traitement à plusieurs données.
        
        ex : diviser par 2 tt les valeurs de qq chose 
        

—→ Tout ca est appeler le parallélisme séquentiel car l'objectif est d'augmenter le nombre d'IPC d'un traitement séquentiel

- Permettre de traiter plus de taches en même temps
    - multicœur
    - multiprocesseur
    - multithreading simultané

********************************************************Avoir plus de cœur permet seulement de faire plus de taches en même temps mais pas forcément + rapidement********************************************************

hyper threading/multi threading (SMT)→ multiplication virtuelle du nombre de cœur sans ajouter d’unité de calcul

𝐹𝐿𝑂𝑃𝑆 = 𝑛𝑜𝑚𝑏𝑟𝑒 𝑐𝑜𝑒𝑢𝑟𝑠 x 𝑓𝑟é𝑞𝑢𝑒𝑛𝑐𝑒 x 𝐹𝐿𝑂𝑃/cycle

**************************************Jeu d’instruction************************************** : ensemble des instructions machine qu’un processeur peut exécuter (~sa langue) assure une compatibilité entre les application et le matériel

 

**Benchmark synthétique**

- Logiciel développé dans le seul but d’évaluer les performances
- C’est du Marketing

**Benchmark applicatif**

- Mesure de performances dans un logiciel ou jeu vidéo
- Les résultats peuvent varier fortement d’un logiciel a l’autre

# RAM

************RAM :************ Contient les données nécessaire bon au fonctionnement du CPU temporairement tel que :

- Données pour calculs
- Résultat des calculs
- Programmes en cours d’exécution

**Mémoire vive** : sollicitée pendant les calculs du CPU

**Mémoire volatile** : les données sont perdues une fois l'alimentation
électrique coupée

**Mémoire RAM (Random Acess Memory) :** L'information peut être accédée directement
(adresse aléatoire)

**Mémoire vive PC :** 

- Moins cher (plus simple)
- Meilleure densité
- Requiert une fréquence de rafraichissement

**Mémoire cache (ex. CPU) :** 

- Plus cher (plus complexe)
- Moins dense
- Plus rapide

********************************************Caractéristique RAM :******************************************** 

•Capacité (Go)
•Type de mémoire (DDRx)
• Format (DIMM, SO-DIMM)
• Fréquence (MHz)
• Timing (latence)
• Canaux
• Fonctionnalités
• Refroidissement, dimensions et soirée disco

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2012.png)

- **DDR Double Data Rate** : optimisé pour les latences (CPU)
    
    à chaque montant ou descendant on lit ou engrave une donnée
    
    ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2013.png)
    

• **GDDR Graphics** : optimisé pour les débits (GPU)
• **HBM Hight Bandwidth Memory** : optimisé pour les débits (GPU) mémoire empilée et soudée

******Fréquance (MHz) x bus (..bit) = débis (mb/s)****** 

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2014.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2015.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2016.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2017.png)

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2018.png)

****************Trouver timing :**************** 

DDR4 4000 MHz `CL18`

Temps de cycle : 1 / par la fréquence de la ram (pas oublier de diviser par 2 si ddr) = nano seconde

tCAS : nano seconde (trouver au dessus) x nbr ecris dans spec (dans ce cas ci 18) = nano seconde réel

**********Dual channel :********** Permet d’exploiter 2 barrettes simultanément (max 2 barrettes)

****************************************Multi channel :**************************************** Permet d’exploiter simultanément plusieurs barrettes de RAM

———> permet de cumuler les débits

UDIMM (Ram unbuffered)

- C'est le contrôleur mémoire du CPU qui adresse la RAM.
- Le CPU ne sait adresser que X Go de RAM
- La RAM grand publique est de la RAM UDIMM

RDIMM (RAM registered)

- Comporte une puce additionnelle (registre) qui s'occupe de l'adressage directe de la mémoire (latence suplémentaire).
- Permet d'installer des barrette de plus forte capacité (si carte mère et CPU sont compatibles)
- La RAM serveur est "souvent" de la RAM RDIMM

************************************Si bit-flips —>************************************ Mémoire ECC (Error Correction Code) —> ajout de bit dédié à la détection voir correction d’erreur

![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2019.png)

Single rank mais quand même des deux coté —> car seulement une sortie

******************En gros :******************

• Choisir le bon format (RDIMM, UDIMM, ECC, SO-DIMM, etc.)
• Favoriser le Dual Channel (c'est gratuit)
• Avoir un bon équilibre entre fréquence et latence
• Les mémoires à très hautes fréquences/basses latences sont des
investissements rarement rentables
• Attention à la hauteur des barrettes
• Eviter de mélanger des RAM avec des spécifications différentes

• Vérifier la comptabilité entre la RAM et le CPU

Pour une utilisation 3D : minimum 8Go de RAM et essayer de respecter :
quantité RAM >= quantité VRAM (=mémoire graphique du GPU)

Pour une utilisation type calcul scientifique, il faut beaucoup de RAM :
quantité RAM >= 2x quantité VRAM (=mémoire graphique du GPU)

# DISQUE DUR ET SSD

Disque dur : stocke les données sur le long terme 

1er disque dur a apparu en 1956 et pouvait contenir max 5 Mo

Différents types : 

- HDD (disque dur mécanique/magnétique)
- SSD (disque électronique, disque statique à semiconducteurs)
- SSHD (HDD incluant un petit SSD)HeMMC
- Clé USB et autres cartes SD

**HDD (hard disk drive) composé de :** 

- **Plateaux qui tourne à vitesse constante**
    - Chaque plateau contient des données
    - Plus ils tournent vites
        - + meilleurs serra le débit (Mo/s)
        - + meilleurs seront les latences (ms)
        - - moins bonne serra consommation électrique
- **Têtes d’écriture/lecture**
    - Electro-aimant qui se baissent et se soulèvent pour lire l’info/écrire
    - Se situe qu’a qq nanomètre de la surface
    - écris sur l’extérieur puis vers le centre
    - 
    
    ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2020.png)
    

- **Caractéristiques importantes pour un HDD**
    
    ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2021.png)
    
    **IOPS → input output par seconde**
    
    ****************************************Technologie d’enregistrement :****************************************
    
    - **PMR (perpendicular Magnetic Recording) :**
    - **SMR (Shingled Magnetic Recording) :**  Permet de stocker plus sur un plateau mais en cas de modification d'une donnée :
    1. écriture dans une zone vide de la nouvelle version de la donnée
    2. lecture des pistes voisines de l'ancienne donnée
    3. écrasement de l'ancienne donnée par la nouvelle
    4. invalidation de la donnée écrite au point 1.
    
    - **********************Interface HDD**********************
        - La connectique (et le protocole communication)
        - Interface disque dur interne grand public (ordi tout le monde) → SATA
        - interface disque dur interne serveur (pro) → SAS
    
    **Temps d’accès :** 
    
    - **Temps moyen pour trouver la bonne info (seek time)**
    - **Temps de latence** = délai entre le moment ou le disque trouve la piste et se synchronise sur ces données (60:rpm)x2
    - **Temps d'accès réel** = temps d'accès moyen + temps de latence
    
    **************IOPS (input/output per second) :************** 
    
    - sans unités ou parfois mo/s
    
    ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2022.png)
    
    ![2023-10-16_08h37_30.png](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/2023-10-16_08h37_30.png)
    
    (hdd montre ses faiblesse lors de IOPS aléatoires)
    
    - **Une tête de lecture/écriture ne sait pas démagnétiser une piste**
    - Le disque contient une forme d'index qui permet de savoir si une données
    est toujours valide ou non.
    - Effacer revient à invalider la donnée, et le disque pourra ainsi réécrire par-dessus si besoin
    
    - ************************************SSD (Solid-State-Drive)************************************
        - Alternative au disque dur magnétique
        - Disque purement électronique :
            - pas de pièces mécaniques
            - résiste mieux aux chocs et vibrations
            - moins de pannes
            - pas de nuisance sonore
            - faible consommation
        - Utilisation massive de mémoire flash
        - Interface SATA identique
        - Plus cher
        
    
    - **************************Types de NAND Flash (meilleurs au moins bien)**************************
        - SLC Single Level Cell (1 bit)
        - MLC Multi Level Cell (2 bit)
        - TLC Triple Level Cell (3 bit)
        - QLC Quadruple Level Cell (4 bit)
    
    ******Contrairement a un HDD le SSD sait effacer des données mais pas les modifier contrairement au HDD******
    
    - ************************************Remplissage des SSD************************************
        - Un des rôles du contrôleur et de la commande TRIM (gérée par l'OS) est
        de s'assurer du wear leveling. (essayer d'user toutes les cellules au même rythme)
        - Avec un SSD sans mémoire vive (sans mémoire cache dédiée),
        l'espace disque libre sert de mémoire cache (en mode SLC).
        (c'est plus lent que de la RAM et cela use légèrement les cellules)
    
    - **Alternatives SSD 2,5”**
        - Sous forme de carte d’extension PCI-Express
        - mSATA (SATA 3.1) :
        ressemble fort à une carte mini PCI-Express
        souvent pour portable
        - Carte M.2 (Next Generation Form Factor) :
        (Wi-Fi, WWAN, USB, PCIe, SSD SATA ou des SSD NVMe).
        - U.2 : (anciennement SFF-8639)
        utilise 4 lignes PCI-Express (comme les SSD M.2. NVMe)
        pour des débits jusqu'à 4 Go/s
        (principalement pour des SSD Pro)
    
    - ********************SSD vs HDD********************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2023.png)
        
    
    - **************RAID :************** Assemblage de plusieurs disques physiques pour constituer un seul disque logique
        
        ![Untitled](Notes%20de%20cours%208dbe861fa45848b58b88f4cdcd9a6576/tempo%2002da92df95184aaf9e324510bef776a3/Untitled.png)
        
    
    - ********RAID 5********
        
        Le ap signifie un contrôle de parité qui permet si on perd la donnée par exemple dans le 2 si on était censé être en pair en nombre de 1 ou de  0 on sait par quoi remplacer 
        
        ![Untitled](Notes%20de%20cours%208dbe861fa45848b58b88f4cdcd9a6576/tempo%2002da92df95184aaf9e324510bef776a3/Untitled%201.png)
        
    
    - **************RAID 10**************
        
        RAID 1 et RAID 0 
        
    
    - **************************Types de RAID**************************
        
        ![Untitled](Notes%20de%20cours%208dbe861fa45848b58b88f4cdcd9a6576/tempo%2002da92df95184aaf9e324510bef776a3/Untitled%202.png)
        
    
    # Carte mère
    
    - Motherboard ou Mainboard (voir mobo dans le jargon)
    - Elément crucial d'un ordinateur :
        
        
    - Ne se remplace pas aussi aisément qu'une barrette de RAM
    - ********************Le bios :******************** Programme stocké dans une ROM sur la carte mère (mémoire morte :
    mémoire en lecture seule) et sert à :
        - Initialiser tous les composants de la carte mère
        - Identifier tous les composants qui lui sont connectés
        - Initialiser l'ordre de priorité des périphériques de stockage
        - Démarrer le système d'exploitation
        
        A été remplacé par l'UEFI (Unified Extensible Firmware Interface) mais dans
        le jargon on utilise toujours (à tord) le terme de BIOS
        
        On peut y changer la date et heure, l'ordre de démarrage, la vitesse de
        rotation des ventilateurs, les fréquences de fonctionnement (CPU/RAM),
        désactiver des connecteurs, etc.
        Les paramètres sont conservés dans une petite mémoire (CMOS) qui doit
        rester alimentée en permanence
        C'est pour cette raison qu'une pile est présente sur la carte mère
        
    
    Il est possible de **remettre à zéro les paramètres de configuration par défaut
    via le jumper (cavalier) : Clear CMOS**
    
    L'opération de mise à jour du Bios = **flasher le Bios**
    
    - ****Socket****
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2024.png)
        
    
    - ********************************Slot barrette de RAM********************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2025.png)
        
    
    - ****************************************************************************Les connecteurs pour cartes extensions****************************************************************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2026.png)
        
    
    - **********************PCI express**********************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2027.png)
        
    
    - ******Ou connecter le SATA******
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2028.png)
        
    
    - ********************Le chipset********************
        - Le chef d'orchestre de la carte mère
        - Soudé et souvent affublé d'un dissipateur
        
        Une grande partie des fonctionnalités
        d'une carte mère dépend du chipset
        Permet ou non :
        
        - l'installation de certains CPU/périphériques
        - l'overclocking
        - le RAID pseudo-matériel
    
    - **************La ventilation**************
        - au minimum 1 cpu fan
        - éventuellement un CHA fan
        - éventuellement watercooling
        - ******************************************************Type connecteur ventilateur******************************************************
            - il faut minimum 2 fils
            - si 3ème fils —> vitesse rotation
            - si 4ème —> régulation électronique
            - si pas 4ème fil —> régulation de façon analogique
        
         
        
    
    - **Circuit d’alimentation (VRM)**
        - A qualité de composant égale, plus le nombre de
        phases est élevé :
            - plus les tensions sont stables
            - moins les VRM s'échauffent pour une même
            puissance totale
            - meilleure est l'efficacité pour des hautes
            puissances
    
    - ********************************************Connecteur entré sortie********************************************
        - Connecteur externe
            - HDMI, VGA, ..
        - Connecteur Interne
            - Usb 2, Audio, USB 3
    
    - ****************Choix d’une carte mère****************
        1. CPU
        2. Le socket
        3. Le facteur d’encombrement (taille)
        4. Le chipset
        5. Les connecteurs internes (PCI-Express, M2, SATA, DIMM)
        6. Les connecteurs d’entrées-sorties
        7. VRM et refroidissement
        8. Fonctionnalités additionnelles (chipset audio, RGB, etc.)
        
        (1 à 3 le + important car si pas compatible c ‘est foutu)
        
    
    **********************************************************************************SAVOIR VOIR QUELLES ELEMENT SUR UNE PHOTO**********************************************************************************
    
    # Bloc d’alimentation
    
    **PSU = Power Supply Unit**
    Composant indispensable et très un important car il doit :
    
    - Délivrer des tensions stables
    - Pouvoir fournir une puissance suffisante
    - Opérer en silence
    - Ne pas réchauffer la machine
    - Fournir suffisamment de connecteurs d'alimentation
    - Si ce composant est négligé (souvent le cas) : plantages, bruits,
    échauffement, consommation excessive et même des risques d'incendie
    - **Alimentation linéaire**
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2029.png)
        
    
    - ************************************************Alimentation à découpage************************************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2030.png)
        
        ![2023-10-23_09h06_23.png](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/2023-10-23_09h06_23.png)
        
        ![2023-10-23_09h06_35.png](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/2023-10-23_09h06_35.png)
        
    
    - ****Qualité des tensions****
        
        Suivant la qualité de l'alimentation, les tensions varieront plus ou moins fortement.
        Pour des tensions stables :
        
        - Hacher à fréquence élevée (entre 32 et 100 kHz)
        - Caractéristiques de la boucle de régulation
        - Condensateurs (pour compenser la latence de la régulation)
    
    - **********************Transistors**********************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2031.png)
        
    
    - ********************Diodes (schottky) du redresseur********************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2032.png)
        
    
    - ********************************PFC passif (power factor corrector)********************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2033.png)
        
        Au plus on se rapproche d’une Sinusoïde au mieux c’est
        
    
    - **Passif VS actif**
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2034.png)
        
    
    - ************************************************Single rail VS dual rail************************************************
        
        si on possède une sortie en 12Volt —> en single rail on aura par exemple 32 ampère qui sortiront                 tandis que en dual rail —> on aura 1 sortie “12 volt” qui sortira par exemple 15 ampère et 17 ampère (on nous le vendra comme 2 sortie 12 volt alors que s’en est juste une divisé en 2
        
    
    pour connaitre ce qu’il faut comme alimentation (avec une marge de 100w) 
    
    Formule empirique pour dimensionner une alim :
    **1,5 * (TDP CPU + TGP GPU + 100W)**
    
    - **************************Certification 80 plus**************************
        
        certification qui garanti le rendement ( la non perte d’énergie par la production de chaleur)
        
    
    - **********************************Format de boitier**********************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2035.png)
        
    
    - **********************Connecteurs**********************
        - Pour carte graphique → pci express
        - Pour périphérique SATA (HDD, SDD, Graveur) —> Connecteur SATA 15
        - ATX 24 broche
        - ATX CPU 4/8 broches
        - Connecteur MOLEX (ventilateur, hub, leds, lecteur de cartes, ..)
    
    - ********************************************Alimentation modulaire********************************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2036.png)
        
        l’avantage du modulaire c’est qu’on peut choisir quelles câble on veut brancher
        
    
    - ****************************************************************Comment choisir son alimentation****************************************************************
        1. Calculer la puissance nécessaire :
        1,5 * (CPU TDP + GPU TGP + 100W) ou utiliser un outil :
        [https://outervision.com/power-supply-calculator](https://outervision.com/power-supply-calculator)
        2. Format (ATX, SFX, etc.) et dimensions de l’alimentation
        (Attention aux tailles exotiques)
        3. Nombre de connecteurs en suffisance (attention aux configurations musclées)
        Modulaire ?
        4. Ventilation et nuisance sonore
        ventilateurs thermo-régulés, taille de ventilateur, 0db, passif ?
        5. Rendements (80plus bronze minimum, Gold préféré)
        6. Marque et Prix
    
    # Processeur graphique (GPU)
    
    - **Le processeur graphique (GPU : Graphics Processing Unit)**
        - Intermédiaire entre ordinateur et écran
        - Décharge le plus possible le CPU des calculs d’affichage
        - Accélère les calculs graphiques
        - Le composant le plus important pour les performances en 3D
        - Pour les PC, principalement 3 constructeurs :
        Également utilisé comme coprocesseur de calcul (exemple : calcul scientifique)
    
    - **Formes de GPU**
        - Intégré au CPU (peu performant) :
            - On parle **d'IGP** (Integrated Graphics Processor) pour les tout petits GPU
            - ou **d’APU** (Accelerated Processing Unit) pour les petits GPU
            - ou de **SoC** (System on Chip) quand le CPU contient également tout le reste (carte son, wifi, gestion des SSD, etc.), comme c'est le cas pour les smartphones et tablettes.
            
        - Soudé sur la carte mère :
            - Portables et certains serveurs
        - Sur une carte graphique :
            - Discrete/Dedicated GPU
            
    
    - **************************************A quoi ca ressemble**************************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2037.png)
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2038.png)
        
    
    - ******************************Caractéristique******************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2039.png)
        
        Processeurs de flux → gaming (32 bits)
        
        Unités FP64 → calcul scientifique (64 bits)
        
        Fréquence de base → fréquence a laquelle il fonctionne normalement mais peut être dépassé
        
        - ********************************************Texturing Memory Units (TMUs)********************************************
            
            ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2040.png)
            
        - **Raster Operation Pipelines (ROPs)**
            
            ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2041.png)
            
            notre ordi ne montre qu’en 2D donc il faut transformer le 3D en 2D
            
        - **RT (Ray Tracing) Cores**
            
            ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2042.png)
            
            avant de transformer en 2D on simule les lumière et reflets
            
        - **Tensor Cores**
            
            ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2043.png)
            
            premier cas → on calcule le double de la résolution puis on va vers celle demandé → on aura plus de pixel pour faire le fondu
            
            Deuxième cas → on calcule la moitié de la résolution puis une IA déduis ou mettre et quoi mettre comme pixel (Deep learning Super Sampling)
            
    
    - **************************************************Puissance de calcul théorique**************************************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2044.png)
        
        - **************Exemple**************
            
            ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2045.png)
            
    
    ## Ram carte graphique (sur-estimé)
    
    **********************************Avoir plus de RAM n’accélère rien mais pas avoir assez ralenti tout**********************************
    
    Besoin de beaucoup de RAM pour : 
    
    - Scènes 3D d'une définition élevée
    - Nombreuses textures différentes à charger
    - Textures de haute définition
    
    - **Quantité de mémoire à avoir dessus ( ⚠️ chiffres qui dates)**
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2046.png)
        
    
    - ******************************************************************************La bande passante mémoire (sous-estimé)******************************************************************************
        
        Les GPU peuvent avoir des milliers de cœurs de calcul donc il faut savoir les alimentées en données donc besoin de bande passante pour transférer beaucoup de donnée
        
        Fréquence de fonctionnement x largeur de bus = bande passante mémoire
        
        Fréquence x coefficient = fréquence logique
        
        𝐵𝑎𝑛𝑑𝑒 𝑝𝑎𝑠𝑠𝑎𝑛𝑡𝑒 𝑒𝑛 𝑜𝑐𝑡𝑒𝑡𝑠 𝑝𝑎𝑟 𝑠𝑒𝑐𝑜𝑛𝑑𝑒 = 𝐹𝑟é𝑞𝑢𝑒𝑛𝑐𝑒 𝒍𝒐𝒈𝒊𝒒𝒖𝒆 x 𝑏𝑢𝑠 𝑒𝑛 𝑏𝑖𝑡𝑠/8
        
    
    ## Interface (bus graphique)
    
    En général PCI-Express x16
    
    - ************************Consommation************************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2047.png)
        
    
    - ********Refroidissement********
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2048.png)
        
        passif → radiateur thermique
        
        actif → ventirad
        
        Blower → bruyant
        
    
    ## Connectique (sortie écran)
    
    ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2049.png)
    
    **************************************Système a plusieurs cartes :************************************** 
    
    **Cumuler la puissance de calcul de plusieurs cartes graphiques pour accélérer ses jeux…**
    
    - La carte mère doit disposer d’autant de connecteurs qu’il y a de cartes
    - La carte mère doit être compatible avec cette fonctionnalité
    - Les cartes doivent être compatibles entre-elles
    
    ⚠️ 2 cartes combinées n'offrent pas 2 fois les performances d'une seule carte :
    
    - elles s'en approchent dans certains cas
    - le gain peut être négatif dans d’autres
    - le prix est toujours double !
    
    Par contre, pour le calcul sur GPU, un systèmes à plusieurs cartes fait sens
    
    ******************************************************************************************************************Support logiciel (API (Application Programming interface)******************************************************************************************************************
    
    ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2050.png)
    
    - ******************************************************************Les 3 gammes de cartes graphiques******************************************************************
        - **GPU Grand Public**
            - Les cartes et les drivers graphiques sont :
                - Optimisés pour le jeu vidéo
                - Très bridés pour les logiciels professionnels (Maya, Catia, etc.)
        - **********GPU pour Imagerie professionnel**********
            - Les cartes et les drivers graphiques sont :
                - Non optimisés pour le jeu vidéo (mais performances OK)
                - Optimisés pour les logiciels professionnels (Maya, Catia, etc.)
        - **************************************GPU dédié au calcul**************************************
            - Absence de sortie écran et ne sert qu’au calcul
    
    ******************Importance du CPU :******************
    
    Si basse révolution le CPU travaillera plus mais si haute révolution c’est le GPU qui travaillera plus
    
    ## Les boitiers
    
    - **Types de boitiers**
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2051.png)
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2052.png)
        
    
    **************************************************************Importances d’un “bon” boitier :**************************************************************
    
    - **Modularité**
        
        Vérifier si formats acceptables pour la carte mère (ATX, micro-ATX, etc.)
        Nombre d'emplacements :
        
        - 2,5" (SSD)
        - 3,5" internes (HDD) et 3.5" externe (Floppy, SD-reader, etc.)
        - 5,25" internes (rien) et 5,25" externe (DVD, Blu-Ray, rhéobus, etc.)
        
        **Espace suffisant pour :**
        
        - Alimentation de taille exotique ?
        - Carte graphique de grande taille ?
        - Ventirad (hauteur) ou watercooling ?
    - ************************Connectivité************************
        
        Les fiches en façade :
        
        - USB 2 ou 3 ou type C
        - Audio
        - Firewire
        - eSATA
        
        Le boitier ne fournit que la connectique :
        
        - Ne pas oublier de câbler ces fiches à la carte mère
        - … à condition que la carte mère le permette…
    - **********************VENTILATION**********************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2053.png)
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2054.png)
        
        Il existe aussi des filtres pour ne pas laisser passer la poussière
        
        - ****************************Les ventilateurs****************************
            
            Dimension (mm) : (80, 92( moins courant),) 120, 140, 200
            Vitesse de rotation **mini/maxi (rpm)**
            **Débit d'air mini/maxi (CFM) <- à favoriser pour la ventilation d'un boitier
            Pression statique (mm H2O) <- à favoriser pour la ventilation d'un radiateur
            Niveau sonore maxi (dB)
            Type de roulement (à bille, hydraulique, magnétique)**
            Favoriser la régulation PWM
            Connectique
            Leds (RGB ?)
            
    - ******************************Nuisance sonore******************************
        
        Sources de nuisances sonores :
        
        - Ventilation :
        - Qualité des ventilateurs
        - Thermorégulation
        - Matériaux utilisés
        - Revêtement de réduction acoustique (pas courant)
        - Vibrations :
        - Qualité d'assemblage
        - Fixation des disques durs et ventilateurs
        - Avec un PC silencieux vous pourrez entendre le coil whine
    - ****Look****
    
    ## Les Ecrans
    
    **********************************************La taille et la définition ne sont pas les seules paramètres, l’écran est sans doute l’élément le plus important (et souvent négligé)**********************************************
    
    - **********Les écrans LCD (TFT, LED)**********
        
        Fonctionnement LCD :
        
        **Repose sur deux principes de ces matériaux très particuliers :**
        
        - Les rayons lumineux qui les traversent s'alignent sur la direction
        dans laquelle sont orientées leurs molécules
        - Lorsque les molécules sont parcourues par un courant électrique,
        les molécules s’alignent dans le sens du courant
        
        Pour maitriser l’orientation des cristaux liquides, il faut connaitre l’orientation
        initiale
        des plaques d'alignement avec de micros-sillons.
        les molécules s'alignent sur la direction des sillons.
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2055.png)
        
        pas etudier (pas exam)
        
        - **********Caractéristique de base**********
            - **taille (diagonale en pouce (”))**
            - ******************************************************Définition en pixel (L x H)******************************************************
            
            ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2056.png)
            
            - **Luminosité (cd/m2)** : critère important si la luminosité ambiante est élevée
            - **Taux de contraste (ratio)** : rapport d'intensité lumineuse entre blanc et noir
            - **Fréquence de rafraichissement**
            - **Temps de réponse**
            - **Type de dalle**
    
    **********************************Rétroéclairage :********************************** 
    
    - **EDGE LED** : les LED sont placées sous le contour de l’écran et éclairent une plaque photoconductrice qui propage la lumière dans la dalle
    - **FULL LED** : Les LED sont placées sous toutes la surface de l’écran. Luminosité et contraste plus uniforme
    - **FULL LED + LOCALDIMING** : identique au FULL LED avec en plus la capacité traiter la luminosité des LED par zone. Le contraste en est amélioré
    - **Mini-LED (Neo LED)** = FULL LED mais avec encore plus de LED (plus de zones)
    
    **********************************************************Le taux de rafraichissement (fréquence quand les images sont rénouvelées :**********************************************************
    
    **Avec les écrans actuels (LCD) 50 Hz (TV) ou 60 (PC) Hz sont bien suffisants car
    il n'y a plus d'effet de clignotement (en théorie)**
    
    - De nombreux rétroéclairages LED clignotent à haute fréquence
    La fonction flicker-free permet d'éviter ce phénomène
    - Les écrans à f. de rafraichissement élevée (> 100Hz) font volontairement
    clignoter le rétroéclairage pour augmenter la fluidité (black frame insertion)
    
    ******************************************************Temps de réponse  :******************************************************
    
    Temps qu'il faut pour que les cristaux changent d'orientation, pour bloquer
    le passage de la lumière, et reviennent dans leur position d'origine (**LCD —> 20 ms a 0,1 ms)**
    
    Au **moins** **grand** est le **temps** de **réponse** au **moins** on aura un **effets** de **flou**
    
    ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2057.png)
    
    ****************************Les pixels mort :**************************** 
    
    Les écrans LCD sont fragile et certaines matrices soient commercialisé avec des pixels défectueux, lorsqu’un transistor ne fonctionne plus, il laissera alors toujours passer la lumière (ou pas du tout)
    
    ## Ecran OLED
    
    - **OLED ( Organic Light-Emitting Diode)**
        
        Pas besoin de rétro-éclairage : la couche organique produit sa propre
        lumière. Le noir serra alors parfaitement noir
        
    
    - **********************OLED VS LCD**********************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2058.png)
        
        BURN IN —> quand les touches sont brulées sur l’écran
        
    
    - **********************************QLED (Quantum LED (ne contient aucune Quantum LED en réalité))**********************************
        
        **Un écran QLED = Ecran LCD classique…
        avec un rétroéclairage bleu
        et un filtre de couleur utilisant des tube "Quantum Dots"
        ce qui améliore les couleurs par rapport à un LCD de base…**
        
        —> **********************************D’ou le nom QLED (pour Quantum dots LED …)**********************************
        
    
    ********HDR (High Dynamic Range) → amélioration dynamique des contrastes********
    
    Si pas HDR —> SDR (Standard Dynamic Range)
    
    Input lag = Temps de calcul du PC + Temps d’affichage 
    
    ******Taux de rafraichissement dynamique :****** 
    
    **Varie le taux d'affichage de l'écran pour qu'il coïncide avec le nombre d'image/seconde que le PC arrive à calculer**
    
    L'avantage c'est quand les FPS sont :
    
    < la fréquence de rafraichissement : meilleure impression de fluidité
    
    > la fréquence de rafraichissement : pas de déchirure d'image
    
    Inconvénient :
    
    - Plusieurs normes de FreeSync et de Gsync
    - Toute la chaine doit être compatible
    - Les écrans compatibles ne descendent
    pas toujours suffisamment bas en fréquence
    
    Motion Interpolation → post-traitement qui a pour but de fluidifier les séquence vidéo
    
    - ******************En résumé******************
        
        ![Untitled](Architecture%20des%20ordinateurs%20745a9fa757254762996dd15a60ed0cee/Untitled%2059.png)