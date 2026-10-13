from poblacion import *

def test_filtra_por_pais():
    REGISTROS = lee_poblaciones("data/population.csv")
    tupla = filtra_por_pais(REGISTROS, 'NAM')
    print(tupla)
    tupla = filtra_por_pais(REGISTROS, 'Namibia')
    print(tupla)

def test_calcula_paises():
    REGISTROS = lee_poblaciones("data/population.csv")
    paises = calcula_paises(REGISTROS)
    print("Se han leido: ", len(paises), " paises")
    print("El primer pais: ", paises[0])
    print("El ultimo pais: ", paises[-1])
    print("TODOS: ", set(paises))

def test_lectura():
    REGISTROS = lee_poblaciones("data/population.csv")
    print("Se han leido: ", len(REGISTROS), " registros")
    print("El primer registro: ", REGISTROS[0])
    print("El ultimo registro: ", REGISTROS[-1])

if __name__ == "__main__":
    #test_lectura()
    #test_calcula_paises()
    test_filtra_por_pais()