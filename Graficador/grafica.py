from math import *
import sympy as sp 
import matplotlib as mat

x,y=sp.symbols('x y')

ecuacion=input("Ingrese la ecuacion: \n")

funcion = sp.sympify(ecuacion)
sp.plot(funcion, (x,-10,10), title=None, aspect_ratio='auto')


# 2x4 – 3.5 x3 + 10.56 x2 – 15.95 x + 11.35