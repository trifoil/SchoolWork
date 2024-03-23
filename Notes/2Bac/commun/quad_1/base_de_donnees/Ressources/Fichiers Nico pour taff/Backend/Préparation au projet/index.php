<?php
require_once '_model.php'; // Nécessité la connexion à la base de données
session_start(); //démarrage de la session
$Base = new bd(); // Création de l'objet bd


// Système de connexion
if ( isset($_POST['connexion']) ) {
    $DOMAIN = "test.lan";
    $ldaprdn = trim($_POST['login'])."@".$DOMAIN;
	$ldappass = trim($_POST['password']);
    $ldapconn = ldap_connect("SRV-TEST") or die("Could not connect to LDAP server.");
	ldap_set_option($ldapconn, LDAP_OPT_PROTOCOL_VERSION, 3);
	ldap_set_option($ldapconn, LDAP_OPT_REFERRALS, 0);

    if ($ldapconn) {
        if ($ldaprdn == "" || $ldappass == "") {echo "<p>Erreur dans l'identifiant ou le mot de passe</p>";}
        elseif (@ldap_bind($ldapconn, $ldaprdn, $ldappass)) {
            $_SESSION['login']=$ldaprdn;
            header('Location:index.php'); //on redirige pour vider $_POST
            exit();
        }
        else {echo "<p>Erreur dans l'identifiant ou le mot de passe</p>" ;}
    }
}
else if ( isset($_POST['deconnexion']) ) {
	session_destroy() ;		//on détruit la session
	header('Location:index.php');	//on redirige
}


// Affichage de la vue des différentes pages
if ( empty($_SESSION) ) {
    include '_connexion.html';
}
else {
    if (isset($_GET['pet'])) { // Si on a cliqué sur un animal, on affiche la page de modification
        // Récupération des données de l'animal à modifier
        $result=$Base->get_pet($_GET['pet']);

        // Update de la base de données avec les nouvelles données
        if (isset($_POST['save'])) {
            $Base->modify_pet((int) $_GET['pet'], $_POST['walks'], $_POST['meals'], $_POST['comment']);
            $_SESSION['pets'][] = $_GET['pet']; // On enregistre l'animal modifié dans la session
            header('Location: index.php'); // retour à la page d'accueil
        }

        include '_vue_modif_pet.php';
    }
    else {
        // Récupération et formatage des catégories pour le header
        $reqCat = $Base->get_categories(); 
        $categories = "- ";
        foreach ($reqCat as $cat) {$categories.= $cat['name']. " - ";}

        // Récupération des données des animaux de compagnie
        $pet_list = $Base->get_pets();

        include '_vue.php';
    }
} 
?>
