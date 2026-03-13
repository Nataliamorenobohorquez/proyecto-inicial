# Sistema de Analisis de Rentabilidad
# Profitability Analysis System
# Programacion Estructurada - Primer Previo
# Estudiante: [Tu nombre]

import json  # para guardar y cargar datos / to save and load data
import os    # para limpiar pantalla / to clear screen

# variable global con la lista de productos
# global variable with the product list
productos = []


# funcion para limpiar la pantalla
# function to clear the screen
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


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

    ganancia = precio_venta - costo_mejor
    rentabilidad = (ganancia / costo_mejor) * 100

    return mejor, costo_mejor, ganancia, rentabilidad


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


# funcion para registrar un producto nuevo
# function to register a new product
def registrar_producto():
    global productos

    print("\n--- Registrar Producto / Register Product ---")

    nombre = input("Nombre del producto / Product name: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio / Name cannot be empty")
        return

    costo1 = pedir_numero("Costo proveedor 1 ($) / Supplier 1 cost: ")
    costo2 = pedir_numero("Costo proveedor 2 ($) / Supplier 2 cost: ")
    precio = pedir_numero("Precio de venta ($) / Sale price: ")

    # llamar a la funcion de calculo / call the calculation function
    mejor, costo_mejor, ganancia, rentabilidad = calcular(costo1, costo2, precio)

    # guardar el producto en la lista / save the product in the list
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

    print("\nProducto registrado! / Product registered!")
    print("Mejor proveedor / Best supplier:", mejor)
    print("Ganancia / Profit: $" + str(round(ganancia, 2)))
    print("Rentabilidad / Profitability:", str(round(rentabilidad, 2)) + "%")

    input("\nPresiona Enter para continuar...")


# funcion para mostrar todos los productos
# function to show all products
def ver_productos():
    print("\n--- Productos Registrados / Registered Products ---")

    if len(productos) == 0:
        print("No hay productos aun / No products yet")
        input("\nPresiona Enter para continuar...")
        return

    print()
    for i in range(len(productos)):
        p = productos[i]
        print(str(i + 1) + ". " + p["nombre"])
        print("   Mejor proveedor / Best supplier: " + p["mejor_prov"])
        print("   Ganancia / Profit: $" + str(round(p["ganancia"], 2)))
        print("   Rentabilidad / Profitability: " + str(round(p["rentabilidad"], 2)) + "%")
        print()

    # calcular promedio / calculate average
    total_rent = 0
    for p in productos:
        total_rent = total_rent + p["rentabilidad"]
    promedio = total_rent / len(productos)

    print("Total productos / Total products:", len(productos))
    print("Rentabilidad promedio / Average profitability:", str(round(promedio, 2)) + "%")

    input("\nPresiona Enter para continuar...")


# funcion para eliminar un producto
# function to delete a product
def eliminar_producto():
    global productos

    print("\n--- Eliminar Producto / Delete Product ---")

    if len(productos) == 0:
        print("No hay productos para eliminar / No products to delete")
        input("\nPresiona Enter para continuar...")
        return

    for i in range(len(productos)):
        print(str(i + 1) + ". " + productos[i]["nombre"])

    try:
        num = int(input("\nNumero a eliminar (0 para cancelar) / Number to delete (0 to cancel): "))
        if num == 0:
            return
        if num >= 1 and num <= len(productos):
            nombre = productos[num - 1]["nombre"]
            confirmar = input("Confirmas eliminar " + nombre + "? (s/n): ")
            if confirmar == "s":
                productos.pop(num - 1)
                print("Producto eliminado / Product deleted!")
            else:
                print("Cancelado / Cancelled")
        else:
            print("Numero invalido / Invalid number")
    except ValueError:
        print("Debes ingresar un numero / You must enter a number")

    input("\nPresiona Enter para continuar...")


# funcion para guardar los datos en un archivo json
# function to save data to a json file
def guardar_datos():
    print("\n--- Guardar Datos / Save Data ---")

    if len(productos) == 0:
        print("No hay datos para guardar / No data to save")
        input("\nPresiona Enter para continuar...")
        return

    try:
        archivo = open("rentabilidad.json", "w", encoding="utf-8")
        json.dump(productos, archivo, ensure_ascii=False, indent=2)
        archivo.close()
        print("Datos guardados en rentabilidad.json / Data saved to rentabilidad.json")
    except Exception as e:
        print("Error al guardar / Error saving:", e)

    input("\nPresiona Enter para continuar...")


# funcion para cargar datos desde un archivo json
# function to load data from a json file
def cargar_datos():
    global productos

    print("\n--- Cargar Datos / Load Data ---")

    try:
        archivo = open("rentabilidad.json", "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        productos = datos
        print("Datos cargados! / Data loaded! Total:", len(productos))
    except FileNotFoundError:
        print("No se encontro el archivo / File not found")
    except Exception as e:
        print("Error al cargar / Error loading:", e)

    input("\nPresiona Enter para continuar...")


# funcion principal con el menu
# main function with the menu
def main():
    # ciclo principal que mantiene el programa activo
    # main loop that keeps the program running
    while True:
        limpiar()

        print("=========================================")
        print("  SISTEMA DE ANALISIS DE RENTABILIDAD")
        print("  Profitability Analysis System")
        print("=========================================")
        print("  Productos: " + str(len(productos)))
        print("-----------------------------------------")
        print("  1. Registrar producto / Register product")
        print("  2. Ver productos / View products")
        print("  3. Eliminar producto / Delete product")
        print("  4. Guardar datos / Save data")
        print("  5. Cargar datos / Load data")
        print("  6. Salir / Exit")
        print("-----------------------------------------")

        opcion = input("Elige una opcion / Choose an option: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            guardar_datos()
        elif opcion == "5":
            cargar_datos()
        elif opcion == "6":
            print("Hasta luego! / Goodbye!")
            break
        else:
            print("Opcion invalida, elige entre 1 y 6 / Invalid option, choose between 1 and 6")
            input("Presiona Enter para continuar...")


# punto de entrada del programa / program entry point
main()
