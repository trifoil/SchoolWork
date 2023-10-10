<?php
session_start();	//démarrage de la session
//si le formulaire a été soumis...
if ( isset($_POST['connexion']) ) {
	//on réceptionne, on trime les chaînes et on hache le mot de passe
	$login = trim($_POST['login']) ;
	$password = SHA1( trim($_POST['password']) ) ;
	
	//si le login et le mot de passe (bill) sont bons... 
	if ( $login=='bill' and $password=='c692d6a10598e0a801576fdd4ecf3c37e45bfbc4') { 
		$_SESSION['nom']='Bill';	//on enregistre en SESSION
		header('Location:index.php');	//on redirige pour vider $_POST
		exit();
	}
}
else if ( isset($_POST['deconnexion']) ) {
	session_destroy() ;		//on détruit la session
}
?><!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Formulaire de connexion</title>
</head>
<body>
	<?php
	if ( empty($_SESSION) ) {
		?>
		<h1>Connexion</h1>
		<form method="post" action="index.php">
			<p><label for="login">Identifiant :<br> 
				<input type="text" name="login" id="login">
			</label>
			<p><label for="password">Mot de passe :<br> 
				<input type="password" name="password" id="password">
			</label>
			<p><input type="submit" name="connexion" value="Connexion">
		</form>
		<?php
	}
	else {
		?>
		<h1>Déconnexion</h1>
		<form method="post" action="index.php">
			<p><input type="submit" name="deconnexion" value="Déconnexion">
		</form>
		<?php
	}
	?>
</body>
</html>