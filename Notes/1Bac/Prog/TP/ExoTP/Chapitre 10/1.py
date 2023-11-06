# Page 241
from random import randrange

game_val = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: 'X',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}


def display_board(board):
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
""".format(game_val.get(1),
           game_val.get(2),
           game_val.get(3),
           game_val.get(4),
           game_val.get(5),
           game_val.get(6),
           game_val.get(7),
           game_val.get(8),
           game_val.get(9),
           ))
# La fonction accepte un paramètre contenant l'état actuel
# de la carte et l'imprime sur la console.


def enter_move(board):
    user_tile = int(input("Case : "))

    game_val[user_tile] = 'O'
    draw_move()


def victory_for():
               # Horizontal
    win_pos = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               # Vertical
               [1, 4, 7],
               [2, 5, 8],
               [2, 6, 9],
               # Oblique 
               [1, 5, 9],
               [2, 5, 7],
               ]

    for i in win_pos:
        for j in i:
            pass


def draw_move():
    temp = []
    for i in range(1, len(game_val) + 1):
        if game_val.get(i) != 'X' or 'O':
            temp.append(i)
    
    game_val[temp[randrange(1, len(temp))]] = 'X'


while True:
    display_board(game_val)
    enter_move(game_val)
