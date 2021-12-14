from principal import *
from configuracion import *

import random
import math


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
## elijo una palabra al azar del lemario
    palabraAzar = lista[random.randint(0, len(lista)-1)]
## me aseguro que no tenga eñe
    enie = True
    while enie == True:
        if "ñ" in palabraAzar:
            palabraAzar = lista[random.randint(0, len(lista)-1)]
        else:
            enie = False
##  chequeo que no tenga acentos

    sinAcentos(palabraAzar)

## la divido en tres para repartir las letras

    palabra = palabraAzar
    palabraEn3 = len(palabra) // 3
    cont = 0

    for letra in palabra:
            if cont < palabraEn3:
                listaIzq.append(letra)
                posicionesIzq.append([random.randrange(0, ANCHO // 3 - 30), 25])
                cont += 1
            elif cont < palabraEn3 * 2:
                listaMedio.append(letra)
                posicionesMedio.append([random.randrange(ANCHO // 3 + 30, (ANCHO // 3) * 2) - 30, 25])
                cont += 1
            else:
                listaDer.append(letra)
                posicionesDer.append([random.randrange((ANCHO // 3) * 2 + 30, ANCHO - 30), 25])

def bajar(listaLetras,posiciones):
    ALTO = 600
    for i in range(len(posiciones)-1,-1,-1):
        posiciones[i][1] = posiciones[i][1] + 40
        if posiciones[i][1]>ALTO-70:
            listaLetras.pop(i)
            posiciones.pop(i)


def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
        bajar(listaIzq,posicionesIzq)
        bajar(listaMedio,posicionesMedio)
        bajar(listaDer,posicionesDer)
        pygame.time.delay(1000)                         #hace que se actualice mas lento



def estaCerca(elem, lista):
##    if len(lista)==0:
##            return False
##    else:
##        for pos in range (len(lista)):
##            if elem - lista[pos] < 15 and elem - lista[pos] > -15:
##                    return True
##            else:
##                cambiar = False
##
##            if not cambiar:
##                return False
        return True



def puntos(candidata):
    #devuelve el puntaje que le corresponde a candidata
    puntaje = 0
    for e in candidata.lower():
        if e < "a" or e > "z" :
            puntaje = 0
            return puntaje

    for e in candidata.lower():
        if e in "aeiou":
            puntaje = puntaje + 1
        else:
            if e in "jkqwxyz":
                puntaje = puntaje + 5
            else:
                puntaje = puntaje + 2

    return puntaje

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha, listaPJ):
    if(esValida(lista, candidata, listaIzq, listaMedio, listaDerecha)):
        if esPersonaje(candidata, listaPJ):
##          si es personaje da un adicional de puntos
            return (puntos(candidata) + 10)
        else:
            sonidos(candidata)
            return (puntos(candidata))
    else:
        return 0


def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    if candidata not in lista:
        return False
    else:
        esta = 0
        for i in range(len(candidata)):
            if esta==0:
                if candidata[i] not in listaIzq:
                    esta=esta + 1
            if esta==1:
                if candidata[i] not in listaMedio:
                    esta=esta + 1
            if esta==2:
                if candidata[i] not in listaDerecha:
                    return False
    return True

