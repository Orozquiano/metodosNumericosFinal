import numpy as np 
from numpy.polynomial import Polynomial as Pol 
import array as arraysito
def RaizP(vector):

    # max=int(input("Ingrese el grado del polinomio: "))

    # B=arraysito.array('d',(0 for i in range(0,max+1)))
    # i=0

    # for n in B:
    #     B[i]=float(input("ingrese el coeficiente de X%s: " %(i)))
    #     i+=1

    cafe=Pol(vector)
    print(cafe)
    return cafe.roots()
    # y=0
    # for i in cafe.roots():
    #     print("La raiz ",y+1, " es: ",i)
    #     y+=1

def Menu(grade,x):
    x=list(x)
    contador=0
    coeficiente=''
    vector=[]
    # print(len(x))

    while(contador<len(x)):
        if(x[contador]!='/' and x[contador]!=' '):
            coeficiente+=x[contador]
            if(contador==len(x)-1):
                vector.append(float(coeficiente))

        else:
            vector.append(float(coeficiente))
            coeficiente=''
        contador+=1
        # print(contador)
        

    # print(vector)
    return RaizP(vector)


# print(Menu(3,"2/5/3/6"))