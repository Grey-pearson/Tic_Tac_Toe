import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tic tac toe")
        self.resizable(0, 0)
        self.board_size = 3
        self.button_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.tracking_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def create_board(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                self.button_board[r][c] = TicTacButton(r, c)
        self.button_board[r][c].grid(row=r, column=c)



class TicTacButton(tk.Tk):
    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.button = tk.Button(
            height=2,
            width=4,
            font=("Ariel", "20"),
            bootstyle=SUCCESS ,
            command=lambda r=self.row, c=self.column: self.clicked(r, c),
        )

    def clicked(r, c):
        print(f"{r} + {c}")
