#!/usr/bin/env python3
import pygame
import data
from pynput import keyboard
import random
pygame.init()
print(data.asciiArt)
def on_press(key):
    print(str(format(key)).replace("Key.", ''))
    try:
        # keys found in the list
        pygame.mixer.Sound.play(data.keylist[str(format(key)).replace("Key.", '').upper()])
    except:
        # keys not found in the list
        pygame.mixer.Sound.play(random.choice(list(data.keylist.values())))

run = True
while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            run = False
    with keyboard.Listener(on_press=on_press) as listener:listener.join()
pygame.quit()