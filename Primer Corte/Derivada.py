from math import *

def f(x):
    return 80*exp(-2*x)+20*exp(-0.5*x)

def ecuacion(x):

    h=0.000001 

    uno=float((f(x+h)-f(x))/h)
    dos=float((f(x+h)-2*f(x)+f(x-h))/h**2)

    print("valor primera derivada",uno)
    print("valor segunda derivada",dos)

def Menu():
    opcion=int(input("Digite su numero\n"))

    ecuacion(opcion)


Menu()
# 80*exp(-2*x)+20*exp(-0.5*x)