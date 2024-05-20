
import json

from funciones import hacer_reserva
from funciones import cancelar_reserva
from funciones import buscar_reserva

reservas = {                            
    "id": [
        {                               
            "numero_habitacion": 1,     
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha_entrada": "",
            "fecha salida": ""
        },
        {
            "numero_habitacion": 2,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha_entrada": "",
            "fecha_salida": ""
        },
        {
            "numero_habitacion": 3,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha_entrada": "",
            "fecha_salida": ""
        },
        {
            "numero_habitacion": 4,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha_entrada": "",
            "fecha_salida": ""
        },
        {
            "numero_habitacion": 5,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha entrada": "",
            "fecha salida": ""
        },
        {
            "numero_habitacion": 6,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha_entrada": "",
            "fecha_salida": ""
        },
        {
            "numero_habitacion": 7,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha entrada": "",
            "fecha salida": ""
        },
        {
            "numero_habitacion": 8,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha_entrada": "",
            "fecha_salida": ""
        },
        {
            "numero_habitacion": 9,
            "tipo_habitacion": "",
            "nombre_cliente": "",
            "fecha_entrada": "",
            "fecha_salida": ""
        }
    ]
}



menu = """

1) Ingresar reserva
2) Cancelar reserva
3) Buscar reserva
4) Salir

Id habitaciones 1,2,3: single
                4,5,6: doble
                7,8,9: triple

"""

while True:

    print(menu)
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        hacer_reserva()
    if opcion == 2:
        cancelar_reserva()
    if opcion == 3:
        buscar_reserva()
    if opcion == 4:
        break