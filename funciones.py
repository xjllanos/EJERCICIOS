#1
#def mostrar_numero(numero:int)->None: 
#    print(f"El numero es {numero}") 

#2 - Crear una función que permita determinar si un número es par o no. La función retorna
# “True” en caso afirmativo y “False” en caso contrario. Probar en el programa principal
# realizando la invocación o llamada.

#def num_par(numero:int) -> bool:
#    if numero % 2 == 0:
#        return True
#    else:
#        return False

#3 - Especializar la función del punto 1 para que valide el número en un rango 
# determinado pasado por parámetro “desde”-“hasta”

def par_valido(numero : int, desde: int, hasta:int):
    if numero < desde or numero > hasta:
        print ("El numero ingresado no esta dentro del rango")
    else:
        if numero % 2 == 0: 
            print(True)
        else:
            print(False)
        