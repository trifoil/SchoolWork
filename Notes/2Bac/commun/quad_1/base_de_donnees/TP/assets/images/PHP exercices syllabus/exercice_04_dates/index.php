<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Jours avant le weekend</title>
</head>
<body>
	<h1>Vivement le weekend !</h1>
	<?php 
	//Fuseau horaire
	date_default_timezone_set('Europe/Brussels');
	$jours = array('dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi');
	
	//Calcul du nombre de jours restant avant samedi
	$joursAvantWE = max( 6 - date('w') ,0);
	
	//Affichage
	echo '<p>Vivement ',$jours[6],' !</p>'; 
	echo '<p>Nous sommes ',$jours[date('w')],'... plus que ',$joursAvantWE,' jours avant ',$jours[6],'.</p>'; 
	?>
</body>
</html>