#Definimos variables
articulos = []
usuarios = []
ventas = []          # Lista de ventas
carrito_actual = []  # Lista de tuplas: (articulo_id, cantidad)
usuario_activo = None
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
#FUNCIONES VENTAS
# Seleccionar usuario activo
def seleccionar_usuario_activo(usuarios):
    global usuario_activo
    listar_usuarios(usuarios, solo_activos=True)
    id_usuario = leer_int("Ingrese ID del usuario para activar: ")
    usuario = buscar_usuario_por_id(usuarios, id_usuario)
    if usuario and usuario["activo"]:
        usuario_activo = id_usuario
        print(f"Usuario activo: {usuario['nombre']}")
    else:
        print("Usuario no encontrado o inactivo.")
        usuario_activo = None

# Añadir artículo al carrito
def anadir_al_carrito(carrito, articulos):
    if usuario_activo is None:
        print("Debe seleccionar un usuario activo primero.")
        return
    listar_articulos(articulos, solo_activos=True)
    id_art = leer_int("Ingrese ID del artículo a añadir: ")
    articulo = buscar_articulo_por_id(articulos, id_art)
    if not articulo or not articulo["activo"]:
        print("Artículo no encontrado o inactivo.")
        return
    cantidad = leer_int("Cantidad: ", minimo=1)
    if cantidad > articulo["stock"]:
        print(f"No hay suficiente stock. Stock disponible: {articulo['stock']}")
        return
    # Si ya está en el carrito, sumar cantidad
    for i, (art_id, cant) in enumerate(carrito):
        if art_id == id_art:
            if cant + cantidad > articulo["stock"]:
                print(f"No se puede agregar. Stock máximo: {articulo['stock']}")
                return
            carrito[i] = (art_id, cant + cantidad)
            print("Cantidad actualizada en el carrito.")
            return
    carrito.append((id_art, cantidad))
    print(f"Artículo '{articulo['nombre']}' añadido al carrito.")

# Quitar artículo del carrito
def quitar_del_carrito(carrito):
    if not carrito:
        print("Carrito vacío.")
        return
    id_art = leer_int("Ingrese ID del artículo a quitar: ")
    for i, (art_id, cant) in enumerate(carrito):
        if art_id == id_art:
            carrito.pop(i)
            print("Artículo eliminado del carrito.")
            return
    print("Artículo no encontrado en el carrito.")

# Ver carrito y calcular total
def calcular_total_carrito(carrito, articulos):
    total = 0
    print("\n--- CARRITO ---")
    for art_id, cant in carrito:
        articulo = buscar_articulo_por_id(articulos, art_id)
        if articulo:
            subtotal = cant * articulo["precio"]
            total += subtotal
            print(f"{articulo['nombre']} | Cantidad: {cant} | Subtotal: {subtotal:.2f}")
    print(f"TOTAL: {total:.2f}\n")
    return total

# Confirmar compra
def confirmar_compra(carrito, articulos, usuario_activo, ventas):
    if usuario_activo is None:
        print("No hay usuario activo.")
        return
    if not carrito:
        print("Carrito vacío.")
        return
    # Verificar stock
    for art_id, cant in carrito:
        articulo = buscar_articulo_por_id(articulos, art_id)
        if cant > articulo["stock"]:
            print(f"Stock insuficiente para {articulo['nombre']}. Compra cancelada.")
            return
    # Crear venta y restar stock
    venta_items = []
    total = 0
    for art_id, cant in carrito:
        articulo = buscar_articulo_por_id(articulos, art_id)
        venta_items.append((art_id, cant, articulo["precio"]))
        articulo["stock"] -= cant
        total += cant * articulo["precio"]
    venta = {
        "id_venta": generar_id(ventas),
        "usuario_id": usuario_activo,
        "items": venta_items,
        "total": total
    }
    ventas.append(venta)
    carrito.clear()
    print(f"Compra realizada. Total: {total:.2f}")

# Historial de ventas por usuario
def historial_ventas_por_usuario(ventas, usuario_id):
    filtradas = [v for v in ventas if v["usuario_id"] == usuario_id]
    if not filtradas:
        print("No hay ventas para este usuario.")
        return
    print(f"\n--- HISTORIAL DE VENTAS USUARIO {usuario_id} ---")
    for v in filtradas:
        print(f"Venta ID {v['id_venta']} | Total: {v['total']:.2f}")
        for art_id, cant, precio in v["items"]:
            print(f"   Artículo ID {art_id} | Cantidad: {cant} | Precio unitario: {precio}")
    print("----------------------------------------\n")

# Vaciar carrito
def vaciar_carrito(carrito):
    carrito.clear()
    print("Carrito vaciado.")
def menu_articulos():
    opcion = ""
    while opcion != "7":
        print("""
========= MENÚ ARTÍCULOS =========
1. Crear artículo
2. Listar artículos
3. Buscar artículo por ID
4. Actualizar artículo
5. Eliminar artículo
6. Alternar activo/inactivo
7. Volver
=================================
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_articulo(articulos)
        elif opcion == "2":
            listar_articulos(articulos)
        elif opcion == "3":
            id_busqueda = leer_int("Ingrese ID a buscar: ")
            a = buscar_articulo_por_id(articulos, id_busqueda)
            if a:
                estado = "Activo" if a["activo"] else "Inactivo"
                print(f"\nID: {a['id']}\nNombre: {a['nombre']}\nPrecio: {a['precio']}\nStock: {a['stock']}\nEstado: {estado}\n")
            else:
                print("Artículo no encontrado.")
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")
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
#MENU VENTAS
def menu_ventas():
    opcion = ""
    while opcion != "8":
        print("""
========= MENÚ VENTAS / CARRITO =========
1. Seleccionar usuario activo
2. Añadir artículo al carrito
3. Quitar artículo del carrito
4. Ver carrito
5. Confirmar compra
6. Historial de ventas por usuario
7. Vaciar carrito
8. Volver
========================================
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            seleccionar_usuario_activo(usuarios)
        elif opcion == "2":
            anadir_al_carrito(carrito_actual, articulos)
        elif opcion == "3":
            quitar_del_carrito(carrito_actual)
        elif opcion == "4":
            calcular_total_carrito(carrito_actual, articulos)
        elif opcion == "5":
            confirmar_compra(carrito_actual, articulos, usuario_activo, ventas)
        elif opcion == "6":
            if usuario_activo is None:
                print("Seleccione primero un usuario activo.")
            else:
                historial_ventas_por_usuario(ventas, usuario_activo)
        elif opcion == "7":
            vaciar_carrito(carrito_actual)
        elif opcion == "8":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")
# MENÚ PRINCIPAL
def menu_principal():
    opcion = ""
    while opcion != "4":
        print("""
========= MENÚ PRINCIPAL =========
1. Gestión de artículos
2. Gestión de usuarios
3. Ventas / Carrito
4. Salir
==================================
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_articulos()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")

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
