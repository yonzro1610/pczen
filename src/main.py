import os
import sys
sys.path.append("./scripts/modules")
sys.path.append("./modules/interface")
sys.path.append("./scripts")
import pygame
from colorama import Fore
import checkforcontroller
import keyboard
import win32gui

def updateconsole():
    os.system("@echo off")
    os.system("cls")
updateconsole()

def main():

    print(f"{Fore.CYAN}Checking for PS4 Controllers...")
    controller = checkforcontroller.main()
    if not controller:
        print("No controllers detected...")
    else:
        print("PS4 Controller Detected!")

    print(f"{Fore.WHITE}")
main()