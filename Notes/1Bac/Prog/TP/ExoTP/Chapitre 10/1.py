# Page 241
from random import randrange

end = 0
used_case = [5]
user_move = []
game_val = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: 'X', 6: '6',
    7: '7', 8: '8', 9: '9'
}


def display_board(bold=[], win=""):
    # Afficher en gras la ligne gagnante à la fin
    global game_val
    for i in bold:
        game_val[i] = "\033[1m" + win + "\033[0m"

    print("""
+-------+-------+-------+
|       |       |       |
|   {}   |   {}   |   {}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {}   |   {}   |   {}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {}   |   {}   |   {}   |
|       |       |       |
+-------+-------+-------+
""".format(*list(game_val.values())))


def enter_move():
    while True:
        try:
            user_case = int(input("Entrez le numéro de la case: "))
        except TypeError:
            print("Entrez un nombre")
        else:
            if user_case in used_case:
                print("Case déjà jouée.")
            elif not user_case in range(1, 10):
                print("Nombre trop grand")
            else:
                used_case.append(user_case)
                game_val[user_case] = 'O'
                break


def victory_for():
    global end
    winner = [], ''
    game_val_lst = [
        [game_val.get(1), game_val.get(2), game_val.get(3)],
        [game_val.get(4), game_val.get(5), game_val.get(6)],
        [game_val.get(7), game_val.get(8), game_val.get(9)]
    ]

    # Horizontal
    for i in range(3):
        if game_val_lst[i][0] == game_val_lst[i][1] == game_val_lst[i][2]:
            winner = ([3*i + 1, 3*i + 2, 3*i + 3], game_val_lst[i][0])
            break

    # Vertical
    for i in range(3):
        if game_val_lst[0][i] == game_val_lst[1][i] == game_val_lst[2][i]:
            print("Vert win")
            winner = ([i + 1, i + 4, i + 7], game_val_lst[0][i])

    # Oblique
    if game_val_lst[0][0] == game_val_lst[1][1] == game_val_lst[2][2]:
        winner = ([1, 5, 9], game_val_lst[0][0])
    elif game_val_lst[2][0] == game_val_lst[1][1] == game_val_lst[0][2]:
        winner = ([3, 5, 7], game_val_lst[0][0])

    # Afficher le vainqueur
    if winner[1] == 'X':
        display_board(winner[0], winner[1])
        print("L'ordinateur a gagné la partie.")
        end = 1
    elif winner[1] == 'O':
        display_board(winner[0], winner[1])
        print("Le joueur a gagné la partie.")
        end = 1
    elif len(used_case) == 9:
        print("Le tableau est rempli, personne n'a gagné.")
        end = 1


def draw_move():
    while True:
        move = randrange(1, 9)
        if move in used_case:
            pass
        else:
            used_case.append(move)
            break

    game_val[move] = 'X'
    print("L'ordinateur a joué sur la case", move)


if __name__ == "__main__":
    try:
        while not end:
            display_board()
            enter_move()
            victory_for()
            if end:
                break
            draw_move()
            victory_for()
    except KeyboardInterrupt:
        print("!!!")
