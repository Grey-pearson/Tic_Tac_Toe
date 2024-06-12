from tkinter import *
import ticTacButton as TicTacButton

# button = Button(
#     height=2,
#     width=4,
#     font=("Ariel", "20"),
#     command=lambda r=i, c=j: clicked(r, c),
# )


class Board(Tk):
    def __init__(self):
        super().__init__()
        self.title("tic tac toe")
        self.resizable(0, 0)
        self.board_size = 3
        self.button_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.tracking_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.mainloop()

    def create_board(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                self.button_board[r][c] = TicTacButton(r, c)
        self.button_board[r][c].grid(row=r, column=c)



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
