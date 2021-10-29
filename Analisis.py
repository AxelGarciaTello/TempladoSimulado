from SemillaAleatoria import *
import numpy as np
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=60)

poblacion = 100

#Analisis de la Función Lineal
def minimoErrorLineal():
    minA = -10  #Dado que A representa la pendiente de la recta, consideramos
    maxA = 10   #que el intervalo comprendido de -10 a 10 cubre un buen rango de
    minB = 0    #valores de la recta
    maxB = 0

    rA = 1000
    rB = 1000
    rZ = 1000

    #Obtenermos el valor maximo de Y
    maximoY = puntos[0][1]

    for punto in puntos:
        if punto[1] > maximoY:
            maximoY = punto[1]

    #Para ampliar nuestra area de busqueda de la función vamos a usar como limites
    #5 veces el valor maximo de Y
    minB = -1 * abs(maximoY)
    maxB = abs(maximoY)

    #Creamos las poblaciones a realizar
    #La población con Z menor se almacena y se devuelve en la función
    for i in range(poblacion):
        # A, B, Z = semillaAleatoria(0, minA, maxA, minB, maxB)
        async_result = pool.apply_async(semillaAleatoria, (0, minA, maxA, minB, maxB))
        A, B, Z = async_result.get()
        if Z < rZ:
            rA = A
            rB = B
            rZ = Z
    return A, B

#Analisis de la función cuadratica
def minimoErrorCuadratico():
    minA = 0
    maxA = 0
    minB = 0
    maxB = 0
    minC = 0
    maxC = 0

    rA = 1000
    rB = 1000
    rC = 1000
    rZ = 1000

    minX = puntos[0]
    maxX = puntos[0]
    hk = [0,0]
    hk[1] = puntos[0][1]

    #Buscamos los puntos con el valor maximo y minimo de X, si existen 2 valores
    # iguales, se escogen el que tiene un valor de Y mayor
    for punto in puntos:
        if punto[0] == minX[0]:
            if punto[1] > minX[1]:
                minX = punto
        if punto[0] < minX[0]:
            minX = punto
        if punto[0] == maxX[0]:
            if punto[1] > maxX[1]:
                maxX = punto
        if punto[0] > maxX[0]:
            maxX = punto
        #Tambien se busca el mayor valor de Y, para relacionarlo con nuestro vertice
        if punto[1] > hk[1]:
            hk[1] = punto[1]
    #Se busca un posible candidato al punto vertice, la Y esta dada por el máximo valor de Y
    #y la X esta dada por la media entre minimo valor y el maximo valor de X
    hk[0] = minX[0] + (maxX[0]-minX[0])/2

    #Para ampliar nuestra area de busqueda de la función, tomaremos el cuadrado de Y en los puntos
    minX[1] = minX[1]*minX[1]
    maxX[1] = maxX[1]*maxX[1]
    hk[1] = hk[1]*hk[1]

    #Con los puntos seleccionados previamente, creamos un sistema de ecuaciones de 3x3
    #y procedemos a resolverlo
    Ec = np.matrix([[minX[0]*minX[0],minX[0],1],[maxX[0]*maxX[0],maxX[0],1],[hk[0]*hk[0],hk[0],1]])
    Rc = np.matrix([[minX[1]],[maxX[1]],[hk[1]]])
    R = (Ec**-1)*Rc
    R = R.tolist()

    #El resultado de nuestro sistema de ecuaciones nos ayudara a establecer los limites de nuestras
    #Variables
    minA = -1 * abs(R[0][0])
    maxA = abs(R[0][0])
    minB = -1 * abs(R[1][0])
    maxB = abs(R[1][0])
    minC = -1 * abs(R[2][0])
    maxC = abs(R[2][0])

    #Creamos las poblaciones a realizar
    #La población con Z menor se almacena y se devuelve en la función
    for i in range(poblacion):
        # A, B, C, Z = semillaAleatoria(1, minA, maxA, minB, maxB, minC, maxC)
        async_result = pool.apply_async(semillaAleatoria, (1, minA, maxA, minB, maxB, minC, maxC))
        A, B, C, Z = async_result.get()
        if Z < rZ:
            rA = A
            rB = B
            rC = C
            rZ = Z
    return A, B, C

#Analisis de la función de campana
def minimoErrorExponencial():
    minA = 0
    maxA = 0
    minB = 0
    maxB = 1    #Dado que B representa la anchura de la campana y es directamente proporcional,
    minC = 0    #es decir, a mayor valor de B menor anchura; y más aparte B tiene que ser mayor a
    maxC = 0    #0 porque si no se vuelve una parabola, hemos decidido dejarlo en un rango de 0 a 1

    rA = 1000
    rB = 1000
    rC = 1000
    rZ = 1000

    #Buscamos los valores maximos de X y de Y
    maxX = puntos[0][0]
    maxY = puntos[0][1]

    for punto in puntos:
        if punto[0] > maxX:
            maxX = punto[0]
        if punto[1] > maxY:
            maxY = punto[1]

    #Determinamos los limites de nuestras variables con el doble de los valores maximos
    #de X y de Y
    maxA = 2*maxX
    maxC = 2*maxY

    #Creamos las poblaciones a realizar
    #La población con Z menor se almacena y se devuelve en la función
    for i in range(poblacion):
        # A, B, C, Z = semillaAleatoria(2, minA, maxA, minB, maxB, minC, maxC)
        async_result = pool.apply_async(semillaAleatoria, (2, minA, maxA, minB, maxB, minC, maxC))
        A, B, C, Z = async_result.get()
        if Z < rZ:
            rA = A
            rB = B
            rC = C
            rZ = Z
    return A, B, C
