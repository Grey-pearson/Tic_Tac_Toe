import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="solar")
root.title("VMS-inator")

TDC = ttk.Entry(bootstyle="success").pack(side=TOP, padx=5, pady=10)
right_cam = ttk.Checkbutton(bootstyle="success").pack()
center_cam = ttk.Checkbutton(bootstyle="success").pack()
left_cam = ttk.Checkbutton(bootstyle="success").pack()


root.mainloop()