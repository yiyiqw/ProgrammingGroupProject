# Initialize the game board.
# Create a 3x3 grid initialized with spaces. Each space represents an empty spot on the board.
board = [[' ' for _ in range(3)] for _ in range(3)]
score = {1: 0, 2: 0}  # Keep score for each player


def print_board(board):
    """
    This function prints the board. Each row of the board is printed on a new lin
    :param board:The 3x3 tic-tac-toe board (list of lists) to be printed
    :return:None
    """
    for row in board:
        print('|'.join(row))
        print('-' * 5)  # Print a divider between each row


def check_win(board):
    """
    Checks rows, columns, and diagonals for a win
    :param board:The 3x3 tic-tac-toe board (list of lists) being checked for a win
    :return:True if there is a winning condition, False otherwise
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':  # Check rows
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':  # Check columns
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][
        0] != ' ':  # Check diagonals
        return True
    return False


def check_tie(board):
    """
    Checks whether the board is completely filled without any winner. If there's an empty spot (' '), the game is not tied. Otherwise, it is.
    :param board:The 3x3 tic-tac-toe board (list of lists) being checked for a tie
    :return:True if there is a tie, False otherwise
    """
    for row in board:
        if ' ' in row:
            return False
    return True


def take_turn(player, board):
    """
    Lets the player choose a spot on the board
    :param player:The current player (1 or 2)
    :param board:The current state of the tic-tac-toe board
    :return:None
    """
    print(f"Player {player}'s turn")
    while True:  # Keep asking until a valid input is provided
        try:
            row = int(input("Choose a row (0-2): "))
            column = int(input("Choose a column (0-2): "))

            # Check if the chosen position is out of bounds
            if row < 0 or row > 2 or column < 0 or column > 2:
                print("Invalid position! Choose a row and a column between 0 and 2.")
                continue  # Skip the rest of the loop and ask for input again

            # Check if the spot is taken. If it is, let the player choose again.
            if board[row][column] != ' ':
                print("Spot taken. Choose another.")
            else:
                break  # Break the loop if a valid, empty spot is chosen
        except ValueError:  # Catch if the input is not an integer
            print("Enter a number.")

    # Place the player's mark on the chosen spot.
    board[row][column] = 'X' if player == 1 else 'O'


def reset_board():
    """
    Resets the tic-tac-toe board to its initial empty state
    :return:A new empty 3x3 tic-tac-toe board
    """
    return [[' ' for _ in range(3)] for _ in range(3)]


def main():
    """
    Main function to control the flow of the tic-tac-toe game
    :return:None
    """
    global board  # Use the global board variable
    for round in range(3):  # Play 3 rounds
        player = 1
        board = reset_board()  # Reset the board for each round
        while True:
            print_board(board)
            take_turn(player, board)
            if check_win(board):
                print(f"Player {player} wins round {round + 1}!")
                score[player] += 1  # Update score
                break
            if check_tie(board):
                print(f"It's a tie in round {round + 1}!")
                break
            player = 2 if player == 1 else 1  # Switch players
        print_board(board)  # Show the final board

    # Print the final scores after all rounds
    print(f"Final scores:\nPlayer 1: {score[1]}\nPlayer 2: {score[2]}")
    # Determine the overall winner
    if score[1] > score[2]:
        print("Player 1 is the overall winner!")
    elif score[1] < score[2]:
        print("Player 2 is the overall winner!")
    else:
        print("The game ends in a tie!")


main()