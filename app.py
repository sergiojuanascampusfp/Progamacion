# Importacion de librerias 
from equipos import *
from jugadores import *
from calendario import *
from ranking import *
# Definimos variables
menuprincipal = [
    "1.- Gestion de equipos",
    "2.- Gestion de jugadores",
    "3.- calendario de partidos",
    "4.- Resultados y clasificación",
    "5.- Salir"
]
opcion = 0
# Desarollamos lógica del programa 
while opcion != 5:
    match opcion:
        case 1:
            menu_gestion_de_equipos()
        case 2:
            menu_gestion_de_jugadores()
        case 3:
            menu_calendario_de_partidos()
        case 4:
            menu_resultados_y_clasificacion()
        case 5:
            valor = "Hasta Luego, que tengas un buen dia"
        case _:
            valor = "Opcion errónea"
    print (f"{valor}")
