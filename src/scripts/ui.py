import sys
sys.path.append("./modules/interface")
import tkinter as tk
from tkinter import ttk
import maketab

def createwin(title):
    root = tk.Tk()
    root.title(title=str)
    notebook = ttk.Notebook
    maketab.tab()

createwin()