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

#def par_valido(numero : int, desde: int, hasta:int):
#    if numero < desde or numero > hasta:
#        print ("El numero ingresado no esta dentro del rango")
#    else:
#        if numero % 2 == 0: 
#            print(True)
#        else:
#            print(False)
# 

# 4 - Realizar un programa en donde se puedan utilizar los prototipos de la función 
# Restar en sus 4 combinaciones.
# restar1(int, int)->int:
# restar2()->int:
# restar3(int, int):
# restar4():

#def restar1(num_1:int,num_2:int)-> int:
#    return num_1-num_2
#def restar2()-> int:
#    return 20-5
#def restar3(num_1:int,num_2:int):
#    print(num_1-num_2)
#def restar4():
#    print(20-5)

# 5 - Realizar un programa que: asigne a la variable numero1 un valor solicitado 
# al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a dicho 
# valor a través de una función llamada realizarDescuento(). Mostrar el resultado 
# por pantalla. Atención: pueden reutilizarse funciones ya creadas.

#def realizarDescuento(num:int):
#    return num - (num * 5/100)

# 6 - Realizar un programa que: asigne a las variables numero1 y numero2 los valores 
# solicitados al usuario, valide los mismos entre 10 y 100, asigne a la variable 
# operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice 
# la operación de dichos valores a través de una función. Mostrar el resultado 
# por pantalla.

#def calculo(operacion:str,num1:int,num2:int) -> None:
#    match operacion:
#        case "S":
#            print("La suma es de: ",(num1+num2))
#        case "R":
#            print("La resta es de: ",(num1-num2))

# 7 - Supongamos que le solicito a chatgpt una función para calcular valores de 
# ventas de productos con impuestos para una determinada empresa:
# La respuesta de chatgpt es:

#def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
#    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
#    resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
#    resultado_final = resultado_nacional + resultado_exportaciones
#    return resultado_final

#def calculo_impuestos_exportaciones(valor_exportaciones,retenciones=15):
#    resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100)) 
#    return resultado_exportaciones 

#def calculo_impuestos_nacionales(valor_ventas_naciones,iva=21):
#    resultado_nacionales = valor_ventas_naciones* (1 / (1 + (iva / 100)))
#    return resultado_nacionales 
#¿Considera que cumple con los objetivos de una función?
#Corrija la función dentro de un módulo, divida en distintas funciones 
# de ser necesario, documente y denomine correctamente.