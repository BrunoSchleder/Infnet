import pygame
from random import randint
from time import sleep

pygame.init()

screen_height, screen_width = 800, 600

number_squares = 5

new_record = 0

screen = pygame.display.set_mode((screen_height, screen_width))

finished = False

clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

def show_time(time):
    font = pygame.font.Font(None, 24)
    text = font.render("Time: " + str(time) + "s", 1, white)
    text_position = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, text_position)
    
def show_points(points):
    font = pygame.font.Font(None, 24)
    text = font.render("Squares: " + str(points), 1, white)
    text_position = text.get_rect(centerx=screen.get_width()-100)
    screen.blit(text, text_position)
    
def show_congrats(record):
    font = pygame.font.Font(None, 120)
    text = font.render("CONGRATS", 1, white)
    text_position = text.get_rect(centerx=screen.get_width()-400, centery=300)
    screen.blit(text, text_position)
    
    record_font = pygame.font.Font(None, 80)
    record_text = record_font.render("Your score: " + str(record), 1, white)
    record_text_position = record_text.get_rect(centerx=screen.get_width()-400, centery=400)
    screen.blit(record_text, record_text_position)
    
def show_defeat():
    font = pygame.font.Font(None, 120)
    text = font.render("You lost", 1, white)
    text_position = text.get_rect(centerx=screen.get_width()-400, centery=300)
    screen.blit(text, text_position)
    
    sleep(1)
    finished = True

class Square():
    def __init__(self):
        self.height = 30
        self.width = 30
        self.x = randint(0, screen_height-self.height)
        self.y = randint(0, screen_width-self.width)
        self.area = pygame.Rect(self.x, self.y, self.height, self.width)
        self.cor = (randint(20, 255), randint(20, 255), randint(20, 255))
    
    def draw(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

#def draw_square():
#    square_height, square_width = 30, 30
#    color = (randint(0,255),randint(0,255),randint(0,255))
#    x,y = randint(0,screen_height - square_height),randint(0,screen_width - square_width)

#    pygame.draw.rect(screen, color, (x, y, square_height, square_width), 0)

#    return True

squares = []

for i in range(0, number_squares):
    square = Square()
    square.draw(screen)
    squares.append(square)

count_clocks = 0

count_seconds = 10
show_time(count_seconds)

points = 0

while not finished:
    
    # For events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            position = pygame.mouse.get_pos()
            
            for q in squares:
                if q.area.collidepoint(position):
                    squares.remove(q)
                    points += 1
    
    count_clocks += 1
    
    if count_clocks == 50 and points != number_squares:
        count_seconds -= 1
        count_clocks = 0
    
    screen.fill(black)
    
    for i in squares:
        i.draw(screen)
    
    show_time(count_seconds)
    show_points(points)
    
    if count_seconds == 0:
        screen.fill(black)
        show_defeat()
    
    if points == number_squares:
        screen.fill(black)
        show_congrats(count_seconds)
    
    pygame.display.update()
 
    clock.tick(50)
    
pygame.display.quit()

pygame.quit()
