import pygame
import random
pygame.init()

pygame.display.set_caption('Rat eating Cheese')

WIDTH = 640
HEIGHT = 480


screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set up the hero
hero = pygame.sprite.Sprite()
hero.image = pygame.image.load('dagiz.png')  # Add image and rectangle properties to the hero
hero.rect = hero.image.get_rect()
hero_group = pygame.sprite.GroupSingle(hero)
TILE_SIZE = hero.rect.width
NUM_TILES_WIDTH = WIDTH / TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE

cheeses1 = pygame.sprite.OrderedUpdates()
def add_cheese1(cheeses1):
    cheese1 = pygame.sprite.Sprite()
    cheese1.image = pygame.image.load('cheese1.bmp')
    cheese1.image = pygame.transform.flip(cheese1.image, True, False)
    cheese1.rect = cheese1.image.get_rect()
    cheese1.rect.left = random.randint(0, NUM_TILES_WIDTH - 1) * TILE_SIZE
    cheese1.rect.top = random.randint(0, NUM_TILES_HEIGHT - 1) * TILE_SIZE
    cheeses1.add(cheese1)
for i in range(25):
    add_cheese1(cheeses1)  # add the cheese!

pygame.time.set_timer(pygame.USEREVENT, 3000)

win = False
quit = False
while quit != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit = True
        if event.type == pygame.KEYDOWN:  # Move the hero around the screen
            if event.key == pygame.K_UP:
                hero.rect.top -= TILE_SIZE
            elif event.key == pygame.K_DOWN:
                hero.rect.top += TILE_SIZE
            elif event.key == pygame.K_RIGHT:
                hero.rect.right += TILE_SIZE
            elif event.key == pygame.K_LEFT:
                hero.rect.right -= TILE_SIZE
        if event.type == pygame.USEREVENT:
            if win == False:
                add_cheese1(cheeses1)


        pygame.sprite.groupcollide(hero_group, cheeses1, False, True)
        collides = pygame.sprite.groupcollide(hero_group,  cheeses1, False, True)

        if len(cheeses1) == 0:
            win = True


    screen.fill((0, 0, 0))
    if win:
        font = pygame.font.Font(None, 60)
        text_image = font.render("NICE! You Win!", True, (0, 255, 0))
        text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
        screen.blit(text_image, text_rect)

    cheeses1.draw(screen)
    hero_group.draw(screen)  # add these lines at the end of the main loop
    pygame.display.update()

pygame.quit()
