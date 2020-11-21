from math import *
from math import pi
import sympy as sp 
import matplotlib as mat
from random import randint, uniform, random
import numpy as np
from scipy import linalg
from Matriz import menu as Matrix

def division(matrizA,matrizB):
    matrizR = np.zeros((matrizA.shape[0],matrizB.shape[1]), dtype = float)

    if(matrizA.shape[1] == matrizB.shape[0]):
        matrizC = np.linalg.inv(matrizB)
        for i in range(matrizA.shape[0]):
            for j in range(matrizC.shape[1]):
                for k in range(matrizC.shape[0]):
                    matrizR[i][j] += matrizA[i][k] * matrizC [k][j]
    else:
        return "imposible dividir"
    return matrizR

def ajustecurva(x,y,grade):
    matriz=np.zeros((grade+1,grade+1), dtype=float)
    for i in range(grade+1):
        for j in range(grade+1):
            if((i==0) & (j==0)):
                matriz[0,0]=len(x)
            else:
                for v in range(len(x)):
                    matriz[i,j]+=float(x[v])**(i+j)
    matriz2=np.zeros((1,grade+1), dtype=float)
    for i in range(grade+1):
        for v in range(len(y)):
            matriz2[0,i]+=float(y[v])*(float(x[v])**i)
    return division(matriz2,matriz)

def menu(datosX, datosY, grado):
    global Resultado
    datosX=np.array(datosX)
    datosY=np.array(datosY)
    Resultado = ajustecurva(datosX,datosY, int(grado))
    return Resultado
# x=[1.6,2,2.4,2.9,3.4,3.7,4.2]
# y=[5,5.8,6.7,7.5,8.3,9.3,10.7]
# menu(x,y,6)
