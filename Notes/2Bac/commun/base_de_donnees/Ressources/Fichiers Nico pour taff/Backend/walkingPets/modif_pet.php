<?php
require '_bd.php';
session_start();	//démarrage de la session

// Récupération des données de la table pets et des catégories associées
$pet=$bd->prepare('SELECT p.id_pet, p.name, p.walks, p.meals, p.comment, p.id_cat FROM pets AS p WHERE p.id_pet = :id'); 
$pet->bindValue(':id', (int) $_GET['pet']);
$pet->execute();
$pet->setFetchMode(PDO::FETCH_OBJ);
if ($pet->rowCount() == 0) {
    header('Location: index.php');
} else {
    $result=$pet->fetch();
};
$pet->closeCursor();

// Update de la base de données avec les nouvelles données
if (isset($_POST['save'])) {
    $modifBD = $bd->prepare('UPDATE pets SET walks=:walks, meals=:meals, comment=:comment WHERE id_pet=:id');
    $modifBD->bindValue(':id', (int) $_GET['pet']);
if ($_POST['walks'] >= 0) { // On vérifie que les valeurs entrées sont positives
    $modifBD->bindValue(':walks', (int) $_POST['walks']); // Si oui, on les enregistre (forcé en entiers)
} else {
    $modifBD->bindValue(':walks', 0); // Si non, on enregistre 0
};
if ($_POST['meals'] >= 0) {
    $modifBD->bindValue(':meals', (int) $_POST['meals']);
} else {
    $modifBD->bindValue(':meals', 0);
};
if (isset($_POST['comment'])) {
    $modifBD->bindValue(':comment', $_POST['comment']);
} else {
    $modifBD->bindValue(':comment', '');
};
$modifBD->execute(); // On exécute la requête
$_SESSION['pets'][] = $_GET['pet']; // On enregistre l'animal modifié dans la session
$modifBD->closeCursor();
header('Location: index.php'); // On retourne à la page d'accueil
}

?><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">  
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Walking Pets | Mofications</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐾</text></svg>"/>
</head>
<body>
    <?php include '_header.php';?>
    <div class="form">
        <img src="./icons/leash.png" alt="leash_icon">
        <h3><?=$result->name?></h3>
        <form method="post" action=<?="modif_pet.php?pet=".$result->id_pet?>> <!-- Formulaire de modification -->
            <p><label for="walks">walks :
                <input type="number" id="walks" name="walks" min="0" value="<?=$result->walks?>">
            </label>
            <p><label for="meals">meals :
                <input type="number" id="meals" name="meals" min="0" value="<?=$result->meals?>">
            </label>
            <p><label for="comment">comment :
                <textarea id="comment" name="comment" cols="40"><?=$result->comment?></textarea>
            </label>
            <p><input type="submit" name="save" value="Enregistrer">
        </form>
    </div>
    <footer>
        <p>*seuls les chien et les chats ont droits aux promenades avec un maximum de 2 promenades par jour pour les chiens et 1 pour les chats.
    </footer>
</body>
</html>
