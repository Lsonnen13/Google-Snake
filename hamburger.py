import random
import pygame
class Hamburger:
    def __init__(self, body) -> None:
        self.color = (186, 150, 41)
        self.grid_pos = [-1, -1]
       # window.blit(sprite_hamburger.png, )
        self.new_position(body)

        self.sprite = pygame.image.load("assets/sprite_hamburger.png")
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))

    def new_position(self, body):
        self.grid_pos = [random.randint(0, 9), random.randint(0, 9)]
        while self.grid_pos in body:
            self.grid_pos = [random.randint(0, 9), random.randint(0, 9)]
