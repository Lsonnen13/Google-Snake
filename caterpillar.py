import pygame

class Caterpillar:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self):
        self.head_gr_pos = [5, 5]
        self.body_gr_pos = [
            [5, 5],
            [4, 5],
            [3, 5]
        ]
        self.body_direction = [
            self.RIGHT,
            self.RIGHT,
            self.RIGHT
        ]
        self.direction = self.RIGHT
        

        self.head_sprites = [
            pygame.image.load("assets/sprite_caterpillar_head1.png"),
            pygame.image.load("assets/sprite_caterpillar_head0.png"),
            pygame.image.load("assets/sprite_caterpillar_head3.png"),
            pygame.image.load("assets/sprite_caterpillar_head2.png"),
        ]

        self.body_sprites = [
            pygame.image.load("assets/sprite_caterpillar_body02.png"),
            pygame.image.load("assets/sprite_caterpillar_body01.png"),
            pygame.image.load("assets/sprite_caterpillar_body04.png"),
            pygame.image.load("assets/sprite_caterpillar_body03.png"),
        ]

        self.turn_sprites = [
            pygame.image.load("assets/sprite_caterpillar_turn01.png"),
            pygame.image.load("assets/sprite_caterpillar_turn02.png"),
            pygame.image.load("assets/sprite_caterpillar_turn03.png"),
            pygame.image.load("assets/sprite_caterpillar_turn04.png"),
            pygame.image.load("assets/sprite_caterpillar_turn05.png"),
            pygame.image.load("assets/sprite_caterpillar_turn06.png"),
            pygame.image.load("assets/sprite_caterpillar_turn07.png"),
            pygame.image.load("assets/sprite_caterpillar_turn08.png")
        ]

        self.tail_sprites = [
            pygame.image.load("assets/sprite_caterpillar_tail02.png"),
            pygame.image.load("assets/sprite_caterpillar_tail00.png"),
            pygame.image.load("assets/sprite_caterpillar_tail03.png"),
            pygame.image.load("assets/sprite_caterpillar_tail01.png"),
        ]
    

        for i in range(4):
            self.head_sprites[i] = pygame.transform.scale(self.head_sprites[i], (50, 50))
        
        
        for i in range(4):
            self.body_sprites[i] = pygame.transform.scale(self.body_sprites[i], (50, 50))

        for i in range(8):
            self.turn_sprites[i] = pygame.transform.scale(self.turn_sprites[i], (50, 50))
        for i in range(4):
            self.tail_sprites[i] = pygame.transform.scale(self.tail_sprites[i], (50, 50))

    def move(self, hamburger_pos):
        if self.direction == self.RIGHT:
            self.head_gr_pos[0] += 1
        elif self.direction == self.LEFT:
            self.head_gr_pos[0] -= 1
        elif self.direction == self.UP:
            self.head_gr_pos[1] -= 1
        elif self.direction == self.DOWN:
            self.head_gr_pos[1] += 1

        self.body_gr_pos.insert(0, self.head_gr_pos.copy())
        self.body_direction.insert(0, self.direction)
        if hamburger_pos != self.head_gr_pos:
            self.body_direction.pop()
            self.body_gr_pos.pop()

    def change_direction(self, new_direction):
        if new_direction == self.RIGHT and self.direction != self.LEFT:
            self.direction = self.RIGHT
        if new_direction == self.LEFT and self.direction != self.RIGHT:
            self.direction = self.LEFT
        if new_direction == self.UP and self.direction != self.DOWN:
            self.direction = self.UP
        if new_direction == self.DOWN and self.direction != self.UP:
            self.direction = self.DOWN
