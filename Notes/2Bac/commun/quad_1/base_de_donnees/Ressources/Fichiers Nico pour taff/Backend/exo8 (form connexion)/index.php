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
		$_SESSION['titre']='Monsieur';
		$_SESSION['admin']=true;
		header('Location:index.php');	//on redirige pour vider $_POST
		exit();
	}
	elseif ($login=='bob' and $password=='48181acd22b3edaebc8a447868a7df7ce629920a') {
		$_SESSION['nom']='Bob';
		$_SESSION['titre']='Monsieur';
		$_SESSION['admin']=false;
		header('Location:index.php');
		exit();
	}
	elseif ($login=='betty' and $password=='5a7a28625bd1f84b38c576bcc0ee78ae9b4eae6b') {
		$_SESSION['nom']='Betty';
		$_SESSION['titre']='Madame';
		$_SESSION['admin']=false;
		header('Location:index.php');
		exit();
	}
	else {
		echo "<p>Erreur dans l'identifiant ou le mot de passe</p>" ;
	}
}
else if ( isset($_POST['deconnexion']) ) {
	session_destroy() ;		//on détruit la session
	header('Location:index.php');	//on redirige pour ne pas devoir cliquer sur le bouton 2 fois
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
		<p><?php if ($_SESSION['admin']) {echo "Bonjour ", $_SESSION['titre'];} ?></p>
		<form method="post" action="index.php">
			<p><input type="submit" name="deconnexion" value="Déconnexion">
		</form>
		<?php
	}
	?>
</body>
</html>