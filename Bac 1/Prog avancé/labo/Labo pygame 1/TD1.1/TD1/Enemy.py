import pygame 
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sW, sH):
        super(Enemy,self).__init__()
        self.surf= pygame.image.load("labo/Labo pygame 1/TD1/img/fireball.png").convert_alpha()
        self.rect = self.surf.get_rect(center=(random.randint(sW+20,sW+100),random.randint(0,sH),))
        self.speed =random.randint(5,10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right<0:
            self.kill()