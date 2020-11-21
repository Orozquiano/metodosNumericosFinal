from math import *
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

    return valor

def f2(x,derivate): 
    b= derivate.free_symbols
    if(b==set()):    
        valor=0
    else:
        var=b.pop()
        valor = derivate.evalf(subs={var:x})

    return valor

def simpson3_8(a,b):
    m1 = (2*a+b)/3
    m2 = (a+2*b)/3
    integral= (b - a)/8 *(f(a)+3*f(m1)+3*f(m2)+f(b))

    return integral

def ErrorP(H,a,b):
    Nrandom = uniform(a,b)
    Deriavada4 = sp.diff(funcion,x,4)
    RanN=f2(Nrandom,Deriavada4)

    E=abs((-((H**5)*3)/80)*RanN)
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
    if(N%3==1):
        N+=2
    elif(N%3==2):
        N+=1

    h = (b - a)/N

    for i in range(N):
        b = a + h
        ar = simpson3_8(a,b) #area
        suma+=ar
        a=b
        # print(i,"\n")
    err=ErrorP(h,a1,b1)
    
    return [str(abs(suma)),str(err)]

# Menu()
    