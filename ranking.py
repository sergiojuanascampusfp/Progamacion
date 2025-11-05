# MENU RANKING
def menu_resultados_y_clasificacion ():
    while True:
        print ("""
 ===== MENU EQUIPOS ====
1. Registrar resultado
2. Clasificacion 
3. Estadisticas por equipo
4. Menú del módulo       
""")
        opcion = input ("Seleccione una opción: ")
        if opcion == "1":
            registrar_resultado()
        elif opcion == "2":
            clasificacion()
        elif opcion == "3":
            estadisticas_por_equipo()
        elif opcion == "4":
            print("Volviando al menu del principal...")
            return 
        else:
            print("Opcion no valida")
# FUNCIONES MENU RANKING
    # REGISTRAR RESULTADO
def registrar_resultado (ranking):
    id_partido = int(input("Introduce el id del partido que deseas: "))
    while True: 
        resultado = input ("Escribe el resultado del partido ")
        return 
print(f"Partido '{id_partido}'el resultado es {resultado}:")