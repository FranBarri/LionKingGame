import pygame
from pygame.locals import *
from configuracion import *
import sys
import random



def dameLetraApretada(key):
    if key == K_a:
        return("A")
    elif key == K_b:
        return("B")
    elif key == K_c:
        return("C")
    elif key == K_d:
        return("D")
    elif key == K_e:
        return("E")
    elif key == K_f:
        return("F")
    elif key == K_g:
        return("G")
    elif key == K_h:
        return("H")
    elif key == K_i:
        return("I")
    elif key == K_j:
        return("J")
    elif key == K_k:
        return("K")
    elif key == K_l:
        return("L")
    elif key == K_m:
        return("M")
    elif key == K_n:
        return("N")
    elif key == K_o:
        return("O")
    elif key == K_p:
        return("P")
    elif key == K_q:
        return("Q")
    elif key == K_r:
        return("R")
    elif key == K_s:
        return("S")
    elif key == K_t:
        return("T")
    elif key == K_u:
        return("U")
    elif key == K_v:
        return("V")
    elif key == K_w:
        return("W")
    elif key == K_x:
        return("X")
    elif key == K_y:
        return("Y")
    elif key == K_z:
        return("Z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)

def dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)

    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #linea vertical
    pygame.draw.line(screen, (255,255,255), (ANCHO//3, ALTO-70) , (ANCHO//3, 0), 5)

    #linea vertical
    pygame.draw.line(screen, (255,255,255), (2*ANCHO//3, ALTO-70) , (2*ANCHO//3, 0), 5)

    ren1 = defaultFont.render(candidata.upper(), 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)

    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    for i in range(len(listaIzq)):
        screen.blit(defaultFont.render(listaIzq[i], 1, COLOR_LETRAS_IZQ), posicionesIzq[i])
    for i in range(len(listaMedio)):
        screen.blit(defaultFont.render(listaMedio[i], 1, COLOR_LETRAS_MEDIO), posicionesMedio[i])
    for i in range(len(listaDer)):
        screen.blit(defaultFont.render(listaDer[i], 1, COLOR_LETRAS_DER), posicionesDer[i])

    screen.blit(ren1, (190, 550))
    screen.blit(ren2, (1000, 10))
    screen.blit(ren3, (10, 10))

def dibujarNombreJugador(screen, nombre):
## escribe el nombre del jugador en la pantalla inicial
    letras = pygame.font.SysFont("Arial_Black", 60)
    screen.blit(letras.render(nombre, 1, (255, 126, 0)), (450, 350))

def esPersonaje(candidata, listaPJ):
##si la palabra candidata es un personaje de la pelicula
    if candidata in listaPJ:
      sonidoAnimal = pygame.mixer.Sound("sonidos/Hakuna.mp3")
      sonidoAnimal.play()
      return True

def sinAcentos(lista):
##    cambiar letras con acento
    for palabra in lista:
            for letra in palabra:
                if letra == "á":
                    letra = "a"
                if letra == "é":
                    letra = "e"
                if letra == "í":
                    letra = "i"
                if letra == "ó":
                    letra = "o"
                if letra == "ú":
                    letra = "u"


def sonidos(candidata):
## si la palabra es correcta, reproduce un sonido para los personajes de la pelicula y otros al azar si son otros animales
    sonidoAnimal = random.randint(1,8)

    if sonidoAnimal == 1:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Hiena.mp3")
            sonidoAnimal.play()
    elif sonidoAnimal == 2:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Cocodrilo.mp3")
            sonidoAnimal.play()
    elif sonidoAnimal == 3:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Elefante.mp3")
            sonidoAnimal.play()
    elif sonidoAnimal == 4:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Jabali.mp3")
            sonidoAnimal.play()
    elif sonidoAnimal == 5:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Leon.mp3")
            sonidoAnimal.play()
    elif sonidoAnimal == 6:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Rinoceronte.mp3")
            sonidoAnimal.play()
    elif sonidoAnimal == 7:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Tigre.mp3")
            sonidoAnimal.play()
    else:
            sonidoAnimal = pygame.mixer.Sound("sonidos/Zebra.mp3")
            sonidoAnimal.play()
