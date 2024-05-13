from tkinter import *


class TicTacButton:
    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.button = Button(
            height=2,
            width=4,
            font=("Ariel", "20"),
            command=lambda r=self.row, c=self.column: self.clicked(r, c),
        )

    def clicked(r, c):
        print(f"{r} + {c}")
