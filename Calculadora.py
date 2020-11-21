#22/08/2020 9:00 pm
#Validaciones, fraccionarios, mejorado xd
def Cualquier_Base(number_rational,dividendo):
    resultado=""
    Numero=[]
    Numero_Invertido=[]
    while (number_rational>0):

        a=int(float(number_rational%dividendo))
        if a<10:
            Numero.append(a)
            

            
        else:
            if a==10:
                Numero.append("A")
                
            if a==11:
                Numero.append('B')
                
            if a==12:
                Numero.append("C")
                
            if a==13:
                Numero.append("D")
                
            if a==14:
                Numero.append("E")
                
            if a==15:
                Numero.append("F")
                
                 
        number_rational=(number_rational-a)/dividendo
                      
    
    Numero_Invertido=Numero[::-1]
    i=0
    while(i<len(Numero_Invertido)):
        resultado+=str(Numero_Invertido[i])
        i+=1
    return resultado

def Binario_Decimal(N):
    N=N[::-1]
    x=0
    acomulado=0

    while(x<len(N)):
        if(N[x]=='1'):
            acomulado+=2**x
        x+=1

    return acomulado



def Hexa_Decimal(N,B):
    N=N[::-1]
    x=0
    acomulado=0
    while(x<len(N)):
        
        if(N[x]=='1'):
            acomulado+=(B**x)
        if(N[x]=='2'):
            acomulado+=2*(B**x)
        if(N[x]=='3'):
            acomulado+=3*(B**x)
        if(N[x]=='4'):
            acomulado+=4*(B**x)
        if(N[x]=='5'):
            acomulado+=5*(B**x)
        if(N[x]=='6'):
            acomulado+=6*(B**x)
        if(N[x]=='7'):
            acomulado+=7*(B**x)
        if(N[x]=='8'):
            acomulado+=8*(B**x)
        if(N[x]=='9'):
            acomulado+=9*(B**x)
        if(N[x]=='A'):
            acomulado+=10*(B**x)
        if(N[x]=='B'):
            acomulado+=11*(B**x)
        if(N[x]=='C'):
            acomulado+=12*(B**x)
        if(N[x]=='D'):
            acomulado+=13*(B**x)
        if(N[x]=='E'):
            acomulado+=14*(B**x)
        if(N[x]=='F'):
            acomulado+=15*(B**x)
        
        x+=1

    return acomulado



def Es_Decimal(N):
    N=list(N)
    i=0
    while(i<len(N)):
        if(N[i]=='.' or N[i]==','):
            return True
        i+=1
    return False
    

def separacion_Decimal(N):
    N=list(N)
    i=0
    Partes=['','0.']
    
    Entera=True
    while(i<len(N)):
        if(N[i]=="." or N[i]==","):
            Entera=False
        else:
            if(Entera):
                Partes[0]+=N[i]
            else:
                Partes[1]+=N[i]
        i+=1
    return Partes


def Decimal_Base(N,B):
    resultado=""
    binario=[]
    i=0
    if(B<10):
        while(N!=0 and i<10):
            N=N*B
            binario.append(int(N))
            N=N-binario[i]
            resultado+=str(binario[i])
            i+=1
    else:
        while(N!=0 and i<10):
            N=N*B
            if(int(N)<10):
                binario.append(int(N))
                N=N-int(N)
                resultado+=str(binario[i])
            if(int(N)==10):
                binario.append("A")
                N=N-int(N)
                resultado+=str(binario[i])

            if(int(N)==11):
                binario.append("B")
                N=N-int(N)
                resultado+=str(binario[i])

            if(int(N)==12):
                binario.append("C")
                N=N-int(N)
                resultado+=str(binario[i])

            if(int(N)==13):
                binario.append("D")
                N=N-int(N)
                resultado+=str(binario[i])

            if(int(N)==14):
                binario.append("E")
                N=N-int(N)
                resultado+=str(binario[i])

            if(int(N)==15):
                binario.append("F")
                N=N-int(N)
                resultado+=str(binario[i])
            i+=1

    return resultado

def base_decimal(N,B):
    i=2
    N=list(N)
    resultado=0.0

    while(i<len(N)):
        a=0
        #resultado+=N[i]*(B**(-(i)+1))
        if(N[i]=="A"):
            a=10
        if(N[i]=="B"):
            a=11
        if(N[i]=="C"):
            a=12
        if(N[i]=="D"):
            a=13
        if(N[i]=="E"):
            a=14
        if(N[i]=="F"):
            a=15
        if(a>=10):
            resultado+=a*(B**(-(i)+1))
        else:
            resultado+=int(N[i])*(B**(-(i)+1))
        i+=1
    return resultado
     
def valido(N,B): 
    i=0
    N=list(N)
    if(B==2):
        while(i<len(N)):
            if(N[i]!='1' and N[i]!='0' and N[i]!='.' and N[i]!=','and N[i]!='-'):
                return False
            i+=1
        return True
    if(B==8):
        while(i<len(N)):
            if(N[i]!='1' and N[i]!='0' and N[i]!='.' and N[i]!=','and N[i]!='2' and N[i]!='3' and N[i]!='4' and N[i]!='5' and N[i]!='6' and N[i]!='7'and N[i]!='-'):
                return False
            i+=1
        return True
    if(B==10):
        while(i<len(N)):
            if(N[i]!='1' and N[i]!='0' and N[i]!='.' and N[i]!=','and N[i]!='2' and N[i]!='3' and N[i]!='4' and N[i]!='5' and N[i]!='6' and N[i]!='7' and N[i]!='8' and N[i]!='9'and N[i]!='-'):
                return False
            i+=1  
        return True
    if(B==16):
        while(i<len(N)):
            if(N[i]!='1' and N[i]!='0' and N[i]!='.' and N[i]!=','and N[i]!='2' and N[i]!='3' and N[i]!='4' and N[i]!='5' and N[i]!='6' and N[i]!='7' and N[i]!='8' and N[i]!='9' and N[i]!='A'and N[i]!='B' and N[i]!='C' and N[i]!='D' and N[i]!='E' and N[i]!='F'and N[i]!='-'):
                return False
            i+=1
        return True
    
  

        
def extraccion(N):
    N=list(N)
    i=1
    resultado=""
    while(i<len(N)):
        resultado+=N[i]
        i+=1
    return resultado


def Ncomas(N):
    i=0
    N=list(N)
    resultado=0
    fin=False
    while(i<len(N)):
        if(N[i]!=',' and N[i]!='.'and fin==False):
           resultado+=1
        else:
            fin=True
        i+=1
        
    return resultado


def Exponente(N,Bit):
   exp=Ncomas(N)+((2**(Bit-1))-1)

   exp=Cualquier_Base(exp,2)

   return exp

def Completar_Mantisa(N,E):
    N=list(N)
    i=0
    resultado=""
    
    while(i<E):
        if(i<len(N)):
            if(N[i]!=','and N[i]!='.'):            
                resultado+=N[i]
        else:
            resultado+="0"
        i+=1
    return resultado

def extraccion_Exponente(N,Bits):
    N=list(N)
    i=0
    resultado=""
    while(i<Bits):
        resultado+=N[i]
        i+=1
    return resultado

def Es_negativo(N):
    N=list(N)
    if(N[0]=='1'):
        return True
    else:
        return False


def Punto_Metido(N,R):
    N=list(N)
    i=0
    resultado=['','']
    while(i<len(N)):
        if(len(resultado[0])<R):
            resultado[0]+=N[i]
        else:
            resultado[1]+=N[i]
        i+=1
    return resultado


def Quitar_Sobrante(n):
    i=0
    J=0
    F=''
    n=list(n)
    sobrantes=0
    while(i<len(n)):
        if(n[i]==0):
            sobrantes+=1
        else:
            sobrantes=0
        i+=1
    if(sobrantes>0):
        n=n[::-1]
        while(sobrantes>0):
            n=extraccion(n)
            sobrantes-=1
        n=n[::-1]
    while(J<len(n)):
        F+=n[J]
        J+=1
    return F



def Menu(NumDec,NumBin,NumOct,NumHex,Es32,Es64):
    opcion=0
    NumDecString=''
    NumBinString=''
    NumOctString=''
    NumHexString=''
    NumE32String=''
    NumE64String=''
    if(NumDec=="borrar"):
        return ['','','','','','']
    if(NumDec!=''):
        opcion=1
    else:
        if(NumBin!=''):
            opcion=2
        else:
            if(NumOct!=''):
                opcion=3
            else:
                if(NumHex!=''):
                    opcion=4
                else:
                    if(Es32!=''):
                        opcion=5
                    else:
                        if(Es64!=''):
                            opcion=6
                        else:
                            opcion=0
    if(opcion==1):
        numero_fraccionario=NumDec
        negativo=''
        if(list(numero_fraccionario)[0]=='-'):
            negativo='-'
            numero_fraccionario=extraccion(numero_fraccionario)
        if(valido(numero_fraccionario,10)==True):
            if(Es_Decimal(numero_fraccionario)==True):
                Entero=int(separacion_Decimal(numero_fraccionario)[0])
                Decimal=float(separacion_Decimal(numero_fraccionario)[1])
                # print("Binario: ",negativo,Cualquier_Base(Entero,2),".",Decimal_Base(Decimal,2))
                NumBinString+=negativo+Cualquier_Base(Entero,2)+"."+Decimal_Base(Decimal,2)

                # print("Octal: ",negativo,Cualquier_Base(Entero,8),".",Decimal_Base(Decimal,8))
                NumOctString+=negativo+Cualquier_Base(Entero,8)+'.'+Decimal_Base(Decimal,8)

                # print("Hexadecimal: ",negativo,Cualquier_Base(Entero,16),".",Decimal_Base(Decimal,16))
                NumHexString+=negativo+Cualquier_Base(Entero,16)+'.'+Decimal_Base(Decimal,16)
                    
            else:
                NumBinString+=negativo+Cualquier_Base(int(numero_fraccionario),2)

                # print("Octal: ",negativo,Cualquier_Base(int(numero_fraccionario),8))
                NumOctString+=negativo+Cualquier_Base(int(numero_fraccionario),8)

                # print("Hexadecimal: ",negativo,Cualquier_Base(int(numero_fraccionario),16))
                NumHexString+=negativo+Cualquier_Base(int(numero_fraccionario),16)

            #decimal a estandares ieee
            number_binari=NumDec
            Signo=0
            
            if(list(number_binari)[0]=='-'):
                # print("es negativo")
                Signo=1
                number_binari=extraccion(number_binari)
            if(valido(number_binari,10)==True):
                if(Es_Decimal(number_binari)==True):
                    Entero=int(separacion_Decimal(number_binari)[0])
                    Decimal=float(separacion_Decimal(number_binari)[1])
                    Entero=Cualquier_Base(Entero,2)
                    Decimal=Decimal_Base(Decimal,2)
                    Mantisa=Entero+"."+Decimal
                    # print("Binario: ",signo_1,Mantisa)
                    Mantisa=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,8),8))+" "+str(Completar_Mantisa(Mantisa,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,11),11))+" "+str(Completar_Mantisa(Mantisa,52))
                    
                else:
                    Mantisa=Cualquier_Base(int(number_binari),2)
                    number_binari=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,8),8))+" "+str(Completar_Mantisa(number_binari,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,11),11))+" "+str(Completar_Mantisa(number_binari,52))

            resultado=[NumDec,NumBinString,NumOctString, NumHexString,NumE32String,NumE64String]
            return resultado
        else:
            return ["El número digitado no es valido base 10",'','','','','']
    if(opcion==2):
        number_binari=NumBin
        negativo=''
        if(list(number_binari)[0]=='-'):
            negativo='-'
            number_binari=extraccion(number_binari)
        if(valido(number_binari,2)==True):
            if(Es_Decimal(number_binari)==True):
                Entero=str(separacion_Decimal(number_binari)[0])
                Decimal=str(separacion_Decimal(number_binari)[1])
                #Pasa de ser binarios a ser decimal
                Entero=int(Binario_Decimal(list(Entero)))
                Decimal=float(base_decimal(Decimal,2))
                NumDecString+=negativo+str(float(Entero+Decimal))
                NumOctString+=negativo+Cualquier_Base(Entero,8)+"."+Decimal_Base(Decimal,8)
                NumHexString+=negativo+Cualquier_Base(Entero,16)+"."+Decimal_Base(Decimal,16)
            else:
                number_rational_1=Binario_Decimal(list(number_binari))
                NumDecString+=negativo+str(number_rational_1) #Decimal
                NumOctString+=negativo+Cualquier_Base(number_rational_1,8)
                NumHexString+=negativo+Cualquier_Base(number_rational_1,16)

            #decimal a estandares ieee
            number_binari=NumDecString
            Signo=0
            
            if(list(number_binari)[0]=='-'):
                # print("es negativo")
                Signo=1
                number_binari=extraccion(number_binari)
            if(valido(number_binari,10)==True):
                if(Es_Decimal(number_binari)==True):
                    Entero=int(separacion_Decimal(number_binari)[0])
                    Decimal=float(separacion_Decimal(number_binari)[1])
                    Entero=Cualquier_Base(Entero,2)
                    Decimal=Decimal_Base(Decimal,2)
                    Mantisa=Entero+"."+Decimal
                    # print("Binario: ",signo_1,Mantisa)
                    Mantisa=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,8),8))+" "+str(Completar_Mantisa(Mantisa,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,11),11))+" "+str(Completar_Mantisa(Mantisa,52))
                    
                else:
                    Mantisa=Cualquier_Base(int(number_binari),2)
                    number_binari=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,8),8))+" "+str(Completar_Mantisa(number_binari,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,11),11))+" "+str(Completar_Mantisa(number_binari,52))

            resultado=[NumDecString,NumBin,NumOctString, NumHexString,NumE32String,NumE64String]
            return resultado

        else:
            return ['',"El numero digitado no es valido base 2",'','','No aplica','No aplica']
    if(opcion==3):
        number_binari=NumOct
        negativo=''
        if(list(number_binari)[0]=='-'):
            negativo='-'
            number_binari=extraccion(number_binari)
        if(valido(number_binari,8)==True):
            if(Es_Decimal(number_binari)==True):
                Entero=str(separacion_Decimal(number_binari)[0])
                Decimal=str(separacion_Decimal(number_binari)[1])
                #Pasa de ser binarios a ser decimal
                Entero=int(Hexa_Decimal(list(Entero),8))
                Decimal=float(base_decimal(Decimal,8))

                NumDecString+=negativo+str(float(Entero+Decimal))
                NumBinString+=negativo+str(Cualquier_Base(Entero,2))+"."+str(Decimal_Base(Decimal,2))
                NumHexString+=negativo+str(Cualquier_Base(Entero,16))+"."+str(Decimal_Base(Decimal,16))
            else:
                number_rational_1=Hexa_Decimal(list(number_binari),8)
                NumDecString+=negativo+str(number_rational_1)
                NumBinString+=negativo+str(Cualquier_Base(number_rational_1,2))
                NumHexString+=negativo+str(Cualquier_Base(number_rational_1,16))
            #decimal a estandares ieee
            number_binari=NumDecString
            Signo=0
            
            if(list(number_binari)[0]=='-'):
                # print("es negativo")
                Signo=1
                number_binari=extraccion(number_binari)
            if(valido(number_binari,10)==True):
                if(Es_Decimal(number_binari)==True):
                    Entero=int(separacion_Decimal(number_binari)[0])
                    Decimal=float(separacion_Decimal(number_binari)[1])
                    Entero=Cualquier_Base(Entero,2)
                    Decimal=Decimal_Base(Decimal,2)
                    Mantisa=Entero+"."+Decimal
                    # print("Binario: ",signo_1,Mantisa)
                    Mantisa=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,8),8))+" "+str(Completar_Mantisa(Mantisa,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,11),11))+" "+str(Completar_Mantisa(Mantisa,52))
                    
                else:
                    Mantisa=Cualquier_Base(int(number_binari),2)
                    number_binari=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,8),8))+" "+str(Completar_Mantisa(number_binari,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,11),11))+" "+str(Completar_Mantisa(number_binari,52))

            resultado=[NumDecString,NumBinString,NumOct, NumHexString,NumE32String,NumE64String]
            return resultado
        else:
            return ['','',"El numero digitado no es valido base 8",'',"No aplica", "No aplica"]
            # Menu()
    
    if(opcion==4):
        number_binari=NumHex.upper()
        negativo=''
        if(list(number_binari)[0]=='-'):
            negativo='-'
            number_binari=extraccion(number_binari)
        if(valido(number_binari,16)==True):
            if(Es_Decimal(number_binari)==True):
                Entero=str(separacion_Decimal(number_binari)[0])
                Decimal=str(separacion_Decimal(number_binari)[1])
                #Pasa de ser binarios a ser decimal
                Entero=int(Hexa_Decimal(list(Entero),16))
                Decimal=float(base_decimal(Decimal,16))
                NumDecString+=negativo+str(float(Entero+Decimal))
                NumBinString+=negativo+Cualquier_Base(Entero,2)+"."+Decimal_Base(Decimal,2)
                NumOctString+=negativo+Cualquier_Base(Entero,8)+"."+Decimal_Base(Decimal,8)
            else:
                number_rational_1=Hexa_Decimal(list(number_binari),16)
                NumDecString+=negativo+str(number_rational_1)
                NumBinString+=negativo+Cualquier_Base(number_rational_1,2)
                NumOctString+=negativo+Cualquier_Base(number_rational_1,8)
            #decimal a estandares ieee
            number_binari=NumDecString
            Signo=0
            
            if(list(number_binari)[0]=='-'):
                # print("es negativo")
                Signo=1
                number_binari=extraccion(number_binari)
            if(valido(number_binari,10)==True):
                if(Es_Decimal(number_binari)==True):
                    Entero=int(separacion_Decimal(number_binari)[0])
                    Decimal=float(separacion_Decimal(number_binari)[1])
                    Entero=Cualquier_Base(Entero,2)
                    Decimal=Decimal_Base(Decimal,2)
                    Mantisa=Entero+"."+Decimal
                    # print("Binario: ",signo_1,Mantisa)
                    Mantisa=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,8),8))+" "+str(Completar_Mantisa(Mantisa,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(Mantisa,11),11))+" "+str(Completar_Mantisa(Mantisa,52))
                    
                else:
                    Mantisa=Cualquier_Base(int(number_binari),2)
                    number_binari=extraccion(Mantisa)
                    NumE32String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,8),8))+" "+str(Completar_Mantisa(number_binari,23))
                    NumE64String+=str(Signo)+" "+str(Completar_Mantisa(Exponente(number_binari,11),11))+" "+str(Completar_Mantisa(number_binari,52))

            resultado=[NumDecString,NumBinString,NumOctString, NumHex,NumE32String,NumE64String]
            return resultado

        else:
            return ['','','',"El numero digitado no es valido base 16","No aplica", "No aplica"]
    
    if(opcion==5):
        EstandarIEEE=Es32
        signo=''
        i=0
        if(Es_negativo(EstandarIEEE)==True):
            signo='-'
        EstandarIEEE_1=extraccion(EstandarIEEE)
        exponente=Binario_Decimal(extraccion_Exponente(EstandarIEEE_1,8))
        Recorrido=exponente-127
        Mantisa=EstandarIEEE_1
        while(i<8):
            Mantisa=extraccion(Mantisa)
            i+=1
        while(len(Mantisa)<23):
            Mantisa+='0'
        Entero=str('1'+Punto_Metido(Mantisa,Recorrido)[0])
        Decimal=str('0.'+Punto_Metido(Mantisa,Recorrido)[1])
        Decimal=Quitar_Sobrante(str(Decimal))
        binario=float(Entero)+float(Decimal)
        Entero_Decimal=int(Binario_Decimal(Entero))
        Decimal_D=float(base_decimal(Decimal,2))
        NDecimal=float(Entero_Decimal+Decimal_D)
        NumBinString+=signo+str(binario)
        NumDecString+=signo+str(NDecimal)
        return Menu(NumDecString,'','','','','')
                
    if(opcion==6):
        EstandarIEEE=Es64
        signo=''
        i=0
        if(Es_negativo(EstandarIEEE)==True):
            signo='-'
        EstandarIEEE_1=extraccion(EstandarIEEE)
        exponente=Binario_Decimal(extraccion_Exponente(EstandarIEEE_1,11))
        Recorrido=exponente-1023
        Mantisa=EstandarIEEE_1
        while(i<11):
            Mantisa=extraccion(Mantisa)
            i+=1
        while(len(Mantisa)<51):
            Mantisa+='0'
        Entero='1'+Punto_Metido(Mantisa,Recorrido)[0]
        Decimal=float('0.'+Punto_Metido(Mantisa,Recorrido)[1])
        Decimal=Quitar_Sobrante(str(Decimal))
        binario=float(Entero)+float(Decimal)
        Entero_Decimal=int(Binario_Decimal(Entero))
        Decimal_D=float(base_decimal(Decimal,2))
        NDecimal=float(Entero_Decimal+Decimal_D)
        NumBinString+=signo+str(binario)
        NumDecString+=signo+str(NDecimal)
        # return [NumDecString,NumBinString,'','','',Es64]
        return Menu(NumDecString,'','','','','')

    
#main
# print(Menu('10.4','','','','',''))



#los dos estandares de una vez xd y el binario mostrarlo tambien












    




