<?php
require '_bd.php';

$reqCat = $bd->query('SELECT * FROM categories');
$categories = "- ";
foreach ($reqCat as $cat) {$categories.= $cat['name']. " - ";}

?><!DOCTYPE html>
<header>
    <h1><a href="index.php">🐾 Walking Pets</a></h1>
    <div>
        <p><?=$categories?></p>
        <p>L'équipe de <b>Walking Pets</b> s'occupe de vos animaux de compagnie.</p>
        <p>Au menu : plusieurs promenades* et repas par jour.</p>
    </div>
</header>
