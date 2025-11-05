# Importacion de librerias 
from utiles import generar_id, leer_int 
# MENU GESTION DE EQUIPOS
def menu_gestion_de_equipos ():
    while True:
        print ("""
 ===== MENU EQUIPOS ====
1. Crear equipo
2. Listrar equipos
3. Buscar por id
4. Actualizar datos
5. Eliminar equipo
6. Menú del módulo       
""")
        opcion = input ("Seleccione una opción: ")
        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            id_equipo = int("Ingrese el ID a buscar: ")
            a = buscar_equipo_por_id(id_equipo)
            if a: 
                print(f"\n ID: {a['ID']}\n Nombre: {a['Nombre']}\n Ciudad: {a['Ciudad']}\ Activo: {a['Activo']}")
            else:
                print ("Equipo no encontrado.")
        elif opcion == "4":
            actualizar_datos()
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "6":
            print("Volviando al menu del principal...")
            return 
        else:
            print("Opcion no valida")
# FUNCIONES MENU EQUIPOS
    #CREAR EQUIPO
def crear_equipo (equipos):
    nombre = input("Nombre del equipo: ")
    while True: 
        ciudad = input ("Nombre de la ciuadad del equipo: ")
        return 
    nuevo = {
        "id": generar_id(equipos),
        "Nombre": nombre,
        "Ciudad": ciudad,
        "Activo": True
    }
    equipos(nuevo)
    print(f"Equipo'{nombre}' Creado con ID {nuevo['ID']}:")
    #LISTAR EQUIPOS
def listar_equipos (equipos, solo_activos=None):
    if solo_activos is True:
        equipo = [u for u in equipos if u["activo"]]
    if solo_activos is False:
        equipo = [u for u in equipos if u ["inactivo"]]
    else:
        equipo = equipos
    if not equipo:
        print("No hay equipos para mostrar. ")
        return
    print("\n LISTA DE EQUIPOS")
    for u in equipo:
        estado = "Activo" if u ["activo"] else "Inactivo"
        print (f"ID {u['ID']}: Nombre {u['Nombre']} Ciudad {u['Ciudad']} {estado}")
    print ("----------------\n")
    #BUSCAR ID
def buscar_equipo_por_id(equipos, id_equipo):
    for u in equipos:
        if u ["ID"] == id_equipo:
            return u 
    return None
    #ACTUALIZAR DATOS
def actualizar_datos(equipos):
    id_equipo = leer_int ("ID del equipo a actualizar: ")
    equipo_1 = buscar_equipo_por_id (equipos, id_equipo)
    ciudad_1 = ""
    if not equipo_1:
        print ("Usuario no encontrado. ")
        return
    print (f"Actualizando '{equipo_1 ['Nombre']}': ")
    nuevo_equipo = input("Nuevo equipo")
    if nuevo_equipo:
        equipo_1 ["Nombre"] = nuevo_equipo 
    nueva_ciudad = input("Nueva ciudad. ")
    if nueva_ciudad:
        ciudad_1 ["Ciudad"] = nueva_ciudad
    #ELIMINAR EQUIPO
def eliminar_equipo (equipos):
    id_equipo = leer_int ("ID del equipo a eliminar: ")
    equipo_1 = buscar_equipo_por_id (equipos, id_equipo)
    if not equipo_1:
        print("Equipo no encontrado: ")
        return
    equipos (equipo_1)
    print(f"Equipo ID {id_equipo} eliminado. ")
    
