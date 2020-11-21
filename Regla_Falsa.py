from math import *
import sympy as sp 
import matplotlib as mat

x,y=sp.symbols('x y')
# str_ecuacion = input("Ingrese la ecuacion: \n")
# funcion= sp.sympify(str_ecuacion)

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
        

def Regla_Falsa(a,b,T,I): 
    I+=1
    p=(a*f(b)-b*f(a))/(f(b)-f(a)) #forma de calcular la regla falsa <---- af(b)-bf(a)//f(b)-f(a)
    fp=f(p)
    fa=f(a)
    fb=f(b)
    global Error
    Error=float(fa*fp)
    if(I>=50):
        return ["NO ENCONTRADO",0.00]
    else:
        if(fa*fb<=0):
            if(validar(p,T)==True):
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
                return [p,Error]
            else:
                if((fa*fp)<=0):
                    print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
                    return Regla_Falsa(a,p,T,I)
                else:
                    print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
                    return Regla_Falsa(p,b,T,I)
        else:
            return ["los limites estan mal",0.0]

def Menu(Ecuacion, Liminf,Limsup,Error):
    global funcion
    funcion=sp.sympify(Ecuacion)
    # A=input("Digite el limite inferior:\n")
    A=Liminf
    l= A.replace("pi",str(pi))
    a = float(sp.sympify(l))

    B=Limsup
    ll = B.replace("pi",str(pi))
    b = float(sp.sympify(ll))

    tol=float(Error)
    iteracion=0
    return Regla_Falsa(a,b,tol,iteracion)

    # print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format("I","Xi","Xu","Xr","f(Xu)","f(Xi)","f(Xr)","f(Xi)*f(Xr)"))

    # print("El resultado es: ",Regla_Falsa(a,b,tol,iteracion))