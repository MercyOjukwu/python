board = []
turn = None


def check_winner():
    a = 0
    while a < 8:
        a += 1

        if a == 0:
            line = board[0] + board[1] + board[2]
        elif a == 1:
            line = board[3] + board[4] + board[5]
        elif a == 2:
            line = board[6] + board[7] + board[8]
        elif a == 3:
            line = board[0] + board[3] + board[6]
        elif a == 4:
            line = board[1] + board[4] + board[7]
        elif a == 5:
            line = board[2] + board[5] + board[8]
        elif a == 6:
            line = board[0] + board[4] + board[8]
        elif a == 7:
            line = board[2] + board[4] + board[6]
        else:
            line = " "

        if line == "XXX":
            print("Player one is the winner!!!")
        elif line == "OOO":
            print("Player teo is thw winner!!!")

    b = 0
    while b < 9:
        b += 1
        if board.items == str(a + 1):
            break
        elif b == 8:
            print("It's a Draw!!!")


def print_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("|-----------|")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("|-----------|")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")


def start_game():
    winner = " "
    turn = "X"
    a = 0
    while a < 9:
        a += 1
        board[a] = str(a + 1)
    print("*******************************")
    print("Welcome to my Tic-Tac-Toe :)")
    print("*******************************")
    print()
    print_board()

    print("Player one please enter a slot number to place X in:")

    while winner is None:
        num_input = 0
        try:
            num_input = int(input("Enter a number to play: "))
            if 0 > num_input >= 9:
                print("Invalid input; re-enter slot number: ")

            expected: ValueError
            print("Kindly restart game")

            expected: IndexError
            print("Re-enter slot number")

        finally:
            print()

        try:
            if board[num_input - 1] == str(num_input):
                board[num_input - 1] = turn

                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"

                    print_board()
                    check_winner()
            else:
                print("Slot already taken; re-enter slot number:")

            expected: IndexError
            print()

        finally:
            print()

    if winner is not None:
        if winner != "X" and winner != "O":
            print("Draw")
        else:
            print(f"Congratulations! {winner} . Thanks for playing.")


if __name__ == '__main__':
    start_game()
