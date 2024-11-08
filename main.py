import pygame


screen_w = 800
screen_h = 600



background_image = pygame.image.load('images/background.png')
character_image = pygame.image.load('images/base.png')


pygame.init()




screen = pygame.display.set_mode([screen_w,screen_h])

clock = pygame.time.Clock()


#petla gry
game_on = True
while game_on == True:


    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False

        if event.type==pygame.QUIT:
            game_on = False




    screen.blit(background_image,(0,0))

    screen.blit(character_image,(270,130))

    pygame.display.flip()

    clock.tick(30)


pygame.quit()

