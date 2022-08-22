from inspect import ClassFoundException
import pygame
from operator import truediv
from pygame import*
import sys ,time
WHITE=(255,255,255)
##
ancho=1400
largo=800
posicionInicialX=620
posicionInicialY=570
CantidSube=185
cont=0
##
Actual=1
Pedido=1
Preguntar=True
velocidad=5


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
    elif PisoActual==4 :
        posicion_y=15
        posicionInicialY=posicion_y
        Piso=PisoRequerido-PisoActual
        posicion_y=-(Piso*CantidSube)+posicion_y
    else:
        posicion_y=15
        posicionInicialY=posicion_y
    return posicion_y

def mover_abajo(PisoRequerido, PisoActual):
    global posicion_y
    posicion_y=0
    if PisoActual==4 and PisoActual>PisoRequerido:
        posicion_y=15
        posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)
    elif PisoActual==3 and PisoActual>PisoRequerido:
        posicion_y=185
        posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)
    elif PisoActual==2 and PisoActual>PisoRequerido:
        posicion_y=385
        posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)
    elif PisoActual==1:
        posicion_y=570
        posicionInicialY=posicion_y
        Piso=PisoActual-PisoRequerido
        posicion_y=posicion_y+(CantidSube*Piso)
    else:
        posicion_y=570
        posicionInicialY=posicion_y
    return posicion_y

def PuertaAbrir():
        mostrar_animacion(screen,Abriendo,1,posicionInicialX,posicionInicialY)
        mostrar_animacion(screen,Abrierto,1,posicionInicialX,posicionInicialY)
def PuertaCerrar():
        mostrar_animacion(screen,Cerrando,1,posicionInicialX,posicionInicialY)
        mostrar_animacion(screen,Cerrado,1,posicionInicialX,posicionInicialY)

##################
init()
#if not Actual==3:
#posicionInicialY=570-((Actual-1)*185)
#else:


#detremina cuando se oprime un boton y arroja el valor de la posicion en ´pixels


#crea la pantalla
screen=display.set_mode((ancho,largo))

#carga el fondo
fondo=image.load('./AscensorImagenes/fondo3.png')
BotonArriba1=image.load('./AscensorImagenes/BotonArriba.png').convert_alpha()
BotonArriba2=image.load('./AscensorImagenes/BotonArriba.png').convert_alpha()
BotonArriba3=image.load('./AscensorImagenes/BotonArriba.png').convert_alpha()
BotonArriba4=image.load('./AscensorImagenes/BotonArriba.png').convert_alpha()
BotonAbajo1=image.load('./AscensorImagenes/BotonAbajo.png').convert_alpha()
BotonAbajo2=image.load('./AscensorImagenes/BotonAbajo.png').convert_alpha()
BotonAbajo3=image.load('./AscensorImagenes/BotonAbajo.png').convert_alpha()
BotonAbajo4=image.load('./AscensorImagenes/BotonAbajo.png').convert_alpha()

BotonNumero1=image.load('./AscensorImagenes/BotonNumero1.png').convert_alpha()
BotonNumero2=image.load('./AscensorImagenes/BotonNumero2.png').convert_alpha()
BotonNumero3=image.load('./AscensorImagenes/BotonNumero3.png').convert_alpha()
BotonNumero4=image.load('./AscensorImagenes/BotonNumero4.png').convert_alpha()

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

###########BOTON ABAJO
RectImagenBotonAbajo1=BotonAbajo1.get_rect()
RectImagenBotonAbajo1.left,RectImagenBotonAbajo1.top= (471,644)

RectImagenBotonAbajo2=BotonAbajo2.get_rect()
RectImagenBotonAbajo2.left,RectImagenBotonAbajo2.top= (471,450)

RectImagenBotonAbajo3=BotonAbajo1.get_rect()
RectImagenBotonAbajo3.left,RectImagenBotonAbajo3.top= (471,256)

RectImagenBotonAbajo4=BotonAbajo1.get_rect()
RectImagenBotonAbajo4.left,RectImagenBotonAbajo4.top= (471,62)

############BOTON ARRIBA
RectImagenBotonArriba1=BotonArriba1.get_rect()
RectImagenBotonArriba1.left,RectImagenBotonArriba1.top= (510,644)

RectImagenBotonArriba2=BotonArriba2.get_rect()
RectImagenBotonArriba2.left,RectImagenBotonArriba2.top= (510,450)

RectImagenBotonArriba3=BotonArriba3.get_rect()
RectImagenBotonArriba3.left,RectImagenBotonArriba3.top= (510,256)

RectImagenBotonArriba4=BotonArriba4.get_rect()
RectImagenBotonArriba4.left,RectImagenBotonArriba4.top= (510,62)

############BOTONES CON NUMEROS

RectImagenBotonNumero1=BotonNumero1.get_rect()
RectImagenBotonNumero1.left,RectImagenBotonNumero1.top= (156,580)

RectImagenBotonNumero2=BotonNumero2.get_rect()
RectImagenBotonNumero2.left,RectImagenBotonNumero2.top= (226,580)

RectImagenBotonNumero3=BotonNumero3.get_rect()
RectImagenBotonNumero3.left,RectImagenBotonNumero3.top= (156,650)

RectImagenBotonNumero4=BotonNumero4.get_rect()
RectImagenBotonNumero4.left,RectImagenBotonNumero4.top= (226,650)

preguntar=True
puerta=False
MostrarPuerta=True


########################################################################
#inicio del programa
while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        if e.type == MOUSEBUTTONDOWN and e.button ==1:
################################################################################################
##BOTON DE BAJADA
            if animando == False:
                if  RectImagenBotonNumero1.collidepoint(mouse.get_pos()):
                    Pedido=1
                elif RectImagenBotonNumero2.collidepoint(mouse.get_pos()):
                    Pedido=2
                elif RectImagenBotonNumero3.collidepoint(mouse.get_pos()):
                    Pedido=3
                elif RectImagenBotonNumero4.collidepoint(mouse.get_pos()):
                    Pedido=4
                else:                
                    if RectImagenBotonAbajo1.collidepoint(mouse.get_pos()):                      
                        Pedido=Pedido-1
                        if Pedido==0 or Actual==2 or Actual==3 or Actual==4 or Actual==5:
                            Pedido=Pedido+1
                    elif RectImagenBotonAbajo2.collidepoint(mouse.get_pos()):                      
                        Pedido=Pedido-1
                        if Pedido==0 or Actual==3 or Actual==4 or Actual==5:
                            Pedido=Pedido+1
                    elif RectImagenBotonAbajo3.collidepoint(mouse.get_pos()):                     
                        Pedido=Pedido-1
                        if Pedido==1 or Actual==4 or Actual==5:
                            Pedido=Pedido+1
                    elif RectImagenBotonAbajo4.collidepoint(mouse.get_pos()):                      
                        Pedido=Pedido-1
                        if Pedido==2 or Pedido==1 or Pedido==0:
                            Pedido=Pedido+1
        ################################################################################################
        ##BOTON DE SUBIDA
                    elif RectImagenBotonArriba4.collidepoint(mouse.get_pos()):                      
                        Pedido=Pedido+1
                        if Pedido==5 or Actual==0 or Actual==1 or Actual==2 or Actual==3:
                            Pedido=Pedido-1
                    elif RectImagenBotonArriba3.collidepoint(mouse.get_pos()):                      
                        Pedido=Pedido+1
                        if Pedido==5 or Actual==0 or Actual==1 or Actual==2:
                            Pedido=Pedido-1
                    elif RectImagenBotonArriba2.collidepoint(mouse.get_pos()):                     
                        Pedido=Pedido+1
                        if Pedido==4 or Actual==0 or Actual==1 or Actual==4:
                            Pedido=Pedido-1
                    elif RectImagenBotonArriba1.collidepoint(mouse.get_pos()):                      
                        Pedido=Pedido+1
                        if Pedido==3 or Pedido==4 or Pedido==5:
                            Pedido=Pedido-1
            else:
                print("MOVIENDOSE")
            print(Actual,Pedido)
    screen.blit(fondo,(0,0))
    screen.blit(fondo,(0,0))
    screen.blit(BotonArriba1,(510,644))
    screen.blit(BotonArriba2,(510,450))
    screen.blit(BotonArriba3,(510,256))
    screen.blit(BotonArriba4,(510,62))
    screen.blit(BotonAbajo1,(471,644))   
    screen.blit(BotonAbajo2,(471,450))
    screen.blit(BotonAbajo3,(471,256))
    screen.blit(BotonAbajo4,(471,62))
    screen.blit(BotonNumero1,(156,580))   
    screen.blit(BotonNumero2,(226,580))
    screen.blit(BotonNumero3,(156,650))
    screen.blit(BotonNumero4,(226,650))
########## 



########## PREGUNTA EL PISO Y MUEVE O BAJA DE PISO
    if Pedido>Actual and preguntar==True:
        CantidSube1=mover_arriba(Pedido,Actual)
        y=-CantidSube1+posicionInicialY
        Arriba=True
        Abajo=False
        preguntar=False
    elif Pedido<Actual and preguntar==True:
        cantidBaja1=mover_abajo(Pedido,Actual)
        y=cantidBaja1-posicionInicialY
        Abajo=True
        Arriba=False
        preguntar=False
    elif preguntar==True and Pedido==Actual:
        Arriba=False
        Abajo=False
        preguntar=True
        animando=False
        mostrar_animacion(screen,Abrierto,1,posicionInicialX,posicionInicialY)
        #print("quieto")

    if  Arriba==True:
        if y>cont:
            if MostrarPuerta==True:
                PuertaCerrar()
                MostrarPuerta=False
            mostrar_animacion(screen,Cerrado,1,posicionInicialX,posicionInicialY-cont)
            animando=True
            #print("subiendo")
            cont=cont+velocidad
        else:
            Arriba =False
            MostrarPuerta=True
            Actual=Pedido
            posicionInicialY=CantidSube1
            preguntar=True
            cont=0
            PuertaAbrir()
    elif Abajo==True:
        if y>cont:
            if MostrarPuerta==True:
                PuertaCerrar()
                MostrarPuerta=False
            mostrar_animacion(screen,Cerrado,1,posicionInicialX,posicionInicialY+cont)
            animando=True
            #print("bajando")
            cont=cont+velocidad
        else:
            Abajo=False
            MostrarPuerta = True
            Actual=Pedido
            posicionInicialY=cantidBaja1
            preguntar=True  
            cont=0
            PuertaAbrir()
    #if Activado==True:
    #    mostrar_animacion(screen,Abrierto,2,posicionInicialX,CantidSube1)
    #else:
    display.flip()
    display.update()