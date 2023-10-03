import pygame

pygame.init()

WIDTH = 1080
HIGHT = 720
running =True
pygame.display.set_caption("Oiseau en danger")
background=pygame.image.load("mountain.png")

#Game loop 
while running:
    pygame.display.init()
    pygame.display.set_mode((WIDTH,HIGHT))
    event = pygame.event.wait()
    if event.type ==pygame.QUIT:
        running = False
    gameDisplay.blit(background,(0,0))