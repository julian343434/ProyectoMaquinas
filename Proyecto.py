from pygame import *
import sys ,time
from time import sleep
WHITE=(255,255,255)
Estado=False

def cargar_animacion(prefijo,sufijo,n):
    images=[]
    for i in range(1,n+1):
        name=prefijo+str(i)+sufijo
        images.append(image.load(name))       
    return images

def mostrar_animacion(screen,images,freq,x,y):
    frame=int(time.time()*freq) %len(images)
    screen.blit(images[frame],(x,y))
   

init()

ancho=1400
largo=800

screen=display.set_mode((ancho,largo))
fondo=image.load('./AscensorImagenes/fondo2.png')
AscensorIma= image.load('./AscensorImagenes/Cerrando1.png')

Abriendo=cargar_animacion("./AscensorImagenes/Cerrando",".png",3)
Cerrando=cargar_animacion("./AscensorImagenes/Abriendo",".png",3)

Cerrado=cargar_animacion("./AscensorImagenes/Cerrando",".png",1)
Estado1=False
Estado2=False

#images=[]
#for i in range(1,4):
#    name= "./AscensorImagenes/Cerrado"+str(i)+".png"
#    images.append(image.load(name))
while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    #frame=int(time.time()*2)% len(images)   
    screen.blit(fondo,(0,0))
    screen.blit(AscensorIma,(620,570))

    if Estado1==True:
        mostrar_animacion(screen,Abriendo,1,100,100)
    elif Estado1==False:
        mostrar_animacion(screen,Cerrado,1,100,100)
    #elif Estado2 == True:
    #    screen.blit(AscensorIma,(100,100))        
        
    #screen.blit(images[3],(100,100))

    display.flip()