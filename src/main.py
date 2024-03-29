import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((500, 500))
background_color = (50,50,50)
font = pygame.font.SysFont('Arial',32)
circles = []
def startScreen(screen):
  global s
  t = True
  while t:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
    if pygame.mouse.get_pressed()[0]:
      pygame.time.delay(200)
      print("clicked")
      s = False
      t = False
    screen.fill(background_color)
    text = "hi"
    text = font.render(text, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (250,200)
    screen.blit(text, textRect)
    clickText = "click"
    clickText = font.render(clickText, True, (0, 0, 0))
    clickRect = clickText.get_rect()
    clickRect.center = (250,300)
    screen.blit(clickText, clickRect)
    pygame.display.flip()

x = 250
y = 250
cx = x
cy = y
movement = 1
cirpos = (cx,cy)
s = True
running = True
fps = 10
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      quit()
    if s:
      startScreen(screen) 
  keys = pygame.key.get_pressed()  
  if keys[pygame.K_UP]:
    y=y-movement
    pygame.time.delay(2)
    movement = 1
  if keys[pygame.K_DOWN]:
    y=y+movement
    pygame.time.delay(2)
    movement = 1
  if keys[pygame.K_LEFT]:
    x=x-movement
    pygame.time.delay(2)
    movement = 1
  if keys[pygame.K_RIGHT]:
    x=x+movement
    pygame.time.delay(2)
    movement = 1
  if keys[pygame.K_ESCAPE]:
    running = False
    quit()
  if keys[pygame.K_c]:
    cy = y
    cx = x
    cirpos = (cx,cy)
    circles.append(cirpos)
    for circle in circles:
      pygame.draw.circle(screen, (255,200,0), circle, 20)
  pygame.draw.rect(screen,(150,200,150),pygame.Rect(x,y,50,50))
  pygame.display.update()
  screen.fill(background_color)
