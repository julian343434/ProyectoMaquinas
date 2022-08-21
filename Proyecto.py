from inspect import ClassFoundException
import pygame
from operator import truediv
from pygame import*
import sys ,time
WHITE=(255,255,255)

ancho=1400
largo=800
posicionInicialX=620
CantidSube=185
cont=0
posicionInicialY=570

def cargar_animacion(prefijo,sufijo,n):
    images=[]
    for i in range(1,n+1):
        name=prefijo+str(i)+sufijo
        images.append(image.load(name))       
    return images


def mostrar_animacion(screen,images,freq,x,y):
    frame=int(time.time()*freq) %len(images)
    screen.blit(images[frame],(x,y))
   
def mover_arriba(PisoRequerido,PisoActual):
    global posicion_y
    posicion_y=0
    if PisoActual==1 and PisoActual<PisoRequerido:
        posicion_y=570
        posicionInicialY=posicion_y
        Piso=PisoRequerido-PisoActual
        posicion_y=-(Piso*CantidSube)+posicion_y
    elif PisoActual==2 and PisoActual<PisoRequerido:
        posicion_y=385
        posicionInicialY=posicion_y
        Piso=PisoRequerido-PisoActual   
        posicion_y=-(Piso*CantidSube)+posicion_y
    elif PisoActual==3 and PisoActual<PisoRequerido:
        posicion_y=185
        posicionInicialY=posicion_y
        Piso=PisoRequerido-PisoActual
        posicion_y=-(Piso*CantidSube)+posicion_y
    elif PisoActual==4 and PisoActual<PisoRequerido:
        posicion_y=15
        posicionInicialY=posicion_y
        Piso=PisoRequerido-PisoActual
        posicion_y=-(Piso*CantidSube)+posicion_y

    return posicion_y

def mover_abajo(PisoRequerido, PisoActual):
    global posicion_y
    posicion_y=0
    if PisoActual==4 and PisoActual>PisoRequerido:
        posicion_y=15
        #posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)
    elif PisoActual==3 and PisoActual>PisoRequerido:
        posicion_y=185
        #posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)
    elif PisoActual==2 and PisoActual>PisoRequerido:
        posicion_y=385
        #posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)
    elif PisoActual==1 and PisoActual>PisoRequerido:
        posicion_y=570
        #posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)

    return posicion_y

def PuertaAbrir():
        mostrar_animacion(screen,Abriendo,1,posicionInicialX,CantidSube1)
        mostrar_animacion(screen,Abrierto,1,posicionInicialX,CantidSube1)
def PuertaCerrar():
        mostrar_animacion(screen,Cerrando,1,posicionInicialX,cantidBaja1)
        mostrar_animacion(screen,Cerrado,1,posicionInicialX,cantidBaja1)




##################
init()

Actual=1
Pedido=1
velocidad=5
#if not Actual==3:
posicionInicialY=570-((Actual-1)*185)
#else:
posicionInicialY=570-((Actual-1)*185)


#detremina cuando se oprime un boton y arroja el valor de la posicion en ´pixels


#crea la pantalla
screen=display.set_mode((ancho,largo))

#carga el fondo
fondo=image.load('./AscensorImagenes/fondo3.png')




#carga animaciones
Abriendo=cargar_animacion("./AscensorImagenes/Cerrando",".png",3)
Cerrando=cargar_animacion("./AscensorImagenes/Abriendo",".png",3)
Cerrado=cargar_animacion("./AscensorImagenes/Abriendo",".png",1)
Abrierto=cargar_animacion("./AscensorImagenes/Cerrando",".png",1)

#mueve el elvador hacia arriba
#CantidSube1=mover_arriba(4,2)

#mueve el elevador hacia abajo o arriba


#CantidBaja1=mover_abajo(Pedido,Actual)
CantidSube1=mover_arriba(Pedido,Actual)
cantidBaja1=mover_abajo(Pedido,Actual)
preguntar=True
puerta=False
MostrarPuerta=True
#inicio del programa
while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    screen.blit(fondo,(0,0))


    screen.blit(fondo,(0,0))




    if Pedido>Actual and preguntar==True:
        y=-CantidSube1+posicionInicialY
        Arriba=True
        Abajo=False
        preguntar=False
    elif Pedido<Actual and preguntar==True:
        y=cantidBaja1-posicionInicialY
        Abajo=True
        Arriba=False
        preguntar=False
    elif preguntar==True and Pedido==Actual:
        Arriba=False
        Abajo=False
        preguntar=True 
        mostrar_animacion(screen,Abrierto,1,posicionInicialX,posicionInicialY)

    if  Arriba==True:
        if y>cont:
            if MostrarPuerta==True:
                PuertaCerrar()

            mostrar_animacion(screen,Cerrado,1,posicionInicialX,posicionInicialY-cont)
            cont=cont+velocidad
        else:
            PuertaAbrir()
            MostrarPuerta=True
    elif Abajo==True:
        if y>cont:
            mostrar_animacion(screen,Cerrado,1,posicionInicialX,posicionInicialY+cont)
            cont=cont+velocidad
        else:
            PuertaAbrir()
            MostrarPuerta = True
    #if Activado==True:
    #    mostrar_animacion(screen,Abrierto,2,posicionInicialX,CantidSube1)
    #else:
        

    display.flip()
    display.update()