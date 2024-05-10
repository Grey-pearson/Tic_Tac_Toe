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
# when True stop game
stop_game = False


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

    check_for_win()


def check_for_win():
    global stop_game

    for tiles in range(board_size):

        if tracking_board[tiles][0] == tracking_board[tiles][1] == tracking_board[tiles][2] != 0:
            stop_game = True
            print('game over condition 1')
            break
        
        if tracking_board[0][tiles] == tracking_board[1][tiles] == tracking_board[2][tiles] != 0:
            stop_game = True
            print('game over, condition 2')
            break
        
        if tracking_board[0][0] == tracking_board[1][1] == tracking_board[2][2] != 0:
            stop_game = True
            print('game over condition 2')
        
        if tracking_board[0][2] == tracking_board[1][1] == tracking_board[2][0] != 0:
            stop_game = True
            print('game over condition 3')
        
    # this is to verify a tie, should check for tie some better way in a seperate function prolly
    for tiles_x in range(board_size):
        for tiles_x in range(board_size):
            if tracking_board[tile]

# print(tracking_board)
# print(button_board)

mainloop()
