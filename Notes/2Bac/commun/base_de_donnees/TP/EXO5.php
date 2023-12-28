<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Tirages du Lotto 0</title>
    <style>
        @import url('https://fonts.cdnfonts.com/css/bitstream-vera-sans');


        body {
            font-family: 'Bitstream Vera Sans', sans-serif;
            font-size: 1.2em;
            text-align: center;
        }

        table {
            margin: auto;
        }

        table td,
        th {
            width: 2em;
            height: 2em;
            text-align: center;
            border: 2px solid black;
        }
    </style>
</head>

<body>
    <h1>Tirages du Lotto 0</h1>
    <?php
    $nb_tirages = rand(4, 10);
    for ($tirage = 1; $tirage <= $nb_tirages; $tirage++) {
        for ($i = 0; $i < 6; $i++) {
            $numeros[$tirage][$i] = rand(1, 50);
        }
    }
    ?>
</body>

</html>