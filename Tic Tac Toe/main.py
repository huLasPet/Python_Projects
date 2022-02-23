ttt_dict = {"top": {"left": " ", "middle": " ", "right": " "},
            "middle": {"left": " ", "middle": " ", "right": " "},
            "bottom": {"left": " ", "middle": " ", "right": " "},
            }
win = False


def draw_board():
    print(f"{ttt_dict['top']['left']} | {ttt_dict['top']['middle']} | {ttt_dict['top']['right']}")
    print("-" * 9)
    print(f"{ttt_dict['middle']['left']} | {ttt_dict['middle']['middle']} | {ttt_dict['middle']['right']}")
    print("-" * 9)
    print(f"{ttt_dict['bottom']['left']} | {ttt_dict['bottom']['middle']} | {ttt_dict['bottom']['right']}")
    print()


def players(player, symbol):
    while True:
        row, column = input(f"{player}: What row and column do you want to put an {symbol} to? ").split()
        if ttt_dict[row][column] == " ":
            ttt_dict[row][column] = symbol
            print()
            draw_board()
            break
        else:
            print("Spot already taken on the board - select another one please.")
            continue


def check_win():
    pass


print("Welcome to a text based Tic Tac Toe game. \n"
      "The rows are called top, middle and bottom.\n"
      "The columns are called left, middle and right.\n"
      "To choose where to put your mark type in the row and column separated by a space, for example: 'top middle'")
print("-" * 110)

while win != True:
    players("Player 1", "X")
    check_win()
    players("Player 2", "O")
    check_win()


