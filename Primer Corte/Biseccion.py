
from math import *
import sympy as sp 
import matplotlib as mat

x,y=sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuacion: \n")
funcion= sp.sympify(str_ecuacion)




def f(x): 
    b= funcion.free_symbols
    var=b.pop()
    valor = funcion.evalf(subs={var:x})

    return valor


def validar(P,T):
    if(f(P)>0):
        if(f(P)<=T):
            return True
    else:
        if((-1*f(P))<=T):
            return True
        else: 
            return False    
        

def Biseccion(a,b,T,I): 
    I+=1
    p=(a+b)/2 #forma de calcular la regla falsa <----
    fp=f(p)
    fa=f(a)
    fb=f(b)

    if(fa*fb<=0):
        if(validar(p,T)==True):
            
            print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
            return p
        else:
            if((fa*fp)<=0):
                
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
                return Biseccion(a,p,T,I)
            else:
                
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
                return Biseccion(p,b,T,I)
    

    else:
        print("los limites estan mal")

a=float(input("\nDigite el limite inferior: "))
b=float(input("\nDigite el limite superior: "))
tol=float(input("\nDigite la tolerancia: "))
n0=50
iteracion=0


print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format("I","Xi","Xu","Xr","f(Xu)","f(Xi)","f(Xr)","f(Xi)*f(Xr)"))
print("El resultado es: ",Biseccion(a,b,tol,iteracion))


