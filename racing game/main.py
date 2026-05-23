import pygame
import random
clock = pygame.time.Clock()
fps = 40
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racing game\\imgs\\purple_car.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width()//2
        self.rect.bottom = screen.get_height() - 40
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if self.rect.left < 150:
            self.rect.left = 150
        if self.rect.right > 600:
            self.rect.right = 600

class Enemy(pygame.sprite.Sprite):
    lanes = [220, 370, 520]

    def __init__(self, i):
        super().__init__()
        image1 = pygame.image.load("racing game\\imgs\\red_car.png")
        image2 = pygame.image.load("racing game\\imgs\\yellow_car.png")
        image3 = pygame.image.load("racing game\\imgs\\green_car.png")
        self.image_list = [image1, image2, image3]
        self.reset(i)
        self.speed = random.randint(4, 15)
        
    def update(self):
        global score
        self.rect.y += self.speed
        if self.rect.y > 710:
            self.reset(random.randint(0, 2))
            score+=1
        print(score)
    
    def reset(self, i):
        self.image = self.image_list[i]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(Enemy.lanes)
        self.rect.bottom = random.randint(0, 50)

def draw_score(score):
    scoretext = scorefont.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(scoretext, (10, 50))

screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Racing Game")
icon = pygame.image.load("racing game\\imgs\\car_icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("racing game\\imgs\\road.png")
gameoverfont = pygame.font.SysFont('Helvetica', 80)
scorefont = pygame.font.SysFont('Helvetica', 40)

score = 0

running = True
road_scroll = -50
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enemy_group = pygame.sprite.Group()

game_over = False
gameovertext = gameoverfont.render("GAME OVER", True, (255, 0, 0))

for i in range(3):
    enemy = Enemy(i)
    enemy_group.add(enemy)

while running:
    clock.tick(fps)
    screen.fill((64, 219, 79))

    #road scroll
    speed = 5
    screen.blit(background, (150, road_scroll))
    if game_over == False:
        road_scroll = road_scroll + speed
        if road_scroll > 0: 
            road_scroll = -50

        #cars
        player_group.draw(screen)
        enemy_group.draw(screen)
        enemy_group.update()
        player_group.update()
        
    #score
    draw_score(score)

    #collision
    if pygame.sprite.groupcollide(player_group, enemy_group, False, False):
        game_over = True
    if game_over == True:
        screen.blit(gameovertext, (200, 300))

    for event in pygame.event.get():
        #end
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()