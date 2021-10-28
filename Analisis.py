from SemillaAleatoria import *
import numpy as np

puntos = [[-7,-9],[9,-4],[6,-9],[7,1],[0,6],[-7,5],[9,-9],[4,8],[-1,9],[9,1]]

poblacion = 600

def minimoErrorLineal():
    minA = -10
    maxA = 10
    minB = 0
    maxB = 0

    rA = 1000
    rB = 1000
    rZ = 1000

    maximo = puntos[0][1]

    for punto in puntos:
        if punto[1] > maximo:
            maximo = punto[1]

    minB = -1 * abs(maximo)
    maxB = abs(maximo)
    for i in range(poblacion):
        A, B, Z = semillaAleatoria(0, minA, maxA, minB, maxB)
        if Z < rZ:
            rA = A
            rB = B
            rZ = Z
    return A, B

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
        if punto[1] > hk[1]:
            hk[1] = punto[1]
    hk[0] = minX[0] + (maxX[0]-minX[0])/2

    minX[1] = minX[1]*minX[1]
    maxX[1] = maxX[1]*maxX[1]
    hk[1] = hk[1]*hk[1]

    Ec = np.matrix([[minX[0]*minX[0],minX[0],1],[maxX[0]*maxX[0],maxX[0],1],[hk[0]*hk[0],hk[0],1]])
    Rc = np.matrix([[minX[1]],[maxX[1]],[hk[1]]])
    R = (Ec**-1)*Rc

    R = R.tolist()

    minA = -1 * abs(R[0][0])
    maxA = abs(R[0][0])
    minB = -1 * abs(R[1][0])
    maxB = abs(R[1][0])
    minC = -1 * abs(R[2][0])
    maxC = abs(R[2][0])

    for i in range(poblacion):
        A, B, C, Z = semillaAleatoria(1, minA, maxA, minB, maxB, minC, maxC)
        if Z < rZ:
            rA = A
            rB = B
            rC = C
            rZ = Z
    return A, B, C

def minimoErrorExponencial():
    minA = 0
    maxA = 0
    minB = 0
    maxB = 1
    minC = 0
    maxC = 0

    rA = 1000
    rB = 1000
    rC = 1000
    rZ = 1000

    """maxY = puntos[0][1]
    maxX = puntos[0][0]

    for punto in puntos:
        if punto[1] > maxY:
            maxY = punto[1]
        if punto[0] > maxX:
            maxX = punto[0]
        maxX = maxX + punto[0]

    maxY = maxY*maxY
    maxX = maxX*maxX

    minA = -1 * abs(maxY)
    maxA = abs(maxY)
    maxB = abs(maxX)
    minC = -1 * abs(maxX)
    maxC = abs(maxX)"""

    maxX = puntos[0][0]
    maxY = puntos[0][1]

    for punto in puntos:
        if punto[0] > maxX:
            maxX = punto[0]
        if punto[1] > maxY:
            maxY = punto[1]

    maxA = 2*maxX
    maxC = 2*maxY

    for i in range(poblacion):
        A, B, C, Z = semillaAleatoria(2, minA, maxA, minB, maxB, minC, maxC)
        if Z < rZ:
            rA = A
            rB = B
            rC = C
            rZ = Z
    return A, B, C
