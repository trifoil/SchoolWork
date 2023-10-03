import pygame 
from Player import Player
from Fruit import Fruit 

pygame.init()
move = pygame.USEREVENT + 1
pygame.time.set_timer(move, 200)
SCREEN_WIDTH = 1200  
SCREEN_HEIGHT = 800
score = 0
game_over=1

pygame.display.set_caption("Snake")

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((0,0,0))

clock= pygame.time.Clock()
pygame.display.flip()

snake= Player(SCREEN_WIDTH,SCREEN_HEIGHT)
fruit = Fruit(SCREEN_WIDTH,SCREEN_HEIGHT)

def afficher_score (color,font,size):
    font_score = pygame.font.SysFont(font,size)
    surface_score = font_score.render('Score : ' + str(score), True, color)
    rect_score =surface_score.get_rect()
    screen.blit(surface_score,rect_score)

def game_over_screen():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
running= True 

while running:
    pressendkeys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == move:
            snake.update(pressendkeys)
        
        if game_over ==0:
            pygame.quit()
            quit()

    screen.fill((0,0,0))
    screen.blit(snake.surf,snake.rect)
    screen.blit(fruit.surf,fruit.rect)
    
    if snake.collide(fruit):
        fruit.spawn()
        score+=10
    afficher_score((255,255,255),'times new roman',20)

    pygame.display.flip()

    clock.tick(60)
