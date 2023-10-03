import pygame

class MovingFloor(pygame.sprite.Sprite):
    def __init__(self,x,y,sW):
        super(MovingFloor,self). __init__()
        self.surf=pygame.image.load("labo/Labo pygame 1/TD1/img/cailloux.png").convert_alpha()
        self.rect=self.surf.get_rect(topleft=(x,y))
        self.sW= sW

    def update(self):
        self.rect.move_ip(-10,0)
        if self.rect.right<10:
            self.rect=self.surf.get_rect(topleft=(self.sW,0))