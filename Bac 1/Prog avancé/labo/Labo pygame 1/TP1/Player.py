import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,sW,sH):
        super(Player,self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((0,0,255))
        self.sW = sW
        self.sH = sH
        self.rect = self.surf.get_rect()
        self.rect.center= (sW/2,sH/2)
        self.speed = 20
        self.direction = 'UP'

    def update(self,keys):
        self.rect.move_ip(0,0)
        if keys[pygame.K_UP] and self.direction!='DOWN':
            self.direction = 'UP'
        elif keys[pygame.K_DOWN] and self.direction !='UP':
            self.direction = 'DOWN'
        elif keys[pygame.K_RIGHT] and self.direction !='LEFT':
            self.direction = 'RIGHT'
        elif keys[pygame.K_LEFT] and self.direction !='RIGHT':
            self.direction = 'LEFT'
        
        if self.direction == 'UP':
            self.rect.move_ip(0, -20)
        if self.direction == 'DOWN':
            self.rect.move_ip(0, 20)
        if self.direction == 'LEFT':
            self.rect.move_ip(-20, 0)
        if self.direction == 'RIGHT':
            self.rect.move_ip(20, 0)

        if self.rect.left<0:
            self.rect.left = 0
        if self.rect.right > self.sW:
            self.rect.right = self.sW
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=self.sH:
            self.rect.bottom=self.sH   
            
    def collide(self,item):
        return self.rect.colliderect(item.rect)