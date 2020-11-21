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
        
    

def CALCULAR():
    str_ecuacion = fLabel1.get()
    funcion1=sp.sympify(str_ecuacion)
    
    global funcion
    
    funcion=funcion1

    a = Ext_Izq1.get()
    aa = a.replace("pi",str(pi))
    A = float(sp.sympify(aa))

    b = Ext_Der1.get()
    bb = b.replace("pi",str(pi))
    B = float(sp.sympify(bb))
    
    N = int(Iteraciones_N1.get())

    m = cota1.get()
    mm = m.replace("pi",str(pi))
    M = float(sp.sympify(mm))

    Resultado1.delete(0,END)
    Resultado1.insert(0,monte_carlo(A,B,N,M))
    

# Menu()

raiz = Tk()

myframe = Frame(raiz,width="650",height="350")
myframe.pack()

#Etiquetas
raiz.title("Metodo MonteCarlo")

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
cota = Label(myframe,text="Cota superior")
cota.grid(row=5,column=0,sticky="e")
Resultado = Label(myframe,text="Area")
Resultado.grid(row=6,column=0,sticky="e")

#Cuadros de texto
fLabel1 = Entry(myframe)
fLabel1.grid(row=1,column=1)
Ext_Izq1 = Entry(myframe)
Ext_Izq1.grid(row=2,column=1)
Ext_Der1 = Entry(myframe)
Ext_Der1.grid(row=3,column=1)
Iteraciones_N1 = Entry(myframe)
Iteraciones_N1.grid(row=4,column=1)
cota1 = Entry(myframe)
cota1.grid(row=5,column=1)
Resultado1 = Entry(myframe)
Resultado1.grid(row=6,column=1)

boton1 = Button(myframe,text="calcular",width="20",height="5",command=CALCULAR)
boton1.grid(row=7,columnspan=2)


raiz.mainloop()