# -*- coding: utf-8 -*-

import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    title = "Hallo Jörg!"
    pygame.display.set_caption(title)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

run_game()
    