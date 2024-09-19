# 7- Supongamos que le solicito a chatgpt una función para calcular valores de 
# ventas de productos con impuestos para una determinada empresa:
# La respuesta de chatgpt es:

def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
    resultado_final = resultado_nacional + resultado_exportaciones
    return resultado_final

#¿Considera que cumple con los objetivos de una función?
#Corrija la función dentro de un módulo, divida en distintas funciones 
# de ser necesario, documente y denomine correctamente.

def calculo_impuestos_exportaciones(valor_exportaciones,retenciones=15):
    resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100)) 
    return resultado_exportaciones 

def calculo_impuestos_nacionales(valor_ventas_naciones,iva=21):
    resultado_nacionales = valor_ventas_naciones* (1 / (1 + (iva / 100)))
    return resultado_nacionales 