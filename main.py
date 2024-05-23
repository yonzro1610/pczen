# Libraries
from colorama import Fore
from tkinter import ttk
import tkinter as tk
import pandas as pd
import keyboard
import pygame
import os

os.system("cls")

# Classes
class UIModule():
    def __init__(self, master, notebook, title):
        self.master = master
        self.notebook = notebook
        
        self.master.title(title)
        self.master.minsize(600, 300)
        self.master.resizable(False, False)
        
        notebook.pack(expand=True, fill="both", padx=3, pady=3)

    def createTab(self, name):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=name)
        
        return tab

    def createSection(self, tab, title):
        section = ttk.LabelFrame(tab, text=title)
        section.pack(fill='both', expand='no', padx=3, pady=2)
        return section

    def createLabel(self, tab, text):
        label = tk.Label(tab, text=text)
        label.pack(anchor="w")
        return label
    
    def createButton(self, tab, text, callback):
        btn = ttk.Button(tab, text=text, command=callback)
        btn.pack(fill="both")

        
    def createBox(self, tab, text, var, callback):
        btn = ttk.Button(tab, text=text, command=callback, variable=var)
    
    def createDropdown(self, tab, opts, callback):
        dropdown = ttk.Combobox(tab, state="readonly", values=opts)
        dropdown.set(opts[0])
        dropdown.bind("<<ComboboxSelected>>", callback)
        dropdown.pack(anchor='w', pady=2, padx=2, expand=tk.YES, fill=tk.BOTH)
        return dropdown

# Functions
def checkForControllers():
    pygame.init()
    pygame.joystick.init()

    controllerCount = pygame.joystick.get_count()
    
    controllers = []
    
    print(f"{Fore.CYAN}Checking for PS4 Controllers...")
    
    if controllerCount > 0:
        for i in range(pygame.joystick.get_count()):
            controller = pygame.joystick.Joystick(i)
            
            if "PS4 Controller" in controller.get_name():
                controllers.append([f"Controller {i + 1}", controller])
    else:
        print(f"No controllers found.{Fore.WHITE}")
        return False
        
    print(f"Controller(s) found.{Fore.WHITE}")
    
    return controllers

# Main
root = tk.Tk()
notebook = ttk.Notebook(root)

UI = UIModule(master=root, notebook=notebook, title="PCZen")

loaderTab = UI.createTab("Macro Loader")
editorTab = UI.createTab("Macro Editor")
configTab = UI.createTab("Controller Configuration")
optionTab = UI.createTab("Settings")

loaderSection = UI.createSection(loaderTab, "Loader")
controlSection = UI.createSection(loaderTab, "Controls")

root.mainloop()