<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="styles.css">
    <title>Tirages du Lotto</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1.2em;
            text-align: center;
        }
        table {margin: auto;}
        table td, th {
            width: 2em;
            height: 2em;
            text-align: center;
            border: 2px solid black;
        }
    </style>
</head>
<body>
    <h1>Tirages du Lotto</h1>
    <?php
    // Génération des tirages
    $nb_tirages = rand(4,10) ;
    for ($tirage=1 ; $tirage<=$nb_tirages ; $tirage++) {
        $numeros[$tirage] = array();
        for ($i=0 ; $i<6 ; $i++) {
            do {
                $random = rand(1,50);
            } while (in_array($random, $numeros[$tirage]));
            $numeros[$tirage][$i] = $random;
        }
        sort($numeros[$tirage]);
    }
    ?>

    <!-- Affichage des tirages dans un tableau -->
    <table>
        <tr>
            <th colspan="6">Numéros</th>
        </tr>
        <?php 
        foreach ($numeros as $ligne) {
            echo '<tr>';
            foreach ($ligne as $num) {
                echo '<td>', $num; 
            }
        } 
        ?>
    </table>

    if (isset($numeros[3][7])) {
    $value = $numeros[3][7];
    echo "The value at index [3][7] is: $value";
} else {
    echo "Index [3][7] does not exist in the array.";
}


</body>
</html>