# def extraccion(N):
#     N=list(N)
#     i=1
#     resultado=""
#     while(i<len(N)):
#         resultado+=N[i]
#         i+=1
#     return resultado
    

# def Cualquier_Base(number_rational,dividendo):
#     resultado=""
#     Numero=[]
#     Numero_Invertido=[]
#     while (number_rational>0):

#         a=int(float(number_rational%dividendo))
#         if a<10:
#             Numero.append(a)
            

            
#         else:
#             if a==10:
#                 Numero.append("A")
                
#             if a==11:
#                 Numero.append('B')
                
#             if a==12:
#                 Numero.append("C")
                
#             if a==13:
#                 Numero.append("D")
                
#             if a==14:
#                 Numero.append("E")
                
#             if a==15:
#                 Numero.append("F")
                
                 
#         number_rational=(number_rational-a)/dividendo
                      
    
#     Numero_Invertido=Numero[::-1]
#     i=0
#     while(i<len(Numero_Invertido)):
#         resultado+=str(Numero_Invertido[i])
#         i+=1
#     return resultado


# def Menu():
#     opcion=int(input("Digite 1: 32 bits\nDigite 2: 64 bits\n"))
#     negativo=0
#     if(opcion==1):
#         numero=input("Digite el numero: ")

#         if(list(numero)[0]=='-'):
#             negativo=1
#             numero=extraccion(numero)
#         print("holi ",negativo,Cualquier_Base(numero,2))


# Menu()