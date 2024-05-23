# Sys
import sys
sys.path.append("./scripts/modules")

# Libraries
from colorama import Fore
import checkforcontroller
import keyboard
import pygame
import os

os.system("@echo off")
os.system("cls")

print(f"{Fore.CYAN}Checking for PS4 Controllers...")
controller = checkforcontroller.main()
if controller == False:
    print("No controllers detected...")
else:
    print("PS4 Controller Detected!")

print(f"{Fore.WHITE}")