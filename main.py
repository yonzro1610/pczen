# Libraries
from colorama import Fore
from tkinter import ttk
import tkinter as tk
import pandas as pd
import keyboard
import pygame
import os

# Classes
class UIModule():
    def __init__(self, master, notebook, title):
        self.master = master
        self.notebook = notebook
        
        self.master.title(title)
        self.master.geometry("700x350")
        self.master.resizable(False, False)
        
        notebook.pack(expand=True, fill="both", padx=3, pady=3)

    def createTab(self, name):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=name)
        
        return tab

# Functions
def checkForControllers():
    pygame.init()
    pygame.joystick.init()

    controllerCount = pygame.joystick.get_count()
    
    controllers = {}
    
    print(f"{Fore.CYAN}Checking for PS4 Controllers...")
    
    if controllerCount > 0:
        for i in range(pygame.joystick.get_count()):
            controller = pygame.joystick.Joystick(i)
            
            if "PS4 Controller" in controller.get_name():
                controllerInfo = {
                    f"Controller {i}": controller
                }
                
                controllers.append(controllerInfo)
    else:
        os.system("cls")
        print(f"No controllers found.{Fore.WHITE}")
        return False
    
    os.system("cls")
    
    print(f"Controller(s) found.{Fore.WHITE}")
    
    return controllers

# Variables
root = tk.Tk()
notebook = ttk.Notebook(root)

UI = UIModule(master=root, notebook=notebook, title="PCZen")
mainTab = UI.createTab("Main")


# Main
os.system("cls")

checkForControllers()

root.mainloop()