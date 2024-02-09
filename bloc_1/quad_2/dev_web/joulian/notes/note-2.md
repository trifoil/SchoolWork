# Prise de note - dev_web - N02

## Introduction HTML

### Attention
- Os
- Police
- Navigateur

### Outils de debug
- inspecteur de page (F11)
- W3C validator

### Code en Html

- En html on code avec des `<balises>`

- Une balise classique se construit comme suit:
```html
<nom_balise> content... </nom_balise>
```

- ne balise peut voir son comportement changer avec des attributs:
```html
<nom_balise atribut-1="valeur1.." atribut-2="valeur2.." ...> content... </nom_balise>
```

- ATTENTION ! Il existe des balises Orphelines (qui n'ont pas de `</fermeture>`)
```
<nom_balise /> ou <nom_balise>
```

### Balises HTML

#### Images

- balise img
```html
<img />
```

- précision de l'image à afficher
```html
<img src="url ou chemin de l'image" />
```

- ATTENTION, l'alt de l'image (texte qui decrit l'image), qui est obligatoire de nos jours
```html
<img alt="description de l'image" />
```

#### Retour a la ligne

- balise br
```html
<br />
```

#### ligne horizontal

- balise hr
```html
<hr />
```

#### Métadonnées (information pour le moteur de recherche) IMPORTANT |!|

- balise meta
```html
<meta />
```

- précision de l'encodage (utf-8, utf-16, ...)
```
<meta charset="utf-8" />
ou
<meta charset="utf-16">
ou
...
```

#### titres
- Les titres vont de 1 à 7 (ATTENTION, utiliser en fonction de l'importance du titre, pas la taille)
```
<h1>titre ici</h1>
<h2>titre ici</h2>
<h3>titre ici</h3>
<h4>titre ici</h4>
<h5>titre ici</h5>
<h6>titre ici</h6>
<h7>titre ici</h7>
```

#### balise obligatoires

- Doctype a la ligne 1 du programme
```
<!DOCTYPE html>
```

- balise qui englobe le programme.
```html
<!DOCTYPE html>
<html>
    ...
</html>
```

- Balise dans laquelle on précise les choses non affichées sur la pag
```html
<!DOCTYPE html>
<html>
    <head>
        ...content the user won't see
    </head>
</html>
```

- Balise dans laquelle on précise les choses qu'on affiche sur la page
```html
<!DOCTYPE html>
<html>
    <head>
        ...
    </head>
    <body>
        ...content the user will see
    </body>
</html>
```

- Dans l'élément html, on précise la langue du site (format iso) dans l'attribut "lang".
```html
<html lang="fr"> 
    ...
</html>
```

- Dans le head on met les `<meta />`, les `<title>nom du tab</title>`
```html
<head>
    <meta charset="utf-8">
    <title>nom de mon tab</html>
</head>
```

## Format d'encodage

- ASCII: 7 bits 128 caractères (iso-8869-1)
- UTF-8: 8 bits 256 caractères
- UTF-16: 16 bits TOUS les caractères

## Familles de bloc
- inline: taille de la box prend la taille de son contenu
- bloc: la hauteur de la box prend la taille de son contenu, mais la largeur est à 100%
- inline-bloc: ...
- flex-box: grille de bloc avec des tailles variables
- grid: grille de bloc avec des tailles précises
> On ne peut pas mettre un inline dans un bloc (convention)

## Notice

> Ces notes ne sont pas forcement correctes (voir syntheses).