from collections import namedtuple
from csv import reader
from datetime import datetime
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta:str)->list[Entreno]:
    result = []
    with open(ruta) as f:
        lector = reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            #Elíptica,5/4/2019 16:19,Sevilla,47,216,9.32,90,S
            tipo = tipo.strip()
            fechahora = datetime.strptime(fechahora.strip(), "%d/%m/%Y %H:%M")
            ubicacion = ubicacion.strip()
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = compartido.strip()=='S'
            result.append(Entreno(tipo, fechahora, ubicacion, duracion, 
                                  calorias, distancia, frecuencia, compartido))

    return result


def tipos_entrenos(entrenos:list[Entreno])->list[str]:
    result = []
    for x in entrenos:
        result.append(x.tipo)
    return sorted(set(result))

def entrenos_duracion_superior(entrenos: list[Entreno], duracion:int) -> list[Entreno]:
    result = []
    for x in entrenos:
        if x.duracion>duracion:
            result.append(x)
    return result


def suma_calorias(entrenos: list[Entreno], f_inicio:datetime.date, f_fin:datetime.date)->int:
    '''suma_calorias: recibe una lista de tuplas de tipo Entreno 
    y dos fechas, de tipo datetime, f_inicio y f_fin, y devuelve la 
    suma de las calorías quemadas en todos los entrenamientos 
    realizados entre las dos fechas f_inicio y f_fin, ambas incluidas.'''
    result = 0

    for x in entrenos:
        if f_inicio <= x.fechahora.date() <= f_fin:
            result += x.calorias

    return result



def filtra_entrenos(entrenos: list[Entreno], f_inicio:datetime.date, f_fin:datetime.date)->int:
    '''suma_calorias: recibe una lista de tuplas de tipo Entreno 
    y dos fechas, de tipo datetime, f_inicio y f_fin, y devuelve la 
    suma de las calorías quemadas en todos los entrenamientos 
    realizados entre las dos fechas f_inicio y f_fin, ambas incluidas.'''
    result = []

    for x in entrenos:
        if f_inicio <= x.fechahora.date() <= f_fin:
            result.append(x)

    return result

def transforma_a_calorias(entrenos: list[Entreno])->list[int]:
    result = []
    for x in entrenos:
        result.append(x.calorias)
    return result

def suma_calorias_2(entrenos: list[Entreno], f_inicio:datetime.date, f_fin:datetime.date)->int:
    result = filtra_entrenos(entrenos, f_inicio, f_fin)
    result = transforma_a_calorias(result)
    return sum(result)