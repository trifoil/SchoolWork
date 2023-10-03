import pygame  #import pygame as p --> pygame deviens p 
from Player import Player
from Enemy import Enemy
from MovingFloor import MovingFloor

pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((0,0,0))

background01 = pygame.image.load("labo/Labo pygame 1/TD1/img/mountain.png").convert_alpha()
screen.blit(background01, (0,0))

floor01 = MovingFloor(0,0,SCREEN_WIDTH)
floor02 = MovingFloor(SCREEN_WIDTH,0,SCREEN_WIDTH)
floorSprites = pygame.sprite.Group()
floorSprites.add(floor01)
floorSprites.add(floor02)

player = Player(SCREEN_WIDTH,SCREEN_HEIGHT)

enemies = pygame.sprite.Group()
sprites = pygame.sprite.Group()
sprites.add(player)

ADDENEMY = pygame.USEREVENT+1        #event tout en majs
pygame.time.set_timer(ADDENEMY,250)

PLAYERANIMATION = pygame.USEREVENT+2
pygame.time.set_timer(PLAYERANIMATION, 125)

clock= pygame.time.Clock()
pygame.display.flip()

running= True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False

        if event.type == ADDENEMY:
            newE = Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)
            enemies.add(newE)
            sprites.add(newE)

        if event.type == PLAYERANIMATION:
            player.playerAnimation()
            
    pressendkeys = pygame.key.get_pressed()
    player.update(pressendkeys)
    enemies.update()
    floorSprites.update()
    
    screen.fill((0,0,0))
    screen.blit(background01,(0,0))

    for entity in floorSprites:
        screen.blit(entity.surf,entity.rect)

    for entity in sprites:
        screen.blit(entity.surf,entity.rect)
    
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        running = False
    
    pygame.display.flip()

    clock.tick(60)