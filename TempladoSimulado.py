import math
import random
from scipy.stats import norm

puntos = [[3,6],[5,3],[5,8]]
n=2
m=5

def templadoSimulado(tipo, minA, maxA, minB, maxB, minC = None, maxC = None):
    mediaA = minA + ((maxA-minA)/2)
    mediaB = minB + ((maxB-minB)/2)
    if tipo != 0:
        mediaC = minC + ((maxC-minC)/2)

    sigmaA = (maxA-minA)/6
    sigmaB = (maxA-minA)/6
    if tipo != 0:
        sigmaC = (maxC-minC)/6

    A = mediaA
    B = mediaB
    if tipo != 0:
        C = mediaC

    Zc = 0
    if tipo == 0:
        for punto in puntos:
            Zc = Zc + (punto[1]-A*punto[0]-B)
    elif tipo == 1:
        for punto in puntos:
            Zc = Zc + (punto[1]-A*punto[0]*punto[0]-B*punto[0]-C)
    elif tipo == 2:
        for punto in puntos:
            Zc = Zc + (punto[1]-A*math.exp((-B)*pow(punto[0]-C,2)))
    aleaA = random.uniform(0,1)
    aleaB = random.uniform(0,1)
    if tipo != 0:
        aleaC = random.uniform(0,1)
    obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
    obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
    if tipo != 0:
        obsAleC = norm.ppf(aleaC, loc=0, scale=sigmaC)
    nA = A+obsAleA
    nB = B+obsAleB
    if tipo != 0:
        nC = C+obsAleC
    if tipo == 0:
        if minA >= nA or nA >= maxA or minB >= nB or nB >= maxB:
            while minA >= nA or nA >= maxA or minB >= nB or nB >= maxB:
                aleaA = random.uniform(0,1)
                aleaB = random.uniform(0,1)
                obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
                obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
                nA = A+obsAleA
                nB = B+obsAleB
    else:
        if minA >= nA or nA >= maxA or minB >= nB or nB >= maxB or minC >= nC or nC >= maxC:
            while minA >= nA or nA >= maxA or minB >= nB or nB >= maxB or minC >= nC or nC >= maxC:
                aleaA = random.uniform(0,1)
                aleaB = random.uniform(0,1)
                aleaC = random.uniform(0,1)
                obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
                obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
                obsAleC = norm.ppf(aleaC, loc=0, scale=sigmaC)
                nA = A+obsAleA
                nB = B+obsAleB
                nC = C+obsAleC
    Zn = 0
    if tipo == 0:
        for punto in puntos:
            Zn = Zn + (punto[1]-nA*punto[0]-nB)
    elif tipo == 1:
        for punto in puntos:
            Zn = Zn + (punto[1]-nA*punto[0]*punto[0]-nB*punto[0]-nC)
    elif tipo == 2:
        for punto in puntos:
            Zn = Zn + (punto[1]-nA*math.exp((-nB)*pow(punto[0]-nC,2)))
    ZZT = (Zn-Zc)/(Zc*0.2)
    PA = math.exp(ZZT)
    Al = []
    Bl = []
    Cl = []
    PAl = []
    if tipo == 0:
        for i in range(n):
            for j in range(m):
                A1, B1, PA1 = cicloTempladoSimulado(tipo,nA, nB, minA, maxA, minB, maxB, sigmaA, sigmaB, i+1, Zn, PA)
                Al.append(A1)
                Bl.append(B1)
                PAl.append(PA1)
            PA1 = PAl[0]
            for numero in PAl:
                if numero > PA1:
                    numero = PA1
            for j in range(m):
                if PAl[j] == numero:
                    PA = PAl[j]
                    nA = Al[j]
                    nB = Bl[j]
        return nA, nB
    else:
        for i in range(n):
            for j in range(m):
                A1, B1, C1, PA1 = cicloTempladoSimulado(tipo,nA, nB, minA, maxA, minB, maxB, sigmaA, sigmaB, i+1, Zn, PA, nC, minC, maxC, sigmaC)
                Al.append(A1)
                Bl.append(B1)
                Cl.append(C1)
                PAl.append(PA1)
            PA1 = PAl[0]
            for numero in PAl:
                if numero > PA1:
                    numero = PA1
            for j in range(m):
                if PAl[j] == numero:
                    PA = PAl[j]
                    nA = Al[j]
                    nB = Bl[j]
                    nC = Cl[j]
        return nA, nB, nC




def cicloTempladoSimulado(tipo, A, B, minA, maxA, minB, maxB, sigmaA, sigmaB, poblacion, Z, mayor, C = None, minC = None, maxC = None, sigmaC = None):
    Zc = 0
    if tipo == 0:
        for punto in puntos:
            Zc = Zc + (punto[1]-A*punto[0]-B)
    elif tipo == 1:
        for punto in puntos:
            Zc = Zc + (punto[1]-A*punto[0]*punto[0]-B*punto[0]-C)
    elif tipo == 2:
        for punto in puntos:
            Zc = Zc + (punto[1]-A*math.exp((-B)*pow(punto[0]-C,2)))
    aleaA = random.uniform(0,1)
    aleaB = random.uniform(0,1)
    if tipo != 0:
        aleaC = random.uniform(0,1)
    obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
    obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
    if tipo != 0:
        obsAleC = norm.ppf(aleaC, loc=0, scale=sigmaC)
    nA = A+obsAleA
    nB = B+obsAleB
    if tipo != 0:
        nC = C+obsAleC
    if tipo == 0:
        if minA >= nA or nA >= maxA or minB >= nB or nB >= maxB:
            while minA >= nA or nA >= maxA or minB >= nB or nB >= maxB:
                aleaA = random.uniform(0,1)
                aleaB = random.uniform(0,1)
                obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
                obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
                nA = A+obsAleA
                nB = B+obsAleB
    else:
        if minA >= nA or nA >= maxA or minB >= nB or nB >= maxB or minC >= nC or nC >= maxC:
            while minA >= nA or nA >= maxA or minB >= nB or nB >= maxB or minC >= nC or nC >= maxC:
                aleaA = random.uniform(0,1)
                aleaB = random.uniform(0,1)
                aleaC = random.uniform(0,1)
                obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
                obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
                obsAleC = norm.ppf(aleaC, loc=0, scale=sigmaC)
                nA = A+obsAleA
                nB = B+obsAleB
                nC = C+obsAleC
    Zn = 0
    if tipo == 0:
        for punto in puntos:
            Zn = Zn + (punto[1]-nA*punto[0]-nB)
    elif tipo == 1:
        for punto in puntos:
            Zn = Zn + (punto[1]-nA*punto[0]*punto[0]-nB*punto[0]-nC)
    elif tipo == 2:
        for punto in puntos:
            Zn = Zn + (punto[1]-nA*math.exp((-nB)*pow(punto[0]-nC,2)))
    ZZT = 0
    if poblacion==1:
        ZZT = (Zn-Zc)/(Z)
    else:
        ZZT = (Zn-Zc)/(Z/pow(2,poblacion-1))
    PA = math.exp(ZZT)
    if mayor >= PA:
        while mayor >= PA:
            aleaA = random.uniform(0,1)
            aleaB = random.uniform(0,1)
            if tipo != 0:
                aleaC = random.uniform(0,1)
            obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
            obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
            if tipo != 0:
                obsAleC = norm.ppf(aleaC, loc=0, scale=sigmaC)
            nA = A+obsAleA
            nB = B+obsAleB
            if tipo != 0:
                nC = C+obsAleC
            if tipo == 0:
                if minA >= nA or nA >= maxA or minB >= nB or nB >= maxB:
                    while minA >= nA or nA >= maxA or minB >= nB or nB >= maxB:
                        aleaA = random.uniform(0,1)
                        aleaB = random.uniform(0,1)
                        obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
                        obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
                        nA = A+obsAleA
                        nB = B+obsAleB
            else:
                if minA >= nA or nA >= maxA or minB >= nB or nB >= maxB or minC >= nC or nC >= maxC:
                    while minA >= nA or nA >= maxA or minB >= nB or nB >= maxB or minC >= nC or nC >= maxC:
                        aleaA = random.uniform(0,1)
                        aleaB = random.uniform(0,1)
                        aleaC = random.uniform(0,1)
                        obsAleA = norm.ppf(aleaA, loc=0, scale=sigmaA)
                        obsAleB = norm.ppf(aleaB, loc=0, scale=sigmaB)
                        obsAleC = norm.ppf(aleaC, loc=0, scale=sigmaC)
                        nA = A+obsAleA
                        nB = B+obsAleB
                        nC = C+obsAleC
            Zn = 0
            if tipo == 0:
                for punto in puntos:
                    Zn = Zn + (punto[1]-nA*punto[0]-nB)
            elif tipo == 1:
                for punto in puntos:
                    Zn = Zn + (punto[1]-nA*punto[0]*punto[0]-nB*punto[0]-nC)
            elif tipo == 2:
                for punto in puntos:
                    Zn = Zn + (punto[1]-nA*math.exp((-nB)*pow(punto[0]-nC,2)))
            ZZT = 0
            if poblacion==1:
                ZZT = (Zn-Zc)/(Z)
            else:
                ZZT = (Zn-Zc)/(Z/pow(2,poblacion-1))
            PA = math.exp(ZZT)
    if tipo == 0:
        return nA, nB, PA
    else:
        return nA, nB, nC, PA
