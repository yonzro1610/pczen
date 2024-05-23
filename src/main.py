# Sys
import sys
sys.path.append("./scripts/modules")

# Libraries
from colorama import Fore
import checkforcontroller
import keyboard
import pygame
import os

# Clear console
os.system("@echo off")
os.system("cls")

# Check for Controllers
print(f"{Fore.CYAN}Checking for PS4 Controllers...")
controller = checkforcontroller.main()
if controller == False:
    print("No controllers detected...")
else:
    print("PS4 Controller Detected!")

print(f"{Fore.WHITE}")



# Minimize
import win32gui
win = win32gui.GetForegroundWindow()
win32gui.ShowWindow(win, 6)