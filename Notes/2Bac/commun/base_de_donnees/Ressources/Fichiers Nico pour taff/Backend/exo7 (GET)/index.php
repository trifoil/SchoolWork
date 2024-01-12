<?php
//valeur par défaut si pas de paramètre GET
$page = 1 ;	
//récupération du paramètre GET s'il existe et conversion (int) pour sécurité
if (isset($_GET['page'])) {
	$page = (int) $_GET['page'];
	if ($page < 1 || $page > 3) {
		$page = 1 ;
	}
}
?><!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Paramètres GET</title>
	<style>
		body {
			color: <?php 
				switch ($page) {
					case 1:
						echo 'red';
						break;
					case 2:
						echo 'blue';
						break;
					case 3:
						echo 'green';
						break;
				}
			?>;
		}
	</style>
</head>
<body>
	<h1>Page <?php echo $page ; ?>/3</h1>
	<nav>
		<ul>
			<li><a href="index.php?page=1">Page 1</a>
			<li><a href="index.php?page=2">Page 2</a>
			<li><a href="index.php?page=3">Page 3</a>
			<li><a href="index.php?page=<?= $page+1; ?>">Page suivante</a></li>
			<li><a href="index.php?page=<?php if ($page-1 < 1) {echo '3';} else {echo $page-1;} ?>">Page précédente</a></li>
		</ul>
	</nav>
</body>
</html>
