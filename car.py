import pygame
import time
import random
pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

car_width = 73
game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("FIRST GAME!")
clock = pygame.time.Clock()
car_image = pygame.image.load('racecar.png')

def car(x,y):
    game_display.blit(car_image,(x,y))

def text_objects(text, font, colour):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_screen(message):
    large_text = pygame.font.Font("freesansbold.ttf", 90)
    textsurf, textrect = text_objects(message, large_text, black)
    textrect.center = ((display_width / 2),(display_height / 2))
    game_display.blit(textsurf, textrect)
    pygame.display.update()
    
    time.sleep(5)
def crash():
    message_screen("YOU CRASHED")
#helps render obstacles
def things(thing_x, thing_y, thing_width, thing_height, colour):
    pygame.draw.rect(game_display, colour, [thing_x, thing_y, thing_width, thing_height])
#main game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    
    start_x = random.randrange(0,display_width)
    start_y = -600
    o_speed = 20
    o_width = 100
    
    o_height = 100    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -50
                elif event.key == pygame.K_RIGHT:
                    x_change = 50  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
            x += x_change        
        
        game_display.fill(white)
        things(start_x, start_y, o_width, o_height, green)
        start_y += o_speed
        car(x,y)
        
        if x > display_width - car_width or x < 0:
            crash()
            gameExit = True
        if start_y > display_height:
            start_y = 0 - display_height
            start_x = random.randrange(0,display_width)    
        
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
                
