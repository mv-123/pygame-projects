import pygame

#bird animation
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        for i in range(3):
            img = pygame.image.load(f"flappy bird\\imgs\\bird{i+1}.png")
            self.images.append(img)
        self.index = 0
        self.count = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.speed = 0
        self.angle = 0
        self.flying = False
        self.gameover = False
    def update(self):
        self.count += 1
        if self.count > 5:
            self.count = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        
        #gravity
        if self.flying == True:
            self.speed += 2
            if self.speed >= 7:
                self.rect.y += self.speed
                self.speed = 0
                self.angle -= 1
                if self.angle < -90:
                    self.angle = -90
            if self.rect.bottom > 600:
                self.rect.bottom = 600
                self.angle = -90
                self.flying = False
                self.gameover = True
        if pygame.mouse.get_pressed()[0] == 1 and self.flying == False and self.gameover == False:
            self.flying = True

        #flying movement
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.flying == True:
            self.angle = 10
            self.speed -= 10
            self.rect.y -= 50
            self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0 and self.flying == True:
            self.clicked = False

        #rotating the bird
        self.image = pygame.transform.rotate(self.images[self.index], self.angle)
        #print(self.flying)
        return self.flying