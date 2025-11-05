# Importacion de librerias 
from utiles import generar_id, leer_int 
# MENU GESTION DE EQUIPOS
def menu_calendario_de_partidos ():
    while True:
        print ("""
 ===== MENU EQUIPOS ====
1. Crear partido
2. Listrar partidos
3. Reprogramar
4. Eliminar partido
5. Menú del módulo       
""")
        opcion = input ("Seleccione una opción: ")
        if opcion == "1":
            crear_partido()
        elif opcion == "2":
            listar_partidos()
        elif opcion == "3":
            reprogramar()
        elif opcion == "4":
            eliminar_partido()
        elif opcion == "5":
            print("Volviando al menu del principal...")
            return 
        else:
            print("Opcion no valida")
# FUNCIONES MENU CALENDARIO
    #CREAR PARTIDO
def crear_partido(calendario):
    jornada = int(input ("Di el número de la jornada: "))
    local = input("Introduce el nombre del equipo local: ")
    visitante = input("Introduce el nombre del equipo visitante: ")
    nuevo= {
        "ID": generar_id (calendario),
        "jornada": jornada,
        "local": local,
        "visitante": visitante,
        "jugado": False,
        "resultado": None
    }
    calendario(nuevo)
    #LISTAR PARTIDOS
def listar_partidos(calendario, solo_activos=None):
    if solo_activos is True:
        partido = [u for u in calendario if u ["Activo"]]
    elif solo_activos is False:
        partido = [u for u in calendario if not u ["Inactivo"]]
    else:
        partido = calendario
    if not partido:
        print ("No hay partidos para mostrar: ")
        return
    print("\n LISTA DE CALENDARIO")
    for u in partido:
        estado = "Activo" if u ["Activo"] else "Inactivo"
        print(f"ID {u['ID']}: Jornada {u['Jornada']} Local {u['Local']} Visitante {u['Visitante']} Jugado {u[False]} Resultado {u[None]} {estado}")
    print("---------\n")
    #REPROGRAMAR
def reprogramar(calendario):
    id_partido = int(input("Introduce el ID del partido a reprogramar: "))
    for partido in calendario:
        if partido["ID"] == id_partido:
            if partido["jugado"] == False:
                nueva_fecha = input("Introduce la nueva fecha (DD/MM/AAAA): ")
                nueva_hora = input("Introduce la nueva hora (HH:MM): ")
                partido["fecha"] = nueva_fecha
                partido["hora"] = nueva_hora
                print("Partido reprogramado correctamente.")
            else:
                print("No se puede reprogramar un partido ya jugado.")
            return
    print("No se encontró un partido con ese ID.")
    #ELIMINAR PARTIDO
def eliminar_partido(calendario):
    id_partido = int(input("Introduce el ID del partido a eliminar: "))
    for partido in calendario:
        if partido["ID"] == id_partido:
            if partido["jugado"] == False:
                calendario(partido)
                print("Partido eliminado correctamente.")
            else:
                print("No se puede eliminar un partido ya jugado.")
            return
    print("No se encontró un partido con ese ID.")
