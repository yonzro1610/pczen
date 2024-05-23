import pygame
import os

def main():
    pygame.init()
    pygame.joystick.init()

    os.system("cls")

    controllerCount = pygame.joystick.get_count()

    if controllerCount > 0:
        for i in range(controllerCount):
            controller = pygame.joystick.Joystick(i)

            if "PS4 Controller" in controller.get_name():
                return controller
            else:
                return False
    else:
        return False