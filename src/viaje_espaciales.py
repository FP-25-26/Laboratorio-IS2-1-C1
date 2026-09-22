def calculo_dias_trayecto(distancia_km:float, velocidad_kmh:float)->float:
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    return tiempo_dias

def check_embarque(fisico:int, edad:int)->str:
    result = ""
    if edad<18:
        result = "Debes ser mayor de edad."
    elif fisico<5:
        result = "Debes estar en mejor forma."
    else:
        result = "Listo para despegar."
    
    return result
