import math

puntos = [[-7,-9],[9,-4],[6,-9],[7,1],[0,6],[-7,5],[9,-9],[4,8],[-1,9],[9,1]]

al = -0.281694
bl = 0.716913

ag = 10.9142
bg = 0.119306
cg = 1.2809

ac = -0.149584
bc = 0.067697
cc = 6.33026

def calcularLineal(x):
    return (al*x)+bl

def calcularGaussiana(x):
    potencia = pow(x-cg,2)
    ne = math.exp((-bg)*potencia)
    return ag*ne

def calcularCuadratica(x):
    return ac*x*x + bc*x + cc

def calcularDistanciasEuclidianas():
    sumaLineal = 0
    sumaGaussiana = 0
    sumaCuadratica = 0
    for par in puntos:
        yl = calcularLineal(par[0])
        yg = calcularGaussiana(par[0])
        yc = calcularCuadratica(par[0])
        disEucL = abs(par[1]-yl)
        disEucG = abs(par[1]-yg)
        disEucC = abs(par[1]-yc)
        print(par[0],"\t",par[1],"\t","{:.3f}".format(yl),"\t",
            "{:.3f}".format(disEucL),"\t","{:.3f}".format(yg),"\t",
            "{:.3f}".format(disEucG),"\t","{:.3f}".format(yc),"\t",
            "{:.3f}".format(disEucC))
        sumaLineal = sumaLineal + disEucL
        sumaGaussiana = sumaGaussiana + disEucG
        sumaCuadratica = sumaCuadratica + disEucC
    print("Suma de la ecuación lineal","{:.3f}".format(sumaLineal))
    print("Suma de la ecuación Gaussiana","{:.3f}".format(sumaGaussiana))
    print("Suma de la ecuación cuadratica","{:.3f}".format(sumaCuadratica))
    if sumaLineal<sumaGaussiana and sumaLineal<sumaCuadratica:
        print("La menor distacia es de la ecuación lineal")
    elif sumaGaussiana<sumaLineal and sumaGaussiana<sumaCuadratica:
        print("La menor distancia es de la ecuación Gaussiana")
    else:
        print("La menor distancia es de la ecuación cuadratica")

calcularDistanciasEuclidianas()