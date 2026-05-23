import pygame
import random
from bird import Bird
from pipe import Pipe
pygame.init()
clock = pygame.time.Clock()
fps = 40

def draw_score(score):
	text = font.render(str(score) , True, (255, 255, 255))
	screen.blit(text, (350, 30))

#images
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("flappy bird\\imgs\\icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((700, 700))
background = pygame.image.load("flappy bird\\imgs\\background.png")
ground = pygame.image.load("flappy bird\\imgs\\ground.png")
ground_scroll = 0
scroll_speed = 3
gameovertext = pygame.image.load("flappy bird\\imgs\\gameover.png")
font = pygame.font.SysFont("Bauhaus 93", 50)

#bird character
bird_group = pygame.sprite.Group()
flappy = Bird(250, 350)
bird_group.add(flappy)

#pipe
pipe_group = pygame.sprite.Group()
counter = 0

#game background
running = True
flying = False
gameover = False
passpipe = False
score = 0
while running:
    clock.tick(fps)
    counter += 1
    screen.blit(background, (0, 0))
    bird_group.draw(screen)
    pipe_group.draw(screen)

    if gameover == False:
        #pipes
        if counter >= 75:
            gapheight = random.randint(0, 200)
            bottompipe = Pipe(500, 250 + gapheight, 1)
            toppipe = Pipe(500, 250 + gapheight, -1)
            pipe_group.add(bottompipe)
            pipe_group.add(toppipe)
            counter = 0

        #screen
        #bird_group.draw(screen)
        flying = bird_group.update()
        #pipe_group.draw(screen)
        pipe_group.update(scroll_speed)
    
    #collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
        gameover = True
    if gameover == True:
        screen.blit(gameovertext, (200, 300))

    #score
    if len(pipe_group) > 0 and gameover == False:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and passpipe == False:
            passpipe = True
        if passpipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                passpipe = False
    draw_score(score)
    
    #ground scroll
    screen.blit(ground, (ground_scroll, 600))
    if gameover == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 30:
            ground_scroll = 0


    #end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()