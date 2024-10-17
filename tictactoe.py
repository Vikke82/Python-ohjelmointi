# Tic-Tac-Toe -peli Pythonilla. Pelaajat vuorottelevat X ja O merkkien asettamisessa 3x3 pelilaudalle. 
# Suorita tiedosto komentoriviltä komennolla "python tictactoe.py".

# Pelilaudan tulostus
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Tarkistetaan voitto
def check_winner(board, player):
    # Tarkista vaakarivit, pystyrivit ja diagonaalit
    for row in board:
        if all([spot == player for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

# Tarkistetaan onko kaikki ruudut täytetty
def check_draw(board):
    return all([spot != ' ' for row in board for spot in row])

# Pelaajien vuorojen käsittely
def player_turn(board, player):
    while True:
        try:
            move = int(input(f"Pelaaja {player}, valitse paikka (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Paikka on jo varattu, yritä uudelleen.")
        except (ValueError, IndexError):
            print("Virheellinen valinta, valitse numero väliltä 1-9.")

# Pelin pääsilmukka
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        player_turn(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Pelaaja {current_player} voitti!")
            break
        
        if check_draw(board):
            print_board(board)
            print("Tasapeli!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Pelin käynnistys
if __name__ == "__main__":
    play_game()
