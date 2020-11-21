from tkinter import *
from math import *
import sympy as sp 
import matplotlib as mat
from random import randint, uniform, random

raiz = Tk()

myframe = Frame(raiz,width="650",height="350")
myframe.pack()

fLabel1 = Entry(myframe)
fLabel1.grid(row=1,column=1)

str_ecuacion=str(fLabel1.get())

funcion= sp.sympify(str_ecuacion)

def f(x): 
    b= funcion.free_symbols
    var=b.pop()
    valor = funcion.evalf(subs={var:x})

    return valor

def f2(x,derivate): 
    b= derivate.free_symbols
    var=b.pop()
    valor = derivate.evalf(subs={var:x})

    return valor

def simpson1_3(a,b):
    m = (a+b)/2
    integral= (b - a)/6 *(f(a)+4*f(m)+f(b))

    return integral

def ErrorP(H,a,b):
    Nrandom = uniform(a,b)
    Deriavada4 = sp.diff(funcion,x,4)
    RanN=f2(Nrandom,Deriavada4)

    E=abs((-(H**5)/90)*RanN)
    return E

def CALCULAR():
    a=float(Ext_Izq1.get())
    b=float(Ext_Der1.get())
    N=int(Iteraciones_N1.get())
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
    suma1=suma
    ErrorP1=ErrorP(h,a1,b1)
    Error1.insert(0,ErrorP1)
    Resultado1.insert(0,suma1)
    
x,y=sp.symbols('x y')
raiz.title("Metodo simpson 1/3")

#Etiquetas
ingreso = Label(myframe,text="Ingreso")
ingreso.grid(row=0,column=0)
fLabel = Label(myframe,text="f(x)")
fLabel.grid(row=1,column=0,sticky="e")
Ext_Izq = Label(myframe,text="Extremo Izquierdo (a)")
Ext_Izq.grid(row=2,column=0,sticky="e")
Ext_Der = Label(myframe,text="Extremo derecho (b)")
Ext_Der.grid(row=3,column=0,sticky="e")
Iteraciones_N = Label(myframe,text="Iteraciones")
Iteraciones_N.grid(row=4,column=0,sticky="e")
Resultado = Label(myframe,text="Area")
Resultado.grid(row=5,column=0,sticky="e")
Error = Label(myframe,text="Error")
Error.grid(row=6,column=0,sticky="e")

#Cuadros de texto
Ext_Izq1 = Entry(myframe)
Ext_Izq1.grid(row=2,column=1)
Ext_Der1 = Entry(myframe)
Ext_Der1.grid(row=3,column=1)
Iteraciones_N1 = Entry(myframe)
Iteraciones_N1.grid(row=4,column=1)
Resultado1 = Entry(myframe)
Resultado1.grid(row=5,column=1)
Error1 = Entry(myframe)
Error1.grid(row=6,column=1)

boton1 = Button(myframe,text="calcular",width="20",height="5",command=CALCULAR)
boton1.grid(row=7,columnspan=2)

raiz.mainloop()
# :)


    

# def CALCULAR():
#     a=Ext_Izq1.get()
#     b=Ext_Der1.get()
#     N=Iteraciones_N1.get()
#     a1=a
#     b1=b
#     suma=0
#     if(N%2==1):
#         N+=1
#     h = (b - a)/N

#     for i in range(N):
#         b = a + h
#         ar = simpson1_3(a,b) #area
#         suma+=ar
#         a=b
#     suma1=suma
#     ErrorP1=ErrorP(h,a1,b1)
#     Error1.insert(0,ErrorP1)
#     Resultado1.insert(0,suma1)

    # print("El area aproximada es: ",abs(suma))

    # print("El error: ",ErrorP(h,a1,b1))
    


    