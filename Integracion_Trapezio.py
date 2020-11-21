from math import *
import sympy as sp 
import matplotlib as mat

x,y=sp.symbols('x y')
# str_ecuacion = input("Ingrese la ecuacion: \n")
funcion= ''

def f(x): 
    b= funcion.free_symbols
    var=b.pop()
    valor = funcion.evalf(subs={var:x})

    return valor

def Delta(a,b,n):
    return (b-a)/n

def Menu(Ecu,A,B,N):
    global funcion
    funcion = sp.sympify(Ecu)
    # A=input("Digite el intervalos a:\n")
    l= A.replace("pi",str(pi))
    a = float(sp.sympify(l))

    # B=input("Digite el intervalos b:\n")
    ll = B.replace("pi",str(pi))
    b = float(sp.sympify(ll))
    
    N=int(N)
    suma=0

    delta=float(Delta(a,b,N))

    for i in range(N):
        Area=(f(a)+f(a+delta))*delta/2
        suma+=Area
        a+=delta
    # print("El área es aproximadamente", suma)
    Vt= 9*pi/2
    # print("El error porcentual es de",abs(Vt-suma)/Vt*100,"%")
    err=str(abs(Vt-suma)/Vt*100)+'%'
    return [suma, err]

# Menu()