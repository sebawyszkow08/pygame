import pygame


screen_w = 800
screen_h = 600



background_image = pygame.image.load('images/background.png')
character_image = pygame.image.load('images/base.png')


pygame.init()




screen = pygame.display.set_mode([screen_w,screen_h])

clock = pygame.time.Clock()

plx = 270
ply = 130
#petla gry
game_on = True
while game_on == True:


    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False



            elif event.key == pygame.K_DOWN:
                ply += 10

            elif event.key == pygame.K_UP:
                ply -= 10
            elif event.key == pygame.K_LEFT:
                plx -= 10

            elif event.key == pygame.K_RIGHT:
                plx += 10




        if event.type==pygame.QUIT:
            game_on = False

        



    screen.blit(background_image,(0,0))

    screen.blit(character_image,(plx,ply))

    pygame.display.flip()

    clock.tick(30)


pygame.quit()

