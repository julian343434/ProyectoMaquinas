from pygame import *
import sys ,time
from time import sleep
WHITE=(255,255,255)

def cargar_animacion(prefijo,sufijo,n):
    images=[]
    for i in range(1,n+1):
        name=prefijo+str(i)+sufijo
        images.append(image.load(name))
    return images

def mostrar_animacion(screen,images,freq,x,y,m):
    frame=int(time.time()*freq) %len(images)
    screen.blit(images[frame],(x,y))   

init()

ancho=1400
largo=800

screen=display.set_mode((ancho,largo))
fondo=image.load('./AscensorImagenes/Fondo.png')
AscensorIma= image.load('./AscensorImagenes/Cerrado1.png')
Abriendo=cargar_animacion("./AscensorImagenes/Cerrado",".png",3)


#images=[]
#for i in range(1,4):
#    name= "./AscensorImagenes/Cerrado"+str(i)+".png"
#    images.append(image.load(name))
cantidad =0
while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    #frame=int(time.time()*2)% len(images)   
    screen.blit(fondo,(0,0))
    screen.blit(AscensorIma,((ancho/2)-(150/2),largo-200))
    mostrar_animacion(screen,Abriendo,2,100,100,1)   
    #screen.blit(images[frame],(0,0))

    display.flip()