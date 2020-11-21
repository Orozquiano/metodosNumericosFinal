from math import *
from math import pi
import sympy as sp 
import matplotlib as mat
from random import randint, uniform, random

x,y=sp.symbols('x y')
# str_ecuacion = input("Ingrese la ecuacion: \n")
funcion= ''


def f(x): 
    b= funcion.free_symbols
    
    var=b.pop()
    valor = funcion.evalf(subs={var:x})

    # print(valor)

    return valor

def f2(x,derivate):
    # print("estamos en la derivada") 
    b= derivate.free_symbols
    if(b==set()):    
        valor=0
    else:
        var=b.pop()
        valor = derivate.evalf(subs={var:x})

    return valor

def simpson1_3(a,b):
    m = (a+b)/2
    integral= (b - a)/6 *(f(a)+4*f(m)+f(b))
    return integral

def ErrorP(H,a,b):
    # print("estamos en el error")
    Nrandom = uniform(a,b)
    Deriavada4 = sp.diff(funcion,x,4)
    RanN=f2(Nrandom,Deriavada4)

    E=abs((-(H**5)/90)*RanN)
    return E
    

def Menu(Ecu,A,B,N):

    global funcion
    funcion = sp.sympify(Ecu)

    l=A.replace("pi",str(pi))
    a=float(sp.sympify(l))

    ll=B.replace("pi",str(pi))
    b=float(sp.sympify(ll))

    N=int(N)
    a1=a
    b1=b
    suma=0
    if(N%2==1):
        N+=1
    h = (b - a)/N

    for i in range(N):
        b = a + h
        ar = simpson1_3(a,b) #area
        suma+=ar
        a=b

    # print("El area aproximada es: ",abs(suma))
    # print(suma)
    # print("El error: ",ErrorP(h,a1,b1))
    err=ErrorP(h,a1,b1)

    return [str(abs(suma)), str(err)]

# Menu()
    

    
