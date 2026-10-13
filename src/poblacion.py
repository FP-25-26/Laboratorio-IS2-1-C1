from collections import namedtuple
from csv import reader


RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, anyo, censo')

'''lee_poblaciones(ruta_fichero): lee el fichero de entrada y devuelve una 
lista de tuplas de tipo RegistroPoblacion.'''

def lee_poblaciones(ruta_fichero: str)-> list[RegistroPoblacion]:
    result = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = reader(f)
        for pais, codigo, anyo, censo in lector:
            pais = pais.strip()
            codigo = codigo.strip()
            anyo = int(anyo)
            censo = int(censo)
            result.append(RegistroPoblacion(pais, codigo, anyo, censo))
    return result

'''calcula_paises(poblaciones): toma una lista de tuplas de 
tipo RegistroPoblacion y devuelve una lista ordenada alfabéticamente 
con los nombres de los países para los que hay datos.'''

def calcula_paises(poblaciones: list[RegistroPoblacion])->list[str]:
    result = []
    for x in poblaciones:
        result.append(x.pais)

    result.sort()
    return result

'''filtra_por_pais(poblaciones, nombre_o_codigo): toma una lista de tuplas 
de tipo RegistroPoblacion, y el nombre o código de un país, 
y devuelve una lista de tuplas con los datos del país que se pasa como parámetro 
(año y censo). ¡Importante!: el país puede venir expresado en el parámetro 
nombre_o_codigo con su nombre completo o con su código.'''

def auxiliar_filtra_por_pais(poblaciones: list[RegistroPoblacion], nombre_o_codigo:str)->list[RegistroPoblacion]:
    result = []
    for x in poblaciones:
        if x.pais == nombre_o_codigo or x.codigo == nombre_o_codigo:
            result.append(x)
    return result

def auxiliar_transforma_registro_a_anyo_censo(lista: list[RegistroPoblacion])->list[tuple[int, int]]:
    result = []
    for x in lista:
        result.append((x.anyo, x.censo))
    return result

def filtra_por_pais(poblaciones: list[RegistroPoblacion], nombre_o_codigo:str)->list[tuple[int, int]]:
    filtrado = auxiliar_filtra_por_pais(poblaciones, nombre_o_codigo)
    transformado = auxiliar_transforma_registro_a_anyo_censo(filtrado)
    return transformado

def filtra_por_pais_2(poblaciones: list[RegistroPoblacion], nombre_o_codigo:str)->list[tuple[int, int]]:
    filtrado = filter(lambda x: x.pais == nombre_o_codigo or x.codigo == nombre_o_codigo, poblaciones)
    transformado = map(lambda x: (x.anyo, x.censo), filtrado)
    return transformado


'''filtra_por_paises_y_anyo(poblaciones, anyo, paises): toma una lista de tuplas 
de tipo RegistroPoblacion, un año y un conjunto de nombres de países, 
y devuelve una lista de tuplas (nombre_pais, num_habitantes) 
con los datos del año pasado como parámetro para los países incluidos en el parámetro paises.'''

def filtra_por_paises_y_anyo_2(poblaciones: list[RegistroPoblacion], 
                               anyo: int, paises: set[str])->list[tuple[str, int]]:
    result = []
    for x in poblaciones:
        if x.anyo == anyo and x.pais in paises:
            result.append((x.pais, x.censo))
    return result

def auxiliar_filtra_por_paises_y_anyo(
        poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str])->list[RegistroPoblacion]:
    result = []
    for x in poblaciones:
        if x.anyo == anyo and x.pais in paises:
            result.append(x)
    return result

def auxiliar_transforma_registro_a_pais_censo(lista: list[RegistroPoblacion])->list[tuple[str, int]]:
    result = []
    for x in lista:
        result.append((x.pais, x.censo))
    return result

def filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str])->list[tuple[str, int]]:
    filtrado = auxiliar_filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    transformado = auxiliar_transforma_registro_a_pais_censo(filtrado)
    return transformado


