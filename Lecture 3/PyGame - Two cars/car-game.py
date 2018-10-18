import pygame
#Let's import the Car Class
from car import Car
pygame.init()
 
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
        
SCREENWIDTH=400
SCREENHEIGHT=500
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# INITIALIZE SPEED
speed = 1


playerCar = Car(RED, 20, 30, speed)
playerCar.rect.x = 200
playerCar.rect.y = 300

PURPLE = (255,0,255)

otherCar = Car(PURPLE, 60,80,50) 
otherCar.rect.x = 60
otherCar.rect.y = 100

# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(otherCar)
 
#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(otherCar)


while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

        # Capture the keys event
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
            
        if keys[pygame.K_UP]:
            speed += 0.05
                
        if keys[pygame.K_DOWN]:
            speed -= 0.05
        
        #Game Logic
        playerCar.moveForward(speed)
        
        if abs(playerCar.rect.y) > SCREENHEIGHT:
            carryOn = False
        
        # COLLISION AVOIDANCE
        pygame.sprite.spritecollide(playerCar, all_coming_cars, dokill=True)
        
        
        all_sprites_list.update()
 
        #Drawing on Screen
        screen.fill(GREEN)
        #Draw The Road
        pygame.draw.rect(screen, GREY, [40,0, 200,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
        
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per second e.g. 60
        clock.tick(60)
 
pygame.quit()