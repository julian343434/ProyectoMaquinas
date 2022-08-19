from re import ASCII
import pygame , sys
pygame.init()

#definen los colores

BLACK   =(0,0,0)
WHITE   =(255,255,255)
GREEN   =(0,255,0)
RED     =(255,0,0)
BLUE    =(0,0,255)


size= (400,1500)

#crear ventana 
screen= pygame.display.set_mode(size)

#cargando imagen
ascensor= pygame.image.load("ANIMACION-ABRIENDOSE.gif")



#class Ascensor(pygame.sprite.Sprite):
    #def __init__(self):
     #   super().__init__()
     #   self.image = pygame.image.load("ANIMACION-ABRIENDOSE.gif").convert()    
     #   self.image.set_colorkey(BLACK)
     #   self.rect=self.image.get_rect()
     #   self.sprites.append(pygame.image.load('ANIMACION-ABRIENDOSE.gif'))

#Ascensor = Ascensor()
#Ascensor.rect.x=200
#Ascensor.rect.y=750 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #colorea la pantalla
    screen.fill(WHITE)

    ##---- ZONA DE DIBUJO
    screen.blit(ANIMACION-ABRIENDOSE.gif,(200,200))

    #for i in range(100,700,100)
        #pygame.draw.rect(screen,BLACK,(x,230,50,50))

    #pygame.draw.line(screen,GREEN,[0,100],[100,100],5)
    #pygame.draw.rect(screen,BLACK,(100,100,80,80))
    #pygame.draw.circle(screen,BLACK,(200,200),30)
    
    
    ##---- ZONA DE DIBUJO

    #actualiza la pantalla
    pygame.display.flip()