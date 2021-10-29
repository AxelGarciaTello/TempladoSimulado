from miRandom import random_numbers
import math

puntos = [[-7,-9],[9,-4],[6,-9],[7,1],[0,6],[-7,5],[9,-9],[4,8],[-1,9],[9,1]]
# puntos = []

individuos = 3500

#Semilla Aletoria
def semillaAleatoria(tipo, minA, maxA, minB, maxB, minC = None, maxC = None):
    Z = 0
    min = 10000
    Sa = 0
    Sb = 0
    Sc = 0
    for i in range(individuos):
        Z = 0

        #Se inicializan las semillas con los limites establecidos en los parametros
        A = random_numbers()*(maxA-minA)+minA
        B = random_numbers()*(maxB-minB)+minB
        #Si es una función lineal, no necesitamos la semilla C
        if tipo != 0:
            C = random_numbers()*(maxC-minC)+minC

        #Dado que Z = (Y1-Yc1)^2+...(Yn-Ycn)^2
        #Colocamos esta operación de un bucle.
        #Como Yc cambia con respecto a la función base que se esta analizando
        #Se tienen que especificar los casos
        if tipo == 0:
            for punto in puntos:
                Z = Z + (punto[1]-A*punto[0]-B)*(punto[1]-A*punto[0]-B)
        elif tipo == 1:
            for punto in puntos:
                Z = Z + (punto[1]-A*punto[0]*punto[0]-B*punto[0]-C)*(punto[1]-A*punto[0]*punto[0]-B*punto[0]-C)
        elif tipo == 2:
            for punto in puntos:
                Z = Z + (punto[1]-A*math.exp((-B)*pow(punto[0]-C,2)))*(punto[1]-A*math.exp((-B)*pow(punto[0]-C,2)))

        #Si la Z encontrada es menor a alguna Z anterior, guardamos su valor
        if Z < min:
            min = Z
            Sa = A
            Sb = B
            if tipo != 0:
                Sc = C
    #Devolvemos los valores que dieron origen a la Z minima
    if tipo == 0:
        return Sa, Sb, min
    return Sa, Sb, Sc, min
