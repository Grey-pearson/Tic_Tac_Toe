import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# from Board import *

root = tk.Tk()

board = Board()

# button = ttk.Button(bootstyle="success")

board.create_board()

root.mainloop()