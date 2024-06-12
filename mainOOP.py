import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()

button1 = ttk.Button(root, text="button 1", bootsyle=SUCCESS)
button1.pack(side=LEFT, padx=5, pady=10)

button2 = ttk.Button(root, text="button 2", bootsyle=INFO)
button2.pack(side=RIGHT, padx=5, pady=10)