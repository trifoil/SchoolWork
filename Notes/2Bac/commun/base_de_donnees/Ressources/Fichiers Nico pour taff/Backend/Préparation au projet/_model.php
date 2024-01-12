<?php
date_default_timezone_set('Europe/Brussels');

class bd {
    private $bd;

    public function __construct() {
        $hote='localhost';
        $nomBD='walking pets';
        $user='root';
        $mdp='';
        try {
            $this->bd=new PDO('mysql:host='.$hote.';dbname='.$nomBD, $user, $mdp);
            $this->bd->exec("SET NAMES 'utf8'");
        }
        catch (Exception $e) {echo "Erreur de connexion à la BD : $e";}
    }

    public function get_categories() {
        return $reqCat = $this->bd->query('SELECT * FROM categories');
    }

    public function get_pets() {
        // Récupération des données de la table pets et des catégories associées
        $pet_list=$this->bd->prepare('SELECT p.id_pet, p.name, p.walks, p.meals, p.comment, p.id_cat, c.icon, c.max_walks FROM pets AS p LEFT JOIN categories AS c ON p.id_cat = c.id_cat ORDER BY p.name ASC');
        $pet_list->execute();
        $pet_list->setFetchMode(PDO::FETCH_OBJ);
        return $pet_list;
    }

    public function get_pet($id) {
        try {
            // Récupération des données de la table pets et des catégories associées
        $pet=$this->bd->prepare('SELECT p.id_pet, p.name, p.walks, p.meals, p.comment, p.id_cat, c.icon, c.max_walks FROM pets AS p LEFT JOIN categories AS c ON p.id_cat = c.id_cat WHERE p.id_pet = :id');
        $pet->bindValue(':id', (int) $id);
        $pet->execute();
        $pet->setFetchMode(PDO::FETCH_OBJ);
        if ($pet->rowCount() == 0) {
            header('Location: index.php');
        } else {
            $result=$pet->fetch();
        };
        $pet->closeCursor();
        return $result;
        }
        catch (Exception $e) {echo "Erreur de connexion à la BD : $e";}
    }

    public function modify_pet($id, $walks, $meals, $comment) {
        try {
            // Update de la base de données avec les nouvelles données
            $modifBD = $this->bd->prepare('UPDATE pets SET walks=:walks, meals=:meals, comment=:comment WHERE id_pet=:id');
            $modifBD->bindValue(':id', (int) $_GET['pet']);
            if ($walks >= 0) { // On vérifie que les valeurs entrées sont positives
                $modifBD->bindValue(':walks', (int) $walks); // Si oui, on les enregistre (forcé en entiers)
            } else {
                $modifBD->bindValue(':walks', 0); // Si non, on enregistre 0
            };
            if ($meals >= 0) {
                $modifBD->bindValue(':meals', (int) $meals);
            } else {
                $modifBD->bindValue(':meals', 0);
            };
            if (isset($comment)) {
                $modifBD->bindValue(':comment', $comment);
            } else {
                $modifBD->bindValue(':comment', '');
            };
            $modifBD->execute(); // On exécute la requête
            $modifBD->closeCursor();
        }
        catch (Exception $e) {echo "Erreur lors de la modification : $e";}
    }
}
?>
