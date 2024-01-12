# Questions d'examen de Windows Server

* Attention à fsmo, les groupes, agdlp, ldap plus question sur le bail. Config de base du dhcp aussi

* Question : Combien d’adresse IPv4 puis-je avoir dans le sous réseaux 192.168.14.0/25 ?
    * Réponse (2^32-25)-2 (une pour le broadcast et une pour le NetID)

* Un serveur DHCP distribue des adresses IP avec un bail de 12h. En combien de temps le PC client va-t-il renouveler son bail pour la première fois ?
    * Réponse : 50% du bail, donc 6h. (Attention à l’examen, il peut rajouter des plages horaires avec des démarrages et redémarrages. Les redémarrages comptent pour une réinitialisation du bail.

* Expliquez AGDLP :
    * Réponse : Division en deux parties avec les utilisateurs dans les groupes globaux et de l’autre les dossiers partagés avec des groupe locaux de domaine. C’est là qu’on attribue aussi les règles avec RW et R.

* Je dois installer des nouveaux serveurs dans une infrastructure existante. Lors de l’installation, je dois choisir le niveau fonctionnel de mes serveurs. Quel niveau vais-je choisir en sachant que mon infrastructure compte plusieurs versions de Windows Server ?
    * Le niveau qui correspond au serveur que j’installe 
    * Le niveau qui correspond à la version la plus élevée
    * Le niveau qui correspond à la version la plus basse ✅

* Définir la notion de site dans un domaine AD :
    * Réponse : Sous domaine relié entre eux par une liaisons haut débit.

* Donner le nom unique (DN) de l’ordinateur CLIENT7 (voir photo) :
    * Réponse : CN = Client7, CN  = Computers, DC = belgique, DC = lan

* Que peut contenir un groupe global et quelle est son étendue :
    * Réponse : Utilisateur du même domaine et étendue visible dans l’ensemble de la forêt
 
* Expliquer l’enregistrement SOA dans un serveur DNS :
    * Réponse : Enregistrement du Start Of Autority, celui qui est en RW sur sa base de données. Il contient les informations importantes sur un domaine ou une zone 

* Différence entre zone de recherche directe et inverse :
    * Réponse : 
        * Directe : nom  IP en retour 
        * Inverse : IP  nom en retour 

* Expliquer le RID Master :
    * Réponse : Le Relative ID Master est le DC qui génère l’ensemble des RID et qui les partage au DC du domaine.

* P204 q d'exam : conflits