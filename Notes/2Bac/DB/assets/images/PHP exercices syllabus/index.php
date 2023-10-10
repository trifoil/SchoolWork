<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="author" content="Ivan Miller">
<title>Exercices PHP</title>
<style>
body { font-family:Arial;}
a { display:block; padding:0.5em;}
a:hover, a:focus { color:#c00;}
a:active { color:#cc0;}
</style>
</head>
<body>
<h1>Exercices du syllabus de PHP</h1>
<ul>
<?php 
$rep1=opendir('./') or die("erreur ouverture du dossier" );
while ($file1 = readdir($rep1)) { 
	if (($file1 != '..') && ($file1 !='.') && ($file1 !='')) {  
		//if (is_dir('./'.$file1)) {
			echo '<li><a href="',$file1,'">',ucfirst($file1),'</a></li>';
		//}
	}
}
closedir($rep1);
?>
</ul>
</body>
</html>