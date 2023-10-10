<?php
if ( isset($_POST['enregistrement']) ) {
	//un champ obligatoire
	if ( !empty($_POST['nom']) ) $nom = trim($_POST['nom']) ;
	else $erreurs['nom'] = true;
	
	//un champ obligatoire avec certaines valeurs rejetées
	if ( !empty($_POST['annee']) ) {
		if ($_POST['annee']>date('Y') or $_POST['annee']<1800) { 
			$erreurs['annee'] = true; 
		}
		else {
			$annee = (int) $_POST['annee'];
		}
	}
	else $erreurs['annee'] = true;
	
	//la liste blanche (seules ces valeurs sont permises)
	$lb = array('bananes', 'framboises', 'pommes');
	if ( isset($_POST['fruits']) ) {
		//les paramètres multiples (dont le name comporte des []) arrivent sous forme de tableaux
		foreach ($_POST['fruits'] as $f) {
			$fruits[] = $f;
		}
	}
	
	//s'il n'y a pas d'erreur...
	if (empty($erreurs)) { 
		//le formulaire est correctement complété
		$form_correct = True;
	}
}
?><!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Formulaire avec gestion des erreurs</title>
	<style>
	.red { color:red; }
	</style>
</head>
<body>
	<h1>Inscription</h1>
	
	<?php
	//Affichage des résultats du formulaire
	if ( !empty($form_correct) ) {
		echo "<p>Bonjour $nom, vous avez choisi : ";
		foreach ($fruits as $f) { 
			echo $f,' ';
		}
	}
	?>
	
	<form method="post" action="index.php">
		<p <?php if ( isset($erreurs['nom']) ) echo 'class="red"'; ?>>
			<label for="nom">Nom :<br> 
				<input type="text" id="nom" name="nom" value="<?php if (isset($nom)) echo $nom; ?>" >
			</label>
		<p <?php if ( isset($erreurs['annee']) ) echo 'class="red"'; ?>>
			<label for="annee">Année de naissance :<br> 
				<input type="number" id="annee" name="annee" step="1" value="<?php if (isset($annee)) echo $annee; ?>">
			</label>
		<ul>
			<li><label for="choix1">
				<input type="checkbox" name="fruits[]" value="bananes" id="choix1">Les bananes
				</label>
			<li><label for="choix2">
				<input type="checkbox" name="fruits[]" value="framboises" id="choix2">Les framboises
				</label>
			<li><label for="choix3">
				<input type="checkbox" name="fruits[]" value="pommes" id="choix3">Les pommes
				</label>
		</ul>
		<p><input type="submit" name="enregistrement" value="Enregistrer">
	</form>
</body>
</html>