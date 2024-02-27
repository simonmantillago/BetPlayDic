from modulos import equipos
from modulos import partidos
from modulos import reportes
import os
if __name__ == '__main__':
    equipos_list = []
    def main():
        os.system('cls')
        equipos_dict = {}  
        while True:
            os.system('cls')
            titulo = """
            ++++++++++++++++++++++++++++++
            + LIGA BETPLAY COLOMBIA 2024 +
            ++++++++++++++++++++++++++++++
            """
            print(titulo)
            print("\n1. Registrar equipo")
            print("2. Registrar partido")
            print("3. Reportes")
            print("4. Salir")

            opcion = solicitar_opcion("Seleccione una opción: ")  

            if opcion == 1:
                os.system('cls')
                nombre_equipo = input("Ingrese el nombre del equipo: ")
                equipos.registrar_equipo(equipos_dict, nombre_equipo)   
            elif opcion == 2:
                os.system('cls')
                while True:
                    print("""
                        ++++++++++++++++++++++++++++++++++
                        + REGISTRO PARTIDOS BETPLAY 2024 +
                        ++++++++++++++++++++++++++++++++++
                        """)
                    for i, equipo in enumerate(equipos_dict, start=1):  
                        print(f"{i}. {equipo}")
                    local_index = solicitar_opcion("Seleccione el equipo local por su número: ") - 1
                    visitante_index = solicitar_opcion("Seleccione el equipo visitante por su número: ") - 1
                    
                    if not (0 <= local_index < len(equipos_dict) and 0 <= visitante_index < len(equipos_dict)):
                        print("Error: Uno o ambos equipos no están registrados.")
                        continue
                    
                    local = list(equipos_dict.keys())[local_index] 
                    visitante = list(equipos_dict.keys())[visitante_index] 
                    
                    goles_local = solicitar_gol(local)
                    goles_visitante = solicitar_gol(visitante)
                    partidos.registrar_partido(equipos_dict, local, visitante, goles_local, goles_visitante)
                    break
            elif opcion == 3:
                os.system('cls')
                submenu_reportes(equipos_dict)  
            elif opcion == 4:
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Opción inválida. Por favor, seleccione una opción válida.")



    def submenu_reportes(equipos_dict):
        os.system('cls')
        while True:
            os.system('cls')
            titulo = """
            ++++++++++++++++++++++++++++++
            + LIGA BETPLAY COLOMBIA 2024 +
            ++++++++++++++++++++++++++++++
            """
            print(titulo)
            print("1. Equipo con más goles anotados")
            print("2. Equipo con más puntos")
            print("3. Equipo con más partidos ganados")
            print("4. Total de goles anotados por todos los equipos")
            print("5. Promedio de goles anotados en el torneo")
            print("6. Ver estadísticas de todos los equipos")
            print("7. Volver al menú principal")

            opcion = solicitar_opcion("Seleccione una opción: ") 

            if opcion == 1:
                reportes.reporte_max_goles(equipos_dict)
                os.system('pause')
                
            elif opcion == 2:
                reportes.reporte_max_puntos(equipos_dict)
                os.system('pause')
                
            elif opcion == 3:
                reportes.reporte_max_partidos_ganados(equipos_dict)
                os.system('pause')
                
            elif opcion == 4:
                reportes.total_goles_anotados(equipos_dict)
                os.system('pause')
                
            elif opcion == 5:
                reportes.promedio_goles_anotados(equipos_dict)
                os.system('pause')
                
            elif opcion == 6:
                reportes.mostrar_estadisticas_equipos(equipos_dict)
                os.system('pause')
                
            elif opcion == 7:
                break

            
    def solicitar_opcion(mensaje):
        while True:
            try:
                opcion = int(input(mensaje))
                return opcion
            except ValueError:
                print("Opcion invalida")

    def solicitar_gol(name):
            while True:
                    try:
                        opcion = int(input(f'Cuantos goles metio el equipo {name}: '))
                        return opcion
                    except ValueError:
                        print('Dato invalido')

    main()





        