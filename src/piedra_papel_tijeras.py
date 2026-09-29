from random import choice

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = choice(opciones)
    return res


def determina_ganador(jugada_usuario, jugada_ordenador):
    res = 0
    if jugada_usuario == jugada_ordenador:
        res = 0
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        res = 1
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        res = 1
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        res = 1
    else:
        res = -1
    return res
