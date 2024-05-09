from tkinter import *
import random


root = Tk()
# Title of the window
root.title("tic tac toe")
root.resizable(0, 0)
# what symbol is put onto the board when when player clicks
player_symbol = "O"
# meant for naming conventions
board_size = 3
# template for board?
board = [[0] * board_size] * board_size
# board for actually displaying buttons
button_board = board
# board for storing where symbols have actually been placed ya know
tracking_board = board


# creating gui grid from button_board
for i in range(board_size):
    for j in range(board_size):
        button_board[i][j] = Button(
            height=2,
            width=4,
            font=("Ariel", "20"),
            command=lambda r=i, c=j: clicked(r, c),
        )
        button_board[i][j].grid(row=i, column=j)


# function to comunicate where buttons been pressed
def clicked(r, c):
    print(f"{r}, {c}")


print(tracking_board)

mainloop()
