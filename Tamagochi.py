class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = ""
        self.esta_vivo = True

    def mostrar_estado(self):
        print("")
        print(f"{self.nombre}:")
        print(f"Nivel de energía: {self.nivel_energia}")
        print(f"Nivel de hambre: {self.nivel_hambre}")
        print(f"Nivel de felicidad: {self.nivel_felicidad}")
        self.verificar_estado()
        if self.nivel_felicidad <= 20 and self.esta_vivo:
            self.humor = "enojado"
            print("Estado de humor: enojado")
        elif 21 <= self.nivel_felicidad <= 40 and self.esta_vivo:
            self.humor = "triste"
            print("Estado de humor: triste")
        elif 41 <= self.nivel_felicidad <= 60 and self.esta_vivo:
            self.humor = "indiferente"
            print("Estado de humor: indiferente")
        elif 61 <= self.nivel_felicidad <= 80 and self.esta_vivo:
            self.humor = "feliz"
            print("Estado de humor: feliz")
        else:
            if self.esta_vivo:
                print("Estado de humor: euforico")
        print("")

    def alimentar(self):
        self.nivel_hambre -= 10
        self.verificar_estado()
        self.mostrar_estado()

    def jugar(self):
        self.nivel_felicidad += 20
        if self.nivel_felicidad > 100:
            self.nivel_felicidad = 100
        self.nivel_energia -= 18
        self.nivel_hambre += 10
        self.verificar_estado()
        self.mostrar_estado()

    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5
        self.verificar_estado()
        self.mostrar_estado()

    def verificar_estado(self):
        if self.nivel_hambre > 20 and self.nivel_energia > 0:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
        self.nivel_hambre = max(0, min(self.nivel_hambre, 100))
        self.nivel_energia = max(0, min(self.nivel_energia, 100))
        self.nivel_felicidad = max(0, min(self.nivel_felicidad, 100))
        if self.nivel_hambre >= 20:
            print("Hambriento")
        if self.nivel_energia == 0:
            print("Muerto")
            self.esta_vivo = False


nombre = input("Ingrese nombre del tamagochi: ")
tamagochi = Tamagotchi(nombre)

tamagochi.mostrar_estado()

while tamagochi.esta_vivo:
    print("1. Alimentar")
    print("2. Jugar")
    print("3. Dormir")
    print("4. Salir")
    opcion = int(input("Ingrese opcion: "))



    if opcion == 1:
        tamagochi.alimentar()
    elif opcion == 2:
        tamagochi.jugar()
    elif opcion == 3:
        tamagochi.dormir()
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")