<?php

require_once('_connexionBD.php');

$req_match = $bd->query('SELECT pays1,pays2,score1,score2,continent1,continent2
FROM(SELECT p1.pays as pays1,p2.pays as pays2,score1,score2,id_match,p1.id_continent as continent1,p2.id_continent as continent2  FROM matchs 
     JOIN equipes p1 ON p1.code = matchs.equipe1
     JOIN equipes p2 ON p2.code = matchs.equipe2
     ORDER BY id_match DESC LIMIT 8) AS test
ORDER BY test.id_match');



$req_stade = $bd->query('SELECT matchs.id_stade, AVG(matchs.spectateurs) as nbr_spectateur, stades.nom as nom, count(*) as nbr 
from matchs 
RIGHT JOIN stades 
ON matchs.id_stade = stades.id_stade 
GROUP BY id_stade 
HAVING nbr > 4 
ORDER BY nbr_spectateur DESC');

$req_select = $bd->query('SELECT * FROM continents');

if (isset($_GET['continent'])){
    $id = $_GET['continent'];
    $req_pays = $bd->prepare('SELECT equipes.code, equipes.pays , participations.place from equipes LEFT JOIN continents ON continents.id_continent = equipes.id_continent LEFT join participations ON equipes.code = participations.code where continents.id_continent=:id HAVING place');
    $req_pays->bindValue(':id',$id);
    $req_pays->execute();

}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WorldCup2</title>
</head>
<body>
    <h2>Les 8 derniers matchs</h2>
    <?php
    while($data = $req_match->fetch()){
        echo '<p>';
        if (isset($id)) if($data['continent1']==$id) echo '<b>';
        echo $data['pays1'];
        if (isset($id))  if($data['continent1']==$id) echo '</b>';
        echo ' - ';
        if (isset($id))  if($data['continent2']==$id) echo '<b>';
        echo $data['pays2'];
        if (isset($id))  if($data['continent2']==$id) echo '</b>';
        echo' : '.$data['score1'].' - '.$data['score2'].'</p>';
    }
    

    ?>
    <h2>Principaux stade</h2>
    <?php


    while ($stade = $req_stade->fetch()) {
        echo '<p><b>'.$stade['nom'].'</b>'.' : '.number_format($stade['nbr_spectateur'],1,'.','').' spectateurs moy ; '.$stade['nbr'].' matchs</p>';
    }
?>
<form action="index.php" method="get"> 
    <select name="continent">
<?php
    while($continent = $req_select->fetch()){
        if(isset($id)&&$continent['id_continent'] == $id){
            echo '<option selected value="'.$continent['id_continent'].'">'.$continent['acronyme'].' : '.$continent['continent'].'</option>';

        }
        else{
        echo '<option value="'.$continent['id_continent'].'">'.$continent['acronyme'].' : '.$continent['continent'].'</option>';
        }
    }

    ?>
    </select>
<input type="submit">
</form>
<?php
if (isset($id)){
while($data = $req_pays->fetch()){
    if($data['place'] >= 8){
        echo '<p> <img src="flags/'.$data['code'].'.webp">  <b>'.$data['pays'].'</b>' ;
    }
    else{
        echo '<p> <img src="flags/'.$data['code'].'.webp">  <b>'.$data['pays'].'</b> : '.$data['place'].'e' ;
    }
}
}
?>
<img src="" alt="">
</body>
</html>