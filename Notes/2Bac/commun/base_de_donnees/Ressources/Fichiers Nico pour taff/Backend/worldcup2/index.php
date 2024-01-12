<?php 
require_once '_connexionBD.php';
session_start();

# Get the last 8 matchs 
$matchs=$DB->query("SELECT e1.pays AS pays1, e2.pays AS pays2, m.score1, m.score2, e1.id_continent AS continent1, e2.id_continent AS continent2
                    FROM `matchs` AS m 
                    JOIN `equipes` AS e1 ON (m.equipe1=e1.code) 
                    JOIN `equipes` AS e2 ON (m.equipe2=e2.code) 
                    ORDER BY m.date DESC LIMIT 8;");
$matchs->setFetchMode(PDO::FETCH_OBJ);

# Get biggest stadiums
$stades=$DB->query("SELECT s.nom, COUNT(m.id_match) AS nbr_matchs, ROUND(AVG(m.spectateurs), 1) AS moy_spec
                    FROM `stades` AS s JOIN `matchs` AS m ON (s.id_stade=m.id_stade)
                    GROUP BY m.id_stade 
                    HAVING nbr_matchs > 4
                    ORDER BY moy_spec DESC;");
$stades->setFetchMode(PDO::FETCH_OBJ);

# Get continents
$continents=$DB->query("SELECT c.continent as nom, c.id_continent AS id FROM `continents` AS c;");
$continents->setFetchMode(PDO::FETCH_OBJ);
$continents=$continents->fetchAll();

# Get countries from continent
$pays=$DB->prepare("SELECT e.code, e.pays, p.place
                    FROM `equipes` AS e 
                    JOIN `continents` AS c ON (e.id_continent=c.id_continent) 
                    JOIN `participations` AS p ON (e.code=p.code) 
                    WHERE c.id_continent=?;");

# Create a white list for existing continents
$continents_list = array();
foreach ($continents as $continent) {
    array_push($continents_list, $continent->id);
}

# Check if existing continent is selected
if (isset($_GET["continent"])) {
    if (in_array($_GET["continent"], $continents_list)) {
        $selected_continent=$_GET["continent"];
        $pays->execute(array($selected_continent));
        $pays->setFetchMode(PDO::FETCH_OBJ);
    } else {
        header('location:index.php');
        exit;
    }
}
?><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">  
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Exo+2&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>World Cup 2018</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏆</text></svg>"/>
</head>
<body>
    <h1><a href="index.php">🏆 World Cup 2018</a></h1>
    <div class="flex">
        <div>
            <h2>8 derniers matchs</h2>
            <?php while ($match=$matchs->fetch()){
                if (isset($selected_continent)) {
                    if ($match->continent1==$selected_continent) {
                        $the_match = "<span class=bold>".$match->pays1."</span>";
                    } else {$the_match = $match->pays1;}
                    $the_match = $the_match." - ";
                    if ($match->continent2==$selected_continent) {
                        $the_match = $the_match."<span class=bold>".$match->pays2."</span>";
                    } else {$the_match = $the_match.$match->pays2;}
                    $the_match = $the_match." : ".$match->score1." - ".$match->score2;
                } else {
                    $the_match = $match->pays1." - ".$match->pays2." : ".$match->score1." - ".$match->score2;
                }
                echo "<p>".$the_match."</p>";
            } ?>
        </div>
        <div>
            <h2>Principaux stades</h2>
            <?php while($stade=$stades->fetch()){
                echo "<p><span class=bold>".$stade->nom."</span> : ".$stade->moy_spec." spectateurs moy. ; ".$stade->nbr_matchs." matchs</p>";
            } ?>
        </div>
        <div>
            <h2>Pays participants</h2>
            <form method="GET" action="index.php" id="form">
                <fieldset>
                    <legend>Choix du continent</legend>
                    <select id="continent" form="form" name="continent">
                        <option value="" disabled selected>Sélectionner un continent</option>
                        <?php foreach ($continents as $continent){
                            if (isset($_GET["continent"]) && $_GET["continent"]==$continent->id) {
                                echo '<option value="'.$continent->id.'" selected>'.$continent->nom.'</option>';
                            } else {
                                echo '<option value="'.$continent->id.'">'.$continent->nom.'</option>';
                            }
                        } ?>
                    <input type="submit" name="save" value="Voir les pays participants">
                </fieldset>
            </form>
            <?php while ($pays1=$pays->fetch()){
                if ($pays1->place<9) {
                    $the_pays="<img src='flags/".$pays1->code.".webp' alt='Drapeau ".$pays1->pays."'> <span class=bold>".$pays1->pays."</span> : ".$pays1->place."ᵉ";
                } else {
                    $the_pays="<img src='flags/".$pays1->code.".webp' alt='Drapeau ".$pays1->pays."'> <span class=bold>".$pays1->pays."</span>";
                }
                echo "<p>".$the_pays."</p>";
            } ?>
        </div>
    </div>
</body>
</html>