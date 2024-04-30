
import json

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
def hacer_reserva():
    with open("reservas.json", "r") as archivo:
        reservas = json.load(archivo)


    numero_habitacion = int(input("Ingrese el número de habitacion: "))
    if numero_habitacion not in range(1, 10):
        print("El id ingresado no existe")
    elif reservas["id"][numero_habitacion-1]["nombre_cliente"] != "":
        print("La habitación ya está reservada")
    else:
        fecha_ingreso = input("Ingrese la fecha de entrada (DD-MM-AAAA): ")
        fecha_salida = input("Ingrese la fecha de salida (DD-MM-AAAA): ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        print(reservas["id"][numero_habitacion-1]["nombre_cliente"])
        
        reservas["id"][numero_habitacion-1] = {
            'numero_habitacion': numero_habitacion,
            'tipo_habitacion': 'single' if numero_habitacion in range(1, 4) else 'doble' if numero_habitacion in range(4, 7) else 'triple',
            'nombre_cliente': nombre_cliente,
            'fecha_ingreso': fecha_ingreso,
            'fecha_salida': fecha_salida            
        }
        

        with open('reservas.json', 'w') as archivo:
            json.dump(reservas, archivo, indent=4)
        print(f"La habitación {numero_habitacion} ha sido reservada para el cliente {nombre_cliente}")
        print("su numero de id de reserva es:",  reservas["id"][numero_habitacion-1]["numero_habitacion"])

def cancelar_reserva():
    with open("reservas.json", "r") as archivo:
        reservas = json.load(archivo)
        
    numero_habitacion = int(input("Ingrese numero id de reserva a cancelar:"))
    
    reservas["id"][numero_habitacion-1] = {
            'numero_habitacion': numero_habitacion,
            'tipo_habitacion': 'single' if numero_habitacion in range(0, 3) else 'doble' if numero_habitacion in range(4, 7) else 'triple',
            'nombre_cliente': "",
            'fecha_ingreso': "",
            'fecha_salida': ""
    }
    print("")
    print("reserva cancelada")
    print("")
    
    with open('reservas.json', 'w') as archivo:
            json.dump(reservas, archivo, indent=4)

def buscar_reserva():
    with open("reservas.json", "r") as archivo:
        reservas = json.load(archivo)
    
    id = int(input("Ingrese numero reserva para consultar:"))
    
    print("")
    
    for fila1, fila2 in zip(reservas["id"][id-1], reservas["id"][id-1].values()):
        print(f"{fila1}: {fila2}")
    
    print("")
    input("Presione ENTER para continuar")


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