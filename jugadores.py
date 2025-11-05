# Importacion de librerias 
from utiles import generar_id, leer_int 
# MENU GESTION DE EQUIPOS
def menu_gestion_de_jugadores ():
    while True:
        print ("""
 ===== MENU EQUIPOS ====
1. Alta de jugador
2. Listrar jugadores
3. Buscar por id
4. Actualizar 
5. Eliminar jugador
6. Menú del módulo       
""")
        opcion = input ("Seleccione una opción: ")
        if opcion == "1":
            alta_de_jugador()
        elif opcion == "2":
            listar_jugadores()
        elif opcion == "3":
            id_equipo = int("Ingrese el ID a buscar: ")
            a = buscar_jugador_por_id(id_equipo)
            if a: 
                print(f"\n ID: {a['ID']}\n Nombre: {a['Nombre']}\n Posición: {a['Posición']}\ Activo: {a['Activo']}")
            else:
                print ("Jugador no encontrado.")
        elif opcion == "4":
            actualizar_jugador()
        elif opcion == "5":
            eliminar_jugador()
        elif opcion == "6":
            print("Volviando al menu principal...")
            return 
        else:
            print("Opcion no valida")
# FUNCIONES MENU JUGADORES
    #ALTA DE JUGADOR
def alta_de_jugador (jugadores):
    nombre = input("Nombre del equipo: ")
    while True: 
        posicion = input ("Nombre de la posición del jugador: ")
        return 
    nuevo = {
        "id": generar_id (equipos),
        "Nombre": nombre,
        "posición": posicion,
        "Activo": True
    }
    jugadores(nuevo)
    print(f"Jugador '{nombre}' Creado con ID {nuevo['ID']}:")
    #LISTAR JUGADORES
def listar_jugadores (jugadores, solo_activos=None):
    if solo_activos is True:
        jugador = [u for u in jugadores if u["activo"]]
    if solo_activos is False:
        jugador = [u for u in jugadores if u ["inactivo"]]
    else:
        jugador = jugadores
    if not jugador:
        print("No hay jugadores para mostrar. ")
        return
    print("\n LISTA DE JUGADORES")
    for u in jugador:
        estado = "Activo" if u ["activo"] else "Inactivo"
        print (f"ID {u['ID']}: Nombre {u['Nombre']} Posición {u['Posición']} {estado}")
    print ("----------------\n")
    #BUSCAR ID
def buscar_jugador_por_id(jugadores, id_jugador):
    for u in jugadores:
        if u ["ID"] == id_jugador:
            return u 
    return None
    #ACTUALIZAR 
def actualizar_jugador(jugadores):
    id_jugador = leer_int ("ID del jugador a actualizar: ")
    jugador_1 = buscar_jugador_por_id (jugadores, id_jugador)
    posicion_1 = ""
    if not jugador_1:
        print ("Jugador no encontrado. ")
        return
    print (f"Actualizando '{jugador_1 ['Nombre']}': ")
    nuevo_jugador = input("Nuevo jugador")
    if nuevo_jugador:
        jugador_1 ["Nombre"] = nuevo_jugador
    nueva_posicion = input("Nueva posición. ")
    if nueva_posicion:
        posicion_1 ["Posición"] = nueva_posicion
    #ELIMINAR JUGADOR
def eliminar_jugador (jugadores):
    id_jugador = leer_int ("ID del equipo a eliminar: ")
    jugador_1 = buscar_jugador_por_id (jugadores, id_jugador)
    if not jugador_1:
        print("Jugador no encontrado: ")
        return
    jugadores (jugador_1)
    print(f"Jugador ID {id_jugador} eliminado. ")