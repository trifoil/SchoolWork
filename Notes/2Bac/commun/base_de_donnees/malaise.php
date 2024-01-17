<?php

require '_connexionBD.php';

if (isset($_GET['pays']))
{

    if(preg_match("#^[A-Z]{3}$#",$_GET['pays']))
    {
        
        $id=$_GET['pays'];
        $joueurs2=$bd->prepare('SELECT naissance,nom,prenom FROM joueurs WHERE equipe=:id ORDER BY nom,prenom');
        $joueurs2->bindValue(':id',$id);
        $joueurs2->execute();
        //var_dump($joueurs2->fetchAll());
    }
}


$classement = $bd->query('SELECT p.code,e.pays,p.place FROM participations  as p JOIN equipes as e ON p.code=e.code ORDER BY p.place ASC LIMIT 0,16');

$joueurs = $bd->query('SELECT j.nom,j.equipe, COUNT(*) as nbr FROM joueurs as j JOIN buts as b ON b.id_joueur=j.id_joueur JOIN participations as p ON p.code= j.equipe  WHERE b.contre_son_camp=0 AND b.penalty=0 GROUP BY j.id_joueur HAVING COUNT(*)>2 ORDER BY nbr DESC, p.place ASC, j.nom ASC;');

$select = $bd->query('SELECT p.code,e.pays,p.place FROM participations  as p JOIN equipes as e ON p.code=e.code ORDER BY e.pays ASC');












while($data = $classement->fetch())
{
    echo '<p>';
    if($data['place']<4)echo '<b>';
    echo $data['place'],'<a href="index.php?pays=',$data['code'],'"><img src="flags/',$data['code'],'.webp">',$data['pays'],'</a>';
    if($data['place']<4)echo '</b>';
    echo '</p>';

}
echo '<br>';

$cpt=0;
while($data = $joueurs->fetch())
{
    echo '<p>';
    if($data['nbr']>=$cpt)
    {
        $cpt=$data['nbr'];
        echo '<b>';
        
    }
    echo '<img src="flags/',$data['equipe'],'.webp">',$data['nom'],' : ',$data['nbr'];

    if($data['nbr']>=$cpt)
    {
        $cpt=$data['nbr'];
        echo '</b>';
        
    }
    echo '</p>';

}

echo '<br>';
?>

<form action="index.php" method="get">

<select name="pays">

<?php

while($data = $select->fetch())
{
    if(isset($id)&& $data['code'] ==$id)
    {
        echo '<option selected value="',$data['code'],'">',$data['pays'],'</option>';

    }
    else
    {
        echo '<option value="',$data['code'],'">',$data['pays'],'</option>';
    }

    
}
?>

</select>
<input type="submit">
</form>

<?php

if(isset($joueurs2))
{
    while($data = $joueurs2->fetch())
        {
            echo $data['prenom'],' <b>',$data['nom'],'</b> (',$data['naissance'],')<br>';
        }

}