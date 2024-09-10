
import pygame
from caterpillar import Caterpillar
from hamburger import Hamburger

pygame.init()

window = pygame.display.set_mode((500, 500))

font = pygame.font.Font("Cattie-Regular.ttf", 50)

caterpillar = Caterpillar()

hamburger = Hamburger(caterpillar.body_gr_pos)


cell_size = 50

score = 0

move_event = pygame.event.custom_type()
pygame.time.set_timer(move_event, 175, 999999999)
new_direction = None

grid_color = [0, 255, 0]
color_change_amt = -3


backround = pygame.image.load("Newbackround.png")
backround = pygame.transform.scale(backround, (window.get_width(), window.get_height()))

def start():
    while True:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    main_game_loop()

def main_game_loop():
    while True:
        event_handler()
        check_if_ate()
        if check_wall_collision() or check_body_collision():
            game_over()
        draw()
        
def event_handler():
    global new_direction
    event_list = pygame.event.get()


    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == move_event:
            caterpillar.change_direction(new_direction)
            caterpillar.move(hamburger.grid_pos)
                
            new_direction = None
            change_color()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                new_direction = caterpillar.UP
            elif event.key == pygame.K_d:
                new_direction = caterpillar.RIGHT
            elif event.key == pygame.K_a:
                new_direction = caterpillar.LEFT
            elif event.key == pygame.K_s:
                new_direction = caterpillar.DOWN

                

def draw():    
    window.blit(backround, (0, 0))
    draw_grid()
    draw_caterpillar()
    draw_hamburger()
    pygame.display.update()

def draw_hamburger():
   # burger_rect = pygame.Rect(convert_gr_to_xy(hamburger.grid_pos), [cell_size, cell_size])
    #pygame.draw.rect(window, hamburger.color, burger_rect)
    window.blit(hamburger.sprite, convert_gr_to_xy(hamburger.grid_pos))
    print(hamburger.grid_pos)

def draw_caterpillar():
    index = 0
    for position in caterpillar.body_gr_pos:
        if index == 0:
            window.blit(caterpillar.head_sprites[caterpillar.direction], convert_gr_to_xy(caterpillar.head_gr_pos))
        elif index == len(caterpillar.body_gr_pos) - 1:
            window.blit(caterpillar.tail_sprites[caterpillar.body_direction[index - 1]], convert_gr_to_xy(caterpillar.body_gr_pos[index]))
        else:
           # body_rect = pygame.Rect(convert_gr_to_xy(position), [cell_size, cell_size])
            #pygame.draw.rect(window, caterpillar.color, body_rect)
            imageToUse = caterpillar.body_sprites[caterpillar.body_direction[index]]
            directions = [
                caterpillar.body_direction[index], caterpillar.body_direction[index - 1]
            ]
            if directions[0] == Caterpillar.DOWN and directions[1] == Caterpillar.LEFT:
                imageToUse = caterpillar.turn_sprites[0]
            elif directions[0] == Caterpillar.RIGHT and directions[1] == Caterpillar.DOWN:
                imageToUse = caterpillar.turn_sprites[1]
            elif directions[0] == Caterpillar.UP and directions[1] == Caterpillar.RIGHT:
                imageToUse = caterpillar.turn_sprites[2]
            elif directions[0] == Caterpillar.LEFT and directions[1] == Caterpillar.UP:
                imageToUse = caterpillar.turn_sprites[3]
            elif directions[0] == Caterpillar.UP and directions[1] == Caterpillar.LEFT:
                imageToUse = caterpillar.turn_sprites[4]
            elif directions[0] == Caterpillar.RIGHT and directions[1] == Caterpillar.UP:
                imageToUse = caterpillar.turn_sprites[5]
            elif directions[0] == Caterpillar.DOWN and directions[1] == Caterpillar.RIGHT:
                imageToUse = caterpillar.turn_sprites[6]
            elif directions[0] == Caterpillar.LEFT and directions[1] == Caterpillar.DOWN:
                imageToUse = caterpillar.turn_sprites[7]
            window.blit(imageToUse, convert_gr_to_xy(position))
        index += 1


def convert_gr_to_xy(gr_pos):
    xy_pos = [gr_pos[0] * cell_size, gr_pos[1] * cell_size ]
    return xy_pos



def draw_grid():
    for row in range(10):
        for col in range(10):
            square = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(window, grid_color, square, 1)


def check_if_ate():
    global score
    if caterpillar.head_gr_pos == hamburger.grid_pos:
        hamburger.new_position(caterpillar.body_gr_pos)
        score += 1

def check_wall_collision():
    if caterpillar.head_gr_pos[0] > 9:
        return True
    if caterpillar.head_gr_pos[1] > 9:
        return True
    if caterpillar.head_gr_pos[0] < 0:
        return True
    if caterpillar.head_gr_pos[1] < 0:
        return True
    
def check_body_collision():
    for body_pos in caterpillar.body_gr_pos[1:]:
        if caterpillar.head_gr_pos == body_pos:
            return True



def game_over():
    game_over_text = font.render("your score was, "+ str(score), True, (0, 50, 0))
    window.blit(game_over_text, (50, 50))
    pygame.display.update()
    pygame.time.wait(2500)
    pygame.quit()
    quit()

def change_color():
    global grid_color
    global color_change_amt
    grid_color[1] += color_change_amt
        
    if grid_color[1] == 120:
            color_change_amt = 3
    if grid_color[1] == 255:
            color_change_amt = -3 



        

start()