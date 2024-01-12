<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Jours avant le weekend</title>
</head>
<body>
    <h1>Vivement le weekend !</h1>
    <?php
    //Fuseau horaire
    date_default_timezone_set('Europe/Brussels');
    $jours = array('dimanche', 'lundi', 'mardi', 'mercredi',
    'jeudi', 'vendredi', 'samedi');
    $mois = array('janvier', 'février', 'mars', 'avril', 'mai', 'juin','juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre');

    //Calcul du nombre de jours restant avant samedi et de la date
    $joursAvantWE = 6 - date('w') ;
    $date = getdate();
    $seconds_since_bd = time() - mktime(0, 0, 0, 10, 24, 2003);
    
    //Affichage
    echo '<p>Vivement ',$jours[6],' !</p>';
    echo '<p>Nous sommes ',$jours[date('w')],'... plus que
    ',$joursAvantWE,' jours avant ',$jours[6],'.</p>';

    // Affichage de la date du jour
    echo '<p>', '▶ '.ucfirst($jours[$date['wday']]).', le '.$date['mday'].' '.$mois[$date['mon']-1].' '.$date['year'].', '.date('H').'h'.date('i').'.','</p>';
    
    // Affichage du nombre de secondes écoulées depuis ma naissance
    echo '<p>', '- Il s\'est écoulé '.$seconds_since_bd.' secondes depuis votre naissance.','</p>';
    echo '<p>', '- Il s\'est écoulé '.round($seconds_since_bd/86400).' jours depuis ma naissance.','</p>';
    ?>
</body>
</html>