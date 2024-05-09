from tkinter import *
import random


root = Tk()
# Title of the window
root.title("tic tac toe")
root.resizable(0, 0)
# what symbol is put onto the board when when player clicks
player_symbol = "X"
# meant for naming conventions
board_size = 3
# board for actually displaying buttons
button_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# board for storing where symbols have actually been placed ya know
tracking_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# creating gui grid from button_board
for i in range(board_size):
    # print(tracking_board)
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

    if tracking_board[r][c] == 0:
        # print(f"{r}, {c}")
        button_board[r][c].configure(text="X")
        tracking_board[r][c] = "X"
        print(tracking_board)


# print(tracking_board)
# print(button_board)

mainloop()
