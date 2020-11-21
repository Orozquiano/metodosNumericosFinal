from flask import Flask, render_template, request
from Raiz_polinomio import Menu as rp
from Calculadora import Menu as CB
from newton_raphson import Menu as NR
from Regla_Falsa import Menu as RF
from Secante import Menu as Sec
from Integracion_Rectangulos import Menu as IR
from Integracion_Trapezio import Menu as IT
from MetodoSimpson1_3 import Menu as IS3
from MetodoSimpson3_8 import Menu as IS8
from MonteCarlo import CALCULAR as IMonteC
from Matriz import menu as matrix
from AjusteCurvas import menu as Ajuste
from math import *
import sympy as sp
import matplotlib as mat
# Metodo de Bisección
# Cálculo de primer y segunda derivada
# Raíz de un Polinomio
# Calculadora
# Newton Raphson
# Secante

app = Flask(__name__)


@app.route('/Grafica.html')
def Grafica():
    return render_template('Grafica.html')


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/About')
def About():
    return render_template('About.html')


@app.route('/Biseccion')
def Biseccion():
    return render_template('Biseccion.html')
@app.route('/calcularBiseccion', methods=['POST'])
def CBisecccion():
    if request.method == 'POST':
        x, y = sp.symbols('x y')
        str_ecuacion = request.form['Ecuacion']
        funcion = sp.sympify(str_ecuacion)

        def f(x):
            b = funcion.free_symbols
            var = b.pop()
            valor = funcion.evalf(subs={var: x})
            return valor

        def validar(P, T):
            if(f(P) > 0):
                if(f(P) <= T):
                    return True
            else:
                if((-1*f(P)) <= T):
                    return True
                else:
                    return False

        def biseccion(a, b, T, I):
            I += 1
            p = (a+b)/2  # forma de calcular la regla falsa <----
            fp = f(p)
            fa = f(a)
            fb = f(b)

            if(fa*fb <= 0):
                global Error
                Error=float(fa*fp)
                if(validar(p, T) == True):
                    print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(
                        I, float(a), float(b), float(p), float(fb), float(fa), float(fp), float(fa*fp)))
                    return p
                else:
                    if((fa*fp)<=0):
                        print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
                        return biseccion(a,p,T,I)
                    else:
                        print('{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}'.format(I, float(a), float(b),float(p),float(fb),float(fa),float(fp),float(fa*fp)))
                        return biseccion(p,b,T,I)
            else:
                print("los limites estan mal")

        a=float(request.form['Limite inferior'])
        b=float( request.form['Limite superior'])
        tol=float( request.form['Tolerancia'])
        n0=50
        iteracion=0


        print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format("I","Xi","Xu","Xr","f(Xu)","f(Xi)","f(Xr)","f(Xi)*f(Xr)"))
        resultado=str(biseccion(a,b,tol,iteracion))

        return render_template('Biseccion.html',resultado=resultado, error=Error)
   
@app.route('/Derivada')
def Derivada():    
    return render_template('Derivada.html')   
@app.route('/calcularDerivada', methods=['POST'])
def CDerivada():
    if request.method=='POST':
        x,y=sp.symbols('x y')
        str_ecuacion = request.form['Ecuacion']
        funcion= sp.sympify(str_ecuacion)
        X=float(request.form['ValorX'])
        Deriavada1 = sp.diff(funcion,x,1)
        Deriavada2 = sp.diff(funcion,x,2)

        def f(x):
            print("Entre a ecuacion")
            b= funcion.free_symbols
            var=b.pop()
            valor = funcion.evalf(subs={var:x})

            return valor

        def ecuacion(x):
            print("Entre a ecuacion")
            h=0.000001 
            uno=float((f(x+h)-f(x))/h)
            dos=float((f(x+h)-2*f(x)+f(x-h))/h**2)
            valor1=uno
            valor2=dos
            print("valor primera derivada",uno)
            print("valor segunda derivada",dos)
            return valor1,valor2

        def Menu():
            opcion=X
            return ecuacion(opcion)

        Menu()
        return render_template('Derivada.html',D1=Menu()[0],D2=Menu()[1],d1=Deriavada1,d2=Deriavada2)

@app.route('/RPolinomio')
def RPolinomio():    
    return render_template('RPolinomio.html')
@app.route('/calcularRPolinomio',methods=['POST'])
def CRPolinomio():
    if request.method=='POST':
        Grado = request.form['Grado']
        X=request.form['valor']

    return render_template('RPolinomio.html',resultado = str(rp(Grado,X)))
 
@app.route('/Calculadora')
def Calculadora():
    return render_template('Calculadora.html')
@app.route('/ConvCalculadora', methods=['POST'])
def ConvCalculadora():
    if request.method=='POST':
        Decimal = request.form['Decimal']
        Binario = request.form['Binario']
        Octal = request.form['Octal']
        Hexadecimal = request.form['Hexadecimal']
        E32 = request.form['E32']
        E64 = request.form['E64']

    Resultado = CB(Decimal,Binario,Octal,Hexadecimal,E32,E64)
    print(Resultado)
    Dec=str(Resultado[0])
    Bin=str(Resultado[1])
    Oct=str(Resultado[2])
    Hex=str(Resultado[3])
    Etd=str(Resultado[4])
    Esc=str(Resultado[5])
    return render_template('Calculadora.html', dec=Dec, bin=Bin, oct=Oct, hex=Hex, e32=Etd, e64=Esc)

@app.route('/Raphson')
def Raphson():
    return render_template('Raphson.html')
@app.route('/NewtonRaphson', methods=['POST'])
def NewtonRaphson():
    if request.method=='POST':
        Ecuacion=request.form['Ecuacion']
        Valor=request.form['ValorX']
        Error=request.form['Error']
        R=NR(Ecuacion,Valor,Error)
    return render_template('Raphson.html',Ecuacion=Ecuacion,Valor=Valor,Error=Error,X=R[0],I=R[1], eror=R[2])

@app.route('/ReglaFalsa')
def ReglaFalsa():
    return render_template('ReglaFalsa.html')
@app.route('/CReglaFalsa', methods=['POST'])
def CReglaFalsa():
    if request.method=='POST':
        Ecuacion=request.form['Ecuacion']
        LI=request.form['Limite inferior']
        LS=request.form['Limite superior']
        Error=request.form['Tolerancia']
        Resultado=RF(Ecuacion,LI,LS,Error)
    return render_template('ReglaFalsa.html',Ecuacion=Ecuacion,LI=LI,LS=LS,Error=Error,Resultado=Resultado[0],eror=Resultado[1])

@app.route('/Secante')
def Secante():
    return render_template('Secante.html')
@app.route('/CSecante', methods=['POST'])
def CSecante():
    if request.method=='POST':
        Ecuacion=request.form['Ecuacion']
        LI=request.form['Limite inferior']
        LS=request.form['Limite superior']
        Error=request.form['Tolerancia']
        Resultado=Sec(Ecuacion,LI,LS,Error)
    return render_template('Secante.html',Ecuacion=Ecuacion,LI=LI,LS=LS,Error=Error,Resultado=Resultado[0], I=Resultado[1],eror=Resultado[2])

@app.route('/IntegracionRectangulos')
def IntegracionRectangulos():
    return render_template('IntegracionRectangulos.html')
@app.route('/CIntegracionRectangulos',methods=['POST'])
def CIntegracionRectangulos():
    if request.method=='POST':
        Ecu=request.form['Ecuacion']
        IA=request.form['IA']
        IB=request.form['IB']
        Iter=request.form['Iteraciones']
    resultado=IR(Ecu,IA,IB,Iter)
    return render_template('IntegracionRectangulos.html',Ecuacion=Ecu,IA=IA,IB=IB,Iteraciones=Iter,Izq=resultado[0],Der=resultado[1],Med=resultado[2])

@app.route('/IntegracionTrapecio')
def IntegracionTrapecio():
    return render_template('IntegracionTrapecio.html')
@app.route('/CIntegracionTrapecio',methods=['POST'])
def CIntegracionTrapecio():
    if request.method=='POST':
        Ecu=request.form['Ecuacion']
        IA=request.form['IA']
        IB=request.form['IB']
        Iter=request.form['Iteraciones']
    resultado=IT(Ecu,IA,IB,Iter)
    return render_template('IntegracionTrapecio.html',Ecuacion=Ecu,IA=IA,IB=IB,Iteraciones=Iter,Area=resultado[0],Error=resultado[1])

@app.route('/IntegracionSimpson1_3')
def IntegracionSimpson1_3():
    return render_template('IntegracionSimpson1_3.html')
@app.route('/CIntegracionSimpson1_3',methods=['POST'])
def CIntegracionSimpson1_3():
    if request.method=='POST':
        Ecu=request.form['Ecuacion']
        IA=request.form['IA']
        IB=request.form['IB']
        Iter=request.form['Iteraciones']
    resultado=IS3(Ecu,IA,IB,Iter)
    return render_template('IntegracionSimpson1_3.html',Ecuacion=Ecu,IA=IA,IB=IB,Iteraciones=Iter,Area=resultado[0],Error=resultado[1])

@app.route('/IntegracionSimpson3_8')
def IntegracionSimpson3_8():
    return render_template('IntegracionSimpson3_8.html')
@app.route('/CIntegracionSimpson3_8',methods=['POST'])
def CIntegracionSimpson3_8():
    if request.method=='POST':
        Ecu=request.form['Ecuacion']
        IA=request.form['IA']
        IB=request.form['IB']
        Iter=request.form['Iteraciones']
    resultado=IS8(Ecu,IA,IB,Iter)
    return render_template('IntegracionSimpson3_8.html',Ecuacion=Ecu,IA=IA,IB=IB,Iteraciones=Iter,Area=resultado[0],Error=resultado[1])

@app.route('/MonteCarlo')
def MonteCarlo():
    return render_template('MonteCarlo.html')
@app.route('/CMonteCarlo',methods=['POST'])
def CMonteCarlo():
    if request.method=='POST':
        Ecu=request.form['Ecuacion']
        IA=request.form['IA']
        IB=request.form['IB']
        Iter=request.form['Iteraciones']
        cota=request.form['Cota']
    resultado=IMonteC(Ecu,IA,IB,Iter,cota)
    return render_template('MonteCarlo.html',Ecuacion=Ecu,IA=IA,IB=IB,Iteraciones=Iter,CotaS=cota,Area=resultado)

@app.route('/Matriz')
def Matriz():
    return render_template('Matriz.html', Result="not operated")
@app.route('/CMatriz',methods = ['POST'])
def CMatriz():
    if request.method == 'POST':
        MA=request.form['vectorA']
        MB=request.form['vectorB']
        op=int(request.form['operacion'])
        Resultado = matrix(MA,MB,op)
        if(op==8):
            Resultado[0]="valor de las variables a0, a1, a2, ..., an \n"+str(Resultado[0])

        return render_template('Matriz.html',Result=Resultado[0], MA=Resultado[1], MB=Resultado[2])

@app.route('/AjusteCurvas')
def AjusteCurvas():
    return render_template('AjusteCurvas.html')
@app.route('/CAjusteCurvas', methods= ['POST'])
def CAjusteCurvas():
    if request.method == 'POST':
        X=request.form['datosX']
        Y=request.form['datosY']
        G=request.form['grado']
        X=X.replace("[","")
        X=X.replace("]","")
        X=X.split(",")
        Y=Y.replace("[","")
        Y=Y.replace("]","")
        Y=Y.split(",")
        resultado=Ajuste(X,Y,G)
        return render_template('AjusteCurvas.html', Result=resultado)

if __name__ == '__main__':
    app.run(debug=True)


