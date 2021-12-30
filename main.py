#!/usr/bin/env python3
# Imports
import pygame
import data
import colorama
from pynput import keyboard
import random

def on_press(key):
    try:     
        pygame.mixer.Sound.play(data.keylist[format(key.char).upper()])
    except AttributeError:
        try:
            pygame.mixer.Sound.play(data.keylist[str(format(key)).upper().replace("KEY.", '')])
        except:
            pygame.mixer.Sound.play(data.keylist["A"])
def startUp():
    pygame.init()
    print(data.theme[0] + data.asciiArt)
    print(data.theme[1] + "Enjoy the " + data.switch)    
def main():
    run = True
    while run:
        with keyboard.Listener(on_press=on_press) as listener:listener.join()
    print("goodbye!!!")
    pygame.quit()
if __name__ == '__main__':
    startUp()
    main()