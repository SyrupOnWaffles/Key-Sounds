#!/usr/bin/env python3
import pygame
from pynput import keyboard
pygame.init()
keylist = {
    "A": pygame.mixer.Sound("sounds/A.wav"),
    "B": pygame.mixer.Sound("sounds/B.wav"),
    "C": pygame.mixer.Sound("sounds/C.wav"),
    "D": pygame.mixer.Sound("sounds/D.wav"),
    "E": pygame.mixer.Sound("sounds/E.wav"),
    "F": pygame.mixer.Sound("sounds/F.wav"),
    "G": pygame.mixer.Sound("sounds/G.wav"),
    "H": pygame.mixer.Sound("sounds/H.wav"),
    "I": pygame.mixer.Sound("sounds/I.wav"),
    "J": pygame.mixer.Sound("sounds/J.wav"),
    "K": pygame.mixer.Sound("sounds/K.wav"),
    "L": pygame.mixer.Sound("sounds/L.wav"),
    "M": pygame.mixer.Sound("sounds/M.wav"),
    "N": pygame.mixer.Sound("sounds/N.wav"),
    "O": pygame.mixer.Sound("sounds/O.wav"),
    "P": pygame.mixer.Sound("sounds/P.wav"),
    "Q": pygame.mixer.Sound("sounds/Q.wav"),
    "R": pygame.mixer.Sound("sounds/R.wav"),
    "S": pygame.mixer.Sound("sounds/S.wav"),
    "T": pygame.mixer.Sound("sounds/T.wav"),
    "U": pygame.mixer.Sound("sounds/U.wav"),
    "V": pygame.mixer.Sound("sounds/V.wav"),
    "W": pygame.mixer.Sound("sounds/W.wav"),
    "X": pygame.mixer.Sound("sounds/X.wav"),
    "Y": pygame.mixer.Sound("sounds/Y.wav"),
    "Z": pygame.mixer.Sound("sounds/Z.wav"),
    "BACKSPACE": pygame.mixer.Sound("sounds/BACKSPACE.wav"),
    "CAPS_LOCK": pygame.mixer.Sound("sounds/CAPS LOCK.wav"),
    "SPACE": pygame.mixer.Sound("sounds/SPACE.wav"),
    "ENTER": pygame.mixer.Sound("sounds/ENTER.wav"),
    "CTRL": pygame.mixer.Sound("sounds/CTRL.wav"),
    "TAB": pygame.mixer.Sound("sounds/TAB.wav"),




}

def on_press(key):
    try:
        
        pygame.mixer.Sound.play(keylist[format(key.char).upper()])
        print(format(key.char))
    except AttributeError:
        pygame.mixer.Sound.play(keylist[str(format(key)).replace("Key.", '').upper()])

run = True
while run:

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
    with keyboard.Listener(on_press=on_press) as listener:listener.join()
pygame.quit()  # If we exit the loop this will execute and close our game