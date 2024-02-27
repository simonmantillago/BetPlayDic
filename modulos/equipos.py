def registrar_equipo(equipos, nombre_equipo):
    if nombre_equipo not in equipos:
        equipos[nombre_equipo] = {
            'PJ': 0,
            'PG': 0,
            'PP': 0,
            'PE': 0,
            'GF': 0,
            'GC': 0,
            'TP': 0
        }

def verificar_equipo(equipos, nombre_equipo):
    return nombre_equipo in equipos
