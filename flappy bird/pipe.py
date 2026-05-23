import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        super().__init__()
        self.image = pygame.image.load("flappy bird\\imgs\\pipe.png")
        self.rect = self.image.get_rect()
        pipegap = 150
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y-(pipegap/2)]
        elif position == -1:
            self.rect.topleft = [x,y+(pipegap/2)]
        
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
        if self.rect.x < 0:
            self.kill()