from math import *
import sympy as sp 
import matplotlib as mat

x,y=sp.symbols('x y')
funcion=''


def f(x): 
    b= funcion.free_symbols
    var=b.pop()
    return funcion.evalf(subs={var:x})


def Secante(a,b,E,I):
    I+=1
    if(f(b)-f(a)==0):
        return ["Los valores estan mal",I,0.00]
    Xr=(a*f(b)-b*f(a))/(f(b)-f(a)) #Intercepto en el eje X
    Error=float(f(Xr))
    V=[Xr,I,Error] 
    if I==50:
        return ["NO ENCONTRADO",I,0.00]
    else:
        if(f(Xr)>=0):
            if(f(Xr)<=E):
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(f(a)),float(f(b)),float(Xr),float(f(Xr))))
                return V
            else:
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(f(a)),float(f(b)),float(Xr),float(f(Xr))))
                return Secante(a,Xr,E,I)
        else:
            if(-f(Xr)<=E):
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(f(a)),float(f(b)),float(Xr),float(f(Xr))))
                return V
            else:
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(f(a)),float(f(b)),float(Xr),float(f(Xr))))
                return Secante(a,Xr,E,I)
    

def Menu(Ecuacion,Xi,Xf,Error):
    global funcion
    funcion= sp.sympify(Ecuacion)

    A=Xi
    l= A.replace("pi",str(pi))
    x1 = float(sp.sympify(l))

    B=Xf
    ll = B.replace("pi",str(pi))
    x0 = float(sp.sympify(ll))

    Er=float(Error)
    # print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format("I","X0","X1","f(Xi)","f(Xi-1)","X2","Error"))
    Z=Secante(x1,x0,Er,0)
    # z=Z[0]
    # y=Z[1]
    
    return Z

# Menu()