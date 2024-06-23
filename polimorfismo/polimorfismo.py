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


# Ejemplo de uso de polimorfismo en combate
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)