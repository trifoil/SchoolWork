import pygame 
import random

class Fruit(pygame.sprite.Sprite):
    def __init__(self,sW,sH):
        super(Fruit,self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((255,255,0))
        self.sW = sW
        self.sH = sH
        self.rect = self.surf.get_rect()
        self.rect.center= (random.randint(0,sW),random.randint(0,sH)),

    def spawn(self):
        x = random.randint(0, self.sW - self.rect.width)
        y = random.randint(0, self.sH - self.rect.height)
        self.rect.topleft = (x, y)  # définir la position du fruit
        