# Libraries
from colorama import Fore
from tkinter import ttk
import tkinter as tk
import pandas as pd
import keyboard
import pygame
import os

VERSION = "a1.0"

# Classes
class UIModule():
    def __init__(self, master, notebook, title):
        self.master = master
        self.notebook = notebook
        
        self.master.title(title)
        self.master.minsize(1, 250)
        self.master.resizable(False, False)
        
        notebook.pack(expand=True, fill="both", padx=3, pady=3)

    def createTab(self, name):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=name)
        
        return tab

    def createLabel(self, tab, text):
        label = tk.Label(tab, text=text)
        label.pack(padx=1, pady=0, anchor="w")
        return label

    def createSection(self, tab, title):
        section = ttk.LabelFrame(tab, text=title)
        section.pack(fill='both', expand="no", padx=5, pady=5)
        return section

    def createButton(self, master, text, callback):
        btn = ttk.Button(master, text=text, command=callback)
        btn.pack(anchor="w", padx=1)
        return btn
    
    def createBox(self, master, text, var, callback):
        var = tk.BooleanVar()
        var.set(False)
        box = ttk.Checkbutton(master=master, text=text, variable=var, command=callback)
        box.pack()
        
        return box

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
        os.system("cls")
        print(f"No controllers found.{Fore.WHITE}")
        return False
    
    os.system("cls")
    
    print(f"Controller(s) found.{Fore.WHITE}")
    
    return controllers

def test():
    print(f"{Fore.CYAN}Test{Fore.WHITE}")

def testBox():
    print("test")
    
# Variables
controllers = checkForControllers()
root = tk.Tk()
notebook = ttk.Notebook(root)

VARIABLE = False

UI = UIModule(master=root, notebook=notebook, title="PCZen")

loaderTab = UI.createTab("Macro Loader")
editTab = UI.createTab("Macro Editor")
configurationTab = UI.createTab("Controller Configuration")
optionsTab = UI.createTab("Settings")
aboutTab = UI.createTab("About/Info")

testSection = UI.createSection(loaderTab, "test")

testBox, val = UI.createBox(testSection, "Test Box", VARIABLE, testBox)
print(str(val))
testBtn = UI.createButton(testSection, "test button", test)
testLabel = UI.createLabel(testSection, "test")

versionLabel = UI.createLabel(aboutTab, f"PCZen version {VERSION}")
creditLabel = UI.createLabel(aboutTab, f"Developed by yonzro1610.")
noticeLabel = UI.createLabel(aboutTab, f"Anybody else claiming to have made PCZen is lying.")

# Main
os.system("title PCZen")

root.mainloop()