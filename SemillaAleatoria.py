from miRandom import random_numbers

puntos = [[3,6],[5,3],[5,8]]

def semillaAleatoria(tipo, minA, maxA, minB, maxB, minC = None, maxC = None):
    Z = 0
    min = 10000
    Sa = 0
    Sb = 0
    Sc = 0
    for i in range(1000):
        Z = 0
        A = random_numbers()*(maxA-minA)+minA
        B = random_numbers()*(maxB-minB)+minB
        if tipo != 0:
            C = random.uniform(0,1)*(maxC-minC)-minC
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
