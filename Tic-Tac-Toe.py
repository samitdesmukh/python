# Tic-Tac-Toe Game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to get player input and validate the move
def get_move(player, board):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column): ").split())
            if board[row][col] == " ":
                return row, col
            else:
                print("This cell is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 2 separated by a space.")

# Main game loop
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Get move from current player
        row, col = get_move(current_player, board)

        # Place the player's mark on the board
        board[row][col] = current_player
        print_board(board)

        # Check if the current player wins
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (draw)
        if is_full(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
