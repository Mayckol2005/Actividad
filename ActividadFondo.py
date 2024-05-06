"""""
Integrantes:
Carlos Moil
Mayckol Mardones 

"""""

import random

"""
simbolos para 
´
*
"""
#Asignamos i y j igual 0

i=0;j=0;


print("\n\n\n")
linea="                                    "

#Hacemos uso de condiciones

for i in range(20):
    linea="                                              "
    for j in range(80):
        random1 = random.randint(1,20)
        if random1==1:
            linea=linea+"*"
        elif random1==2:
            linea=linea+"´"
        else:
            linea=linea+" "
        if j==79:

#Mostramos el fondo
            
            print(linea)
print("\n\n\n")
