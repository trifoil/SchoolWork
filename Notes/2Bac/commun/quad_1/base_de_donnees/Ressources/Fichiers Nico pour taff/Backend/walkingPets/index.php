<?php
require '_bd.php'; // Nécessité la connexion à la base de données
session_start(); //démarrage de la session

// Récupération des données de la table pets et des catégories associées
$pet_list=$bd->prepare('SELECT p.id_pet, p.name, p.walks, p.meals, p.comment, p.id_cat, c.icon, c.max_walks FROM pets AS p LEFT JOIN categories AS c ON p.id_cat = c.id_cat ORDER BY p.name ASC');
$pet_list->execute();
$pet_list->setFetchMode(PDO::FETCH_OBJ);

if (isset($_SESSION['LAST_ACTIVITY']) && (time() - $_SESSION['LAST_ACTIVITY'] > 1800)) { // Il mieux de définir ça sur le serveur
    // last request was more than 30 minutes ago
    session_unset();     // unset $_SESSION variable for the run-time 
    session_destroy();   // destroy session data in storage
}
$_SESSION['LAST_ACTIVITY'] = time(); // update last activity time stamp

?><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">  
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Walking Pets</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐾</text></svg>"/>
</head>
<body>
    <?php include '_header.php';?> <!-- Inclusion du header -->
    <div class="pets">
        <?php // Affichage des données des animaux de compagnie
        while ($result=$pet_list->fetch() ) {
            echo "<div class='pet'><a href='modif_pet.php?pet=". $result->id_pet. "'>"; // Lien vers la page de modification
            if ($result->id_cat == 0) {echo "<img src='icons/unknown.png' alt='icon'>";} // Si l'animal n'a pas de catégorie, on affiche une icône par défaut
            else {echo "<img src='icons/". $result->icon. "' alt='icon'>";}
            if (isset($_SESSION['pets'])) { // Si l'animal a été modifié, on affiche son nom en gras
                if (in_array($result->id_pet, $_SESSION['pets'])){
                    echo "<h2 class='modified'>". $result->name. "</h2>";
                } else {echo "<h2>". $result->name. "</h2>";}
            } else {echo "<h2>". $result->name. "</h2>";}
            if ($result->id_cat == 0) {echo "<p>". "walks : <span>". $result->walks. "</span> 0";} // Si l'animal n'a pas de catégorie, on affiche 0 promenade
            elseif ($result->walks > $result->max_walks) {echo "<p>". "walks : <span>". $result->walks. "</span> ". $result->max_walks;}
            else {echo "<p>". "walks : ". $result->walks;}
            echo "<p>". "meals : ". $result->meals; // Affichage du nombre de repas
            echo "</a>";
            if ($result->comment != "") {echo "<p class='comment' title='". $result->comment. "'> - remarque -";} // Si l'animal a une remarque, on affiche un message
            echo "</div>";
        }?>
    </div>
    <footer>
        <p>*seuls les chien et les chats ont droits aux promenades avec un maximum de 2 promenades par jour pour les chiens et 1 pour les chats.
    </footer>
</body>
</html>