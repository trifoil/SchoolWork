<?php
header('Location: index.php');
exit;
?><!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Administration</title>
</head>
<body>
	<?php 
	include '_header.html' ; # We can also include php files ;)
	include '_nav.html' ;
	?>
	<h2>Administration</h2>
	<?php
	include '_footer.html';
	?>
</body>
</html>