import tkinter as Tk


class Board:
    def __init__(self):
        # for naming
        board_size = 3
        # creating board
        button_board = [[0] * board_size] * board_size
