from entrenos import *


def test_lectura():
	entrenos = lee_entrenos("data/entrenos.csv")
	print("===> Test de la función lee_entrenos")
	print(f"Se han leído {len(entrenos)} entrenos.")
	print("Mostrando los 3 primeros:")
	for i in range(3):
		print(f"         {entrenos[i]}")
	print("Mostrando los 3 últimos:")
	for i in range(-3, 0):
		print(f"         {entrenos[i]}")

def test_tipos_entrenos(entrenos: list[Entreno])->None:
	print('===> Test de la función tipos_entreno')
	print('Los tipos diferentes de entreno son:')
	lista = tipos_entrenos(entrenos)
	for x in lista:
		print(x)	

def test_entrenos_duracion_superior(ent: list[Entreno], d: int)->None:
	'''===> Test de la función entrenos_duracion_superior
		Hay 61 entrenos con una duración superior a 100 minutos.
		Mostrando los 3 primeros:
				Entreno(tipo='Remo', fechahora=datetime.datetime(2021, 2, 7, 17, 31), ubicacion='Málaga', duracion=127, calorias=261, distancia=18.83, frecuencia=124, compartido=False)      
				Entreno(tipo='Cinta', fechahora=datetime.datetime(2019, 5, 30, 3, 39), ubicacion='Sevilla', duracion=125, calorias=277, distancia=6.81, frecuencia=135, compartido=False)     
				Entreno(tipo='Bici', fechahora=datetime.datetime(2021, 11, 24, 2, 10), ubicacion='Cádiz', duracion=114, calorias=284, distancia=16.96, frecuencia=116, compartido=True) '''
	
	entrenos = entrenos_duracion_superior(ent, d)
	print('===> Test de la función entrenos_duracion_superior')
	print('Hay ',len(entrenos), 
	      ' entrenos con una duración superior a ',d,' minutos')
	print('Mostrando los 3 primeros:')
	for i in range(3):
		print(entrenos[i])
	

'''===> Test de la función suma_calorias
En los entrenamientos realizados entre 2020-03-15 00:00:00 y 2020-06-30 23:59:00 se han quemado 5189 calorías.
'''

if __name__ == "__main__":
	#test_lectura()
	ENTRENOS = lee_entrenos("data/entrenos.csv")
	#test_tipos_entrenos(ENTRENOS)
	test_entrenos_duracion_superior(ENTRENOS, 100)