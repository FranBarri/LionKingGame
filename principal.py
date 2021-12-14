import os, random, sys, math, time


import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
##        inicio del soundmixer
        pygame.mixer.init()

        #Preparar la ventana
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        listaIzq = []
        listaMedio = []
        listaDer = []
        posicionesIzq = []
        posicionesMedio = []
        posicionesDer = []
        lista = []
        listaPJ = []
        listaRecords = []
        listaJugadores = []
        milisegundos = []
        nombre = ""
        texto = ""
        textoFinal = ""

##    abrir el lemario de todos los personajes

        archivo= open("lemario_rey_leon.txt","r", encoding='ISO8859')
        for linea in archivo.readlines():
            lista.append(linea[0:-1])

##    abrir el lemario de personajes especiales

        archivo= open("personajes_rey_leon.txt","r", encoding='ISO8859')
        for linea in archivo.readlines():
            listaPJ.append(linea[0:-1])



#               Bucle principal


##              Pantalla Inicio
##      Musica
        pygame.mixer.music.load("sonidos/inicio.mp3")
        pygame.mixer.music.play(1)

##      Pantalla, titulo y fondo del juego, centrar ventana
        pygame.display.set_caption("¡Bienvenido a Las Tierras del Reino!")
        pantalla = pygame.display.set_mode((1250, 600))
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        fondo = pygame.image.load("imagenes/inicio.png")
        pantalla.blit(fondo, [0,0])
        pygame.display.flip()
##      Icono
        pygame.display.set_caption("¡Bienvenido a Las Tierras del Reino!")
        icono = pygame.image.load("imagenes/icono.png")
        pygame.display.set_icon(icono)

##          recorrer eventos para tomar las teclas presionadas
        inicio = True
        while inicio:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    texto += letra
                    if e.key == K_BACKSPACE:
                        texto = texto[0:len(texto)-1]
                    if e.key == K_RETURN:
                        nombre = texto
                        texto = ""
                        inicio = False

                dibujarNombreJugador(pantalla, texto)

                pygame.display.flip()
                screen.blit(fondo, [0,0])

##              Juego Principal

##      Musica principal
        pygame.mixer.music.load("sonidos/ambiente2.mp3")
        pygame.mixer.music.play(3)

##      Pantalla, titulo y fondo del juego
        pygame.display.set_caption("¡A jugar en la selva!")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        fondo = pygame.image.load("imagenes/principal.jpeg").convert()
        screen.blit(fondo, [0,0])
        pygame.display.flip()
##
        while segundos > fps/1000:

            cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
            dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)


        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer, listaPJ)

                        candidata = ""


            milisegundos.append(pygame.time.get_ticks()) #toma el tiempo transcurrido en la primer pantalla
            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000 + milisegundos[0]/1000 #suma el tiempo transcurrido al tiempo total

            #Limpiar pantalla anterior

            screen.blit(fondo, [0,0])

          #Dibujar de nuevo todo
            dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)
            pygame.display.flip()

            actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer)

        fin = True
        jugador = ""
        while fin:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == KEYDOWN:
##                    if e.key == K_RETURN:
                        fin = False
                if e.type == QUIT:
                        pygame.quit()
                        return()
#

                        fin = False

            pygame.display.flip
            screen.fill(COLOR_FONDO)

##           Pantalla Final

##      Musica
        pygame.mixer.music.load("sonidos/cierre.mp3")
        pygame.mixer.music.play(1)

##      Pantalla, titulo y fondo, volver a centrar ventana
        pantalla = pygame.display.set_mode((1250, 600))
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.display.set_caption("¡Esperamos que te hayas divertido!")
        fondo = pygame.image.load("imagenes/fin.png").convert()
        screen.blit(fondo, [0,0])
        pygame.display.flip()

##      Muestra carteles con el nombre del usuario ingresado anteriormente y los puntos hechos
        textoFinal = "TU PUNTAJE FUE :  " + str(puntos)
        textoFinal2 = "¡Gracias por jugar  " + nombre + "!"

##      abre un .txt para guardar los jugadores
        archivo = open("jugadores.txt","a", encoding='ISO8859')
        jugador = nombre
        archivo.writelines(jugador + "\n")
        archivo.close()

##      guarda los nombres de los jugadores en una lista
        archivo= open("jugadores.txt","r", encoding='ISO8859')
        for linea in archivo.readlines():
            listaJugadores.append(linea[0:-1])

##      abre un .txt para guardas los puntajes
        archivo = open("records.txt","a", encoding='ISO8859')
        archivo.writelines(str(puntos) + "\n")
        archivo.close()

##      guarda los puntajes en una lista
        archivo= open("records.txt","r", encoding='ISO8859')
        for linea in archivo.readlines():
            listaRecords.append(linea[0:-1])

        for i in range(len(listaRecords)):
            listaRecords[i] = int(listaRecords[i])

##      busco el mayor puntaje, luego lo vuelvo a pasar a str para poder mostrarlo en pantalla
        recordMax = max(listaRecords)

##      busca el jugador con mejor puntaje y lo muestra en pantalla
        for i in range(len(listaRecords)):
            if listaRecords [i] == recordMax:
                jugadorRecord = "El record del juego es de  " + listaJugadores[i] + "  con  " + str(recordMax) + "  puntos"
                escribirEnPantalla(screen, jugadorRecord , (120, 500), 40, (191,122,54))

##  escribe en pantalla todas las lineas finales
        escribirEnPantalla(screen, textoFinal, (30, 20), 40, (20,200,20))
        escribirEnPantalla(screen, textoFinal2, (210, 200), 60, (255,255,0))




        pygame.display.flip()

        final = True
        while final:


            # para Recorrer la cola de eventos
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            pygame.display.flip()


##Programa Principal ejecuta Main
if __name__ == "__main__":
    main()