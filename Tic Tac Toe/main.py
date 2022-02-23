ttt_dict = {"top": {"left": "", "middle": "", "right": ""},
            "middle": {"left": "", "middle": "", "right": ""},
            "bottom": {"left": "", "middle": "", "right": ""}}

print("Welcome to a text based Tic Tac Toe game. \n"
      "The rows are called top, middle and bottom.\n"
      "The columns are called left, middle and right.\n"
      "To choose where to put your mark type in the row and column separated by a space, for example: 'top middle'")
row, column = input("Player X: What row and column do you want to put an X to? ").split()
ttt_dict[row][column] = "X"
print(ttt_dict)