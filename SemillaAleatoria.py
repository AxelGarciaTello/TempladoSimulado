from miRandom import random_numbers
import math

puntos = [[-7,-9],[9,-4],[6,-9],[7,1],[0,6],[-7,5],[9,-9],[4,8],[-1,9],[9,1]] 

individuos = 1000

def semillaAleatoria(tipo, minA, maxA, minB, maxB, minC = None, maxC = None):
    Z = 0
    min = 10000
    Sa = 0
    Sb = 0
    Sc = 0
    for i in range(individuos):
        Z = 0
        A = random_numbers()*(maxA-minA)+minA
        B = random_numbers()*(maxB-minB)+minB
        if tipo != 0:
            C = random_numbers()*(maxC-minC)+minC
        if tipo == 0:
            for punto in puntos:
                Z = Z + (punto[1]-A*punto[0]-B)*(punto[1]-A*punto[0]-B)
        elif tipo == 1:
            for punto in puntos:
                Z = Z + (punto[1]-A*punto[0]*punto[0]-B*punto[0]-C)*(punto[1]-A*punto[0]*punto[0]-B*punto[0]-C)
        elif tipo == 2:
            for punto in puntos:
                Z = Z + (punto[1]-A*math.exp((-B)*pow(punto[0]-C,2)))*(punto[1]-A*math.exp((-B)*pow(punto[0]-C,2)))
        if Z < min:
            min = Z
            Sa = A
            Sb = B
            if tipo != 0:
                Sc = C
    if tipo == 0:
        return Sa, Sb, min
    return Sa, Sb, Sc, min
