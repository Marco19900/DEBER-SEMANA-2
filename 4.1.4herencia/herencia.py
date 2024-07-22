lass Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self._nombre = nombre
        self._fuerza = fuerza
        self._inteligencia = inteligencia
        self._defensa = defensa
        self._vida = vida

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Fuerza:", self._fuerza)
        print("·Inteligencia:", self._inteligencia)
        print("·Defensa:", self._defensa)
        print("·Vida:", self._vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._defensa += defensa

    def esta_vivo(self):
        return self._vida > 0

    def morir(self):
        self._vida = 0
        print(self._nombre, "ha muerto")

    def calcular_daño(self, enemigo):
        pass

    def atacar(self, enemigo):
        pass


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self._espada = 8
        elif opcion == 2:
            self._espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self._espada)

    def calcular_daño(self, enemigo):
        return self._fuerza * self._espada - enemigo.get_defensa()


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self._libro)

    def calcular_daño(self, enemigo):
        return self._inteligencia * self._libro - enemigo.get_defensa()


# Ejemplo de uso de 4.1.4herencia
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()