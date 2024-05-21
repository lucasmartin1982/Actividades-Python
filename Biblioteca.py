import json

class Libro:
    def __init__(self, nombre, autor, año_publicacion, disponible, unidades):
        self.nombre = nombre
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = disponible == "True"
        self.unidades = int(unidades)

class Biblioteca:
    def __init__(self, archivo_json):
        self.libros = self.cargar_libros(archivo_json)
        self.archivo_json = archivo_json

    def cargar_libros(self, archivo_json):
        with open(archivo_json, 'r') as archivo:
            datos = json.load(archivo)
            libros = []
            for dato in datos:
                libro = Libro(dato['nombre'], dato['autor'], dato['año_publicacion'], dato['disponible'], dato['unidades'])
                libros.append(libro)
            return libros

    def guardar_libros(self):
        datos = []
        for libro in self.libros:
            datos.append({
                'nombre': libro.nombre,
                'autor': libro.autor,
                'año_publicacion': libro.año_publicacion,
                'disponible': "True" if libro.disponible and libro.unidades > 0 else "False",
                'unidades': str(libro.unidades)
            })
        with open(self.archivo_json, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible and libro.unidades > 0]
        if disponibles:
            for libro in disponibles:
                print(f"Nombre: {libro.nombre}, Autor: {libro.autor}, Año: {libro.año_publicacion}, Unidades: {libro.unidades}")
        else:
            print("No hay libros disponibles.")

    def prestar_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre and libro.disponible and libro.unidades > 0:
                libro.unidades -= 1
                if libro.unidades == 0:
                    libro.disponible = False
                self.guardar_libros()
                print(f"El libro '{nombre}' ha sido prestado.")
                return
        print(f"El libro '{nombre}' no está disponible.")

    def recibir_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre:
                libro.disponible = True
                libro.unidades += 1
                self.guardar_libros()
                print(f"El libro '{nombre}' ha sido devuelto.")
                return
        print(f"El libro '{nombre}' no esta disponible.")

def seleccionar_biblioteca():
    print("Seleccione una biblioteca:")
    print("1. Biblioteca 1")
    print("2. Biblioteca 2")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == '1':
        return Biblioteca('biblioteca1.json')
    elif opcion == '2':
        return Biblioteca('biblioteca2.json')
    elif opcion == '3':
        return None
    else:
        print("Opción inválida.")
        return seleccionar_biblioteca()

def menu_biblioteca(biblioteca):
    while True:
        print("\nOpciones:")
        print("1. Mostrar todos los libros disponibles")
        print("2. Prestar un libro")
        print("3. Recibir un libro")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            biblioteca.mostrar_libros_disponibles()
        elif opcion == '2':
            nombre = input("Ingrese el nombre del libro a prestar: ")
            biblioteca.prestar_libro(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del libro a recibir: ")
            biblioteca.recibir_libro(nombre)
        elif opcion == '4':
            break
        else:
            print("Opcion invalida.")

def sistema_bibliotecas():
    while True:
        biblioteca = seleccionar_biblioteca()
        if biblioteca:
            menu_biblioteca(biblioteca)
        else:
            break

sistema_bibliotecas()