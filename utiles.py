# Funciones principales
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
