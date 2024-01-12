<?php
$taux_USD = 0.884 ;
$taux_GBP = 1.225 ;
$taux_SEK = 0.096 ;
?><!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Opérations sur les variables</title>
</head>
<body>
<?php
$prix_EUR = 18.50;
$prix_USD = $prix_EUR/$taux_USD;
$prix_GBP = $prix_EUR/$taux_GBP;
$prix_SEK = $prix_EUR/$taux_SEK;
echo '<p>', 'Prix en euros : '.number_format($prix_EUR, 2, ',', ' ').' €', '</p>';
echo '<p>', 'Prix en dollars : '.number_format($prix_USD, 2, ',', ' ').'$', '</p>';
echo '<p>', 'Prix en livres sterling : '.number_format($prix_GBP, 2, ',', ' ').' £', '</p>';
echo '<p>', 'Prix en couronnes suédoises : '.number_format($prix_SEK, 2, ',', ' ').' SEK', '</p>';
?>
</body>
</html>