<?php
require('_connexionBD.php');

$req_classement = $bd->query('SELECT participations.code,participations.place,equipes.pays FROM participations JOIN equipes ON equipes.code=participations.code ORDER BY participations.place LIMIT 16 ') ;

$req_but = $bd->query('SELECT joueurs.equipe, nom, COUNT(id_but) AS nb, participations.place FROM joueurs JOIN buts ON buts.id_joueur = joueurs.id_joueur JOIN participations ON participations.code = joueurs.equipe WHERE penalty = 0 AND contre_son_camp = 0 GROUP BY joueurs.equipe, nom, participations.place HAVING nb >= 3 ORDER BY nb DESC, participations.place ASC, nom ASC');
echo '<h1> Classsement </h1>';

while($data = $req_classement->fetch()){
    
    if($data['place']<4){
        echo '<b>';
    }
    echo $data['place'];
    
    echo '<img src="flags/'.$data['code'].'.webp" >';
    
    echo $data['pays'].'<br>';
    
    if($data['place']<4){
        echo '</b>';
    }

}

















echo '<h1>Meilleur buteur</h1>';
while($tmp = $req_but->fetch()){
    echo '<img src="flags/'.$tmp['equipe'].'.webp">';
    echo $tmp['nom'];
    echo ' : ';
    echo $tmp['nb'];
    echo '<br>';

}




?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    
</body>
</html>
