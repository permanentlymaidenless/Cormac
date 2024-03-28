import pygame
import random
#from player import player
pygame.init()
screen = pygame.display.set_mode((500, 500))
background_color = (50,50,50)
font = pygame.font.SysFont('Arial',32)

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

x = 200
y = 200
s = True
running = True
fps = 5
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
          quit()
    if s:
      startScreen(screen)
  keys = pygame.key.get_pressed()    
  if keys[pygame.K_UP]:
        y=y-1
        pygame.time.delay(2)
  if keys[pygame.K_DOWN]:
        y=y+1
        pygame.time.delay(2)
  if keys[pygame.K_LEFT]:
        x=x-1
        pygame.time.delay(2)
  if keys[pygame.K_RIGHT]:
        x=x+1
        pygame.time.delay(2)
  if keys[pygame.K_ESCAPE]:
        quit()
        running = False
  screen.fill(background_color)
  pygame.draw.rect(screen,(150,200,150),pygame.Rect(x,y,50,50))
  pygame.display.update()
  
    
      
    
