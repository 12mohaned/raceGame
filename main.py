import pygame
import time
import random
from game_settings import Settings
from car import car
pygame.init()
car = car(400,400)
steps = 50
thing_startx = random.randrange(0, Settings.display_width)
thing_starty =-100
thing_speed = 10
thing_width = 100
thing_height = 100
score = 0

Gamescreen = pygame.display.set_mode((Settings.display_width,Settings.display_height))
pygame.display.set_caption(Settings.title)
car_spirite = pygame.image.load(Settings.car)
Background = pygame.image.load(Settings.Background)
clock = pygame.time.Clock()
Running = True

def Block(x,y,width,height,color):
    pygame.draw.rect(Gamescreen, color, [x,y,width,height])
    
def background():
    Gamescreen.blit(Background,(0,0))

def Car(x,y):
    Gamescreen.blit(car_spirite,(x,y))
    
#def  HandleControl(event):

def text_objects(Text,font):
    textSurface = font.render(Text,True,Settings.rectangle_color)
    return textSurface, textSurface.get_rect()

def message_display(Text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(Text, largeText)
    TextRect.center = ( (Settings.display_width//2) , (Settings.display_height//2) )
    Gamescreen.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    
def Crash():
    message_display("You Crashed")
    
while Running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            break
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
               
               if(car.get_x() < 700):
                car.x = car.x + steps
                car.set_x(car.x)
                
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
               if(car.get_x() > 0):
                   car.x = car.x - steps
                   car.set_x(car.x)
    background()
        
    if thing_starty > Settings.display_height:
        thing_startx = random.randrange(0, Settings.display_width-Settings.car_width)
        thing_starty = -100
        
    Car(car.get_x(),car.get_y())
    thing_starty+=thing_speed
    Block(thing_startx,thing_starty,thing_width,thing_height,Settings.rectangle_color)
    clock.tick(60)

    if car.get_y()< thing_starty+thing_height:
            if car.get_x() == thing_startx and car.get_x() < thing_startx + thing_width or car.get_x()+Settings.car_width > thing_startx and car.get_x() + Settings.car_width < thing_startx+thing_width:
                Crash()
                x  = 300
                y  =  400
                score+=1
                print(score)

        
    pygame.display.update()
    
pygame.quit()
