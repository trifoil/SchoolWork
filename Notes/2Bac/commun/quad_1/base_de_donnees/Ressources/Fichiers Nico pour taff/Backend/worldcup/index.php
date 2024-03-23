<?php
require '_bd.php'; // Nécessité la connexion à la base de données

// Récupération des pays du classement final
$country_list=$bd->prepare('SELECT p.place, p.code, e.pays FROM participations AS p LEFT JOIN equipes AS e ON p.code=e.code ORDER BY p.place ASC LIMIT 8');
$country_list->execute();
$country_list->setFetchMode(PDO::FETCH_OBJ);

// Récupération des meilleurs buteurs
$player_list=$bd->prepare('SELECT COUNT(b.id_but) AS buts, j.equipe, j.nom FROM buts AS b LEFT JOIN participations AS p ON p.code=b.equipe LEFT JOIN joueurs AS j ON b.id_joueur=j.id_joueur WHERE (b.contre_son_camp=0 AND b.penalty=0) GROUP BY b.id_joueur HAVING buts>2 ORDER BY buts DESC, ANY_VALUE(p.place), j.nom');
$player_list->execute();
$player_list->setFetchMode(PDO::FETCH_OBJ);
$max=$bd->query('SELECT MAX(table1.buts) AS max FROM (SELECT COUNT(b.id_but) AS buts, j.equipe, j.nom FROM buts AS b LEFT JOIN joueurs AS j ON b.id_joueur=j.id_joueur WHERE (b.contre_son_camp=0 AND b.penalty=0) GROUP BY b.id_joueur) AS table1');
foreach ($max as $max_) {$max = $max_['max'];}

// Récupération des pays ayant participé à la coupe du monde
$countries=$bd->query('SELECT e.pays, e.code FROM participations AS p LEFT JOIN equipes AS e ON p.code=e.code ORDER BY pays ASC');

// Récupération des joueurs de l'équipe sélectionnée
if (isset($_GET["nation"])) {
    $country_player=$bd->prepare('SELECT j.nom, j.prenom, j.naissance FROM joueurs AS j WHERE j.equipe=:nation ORDER BY j.nom, j.prenom ASC');
    $country_player->bindValue(':nation', $_GET["nation"]);
    $country_player->execute();
    $country_player->setFetchMode(PDO::FETCH_OBJ);
} else {
    $country_player=$bd->query('SELECT j.nom, j.prenom, j.naissance FROM joueurs AS j WHERE j.equipe="GER" ORDER BY j.nom, j.prenom ASC');
    $country_player->setFetchMode(PDO::FETCH_OBJ);
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
    <h1>🏆 World Cup 2018</h1>
    <div class="flex">
    <div>
        <h2>Classement final</h2>
        <?php
        $compteur=0;
        while ($result=$country_list->fetch() ) {
            $compteur++;
            if ($compteur<=3) {
                echo '<div class="pays bold">';
            } else {
                echo '<div class="pays">';
            }
            echo '<a href="index.php?nation='.$result->code.'">';
            echo $result->place, ' ';
            echo '<img src="flags/'.$result->code.'.webp">', ' ';
            echo $result->pays;
            echo '</a>';
            echo '</div>';
        }
    ?></div>
    <div>
        <h2>Meilleurs buteurs</h2>
        <?php
        while ($result=$player_list->fetch() ) {
            if ($max==$result->buts) {
                echo '<div class="joueur bold">';
            } else {
                echo '<div class="joueur">';
            }
            echo '<img src="flags/'.$result->equipe.'.webp">', ' ';
            echo $result->nom. ' : ';
            echo $result->buts;
            echo '</div>';
        }
    ?></div>
    <div>
        <h2>Joueurs</h2>
        <form method="GET" action="index.php" id="form">
            <fieldset>
                <legend>Choix de l'équipe</legend>
                <select id="nation" form="form" name="nation" placeholder="Sélectionner nationalité">
					<?php
                        foreach ($countries as $country) {
                            if (isset($_GET["nation"]) && $_GET["nation"]==$country['code']) {
                                echo '<option value="'.$country['code'].'" selected>'.$country['pays'].'</option>';
                            } else {
                                echo '<option value="'.$country['code'].'">'.$country['pays'].'</option>';
                            }
                        }
                    ?>
                <input type="submit" name="save" value="Voir les joueurs">
            </fieldset>
        </form>
        <?php
        while ($result=$country_player->fetch()) {
            echo '<div class="joueur">';
            echo $result->prenom, ' ';
            echo '<b>',$result->nom, '</b> ';
            echo '(',$result->naissance,')';
            echo '</div>';
        }
    ?></div>
    </div>
</body>
</html>