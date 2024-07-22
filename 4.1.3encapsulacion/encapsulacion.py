class Personaje:
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

    # Getters y Setters para los atributos privados
    def get_nombre(self):
        return self._nombre

    def get_fuerza(self):
        return self._fuerza

    def get_inteligencia(self):
        return self._inteligencia

    def get_defensa(self):
        return self._defensa

    def get_vida(self):
        return self._vida


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


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.get_nombre(), ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.get_nombre(), ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.get_nombre())
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.get_nombre())
    else:
        print("\nEmpate")


# Ejemplo de uso
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)