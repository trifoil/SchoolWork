print()  # Correct, écrit une tabulation
print("Hello World!")  # Correct, utilise des guillemets doubles, écrit "Hello World"
print('Hello World!')  # Correct, utilise des guillemets simples, écrit "Hello World"
# print(hello) => NameError: hello n'est pas défini.
# print(Hello world!) => SyntaxError : syntaxe incorrecte.
# print("Hello world!") => SyntaxError : Il manque des parenthèses dans l'appel à 'print'.
print("Hello \nWorld!")  # \n crée un retour à la ligne
print("Hello,", "World" + "!")  # Répétition de chaîne => Hello, World!
print("Hello", " World!", end=" fin.")  # L'argument end permet d'écrire un message à la fin du print. Par défaut, c'est un retour à la ligne => Hello World! fin.
print("Hello", "World!", sep="-")  # L'argument sep permet de mettre une séparation entre les concaténations => Hello-World
print("My", "hello ", sep=" ", end="World! \n")
print("je me répète, " * 3)  # Permet de faire une répétition de chaîne => je me répète, je me répète, je me répète
