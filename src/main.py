#Cormac Stone
import pygame
import random
#from player import player
x = 200
y = 200
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
fps = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y=y-10
    if keys[pygame.K_DOWN]:
          y=y+10
    if keys[pygame.K_LEFT]:
          x=x-10
    if keys[pygame.K_RIGHT]:
          x=x+10
    if keys[pygame.K_ESCAPE]:
          running = False
    #if collision == True
      
    background_color = (50,50,50)
    screen.fill(background_color)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(x,y,100,100))
    pygame.display.update()
  
