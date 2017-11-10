# -*- coding: utf-8 -*-

import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Hallo Jörg! 😇")
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

run_game()
    