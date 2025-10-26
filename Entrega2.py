#Definimos variables
articulos = []
usuarios = []
#Definimos funciones
def generar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

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
# FUNCIONES ARTÍCULOS
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

def buscar_articulo_por_id(articulos, id_busqueda):
    for a in articulos:
        if a["id"] == id_busqueda:
            return a
    return None

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

def eliminar_articulo(articulos):
    id_busqueda = leer_int("ID del artículo a eliminar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        print("Artículo no encontrado.")
        return
    articulos.remove(articulo)
    print(f"Artículo ID {id_busqueda} eliminado.")

def alternar_activo_articulo(articulos):
    id_busqueda = leer_int("ID del artículo a activar/desactivar: ")
    articulo = buscar_articulo_por_id(articulos, id_busqueda)
    if not articulo:
        print("Artículo no encontrado.")
        return
    articulo["activo"] = not articulo["activo"]
    estado = "activo" if articulo["activo"] else "inactivo"
    print(f"El artículo '{articulo['nombre']}' ahora está {estado}.")
# FUNCIONES USUARIOS
def crear_usuario(usuarios):
    nombre = input("Nombre del usuario: ")
    while True:
        email = input("Email: ")
        if "@" in email and "." in email:
            break
        print("Email no válido, debe contener '@' y '.'")
    nuevo = {
        "id": generar_id(usuarios),
        "nombre": nombre,
        "email": email,
        "activo": True
    }
    usuarios.append(nuevo)
    print(f"Usuario '{nombre}' creado con ID {nuevo['id']}.")

def listar_usuarios(usuarios, solo_activos=None):
    if solo_activos is True:
        filtrados = [u for u in usuarios if u["activo"]]
    elif solo_activos is False:
        filtrados = [u for u in usuarios if not u["activo"]]
    else:
        filtrados = usuarios

    if not filtrados:
        print("No hay usuarios para mostrar.")
        return

    print("\n--- LISTA DE USUARIOS ---")
    for u in filtrados:
        estado = "Activo" if u["activo"] else "Inactivo"
        print(f"ID {u['id']}: {u['nombre']} | Email: {u['email']} | {estado}")
    print("---------------------------\n")

def buscar_usuario_por_id(usuarios, id_busqueda):
    for u in usuarios:
        if u["id"] == id_busqueda:
            return u
    return None

def actualizar_usuario(usuarios):
    id_busqueda = leer_int("ID del usuario a actualizar: ")
    usuario = buscar_usuario_por_id(usuarios, id_busqueda)
    if not usuario:
        print("Usuario no encontrado.")
        return

    print(f"Actualizando '{usuario['nombre']}' (deje vacío para no cambiar):")
    nuevo_nombre = input("Nuevo nombre: ")
    if nuevo_nombre:
        usuario["nombre"] = nuevo_nombre

    nuevo_email = input("Nuevo email: ")
    if nuevo_email:
        if "@" in nuevo_email and "." in nuevo_email:
            usuario["email"] = nuevo_email
        else:
            print("Email no válido. No se modificó.")

    print("Usuario actualizado correctamente.")

def eliminar_usuario(usuarios):
    id_busqueda = leer_int("ID del usuario a eliminar: ")
    usuario = buscar_usuario_por_id(usuarios, id_busqueda)
    if not usuario:
        print("Usuario no encontrado.")
        return
    usuarios.remove(usuario)
    print(f"Usuario ID {id_busqueda} eliminado.")

def alternar_activo_usuario(usuarios):
    id_busqueda = leer_int("ID del usuario a activar/desactivar: ")
    usuario = buscar_usuario_por_id(usuarios, id_busqueda)
    if not usuario:
        print("Usuario no encontrado.")
        return
    usuario["activo"] = not usuario["activo"]
    estado = "activo" if usuario["activo"] else "inactivo"
    print(f"El usuario '{usuario['nombre']}' ahora está {estado}.")
# MENÚ USUARIOS
def menu_usuarios():
    opcion = ""
    while opcion != "7":
        print("""
========= MENÚ USUARIOS =========
1. Crear usuario
2. Listar usuarios
3. Buscar usuario por ID
4. Actualizar usuario
5. Eliminar usuario
6. Alternar activo/inactivo
7. Volver
================================
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_usuario(usuarios)
        elif opcion == "2":
            listar_usuarios(usuarios)
        elif opcion == "3":
            id_busqueda = leer_int("Ingrese ID a buscar: ")
            u = buscar_usuario_por_id(usuarios, id_busqueda)
            if u:
                print(f"\nID: {u['id']}\nNombre: {u['nombre']}\nEmail: {u['email']}\nActivo: {u['activo']}\n")
            else:
                print("Usuario no encontrado.")
        elif opcion == "4":
            actualizar_usuario(usuarios)
        elif opcion == "5":
            eliminar_usuario(usuarios)
        elif opcion == "6":
            alternar_activo_usuario(usuarios)
        elif opcion == "7":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida. Intente otra vez.")
# MENÚ PRINCIPAL
def menu_principal():
    opcion = ""
    while opcion != "3":
        print("""
========= MENÚ PRINCIPAL =========
1. Gestión de artículos
2. Gestión de usuarios
3. Salir
==================================
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            subop = ""
            while subop != "7":
                print("""
--- MENÚ ARTÍCULOS ---
1. Crear artículo
2. Listar artículos
3. Buscar artículo por ID
4. Actualizar artículo
5. Eliminar artículo
6. Alternar activo/inactivo
7. Volver
""")
                subop = input("Seleccione una opción: ")
                if subop == "1":
                    crear_articulo(articulos)
                elif subop == "2":
                    listar_articulos(articulos)
                elif subop == "3":
                    id_busqueda = leer_int("Ingrese ID a buscar: ")
                    a = buscar_articulo_por_id(articulos, id_busqueda)
                    if a:
                        print(f"\nID: {a['id']}\nNombre: {a['nombre']}\nPrecio: {a['precio']}\nStock: {a['stock']}\nActivo: {a['activo']}\n")
                    else:
                        print("Artículo no encontrado.")
                elif subop == "4":
                    actualizar_articulo(articulos)
                elif subop == "5":
                    eliminar_articulo(articulos)
                elif subop == "6":
                    alternar_activo_articulo(articulos)
                elif subop == "7":
                    print("Volviendo al menú principal...")
                else:
                    print("Opción no válida.")
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")
#Definimos la logica del programa
if __name__ == "__main__":
    menu_principal()
