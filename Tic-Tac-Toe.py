# Das Spielfeld ist eine Liste mit 9 Feldern
board = [" ", " ", " ",
 " ", " ", " ",
 " ", " ", " "]

# Funktion zum Anzeigen des Spielfelds
def show_board():
    print()
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])
    print()

# Funktion zum Prüfen, ob jemand gewonnen hat
def check_winner():
    winning_lines = [(0,1,2), (3,4,5), (6,7,8), # Reihen
                     (0,3,6), (1,4,7), (2,5,8), # Spalten
                     (0,4,8), (2,4,6)           # Diagonalen
                    ]
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a] # "X" oder "O"
    if " " not in board:
        return "DRAW"
    return None

# Startspieler
turn = "X"

# Hauptspielschleife
while True:
    show_board()
    print("Spieler",turn, "ist am Zug.")

    # Eingabe eines Feldes (0-8)
    move = int(input("Wähle ein Feld (0-8): "))

    # Nur erlauben, wenn das Feld frei ist
    if board[move] == " ":
        board[move] = turn
    else:
        print("Feld ist schon belegt!")
        continue
    # Prüfen, ob jemand gewonnen hat
    winner = check_winner()
    if winner == "X":
        show_board()
        print ("X hat gewonnen!")
        break
    elif winner == "O":
        show_board()
        print ("O hat gewonnen!")
        break
    elif winner == "DRAW":
        show_board()
        print("Unentschieden!")
        break

    # Spieler wechseln
    if turn == "X":
        turn = "O"
    else:
       turn = "X"
