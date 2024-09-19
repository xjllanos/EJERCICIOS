import modulos.funciones as funciones
import modulos.ejercicio_8 as ejercicio_8 
#1
#funciones.mostrar_numero(10)

#2
#print(funciones.num_par(20))

#3
#funciones.par_valido(72,6,100)

#4

#print(funciones.restar1(10,20))
#print(funciones.restar2())
#funciones.restar3(30,10)
#funciones.restar4()

#5 
#numero1 = int(input("Ingrese un numero entre 10 y 100: "))

#while numero1 <= 10 or numero1 >= 100:
#    print (f"El numero,",{numero1}, " no esta dentro del rango")
#    numero1 = int(input("Ingrese un numero entre 10 y 100: "))

#print(f"El descuento fue de:",funciones.realizarDescuento(numero1))

#6 
#numero1 = int(input("Ingrese un numero entre 10 y 100: "))
#while numero1 <= 10 or numero1 >= 100:
#    print (f"El numero,", {numero1}, "no esta dentro del rango")
#    numero1 = int(input("Ingrese un numero entre 10 y 100: "))

#numero2 = int(input("Ingrese un numero entre 10 y 100: "))
#while numero2 <= 10 or numero2 >= 100:
#    print (f"El numero,", {numero2}, "no esta dentro del rango")
#    numero2 = int(input("Ingrese un numero entre 10 y 100: "))

#operacion = input("Ingrese operacion a realizar: R(restar)/S(sumar)")
#while operacion !="R" and operacion !="S":
#    print(f"La operacion no es valida: ",{operacion}) 
#    operacion = input("Ingrese operacion a realizar: R(restar)/S(sumar)")

#funciones.calculo(operacion,numero1,numero2)

#7
valor_exportaciones= float(input("Ingrese valor exportaciones: "))
valor_nacionales= float(input("Ingrese valor nacionales: "))
resultado_exportaciones = funciones.calculo_impuestos_exportaciones(valor_exportaciones)
resultado_nacionales = funciones.calculo_impuestos_nacionales(valor_nacionales)
print(f"Resultado nacionales:",{resultado_nacionales},"- Resultado exportaciones:",{resultado_exportaciones})
print(f"Total:",(resultado_exportaciones+resultado_nacionales))

#8
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
horas_trabajadas = int(input("Ingrese sus horas trabajadas: "))
antiguedad = int(input("Ingrese años trabajando: "))
artefactos = int(input("Ingrese artefactos producidos: "))

ejercicio_8.imprimir_informacion(nombre,edad,horas_trabajadas,antiguedad,artefactos)