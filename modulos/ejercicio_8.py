# 8 - Genere un segundo módulo en el cual existan las funciones necesarias para la 
# gestión del equipo de recursos humanos de la empresa. En el mismo debe existir 
# una primera función que calcule el valor del salario de cada empleado. El valor del 
# mismo es la cantidad de horas trabajadas multiplicadas por 10 y un incremento del 
# 3% por cada año de antigüedad.
# También debe haber una segunda función que calcule la productividad del empleado. La
# misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad 
# de horas de trabajo.
# En tercer lugar debe haber una función que reporte toda la información del empleado
# incluyendo la calculada en las dos funciones anteriores, nombre y edad.

def calcular_salario(horas_trabajadas:int,antiguedad:int):
    salario = (horas_trabajadas*10)*((3/100)*antiguedad)
    return salario

def calcular_productividad(artefactos:int,horas_trabajadas:int): 
    produccion = (artefactos/horas_trabajadas)
    return produccion 

def imprimir_informacion(nombre,edad,horas_trabajadas,antiguedad,artefactos):
    print(f"Nombre:",{nombre})
    print(f"Edad:",{edad})
    print(f"Horas trabajadas:",{horas_trabajadas})
    print(f"Antiguedad:",{antiguedad})
    print(f"Artefactos producidos:",{artefactos}) 
    print(f"Salario:",{calcular_salario(horas_trabajadas,antiguedad)})
    print(f"Productividad",{calcular_productividad(artefactos,horas_trabajadas)})