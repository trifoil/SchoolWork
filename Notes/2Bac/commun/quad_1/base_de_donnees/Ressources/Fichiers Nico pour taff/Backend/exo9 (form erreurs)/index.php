<?php
$titre = "H";
$nation = "";
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

	//un champ facultatif
	if ( !empty($_POST['pseudo']) ) $pseudo = trim($_POST['pseudo']) ;

	// radio buttons
	$titre_list = array('H', 'F');
	if ( !empty($_POST['titre']) ) {
		if (in_array($_POST['titre'], $titre_list)) { 
			$titre = $_POST['titre']; 
		} else {
			$erreurs['titre'] = true; 
		}
	} else {
		$erreurs['titre'] = true; 
	}

	//select
	$nation_list = array('be', 'fr', 'lu');
	if ( !empty($_POST['nation']) ) {
		if (in_array($_POST['nation'], $nation_list)) { 
			$nation = $_POST['nation']; 
		} else {
			$erreurs['nation'] = true; 
		}
	} else {
		$erreurs['nation'] = true; 
	}

	//la liste blanche (seules ces valeurs sont permises)
	$lb = array('bananes', 'framboises', 'pommes', 'kiwis');
	if ( isset($_POST['fruits']) ) {
		//les paramètres multiples (dont le name comporte des []) arrivent sous forme de tableaux
		foreach ($_POST['fruits'] as $f) {
			if ( in_array($f, $lb)) {
				$fruits[] = $f;
			}
		}
	}

	// conditions d'utilisation
	if (empty($_POST['condition'])) $erreurs['condition'] = true;
	
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
		body { 
			font-family: Arial, Helvetica, sans-serif;
			font-size: 1.3em;
			padding-left: 10%;
		}
		ul {
			list-style-type: none;
			padding: 0;
		}
		.red { color:red; }
		input[type="checkbox"], input[type="radio"], input[type="submit"], select {
			cursor: pointer;
		}
		input[type="checkbox"]{
			transform: scale(1.5);
			margin-right: 1em;
		}
	</style>
</head>
<body>
	<h1>Inscription</h1>
	
	<?php
	//Affichage des résultats du formulaire
	if ( !empty($form_correct) and isset($fruits) ) {
		echo "<p>Bonjour $nom, vous avez choisi : ";
		foreach ($fruits as $f) { 
			echo $f,' ';
		}
	}
	?>
	
	<form method="post" action="index.php" id="form">
		<p <?php if ( isset($erreurs['nom']) ) echo 'class="red"'; ?>>
			<label for="nom">Nom :<br> 
				<input type="text" id="nom" name="nom" value="<?php if (isset($nom)) echo $nom; ?>" >
			</label>
		<p>
			<label for="titre">
				<input type="radio" value="H" name="titre" id="titre" <?php if ($titre=="H") {echo "checked";} ?>>Homme
			</label>
			<label for="titre2">
				<input type="radio" value="F" name="titre" id="titre2" <?php if ($titre=="F") {echo "checked";} ?>>Femme
			</label>
		<p>
			<label for="pseudo">Pseudo :<br>
				<input type="text" id="pseudo" name="pseudo" value="<?php if (isset($pseudo)) echo $pseudo; ?>">
			</label>
		<p <?php if ( isset($erreurs['annee']) ) echo 'class="red"'; ?>>
			<label for="annee">Année de naissance :<br> 
				<input type="number" id="annee" name="annee" step="1" value="<?php if (isset($annee)) echo $annee; ?>">
			</label>
		<p <?php if ( isset($erreurs['nation']) ) echo 'class="red"'; ?>>
			<label for="nation">Nationalité :<br>
				<select id="nation" form="form" name="nation" placeholder="Sélectionner nationalité">
					<option value="" disabled <?php if ($nation=="") echo "selected"; ?>>Sélectionner nationalité</option>
					<option value="be" <?php if ($nation=="be") echo "selected"; ?>>Belgique</option>
					<option value="fr" <?php if ($nation=="fr") echo "selected"; ?>>France</option>
					<option value="lu" <?php if ($nation=="lu") echo "selected"; ?>>Luxembourg</option>
				</select>
			</label>
		<ul>
			<?php
			foreach ($lb as $f) {
				echo '<li><label for="choix',$f,'">';
				echo '<input type="checkbox" name="fruits[]" value="',$f,'" id="choix',$f,'"';
				if ( isset($fruits) and in_array($f, $fruits) ) echo ' checked';
				echo '>Les ',$f,'</label>';
			}
			?>
		</ul>
		<p <?php if ( isset($erreurs['condition']) ) echo 'class="red"'; ?>>
			<label for="condition">
				<input type="checkbox" name="condition" id="condition">J’ai lu et j’approuve les conditions d’utilisation.
			</label>
		<p><input type="submit" name="enregistrement" value="Enregistrer">
	</form>
</body>
</html>