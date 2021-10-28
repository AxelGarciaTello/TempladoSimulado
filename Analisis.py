from SemillaAleatoria import *

puntos = [[3,6],[5,3],[5,8]]

def minimoErrorLineal():
    minA = -10
    maxA = 10
    minB = 0
    maxB = 0

    maximo = puntos[0][1]

    for punto in puntos:
        if punto[1] > maximo:
            maximo = punto[1]

    minB = -1 * abs(maximo)
    maxB = abs(maximo)
    A, B, Z = semillaAleatoria(0, minA, maxA, minB, maxB)
    print(A,"\t",B,"\t",Z)

minimoErrorLineal()
