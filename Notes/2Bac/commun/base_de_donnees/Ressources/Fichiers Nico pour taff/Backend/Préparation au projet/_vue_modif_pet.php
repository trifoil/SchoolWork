<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">  
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Walking Pets | Mofications</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐾</text></svg>"/>
</head>
<body>
    <h1><a href="index.php">🐾 Walking Pets</a></h1>
    <div class="form">
        <img src="./icons/leash.png" alt="leash_icon">
        <h3><?=$result->name?></h3>
        <!-- Formulaire de modification -->
        <form method="post" action=<?="index.php?pet=".$result->id_pet?>>
            <p><label for="walks">walks :
                <input type="number" id="walks" name="walks" min="0" value="<?=$result->walks?>">
            </label>
            <p><label for="meals">meals :
                <input type="number" id="meals" name="meals" min="0" value="<?=$result->meals?>">
            </label>
            <p><label for="comment">comment :
                <textarea id="comment" name="comment" cols="40"><?=$result->comment?></textarea>
            </label>
            <p><input type="submit" name="save" value="Enregistrer">
        </form>
    </div>
    <footer>
        <p>*seuls les chien et les chats ont droits aux promenades avec un maximum de 2 promenades par jour pour les chiens et 1 pour les chats.
    </footer>
</body>
</html>
