from piedra_papel_tijeras import ordenador_decide_jugada, determina_ganador


def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario


def jugar_ronda():
    '''Muestre un mensaje de bienvenida
    Haga que el ordenador decida su jugada
    Haga que el jugador decida su jugada
    Muestre un mensaje indicando la elección del ordenador
    Determine quién es el ganador
    Muestre un mensaje con el resultado de la ronda.'''
    result = None
    print("Bienvenido a la ronda de: 'PiedraPapelTijering'")
    jugada_ordenador = ordenador_decide_jugada()
    jugada_usuario = usuario_decide_jugada()
    print("El ordenador eligió: ", jugada_ordenador)
    ganador = determina_ganador(jugada_usuario, jugada_ordenador)
    if ganador == 1:
        print("Usted ganó la ronda")
        result = (1, 0)
    elif ganador == -1:
        print("Usted perdió la ronda")
        result = (0, 1)
    else:
        print("Empate!!")
        result = (0, 0)
    return result

def jugar_partida(n:int)->None:
    print("Bienvenido a mi primer videojuego: 'PiedraPapelTijering'")
        
    ganadas_usuario, ganadas_ordenador = 0, 0

    while ganadas_usuario < n and ganadas_ordenador < n:
        usuario, ordenador = jugar_ronda()
        ganadas_usuario += usuario
        ganadas_ordenador += ordenador

    if ganadas_usuario>ganadas_ordenador:
        print("Eres un campeón")
    else:
        print("Sigue jugando...")


def test_ordenador_decide_jugada():
    '''
    Test para la función ordenador_decide_jugada.
    '''
    print("Testeando ordenador_decide_jugada...")
    eleccion = ordenador_decide_jugada()
    print("El ordenador eligió:", eleccion)
    print()

def test_usuario_decide_jugada():
    '''
    Test para la función usuario_decide_jugada.
    '''
    print("Testeando usuario_decide_jugada...")
    eleccion = usuario_decide_jugada()
    print("El usuario eligió:", eleccion)
    print()

def test_determina_ganador(eleccion_usuario, eleccion_ordenador):
    '''
    Test para la función determina_ganador.
    '''
    print("Testeando determina_ganador...")        
    print(f"Jugador: {eleccion_usuario} vs. Ordenador: {eleccion_ordenador}")
    resultado = determina_ganador(eleccion_usuario, eleccion_ordenador)
    print("Resultado:", resultado)
    print()







# Función principal
if __name__ == "__main__":
    #test_ordenador_decide_jugada()
    #test_usuario_decide_jugada()
    #test_determina_ganador("piedra", "tijeras")
    #test_determina_ganador("piedra", "papel")
    #test_determina_ganador("piedra", "piedra")
    #test_determina_ganador("tijeras", "tijeras")
    #test_determina_ganador("tijeras", "papel")
    #test_determina_ganador("tijeras", "piedra")
    #test_determina_ganador("papel", "tijeras")
    #test_determina_ganador("papel", "papel")
    #test_determina_ganador("papel", "piedra")
    jugar_partida(2)

