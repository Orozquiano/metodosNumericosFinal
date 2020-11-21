from math import *
import sympy as sp 
import matplotlib as mat

x,y=sp.symbols('x y')
# str_ecuacion = input("Ingrese la ecuacion: \n")
# funcion= sp.sympify(str_ecuacion)
funcion = ''


def f(x): 
    b= funcion.free_symbols
    var=b.pop()
    valor = funcion.evalf(subs={var:x})

    return valor

def Delta(a,b,n):
    return (b-a)/n

def Metodo_izquierda(a,delta,suma,N):
    for i in range(N):
            altura = f(a)
            Area = delta*altura
            suma += Area
            a = a+delta
    return abs(suma)

def Metodo_Derecha(a,delta,suma,N):
    for i in range(N):
            altura = f(a+delta)
            Area = delta*altura
            suma += Area
            a = a+delta
    return abs(suma)

def Metodo_PuntoMedio(a,delta,suma,N):
    for i in range(N):
            altura = f(a+delta/2)
            Area = delta*altura
            suma += Area
            a = a+delta
    return abs(suma)

def Menu(Ecuacion,A,B,N):
    global funcion
    funcion = sp.sympify(Ecuacion)


    # A=input("Digite el intervalo a:\n")
    l= A.replace("pi",str(pi))
    a = float(sp.sympify(l))

    # B=input("Digite el intervalo b:\n")
    ll = B.replace("pi",str(pi))
    b = float(sp.sympify(ll))
    
    N=int(N) #Numero de iteraciones
    suma=0

    delta=float(Delta(a,b,N))
    return [Metodo_izquierda(a,delta,suma,N),Metodo_Derecha(a,delta,suma,N),Metodo_PuntoMedio(a,delta,suma,N)]
    
    # print("El resultado por la izquierda es: ",Metodo_izquierda(a,delta,suma,N))
    # print("El resultado por la Derecha es: ",Metodo_Derecha(a,delta,suma,N))
    # print("El resultado por punto medio es: ",Metodo_PuntoMedio(a,delta,suma,N))


# Menu()

