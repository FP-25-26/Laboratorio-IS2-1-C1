## Fundamentos de Programación
# Ejercicio de laboratorio: Entrenos

Disponemos de datos sobre los entrenamientos realizados por un usuario. Para cada entrenamiento se tiene 
la siguiente información: 
* tipo: tipo de entrenamiento realizado, de tipo str. 
* fechahora: fecha y hora del entrenamiento, de tipo datetime. 
* ubicación: lugar donde se ha realizado el entrenamiento, de tipo str 
* duración: duración del entrenamiento en minutos, de tipo int. 
* calorías: número de kilocalorías activas quemadas en el entrenamiento, de tipo int. 
* distancia: distancia en kilómetros recorrida en el entrenamiento, de tipo float. 
* frecuencia: frecuencia cardiaca media registrada en el entrenamiento, de tipo int. 
* compartido: indica si el entrenamiento ha sido compartido por el usuario, de tipo bool (S si ha sido 
compartido, N si no lo ha sido). 

Por ejemplo, la siguiente línea del fichero: 

```Andar,12/11/2021 8:14,Sevilla,48,155,3.49,89,N```

indica que el 12 de noviembre de 2021 a las 8:14 horas, el usuario realizó un entrenamiento de tipo ‘Andar’
durante 48 minutos, quemando 155 kilocalorías activas y recorriendo un total de 3.49 kilómetros con una
frecuencia cardiaca media de 89 lpm, y que no compartió este entreno.

Para almacenar los datos de un entrenamiento se usará obligatoriamente la siguiente namedtuple:

```python
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
```

Cree un módulo **entrenos.py** e implemente en él una función **lee_entrenos**, que reciba la ruta de un fichero en formato CSV codificado en UTF-8 y devuelva una lista de tuplas de tipo Entreno. Utilice la función datetime.strptime con el formato ```%d/%m/%Y %H:%M``` para convertir la fecha. 

Cree un módulo **entrenos_test.py** e implemente en él una prueba de la función anterior, que lea los datos del ficheros ```entrenos.csv``` ubicado en la carpeta ```data``` y muestre los tres primeros y tres últimos registros leídos. 

Los resultados esperados del test son:
```python
===> Test de la función lee_entrenos
Se han leído 200 entrenos.
Mostrando los 3 primeros:
         Entreno(tipo='Elíptica', fechahora=datetime.datetime(2019, 4, 5, 16, 19), ubicacion='Sevilla', duracion=47, calorias=216, distancia=9.32, frecuencia=90, compartido=True)     
         Entreno(tipo='Tenis', fechahora=datetime.datetime(2020, 9, 27, 10, 17), ubicacion='Huelva', duracion=97, calorias=338, distancia=16.41, frecuencia=115, compartido=True)      
         Entreno(tipo='Elíptica', fechahora=datetime.datetime(2021, 7, 1, 3, 47), ubicacion='Sevilla', duracion=57, calorias=357, distancia=19.74, frecuencia=129, compartido=False)   
Mostrando los 3 últimos:
         Entreno(tipo='Remo', fechahora=datetime.datetime(2020, 8, 28, 3, 42), ubicacion='Cádiz', duracion=77, calorias=225, distancia=15.82, frecuencia=110, compartido=True)
         Entreno(tipo='Remo', fechahora=datetime.datetime(2019, 11, 23, 10, 25), ubicacion='Sevilla', duracion=109, calorias=304, distancia=6.39, frecuencia=113, compartido=True)     
         Entreno(tipo='Senderismo', fechahora=datetime.datetime(2020, 5, 4, 21, 55), ubicacion='Córdoba', duracion=126, calorias=338, distancia=15.5, frecuencia=136, compartido=False)
```
Implemente en el módulo **entrenos.py** las siguientes funciones. Para cada una de ellas, implemente una prueba en el módulo **entrenos_test.py**.

1. **tipos_entreno**: recibe una lista de tuplas de tipo Entreno, y devuelve una lista con todos los tipos de entrenamientos en orden alfabético y sin repetir ninguno.

Los resultados esperados del test son:

```python
===> Test de la función tipos_entreno
Los tipos diferentes de entreno son:
         Andar
         Bici
         Cinta
         Correr
         Elíptica
         Nadar
         Pilates
         Remo
         Senderismo
         Tenis
         Yoga
```
2. **entrenos_duracion_superior**: recibe una lista de tuplas de tipo Entreno y un valor entero d, y devuelve una lista con todos los entrenamientos que tienen una duración superior al valor d.
Los resultados esperados del test son:
```python
===> Test de la función entrenos_duracion_superior
Hay 61 entrenos con una duración superior a 100 minutos.
Mostrando los 3 primeros:
         Entreno(tipo='Remo', fechahora=datetime.datetime(2021, 2, 7, 17, 31), ubicacion='Málaga', duracion=127, calorias=261, distancia=18.83, frecuencia=124, compartido=False)      
         Entreno(tipo='Cinta', fechahora=datetime.datetime(2019, 5, 30, 3, 39), ubicacion='Sevilla', duracion=125, calorias=277, distancia=6.81, frecuencia=135, compartido=False)     
         Entreno(tipo='Bici', fechahora=datetime.datetime(2021, 11, 24, 2, 10), ubicacion='Cádiz', duracion=114, calorias=284, distancia=16.96, frecuencia=116, compartido=True)       
```

3. **suma_calorias**: recibe una lista de tuplas de tipo Entreno y dos fechas, de tipo `datetime`, f_inicio y f_fin, y devuelve la suma de las calorías quemadas en todos los entrenamientos realizados entre las dos fechas f_inicio y f_fin, ambas incluidas.

Los resultados esperados del test son:
```python
===> Test de la función suma_calorias
En los entrenamientos realizados entre 2020-03-15 00:00:00 y 2020-06-30 23:59:00 se han quemado 5189 calorías.
```

## Ejercicios extra

4. **entrenamiento_mas_kms**: recibe una lista de tuplas de tipo Entreno y devuelve el entrenamiento en el que se han recorrido más kilómetros.
Los resultados esperados del test son:

```python
===> Test de la función entrenamiento_mas_kms
El entrenamiento de mas kilometros es Entreno(tipo='Elíptica', fechahora=datetime.datetime(2021, 7, 1, 3, 47), ubicacion='Sevilla', duracion=57, calorias=357, distancia=19.74, frecuencia=129, compartido=False).
```

5. **duracion_media_entrenos**: recibe una lista de tuplas de tipo Entreno,  un año y un mes, y devuelve la duración media de los entrenamientos de ese mes y año. Si la media no se puede calcular, devuelve None.
Los resultados esperados del test son:

```python
===> Test de la función duracion_media_entrenos
La duración media de los entrenos del año 2020 y el mes 6 es 75.2560975609756.

===> Test de la función duracion_media_entrenos
La duración media de los entrenos del año 2020 y el mes 3 es 75.36486486486487.
```