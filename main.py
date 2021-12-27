#!/usr/bin/env python3
# Imports
import pygame
import data
from pynput import keyboard
import random
def on_press(key):
    print(str(format(key)).replace("Key.", ''))
    try:
        # keys found in the list
        pygame.mixer.Sound.play(data.keylist[str(format(key)).replace("Key.", '').upper()])
    except:
        # keys not found in the list
        pygame.mixer.Sound.play(random.choice(list(data.keylist.values())))
def main():
    pygame.init()
    print(data.asciiArt)
    run = True
    while run:
        with keyboard.Listener(on_press=on_press) as listener:listener.join()
    print("goodbye!!!")
    pygame.quit()
if __name__ == '__main__':
    main()