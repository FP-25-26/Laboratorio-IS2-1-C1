from viaje_espaciales import *

def test_check_embarque():
    nivel_fisico = input("Dame tu nivel físico [1-10]: ")
    nivel_fisico = int(nivel_fisico)
    edad = input("Dame tu edad: ")
    edad = int(edad)
    mensaje_embarque = check_embarque(nivel_fisico, edad)
    print(mensaje_embarque)

def test_viajar_a_marte():
    distancia_a_marte = 225000000
    for velocidad in range(10000, 50001, 10000):
        dias = calculo_dias_trayecto(distancia_a_marte, velocidad)
        print(f"Velocidad: {velocidad} km/h -> Tiempo: {dias} días")


def test_calculo_dias_trayecto():
    kilometros = input("Dame la distancia en kms: ")
    kilometros = float(kilometros)
    velocidad = input("Dame la velocidad en kms/hora: ")
    velocidad = float(velocidad)

    tiempo_dias = calculo_dias_trayecto(kilometros, velocidad)
    print(f"Tardarías {tiempo_dias} días en llegar.")

def test_simula_calculos_dias_trayecto():
    opcion = 's'
    while opcion == 's':
        test_calculo_dias_trayecto()
        opcion = input('Quiere usted seguir trabajando?[s/n]: ')

#test_calculo_dias_trayecto()
#test_check_embarque()
#test_viajar_a_marte()
test_simula_calculos_dias_trayecto()