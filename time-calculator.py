def add_time (start_Time, duration, day=""):

    day = day.lower()
    day = day.capitalize()

    puntos = start_Time.index(":")
    puntos2 = duration.index(":")

    horas_Start = int(start_Time[0:puntos])
    minutos_Start = int(start_Time[puntos+1:puntos+3])

    franja_Inicial = start_Time[puntos+4:puntos+6]

    horas_Duracion = int(duration[0:puntos2])
    minutos_Duracion = int(duration[puntos2+1:puntos2+3])

    ###### conversor 24 horas
    if (franja_Inicial == "AM" and horas_Start == 12):  
        hora24 = "00"
    elif franja_Inicial == "AM": 
        hora24 = horas_Start 
    elif (franja_Inicial == "PM" and horas_Start == 12): 
        hora24 = horas_Start
    else:   
        hora24 = str(int(horas_Start) + 12)
  
    dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for i in range(len(dias)):
        if day == dias[i]:
            indiceDia = i
            break
        else:
            indiceDia = 0

    suma_Minutos = 0
    resto_minutos = 0

    if minutos_Duracion != 0 or minutos_Duracion != 00:
        suma_Minutos = minutos_Start + minutos_Duracion
    else:
        suma_Minutos = minutos_Start

    if suma_Minutos >= 60:
        resto_minutos = suma_Minutos//60
        suma_Minutos = suma_Minutos - 60 * resto_minutos

    if suma_Minutos < 10:
        suma_Minutos = "0"+ str(suma_Minutos)

    horas_Duracion += resto_minutos

    horas_Sumar = int(hora24) + horas_Duracion 

    hasta24 = 0

    diasPasan = 0 

    hora1 = int(hora24)
    hora2 = horas_Duracion

    horas_Sumar = int(hora24) + horas_Duracion 

    suma = horas_Sumar

    if suma >= 24:
        diasPasan += 1
        hasta24 = 24 - hora1
        quitar = hora2 - hasta24
    else:
        quitar = hora1 + hora2

    if quitar >= 24:
        quitar2 = quitar//24
        quitar3 = quitar - (24 * quitar2)
        resultado = 0 + quitar3
        diasPasan += quitar2

    elif quitar == 0:
        resultado = quitar
    else:
        resultado = 0 + quitar

    if diasPasan == 0:
        dias = dias
    elif diasPasan == 1:
        dias = dias*2
    else:
        dias = dias * (2 + diasPasan//7)

    dia_Final = dias[indiceDia]

    if diasPasan == 1:
        dias_Resultado = " (next day)"
    elif diasPasan == 0:
        dias_Resultado = ""
    else:
        dias_Resultado = " ("+ str(diasPasan) + " days later)"
    ########################

    if diasPasan >= 1:
        dias = dias * diasPasan
        indiceDia = indiceDia + diasPasan
    else:
        dias = dias * 2
        indiceDia = indiceDia + diasPasan 

    hora = resultado

    dia_Final = dias[indiceDia]

    if hora >= 12:
        franja = "PM"
    else:
        franja = "AM"
   
    ##### Conversor formato 12 horas

    if (franja == "AM" and ((hora == 0) or (hora == 00))):  
        hora12 = "12"
    elif franja == "AM" and hora != 0: 
        hora12 = hora
    elif (franja == "PM" and hora == 12): 
        hora12 = hora
    else:   
        hora12 = str(int(hora) - 12)

    hora_Finales = hora12

    if day == "" and dias_Resultado != "":
        #resultado = str(hora_Finales) + ":" + str(suma_Minutos)+ " " + franja + " " + dias_Resultado
        resultado = str(hora_Finales) + ":" + str(suma_Minutos)+ " " + franja +  dias_Resultado
    elif day == "" and dias_Resultado == "":
        resultado = str(hora_Finales) + ":" + str(suma_Minutos)+ " " + franja
    else:
        resultado = str(hora_Finales) + ":" + str(suma_Minutos)+ " " + franja + ", " + dia_Final + dias_Resultado
    
    return resultado
