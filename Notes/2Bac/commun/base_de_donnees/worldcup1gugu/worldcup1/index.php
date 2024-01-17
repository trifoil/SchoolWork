<?php
require('_connexionBD.php');
if(isset($_GET['pays']))
{
    if(preg_match("#^[A-Z]{3}$#",$_GET['pays'])){
    $id = $_GET['pays'];
    $req_joueur = $bd->prepare('SELECT naissance,nom,prenom FROM joueurs WHERE equipe=:id ORDER BY nom,prenom');
    $req_joueur->bindValue(':id',$id);
    $req_joueur->execute();
}
}
$req_classement = $bd->query('SELECT participations.code,participations.place,equipes.pays FROM participations JOIN equipes ON equipes.code=participations.code ORDER BY participations.place LIMIT 16 ') ;

$req_but = $bd->query('SELECT joueurs.equipe, nom, COUNT(id_but) AS nb, participations.place FROM joueurs JOIN buts ON buts.id_joueur = joueurs.id_joueur JOIN participations ON participations.code = joueurs.equipe WHERE penalty = 0 AND contre_son_camp = 0 GROUP BY joueurs.equipe, nom, participations.place HAVING nb >= 3 ORDER BY nb DESC, participations.place ASC, nom ASC');
echo '<h1> Classsement </h1>';
$req_pays = $bd->query('SELECT p.code,e.pays,p.place FROM participations  as p JOIN equipes as e ON p.code=e.code ORDER BY e.pays ASC');

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
$cpt = 0;
while($tmp = $req_but->fetch()){
    if($tmp['nb']>=$cpt){
        $cpt = $tmp['nb'];
        echo '<b>';
    }
    echo '<img src="flags/'.$tmp['equipe'].'.webp">';
    echo $tmp['nom'];
    echo ' : ';
    echo $tmp['nb'];
    if($tmp['nb']>=$cpt){
        
        echo '</b>';
    }
    echo '<br>';

}

?>

<form action="index.php" method="get">
    <select name="pays" >
    <?php
    while($data = $req_pays->fetch()){
        if(isset($id)&& $data['code'] ==$id){
        echo '<option selected value="'.$data['code'].'">'.$data['pays'].'</option>';
    }
    else{
        echo '<option value="',$data['code'],'">',$data['pays'],'</option>';
    }
}
    
    ?>
    </select>
    <input type="submit">
</form>
<?php
while($data=$req_joueur->fetch()){
    echo $data['nom'].' <b>'.$data['prenom'].'</b> '.$data['naissance'];

    echo '<br>';
}
?>
