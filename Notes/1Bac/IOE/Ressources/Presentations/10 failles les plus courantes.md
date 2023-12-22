Un groupe de recherche Open Source publie la liste des dix failles web les plus courantes. L'objectif est de réveiller les administrateurs et les développeurs, qui souvent ignorent jusqu'aux vulnérabilités les plus simples. C'est aussi une bonne check-list pour valider son propre site.

L'OWASP (Open Web Application Security Project) est un projet Open Source. Il réunit des experts bénévoles autour d'un objectif commun : éduquer les professionnels du web en matière de sécurité. Le groupe vient pour cela de publier la liste des dix failles les plus courantes sur le web. Elles sont pour la plupart connues depuis très longtemps mais, étrangement, de nombreux projets web en sont encore victimes aujourd'hui.

L'objectif avoué de l'OWASP est de donner une arme aux entreprises lorsqu'elles commandent un développement web : elles peuvent désormais inclure dans le contrat avec leur prestataire cette liste de failles stupides à éviter. Toutes sont parfaitement parables, pour peu que l'on se donne la peine de les connaître.

Voici les dix erreurs-type dénoncées par l'OWASP :

1. Oubli de valider les entrées des utilisateurs.
Un classique, qui permet aux pirates de faire accepter des commandes au serveur à travers un formulaire web ou une simple URL, ou d'exécuter des contenus dynamiques (Javascript, par exemple) chez les autres utilisateurs d'un site.

2. Contrôle d'accès inefficace.
Mauvaise mise en oeuvre des outils de contrôle d'accès (fichier .htpasswd lisible par tous, mots de passes nuls par défaut, etc...).

3. Mauvaise gestion des sessions.
Cela permet aux pirates de "voler des sessions" d'autres utilisateurs (en devinant un numéro de session simple, en dérobant un cookie, ou en allant regarder les fichiers de sessions de PHP).

4. Cross Site Scripting.
Un autre grand classique, lui aussi lié à un manque de contrôle des entrées de l'utilisateur. Cette faille touche les sites web qui laissent les internautes publier du code HTML susceptible d'être vu par les autres utilisateurs du site (dans un forum, par exemple). Cela permet d'exécuter des contenus dynamiques sur les navigateurs des internautes, avec les droits associés au site web.

5. Dépassement de mémoire tampon.
Une faille vieille comme le monde, qui frappe certains langages de programmation plus que d'autres (le C, par exemple). Si des composants CGI sont (mal) écrits dans ces langages, il peut-être simple de compromettre totalement le serveur par une telle attaque.

6. Injection de commandes.
Là encore, la source de la faille est un manque de contrôle des entrées de l'utilisateur. Elle permet au pirate de faire exécuter des commandes au serveur (au système d'exploitation ou à un serveur SQL, par exemple) en les attachant à une entrée web légitime avant que celle-ci ne soit transmise au serveur.

7. Mauvaise gestion des erreurs.
Les messages d'erreur utiles aux développeurs le sont souvent aussi pour les pirates ! Il faut donc penser à les supprimer une fois le développement terminé.

8. Mauvaise utilisation du chiffrement.
La mise en oeuvre du chiffrement au sein des applications web se révèle ardue. Des développeurs non spécialisés peuvent commettre des erreurs difficiles à déceler et créer ainsi une protection illusoire.

9. Failles dans l'administration distante.
C'est la voie royale : si les pages réservées aux administrateurs du site ne sont pas réellement protégées (authentification forte du client, chiffrement, contrôles réguliers...), un pirate peut prendre le contrôle du site sans avoir à pirater le serveur. Une aubaine, en quelque sorte.

10. Mauvaise configuration du serveur web et des applications.
Un classique : le serveur web qui permet de lister n'importe quel répertoire, ou les outils de développement qui laissent des versions temporaires des fichiers, lisibles par tout le monde. Avant de mettre un serveur en ligne, il est bon de faire le ménage et de bien comprendre toutes les options de ses fichiers de configuration...

Toutes ces failles sont à l'origine de la très grande majorité des piratages sur le web. Elles sont bien sûr parfois difficiles à traquer à posteriori, mais en les prenant en compte dès le début d'un projet, il est possible de les minimiser de façon efficace. Encore faut-il y penser...

Source : https://www.futura-sciences.com/tech/actualites/tech-top-10-failles-web-plus-courantes-1625/
