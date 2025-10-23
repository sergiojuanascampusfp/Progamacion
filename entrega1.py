# Definimos variables
articulos = []

    # Opción A: diccionario de ejemplo
diccionario = {"id": 1, "nombre": "Ratón", "precio": 12.5, "stock": 20, "activo": True}
    # Lista con las opciones del menú (solo para mostrar)
menu_opciones = [
    "1.- Crear artículo",
    "2.- Listar artículos",
    "3.- Buscar artículo por ID",
    "4.- Actualizar artículo",
    "5.- Eliminar artículo",
    "6.- Alternar activo/inactivo",
    "7.- Salir"
]
# Definimos funciones
    # Generar nuevo ID
def generar_id(articulos):
    if not articulos:
        return 1
    return max(a["id"] for a in articulos) + 1

    # Crear artículo
def crear_articulo(articulos):
    nombre = input("Nombre del artículo: ")
    precio = leer_float("Precio: ", minimo=0.01)
    stock = leer_int("Stock: ", minimo=0)
    nuevo = {
        "id": generar_id(articulos),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    }
    articulos.append(nuevo)
    print(f"Artículo '{nombre}' creado con ID {nuevo['id']}.")

    # Listar artículos
def listar_articulos(articulos, solo_activos=None):
    if solo_activos is True:
        filtrados = [a for a in articulos if a["activo"]]
    elif solo_activos is False:
        filtrados = [a for a in articulos if not a["activo"]]
    else:
        filtrados = articulos

    if not filtrados:
        print("No hay artículos para mostrar.")
        return

    print("\n--- LISTA DE ARTÍCULOS ---")
    for a in filtrados:
        estado = "Activo" if a["activo"] else "Inactivo"
        print(f"ID {a['id']}: {a['nombre']} | Precio: {a['precio']} | Stock: {a['stock']} | {estado}")
    print("---------------------------\n")

    # Buscar artículo por ID
def buscar_articulo_por_id(articulos, id_busqueda):
    for a in articulos:
        if a["id"] == id_busqueda:
            return a
    return None

    # Actualizar artículo
def actualizar_articulo(articulos):
    id_busqueda = leer_int("ID del artículo a actualizar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        print("Artículo no encontrado.")
        return

    print(f"Actualizando '{articulo['nombre']}' (deje vacío para no cambiar):")
    nuevo_nombre = input("Nuevo nombre: ")
    if nuevo_nombre:
        articulo["nombre"] = nuevo_nombre

    nuevo_precio = input("Nuevo precio: ")
    if nuevo_precio:
        try:
            articulo["precio"] = float(nuevo_precio)
        except ValueError:
            print("Precio no válido. No se modificó.")

    nuevo_stock = input("Nuevo stock: ")
    if nuevo_stock:
        try:
            articulo["stock"] = int(nuevo_stock)
        except ValueError:
            print("Stock no válido. No se modificó.")

    print("Artículo actualizado correctamente.")

    # Eliminar artículo
def eliminar_articulo(articulos):
    id_busqueda = leer_int("ID del artículo a eliminar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        print("Artículo no encontrado.")
        return
    articulos.remove(articulo)
    print(f"Artículo ID {id_busqueda} eliminado.")

    # Alternar activo/inactivo
def alternar_activo(articulos):
    id_busqueda = leer_int("ID del artículo a activar/desactivar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        print("Artículo no encontrado.")
        return
    articulo["activo"] = not articulo["activo"]
    estado = "activo" if articulo["activo"] else "inactivo"
    print(f"El artículo '{articulo['nombre']}' ahora está {estado}.")

    # Leer float con validación
def leer_float(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ser mayor o igual que {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número decimal.")

    # Leer int con validación
def leer_int(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ser mayor o igual que {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    # Menú principal 
def menu_tienda_online():
    print("""
========= MENÚ PRINCIPAL =========
1. Crear artículo
2. Listar artículos
3. Buscar artículo por ID
4. Actualizar artículo
5. Eliminar artículo
6. Alternar activo/inactivo
7. Salir
==================================
""")
    return input("Seleccione una opción: ")


#Desarrollamos lógica del programa
def main():
    articulos = []
    opcion = ""
    while opcion != "7":
        opcion = menu_tienda_online()
        match opcion:
            case "1":
                crear_articulo(articulos)
            case "2":
                listar_articulos(articulos)
            case "3":
                id_busqueda = leer_int("Ingrese ID a buscar: ")
                b = buscar_articulo_por_id(articulos, id_busqueda)
                if b:
                    print(f"\nID: {b['id']}\nNombre: {b['nombre']}\nPrecio: {b['precio']}\nStock: {b['stock']}\nActivo: {b['activo']}\n")
                else:
                    print("Artículo no encontrado.")
            case "4":
                actualizar_articulo(articulos)
            case "5":
                eliminar_articulo(articulos)
            case "6":
                alternar_activo(articulos)
            case "7":
                print("Saliendo del programa...")
            case _:
                print("Opción no válida. Intente otra vez.")
# Ejecutar programa
if __name__ == "__main__":
    main()


