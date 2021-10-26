import random
from scipy.stats import norm
import math

def templadoSimulado(minX, maxX, tipo, A, B, C = None):
    mediaX = minX+((maxX-minX)/2)

    sigmaX = (maxX-minX)/6

    if tipo == 0:
        Zc = A*mediaX+B
    elif tipo == 1:
        Zc = A*math.exp((-B)*pow(mediaX-C),2)
    elif tipo == 2:
        Zc = A*mediaX*mediaX + B*mediaX + C
    else:
        return "error"

    aleatX = random.uniform(0,1)
    obsAleX = norm.ppf(aleatX,loc=0,scale=sigmaX)
    x = mediaX+obsAleX

    if minX <= x and maxX >= x:
        if tipo == 0:
            Zn = A*x+B
        elif tipo == 1:
            Zn = A*math.exp((-B)*pow(x-C),2)
        elif tipo == 2:
            Zn = A*x*x + B*x + C
