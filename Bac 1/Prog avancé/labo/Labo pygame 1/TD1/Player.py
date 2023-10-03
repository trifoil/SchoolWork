import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sW,sH):
        super(Player,self).__init__()

        self.anim01 = pygame.image.load("labo/Labo pygame 1/TD1/img/bird_01.png").convert_alpha()
        self.anim02 = pygame.image.load("labo/Labo pygame 1/TD1/img/bird_02.png").convert_alpha()
        self.anim03 = pygame.image.load("labo/Labo pygame 1/TD1/img/bird_03.png").convert_alpha()
        self.anim04 = pygame.image.load("labo/Labo pygame 1/TD1/img/bird_04.png").convert_alpha()
        self.anim05 = pygame.image.load("labo/Labo pygame 1/TD1/img/bird_05.png").convert_alpha()
        self.anim06 = pygame.image.load("labo/Labo pygame 1/TD1/img/bird_06.png").convert_alpha()

        self.animPlayer = [self.anim01,self.anim02,self.anim03,self.anim04,self.anim05,self.anim06]
        self.index = 0
    
        self.surf= self.animPlayer[self.index]
        self.rect=self.surf.get_rect()
        self.sW=sW
        self.sH=sH
    
    def update(self,keys):
        if keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)

        if self.rect.left<0:
            self.rect.left = 0
        if self.rect.right > self.sW:
            self.rect.right = self.sW
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=self.sH:
            self.rect.bottom=self.sH

    def playerAnimation(self):
        self.index +=1
        if self.index>5:
            self.index =0
        self.surf= self.animPlayer[self.index]