<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<title>Générateur de noms de nains</title>
	<style>
	@font-face { 
		font-family:"ARJulian"; 
		src:url("ARJULIAN.ttf"); 
	}

	body { font-family:"ARJulian", Arial; }

	.couleur0 { color:maroon; }
	.couleur1 { color:navy; }
	</style>
</head>
<body>
	<h1>Noms de nains</h1>
	<?php 
	$nain_debut=array('A','Ba','Bo','Bu','Bra','Bre','Bro','Da','Dra','Dro','Du','Ga','Go','Gu','Gra','Gri','Gro','I','Ka','Ko','Ku','O','U','Ta','Ti','To','Tu');
	$nain_liaison=array('ka','ko','la','lo','ra','rba','ro','rbo');
	$nain_fin=array('ban','dar','dir','dor','dur','gal','gan','gar','gor','grim','gur','kan','lan','lar','lek','li','lin','lion','lir','rak','ran','rek','rgrim','rgor','rik','ril','rion','rok','ron','tar','trek','tron');	

	// Génération des noms
	$noms = array();
	for ($i=0; $i < 20; $i++) {
		do {
			$nom = $nain_debut[array_rand($nain_debut)];
			if (rand(0, 99) <= 40) {
				$nom .= $nain_liaison[array_rand($nain_liaison)];
			}
			$nom .= $nain_fin[array_rand($nain_fin)];
		} while (array_search($nom, $noms) !== false);
		$noms[$i] = $nom;
	}

	// Affichage des noms
	sort($noms);
	echo '<ul>';
	foreach ($noms as $nom) {
		if (array_search($nom, $noms)%2 == 0) {
			echo '<li class="couleur0">', $nom, '</li>';
		} else {
			echo '<li class="couleur1">', $nom, '</li>';
		}
	}
	echo '</ul>';
	?>
</body>
</html>