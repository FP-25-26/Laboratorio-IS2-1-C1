from ahorcado import *

def test_cargar_palabras(ruta):
    print("Testeando cargar_palabras()... ")
    palabras = cargar_palabras(ruta)
    print(f"Palabras cargadas: {len(palabras)}")
    print("Primeras 3 palabras:", palabras[:3])
    print("Últimas 3 palabras:", palabras[-3:])

def test_elegir_palabra(palabras):
    print("Testeando elegir_palabra()... ")
    palabra = elegir_palabra(palabras)
    print(f"Palabra elegida: {palabra}")

def test_enmascarar_palabra(palabra, letras_probadas):
    print(f"Testeando enmascarar_palabra() con la palabra '{palabra}' y las letras ({','.join(letras_probadas)})... ")
    resultado = enmascarar_palabra(palabra, letras_probadas)
    print(f"Palabra enmascarada: {resultado}")
    print()

def test_pedir_letra(letras_probadas):
    print(f"Testeando pedir_letra() con las letras ({','.join(letras_probadas)})... ")
    letra = pedir_letra(letras_probadas)
    print(f"Letra introducida: {letra}")

def test_comprobar_letra(palabra, letra):
    print(f"Testeando comprobar_letra() con la palabra '{palabra}' y la letra '{letra}'... ")
    acierto = comprobar_letra(palabra, letra)
    print(f"Resultado: {'Acierto' if acierto else 'Fallo'}")
    print()

def test_comprobar_palabra_completa(palabra, letras_probadas):
    print(f"Testeando comprobar_palabra_completa() con la palabra '{palabra}' y las letras ({','.join(letras_probadas)})... ")
    resultado = comprobar_palabra_completa(palabra, letras_probadas)
    print(f"Resultado: {'Completa' if resultado else 'Incompleta'}")
    print()

def test_ejecutar_turno(palabra_secreta, letras_probadas):
    print(f"Testeando ejecutar_turno() con la palabra '{palabra_secreta}' y las letras ({','.join(letras_probadas)})... ")
    acierto = ejecutar_turno(palabra_secreta, letras_probadas)
    print(f"Resultado: {'Acierto' if acierto else 'Fallo'}")
    print()

def jugar(max_intentos, palabras):
    '''
      Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes

    :param max_intentos: Número máximo de intentos que el usuario tiene para adivinar la palabra
    :type max_intentos: int
    :param palabras: lista de palabras para adivinar
    :type palabras: list[str]
    '''
    print("Bienvenido a una partida del AhorcadoFP")
    palabra_secreta = elegir_palabra(palabras)
    letras_probadas, intentos_fallidos = set(), 0

    intentos_restantes = max_intentos-intentos_fallidos
    while intentos_fallidos < max_intentos and not comprobar_palabra_completa(palabra_secreta, letras_probadas):
        acierto = ejecutar_turno(palabra_secreta, letras_probadas)
        if not acierto:
            intentos_fallidos += 1
            intentos_restantes = max_intentos-intentos_fallidos
        if comprobar_palabra_completa(palabra_secreta, letras_probadas):
            print("Has ganado el juego")
        else:
            print("Te quedan ", intentos_restantes, " intentos")

    print("La palabra era ", palabra_secreta)    



if __name__ == "__main__":
    test_cargar_palabras("data/palabras_ahorcado.txt")
    #test_elegir_palabra(['python', 'fundamentos', 'programacion'])
    #test_enmascarar_palabra('python', {})
    #test_enmascarar_palabra('python', {'p', 'y', 't', 'h', 'o', 'n'})
    #test_enmascarar_palabra('python', {'a', 'b', 'c', 'd', 'e'})
    #test_enmascarar_palabra('python', {'a', 'e', 'i', 'o', 'u'})
    #test_pedir_letra({'a', 'b', 'c'})
    #test_comprobar_letra('python', 'p')
    #test_comprobar_letra('python', 'a')
    #test_comprobar_palabra_completa('python', {'p', 'y', 't', 'h', 'o', 'n'})
    #test_comprobar_palabra_completa('python', {'a', 'b', 'c', 'd', 'e'})
    #test_comprobar_palabra_completa('python', {})
    #test_ejecutar_turno('python', {'a', 'b', 'c', 'd', 'e'})
    #test_ejecutar_turno('python', {'p', 'y', 't', 'h', 'o'}) 
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(6, palabras)