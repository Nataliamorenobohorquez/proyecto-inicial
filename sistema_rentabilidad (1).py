# sistema_rentabilidad.py
# Sistema de Analisis de Rentabilidad - Avance 5
# Profitability Analysis System - Advance 5
# Unidad 2: Tratamiento de cadenas / String treatment
# Programacion Estructurada - Primer Previo

import json  # para guardar y cargar datos / to save and load data
import os    # para limpiar pantalla / to clear screen

# variable global con la lista de productos
# global variable with the product list
productos = []


# =============================================================================
# FUNCIONES UTILITARIAS / UTILITY FUNCTIONS
# =============================================================================

# funcion para limpiar la pantalla
# function to clear the screen
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


# funcion para estandarizar texto: quita espacios y pasa a minusculas
# function to standardize text: removes spaces and converts to lowercase
def estandarizar_dato(texto_entrada):
    return texto_entrada.strip().lower()


# funcion para capitalizar el nombre correctamente
# function to properly capitalize the name
def formatear_nombre(texto_entrada):
    return texto_entrada.strip().title()


# funcion para pedir un numero valido al usuario
# function to ask the user for a valid number
def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("  El valor debe ser mayor a 0 / Value must be greater than 0")
            else:
                return valor
        except ValueError:
            print("  Debes ingresar un numero / You must enter a number")


# =============================================================================
# LOGICA DE NEGOCIO / BUSINESS LOGIC
# =============================================================================

# funcion para calcular la rentabilidad de un producto
# function to calculate the profitability of a product
def calcular(costo1, costo2, precio_venta):
    # comparar cual proveedor es mas barato / compare which supplier is cheaper
    if costo1 < costo2:
        mejor = "Proveedor 1"
        costo_mejor = costo1
    elif costo2 < costo1:
        mejor = "Proveedor 2"
        costo_mejor = costo2
    else:
        mejor = "Empate"
        costo_mejor = costo1

    # calcular ganancia y rentabilidad / calculate profit and profitability
    ganancia = precio_venta - costo_mejor
    rentabilidad = (ganancia / costo_mejor) * 100

    return mejor, costo_mejor, ganancia, rentabilidad


# =============================================================================
# MODULO 1 - REGISTRAR PRODUCTO / REGISTER PRODUCT
# =============================================================================

def registrar_producto():
    global productos

    print("\n--- Registrar Producto / Register Product ---")

    # limpiar y formatear nombre con strip() y title()
    # clean and format name with strip() and title()
    nombre_raw = input("Nombre del producto / Product name: ")
    nombre = formatear_nombre(nombre_raw)

    if nombre == "":
        print("El nombre no puede estar vacio / Name cannot be empty")
        return

    costo1 = pedir_numero("Costo proveedor 1 ($) / Supplier 1 cost: ")
    costo2 = pedir_numero("Costo proveedor 2 ($) / Supplier 2 cost: ")
    precio = pedir_numero("Precio de venta ($)   / Sale price      : ")

    # llamar funcion de calculo / call calculation function
    mejor, costo_mejor, ganancia, rentabilidad = calcular(costo1, costo2, precio)

    # guardar en lista global / save in global list
    producto = {
        "nombre": nombre,
        "costo1": costo1,
        "costo2": costo2,
        "precio_venta": precio,
        "mejor_prov": mejor,
        "mejor_costo": costo_mejor,
        "ganancia": ganancia,
        "rentabilidad": rentabilidad
    }
    productos.append(producto)

    # mostrar resultado con f-strings alineados / show result with aligned f-strings
    print()
    print(f"  {'-'*40}")
    print(f"  {'Nombre / Name':<28} {nombre}")
    print(f"  {'Mejor proveedor / Best supplier':<28} {mejor}")
    print(f"  {'Costo mejor / Best cost':<28} ${costo_mejor:.2f}")
    print(f"  {'Ganancia / Profit':<28} ${ganancia:.2f}")
    print(f"  {'Rentabilidad / Profitability':<28} {rentabilidad:.2f}%")
    print(f"  {'-'*40}")

    input("\nPresiona Enter para continuar / Press Enter to continue...")


# =============================================================================
# MODULO 2 - VER PRODUCTOS / VIEW PRODUCTS
# =============================================================================

def ver_productos():
    print("\n--- Productos Registrados / Registered Products ---")

    if len(productos) == 0:
        print("No hay productos aun / No products yet")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # tabla alineada con f-strings y ancho fijo
    # aligned table with f-strings and fixed width
    print()
    print(f"  {'#':<4} {'Nombre / Name':<22} {'Mejor Prov.':<14} {'Ganancia':>10} {'Rentab.':>10}")
    print("  " + "-" * 62)

    for i in range(len(productos)):
        p = productos[i]
        nombre_corto = p["nombre"][:20]
        print(f"  {i+1:<4} {nombre_corto:<22} {p['mejor_prov']:<14} "
              f"${p['ganancia']:>8.2f} {p['rentabilidad']:>8.2f}%")

    print("  " + "-" * 62)

    # calcular promedio / calculate average
    total_rent = 0
    for p in productos:
        total_rent = total_rent + p["rentabilidad"]
    promedio = total_rent / len(productos)

    print(f"\n  {'Total productos / Total products':<35} {len(productos)}")
    print(f"  {'Rentabilidad promedio / Avg profitability':<35} {promedio:.2f}%")

    input("\nPresiona Enter para continuar / Press Enter to continue...")


# =============================================================================
# MODULO 3 - BUSCAR PRODUCTO / SEARCH PRODUCT
# =============================================================================

def buscar_producto():
    print("\n--- Buscar Producto / Search Product ---")

    if len(productos) == 0:
        print("No hay productos para buscar / No products to search")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # estandarizar busqueda con strip() y lower() para ignorar mayusculas
    # standardize search with strip() and lower() to ignore uppercase
    termino_raw = input("Nombre a buscar / Name to search: ")
    termino = estandarizar_dato(termino_raw)

    print(f"\n  Buscando / Searching: '{termino}'...")
    print()

    # comparar en minusculas para no depender de mayusculas
    # compare in lowercase to not depend on uppercase
    encontrados = []
    for p in productos:
        if termino in estandarizar_dato(p["nombre"]):
            encontrados.append(p)

    if len(encontrados) == 0:
        print(f"  No se encontro / Not found: '{termino}'")
    else:
        print(f"  {'Nombre / Name':<22} {'Mejor Prov.':<14} {'Ganancia':>10} {'Rentab.':>10}")
        print("  " + "-" * 58)
        for p in encontrados:
            print(f"  {p['nombre']:<22} {p['mejor_prov']:<14} "
                  f"${p['ganancia']:>8.2f} {p['rentabilidad']:>8.2f}%")
        print(f"\n  Resultados / Results: {len(encontrados)}")

    input("\nPresiona Enter para continuar / Press Enter to continue...")


# =============================================================================
# MODULO 4 - ELIMINAR PRODUCTO / DELETE PRODUCT
# =============================================================================

def eliminar_producto():
    global productos

    print("\n--- Eliminar Producto / Delete Product ---")

    if len(productos) == 0:
        print("No hay productos para eliminar / No products to delete")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    for i in range(len(productos)):
        print(str(i + 1) + ". " + productos[i]["nombre"])

    try:
        num = int(input("\nNumero a eliminar (0 cancelar) / Number to delete (0 cancel): "))
        if num == 0:
            return
        if num >= 1 and num <= len(productos):
            nombre = productos[num - 1]["nombre"]
            confirmar = input(f"Confirmas eliminar '{nombre}'? (s/n): ")
            # estandarizar respuesta / standardize response
            if estandarizar_dato(confirmar) == "s":
                productos.pop(num - 1)
                print("Producto eliminado / Product deleted!")
            else:
                print("Cancelado / Cancelled")
        else:
            print("Numero invalido / Invalid number")
    except ValueError:
        print("Debes ingresar un numero / You must enter a number")

    input("\nPresiona Enter para continuar / Press Enter to continue...")


# =============================================================================
# MODULO 5 - GUARDAR DATOS / SAVE DATA
# =============================================================================

def guardar_datos():
    print("\n--- Guardar Datos / Save Data ---")

    if len(productos) == 0:
        print("No hay datos para guardar / No data to save")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    try:
        archivo = open("rentabilidad.json", "w", encoding="utf-8")
        json.dump(productos, archivo, ensure_ascii=False, indent=2)
        archivo.close()
        print(f"  {'Archivo / File':<30} rentabilidad.json")
        print(f"  {'Registros / Records':<30} {len(productos)}")
    except Exception as e:
        print("Error al guardar / Error saving:", e)

    input("\nPresiona Enter para continuar / Press Enter to continue...")


# =============================================================================
# MODULO 6 - CARGAR DATOS / LOAD DATA
# =============================================================================

def cargar_datos():
    global productos

    print("\n--- Cargar Datos / Load Data ---")

    try:
        archivo = open("rentabilidad.json", "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        productos = datos
        print(f"  Datos cargados / Data loaded: {len(productos)} producto(s)")
    except FileNotFoundError:
        print("No se encontro el archivo / File not found")
    except Exception as e:
        print("Error al cargar / Error loading:", e)

    input("\nPresiona Enter para continuar / Press Enter to continue...")


# =============================================================================
# MENU PRINCIPAL / MAIN MENU
# =============================================================================

def main():
    # ciclo principal que mantiene el programa activo
    # main loop that keeps the program running
    while True:
        limpiar()

        print("=" * 45)
        print(f"  {'SISTEMA DE ANALISIS DE RENTABILIDAD':^41}")
        print(f"  {'Profitability Analysis System':^41}")
        print("=" * 45)
        print(f"  {'Productos / Products':<30} {len(productos)}")
        print("-" * 45)
        print(f"  1. Registrar producto / Register product")
        print(f"  2. Ver productos      / View products")
        print(f"  3. Buscar producto    / Search product")
        print(f"  4. Eliminar producto  / Delete product")
        print(f"  5. Guardar datos      / Save data")
        print(f"  6. Cargar datos       / Load data")
        print(f"  7. Salir              / Exit")
        print("-" * 45)

        opcion = input("Elige una opcion / Choose an option: ")

        # navegar al modulo / navigate to module
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            guardar_datos()
        elif opcion == "6":
            cargar_datos()
        elif opcion == "7":
            print("Hasta luego! / Goodbye!")
            break
        else:
            # opcion invalida / invalid option
            print("Opcion invalida, elige entre 1 y 7 / Invalid option, choose 1 to 7")
            input("Presiona Enter para continuar / Press Enter to continue...")


# punto de entrada / entry point
main()
