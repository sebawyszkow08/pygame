import pygame
import Element

screen_w = 800
screen_h = 600



background_image = pygame.image.load('images/background.png')
character_image = pygame.image.load('images/base.png')


pygame.init()




screen = pygame.display.set_mode([screen_w,screen_h])

clock = pygame.time.Clock()


headgear = Element.HeadElement()
bodygear = Element.ClothesElement()
eyesgear = Element.EyesElement()
weaponsgear = Element.WeaponElement()


pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS',30)

def create_text(screen,tekst,position):
    paragraph = my_font.render(tekst,False,(255,255,255))
    screen.bilit(paragraph,position)

#kordy poczatkowe gracza
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
                ply += 40

            elif event.key == pygame.K_UP:
                ply -= 40

            elif event.key == pygame.K_LEFT:
                plx -= 40

            elif event.key == pygame.K_RIGHT:
                plx += 40
            


            elif event.key == pygame.K_q:
                headgear.choseNext()

            elif event.key == pygame.K_w:
                weaponsgear.choseNext()
            
            elif event.key == pygame.K_e:
                eyesgear.choseNext()
            
            elif event.key == pygame.K_r:
                bodygear.choseNext()



        if event.type==pygame.QUIT:
            game_on = False

        



    screen.blit(background_image,(0,0))

    screen.blit(character_image,(plx,ply))


    screen.blit(headgear.chosenImage(),(plx,ply))
    screen.blit(bodygear.chosenImage(),(plx,ply))        
    screen.blit(eyesgear.chosenImage(),(plx,ply))        
    screen.blit(weaponsgear.chosenImage(),(plx,ply))            


    pygame.display.flip()

    clock.tick(30)


pygame.quit()

