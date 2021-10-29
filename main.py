from Analisis import *
import matplotlib.pyplot as plt
import math
import time

al = 0
bl = 0

ag = 0
bg = 0
cg = 0

ac = 0
bc = 0
cc = 0

#Dado un valor de X y los valores de las contantes de la función (buscados
#previamente) buscamos el resultado Y
def calcularLineal(x):
    return (al*x)+bl

def calcularGaussiana(x):
    potencia = pow(x-cg,2)
    ne = math.exp((-bg)*potencia)
    return ag*ne

def calcularCuadratica(x):
    return ac*x*x + bc*x + cc

def calcularDistanciasEuclidianas():
    response = ""
    sumaLineal = 0
    sumaGaussiana = 0
    sumaCuadratica = 0

    global al, bl, ac, bc, cc, ag, bg, cg

    #Buscamos nuestros valores de cada función con respecto a los puntos
    al, bl = minimoErrorLineal()
    ac, bc, cc = minimoErrorCuadratico()
    ag, bg, cg = minimoErrorExponencial()

    print("lineal: \tA:", al, "\tB:", bl)
    response += "lineal:              A: {}   \tB: {} \n".format(al,bl)
    print("cuadratico: A:", ac, "\tB:", bc, "\tC:", cc)
    response += "cuadratico:    A: {}   \tB: {} \tC: {}\n".format(ac,bc,cc)
    print("exponencial: A:", ag, "\tB:", bg, "\tC:", cg)
    response += "exponencial:  A: {}   \tB: {} \tC: {}\n\n".format(ag,bg,cg)

    for par in puntos:
        #Resolvemos las ecuaciones con los valores de X
        yl = calcularLineal(par[0])
        yg = calcularGaussiana(par[0])
        yc = calcularCuadratica(par[0])

        #Buscamos la distrancia entre el punto y el valor de la función
        disEucL = abs(par[1]-yl)
        disEucG = abs(par[1]-yg)
        disEucC = abs(par[1]-yc)
        print(par[0],"\t",par[1],"\t","{:.3f}".format(yl),"\t",
            "{:.3f}".format(disEucL),"\t","{:.3f}".format(yg),"\t",
            "{:.3f}".format(disEucG),"\t","{:.3f}".format(yc),"\t",
            "{:.3f}".format(disEucC))
        response += "{} \t {} \t {:.3f} \t {:.3f} \t {:.3f} \t {:.3f} \t {:.3f} \t {:.3f} \n".format(par[0],par[1],yl,disEucL,yg,disEucG,yc,disEucC)

        #Vamos sumando esta diferencia de distancias
        sumaLineal = sumaLineal + disEucL
        sumaGaussiana = sumaGaussiana + disEucG
        sumaCuadratica = sumaCuadratica + disEucC

    #Imprimimos las diferencias
    print("Suma de la ecuación lineal","{:.3f}".format(sumaLineal))
    response += "\nSuma de la ecuación lineal:            {:.3f}\n".format(sumaLineal)
    print("Suma de la ecuación Gaussiana","{:.3f}".format(sumaGaussiana))
    response += "Suma de la ecuación Gaussiana:   {:.3f}\n".format(sumaGaussiana)
    print("Suma de la ecuación cuadratica","{:.3f}".format(sumaCuadratica))
    response += "Suma de la ecuación cuadratica:   {:.3f}\n".format(sumaCuadratica)

    #Elegimos la funciones con menor diferencia
    if sumaLineal<sumaGaussiana and sumaLineal<sumaCuadratica:
        print("La menor distacia es de la ecuación lineal")
        response += "\n La menor distacia es de la ecuación lineal"
    elif sumaGaussiana<sumaLineal and sumaGaussiana<sumaCuadratica:
        print("La menor distancia es de la ecuación Gaussiana")
        response += "\n La menor distancia es de la ecuación Gaussiana"
    else:
        print("La menor distancia es de la ecuación cuadratica")
        response += "\n La menor distancia es de la ecuación cuadratica"

    return response

def graficador():
    x = range(-25, 25)
    # Graficar ambas funciones.
    plt.plot(x, [calcularLineal(i) for i in x])
    plt.plot(x, [calcularGaussiana(i) for i in x])
    plt.plot(x, [calcularCuadratica(i) for i in x])
    for punto in puntos:
        plt.plot(punto[0],punto[1],"o",color="red",)
    # Establecer el color de los ejes.
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    # Limitar los valores de los ejes.
    plt.xlim(-15, 15)
    plt.ylim(-10, 10)
    # Guardar gráfico como imágen PNG.
    plt.savefig("./static/img/grafica.png")
    # Esperamos medio segundo para que se guarde correctamente
    time.sleep(0.5)
    # Mostrarlo.
    # plt.show()
