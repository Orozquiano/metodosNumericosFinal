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

def Derivada(x):

    h=0.0001 

    uno=float((f(x+h)-f(x))/h)
    #dos=float((f(x+h)-2*f(x)+f(x-h))/h**2)

    return uno
    # print("valor segunda derivada",dos)

def newton_raphson(x,E,I):
    I+=1
    MT=float(Derivada(x))#penidente de la recta tangente de la funcion 
    Xr=x-(f(x)/MT) #Intercepto en el eje X
    global Error
    Error = float(f(Xr))
    V=[Xr,I,Error]
    if(I>50):
        return ["NO ENCONTRADO",I]
    else:
        if(f(Xr)>=0):
            if(f(Xr)<=E):
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(x),float(f(x)),MT,float(Xr),float(f(Xr))))
                return V
            else:
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(x),float(f(x)),MT,float(Xr),float(f(Xr))))
                return newton_raphson(Xr,E,I)
        else:
            if(-f(Xr)<=E):
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(x),float(f(x)),MT,float(Xr),float(f(Xr))))
                return V
            else:
                print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(x),float(f(x)),MT,float(Xr),float(f(Xr))))
                return newton_raphson(Xr,E,I) 




def Menu(f,valor,e):
    global funcion
    x,y=sp.symbols('x y')
    funcion=sp.sympify(f)
    Opcion=valor
    ll = Opcion.replace("pi",str(pi))
    opcion = float (sp.sympify(ll))
    
    Er=float(e)
    iteraciones=0
    # print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format("I","X1","f(Xi)","f'(Xi)","X2","Error"))

    Z=newton_raphson(opcion,Er,iteraciones)
    # z=Z[0]
    # y=Z[1]
    
    # print("La intercepcion en el eje X es: ",z,"a las ",y," iteraciones")
    return Z



     
    


# Menu()