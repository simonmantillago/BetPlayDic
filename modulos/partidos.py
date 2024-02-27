def actualizar_estadisticas(equipo, goles_a_favor, goles_en_contra, resultado):
    equipo['PJ'] += 1
    equipo['GF'] += goles_a_favor
    equipo['GC'] += goles_en_contra

    if resultado == "Ganado":
        equipo['PG'] += 1
        equipo['TP'] += 3
    elif resultado == "Empatado":
        equipo['PE'] += 1
        equipo['TP'] += 1
    else:
        equipo['PP'] += 1

def registrar_partido(equipos, local, visitante, goles_local, goles_visitante):
    if local in equipos and visitante in equipos:
        equipo_local = equipos[local]
        equipo_visitante = equipos[visitante]

        if goles_local > goles_visitante:
            actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Ganado")
            actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Perdido")
        elif goles_local < goles_visitante:
            actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Ganado")
            actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Perdido")
        else:
            actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Empatado")
            actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Empatado")
    else:
        print("Uno o ambos equipos no están registrados.")
