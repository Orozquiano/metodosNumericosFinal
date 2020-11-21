from tkinter import *
from math import pi
import sympy as sp 
import matplotlib as mat
from random import randint, uniform, random

funcion= ""
x,y=sp.symbols('x y')



def f(x): 
    b= funcion.free_symbols
    var=b.pop()
    valor = funcion.evalf(subs={var:x})

    return valor

def monte_carlo(a,b,N,M):
    n = 0

    for i in range(N):
        random2 = uniform(0,1)
        random1 = uniform(0,1)
        x_i = (b-a)*random1 + a
        y_i = M*random2
        if(y_i<=abs(f(x_i))):
            n += 1
    return (n/N)*(b-a)*M
        
    

def CALCULAR(Ecu,a,b,n,cota):
    
    funcion1=sp.sympify(Ecu)
    
    global funcion
    funcion=funcion1

    aa = a.replace("pi",str(pi))
    A = float(sp.sympify(aa))

    bb = b.replace("pi",str(pi))
    B = float(sp.sympify(bb))
    
    N = int(n)

    mm = cota.replace("pi",str(pi))
    M = float(sp.sympify(mm))

    # Resultado1.delete(0,END)
    # Resultado1.insert(0,monte_carlo(A,B,N,M))
    return monte_carlo(A,B,N,M)
    