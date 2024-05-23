import tkinter as tk
from tkinter import ttk

def tab(name, notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=name)

    return tab