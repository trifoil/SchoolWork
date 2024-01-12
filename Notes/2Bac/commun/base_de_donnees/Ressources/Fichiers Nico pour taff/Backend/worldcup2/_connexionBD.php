<?php
date_default_timezone_set('Europe/Brussels');
$hote = 'localhost';
$nomBD = 'worldCup2018';
$user = 'root';
$password = '';

try {
	$DB = new PDO('mysql:host='.$hote.';dbname='.$nomBD, $user, $password);
	$DB->exec("SET NAMES 'utf8'");
}
catch (Exception $e) {
	echo 'Erreur de connexion à la BD : ',$e;
}