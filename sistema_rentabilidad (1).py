# =============================================================================
# sistema_rentabilidad.py
# Sistema de Analisis de Rentabilidad - Avance 6
# Profitability Analysis System - Advance 6
# -----------------------------------------------------------------------------
# Descripcion / Description:
#   Sistema que permite registrar productos, comparar costos entre dos
#   proveedores y calcular automaticamente la ganancia y rentabilidad.
#   Implementa almacenamiento dinamico con listas, operaciones CRUD
#   (agregar con .append y consultar con ciclo for), busqueda con
#   tratamiento de cadenas, y bilingüismo en encabezados y confirmaciones.
#
#   System that allows registering products, comparing costs between two
#   suppliers and automatically calculating profit and profitability.
#   Implements dynamic storage with lists, CRUD operations (add with
#   .append and query with for loop), string-based search, and bilingual
#   headers and confirmation messages.
# -----------------------------------------------------------------------------
# Avance 6: Implementacion de listas para almacenamiento dinamico de datos
# Advance 6: Implementation of lists for dynamic data storage
# -----------------------------------------------------------------------------
# Asignatura / Subject : Programacion Estructurada
# Docente / Teacher    : Robinson Damian Gomez Sanchez
# =============================================================================

import json  # modulo para guardar y leer archivos JSON / module to save and read JSON files
import os    # modulo para limpiar la pantalla del sistema / module to clear system screen

# =============================================================================
# VARIABLES GLOBALES / GLOBAL VARIABLES
# =============================================================================

# lista que almacena todos los productos registrados como diccionarios
# list that stores all registered products as dictionaries
productos = []

# contador que asigna un ID unico a cada producto nuevo
# counter that assigns a unique ID to each new product
contador_id = 9  # empieza en 9 porque ya hay 8 datos precargados / starts at 9 because 8 are preloaded

# =============================================================================
# DATOS PRECARGADOS / PRELOADED DATA
# -----------------------------------------------------------------------------
# Se cargan 8 productos de ejemplo al iniciar el programa para que el sistema
# no inicie vacio y se pueda probar de inmediato.
# 8 example products are loaded at startup so the system is not empty
# and can be tested immediately.
# =============================================================================

productos = [
    {
        "id":           1,
        "nombre":       "Auriculares Bluetooth",
        "costo1":       80000.0,
        "costo2":       95000.0,
        "precio_venta": 150000.0,
        "mejor_prov":   "Proveedor 1",
        "mejor_costo":  80000.0,
        "ganancia":     70000.0,
        "rentabilidad": 87.5,
        "disponible":   True
    },
    {
        "id":           2,
        "nombre":       "Teclado Mecanico",
        "costo1":       120000.0,
        "costo2":       105000.0,
        "precio_venta": 200000.0,
        "mejor_prov":   "Proveedor 2",
        "mejor_costo":  105000.0,
        "ganancia":     95000.0,
        "rentabilidad": 90.48,
        "disponible":   True
    },
    {
        "id":           3,
        "nombre":       "Mouse Gamer",
        "costo1":       45000.0,
        "costo2":       45000.0,
        "precio_venta": 90000.0,
        "mejor_prov":   "Empate",
        "mejor_costo":  45000.0,
        "ganancia":     45000.0,
        "rentabilidad": 100.0,
        "disponible":   False
    },
    {
        "id":           4,
        "nombre":       "Monitor 24 Pulgadas",
        "costo1":       550000.0,
        "costo2":       490000.0,
        "precio_venta": 780000.0,
        "mejor_prov":   "Proveedor 2",
        "mejor_costo":  490000.0,
        "ganancia":     290000.0,
        "rentabilidad": 59.18,
        "disponible":   True
    },
    {
        "id":           5,
        "nombre":       "Camara Web Full Hd",
        "costo1":       95000.0,
        "costo2":       110000.0,
        "precio_venta": 180000.0,
        "mejor_prov":   "Proveedor 1",
        "mejor_costo":  95000.0,
        "ganancia":     85000.0,
        "rentabilidad": 89.47,
        "disponible":   True
    },
    {
        "id":           6,
        "nombre":       "Disco Duro Externo 1Tb",
        "costo1":       160000.0,
        "costo2":       148000.0,
        "precio_venta": 260000.0,
        "mejor_prov":   "Proveedor 2",
        "mejor_costo":  148000.0,
        "ganancia":     112000.0,
        "rentabilidad": 75.68,
        "disponible":   True
    },
    {
        "id":           7,
        "nombre":       "Silla Ergonomica",
        "costo1":       320000.0,
        "costo2":       340000.0,
        "precio_venta": 580000.0,
        "mejor_prov":   "Proveedor 1",
        "mejor_costo":  320000.0,
        "ganancia":     260000.0,
        "rentabilidad": 81.25,
        "disponible":   True
    },
    {
        "id":           8,
        "nombre":       "Memoria Ram 16Gb",
        "costo1":       185000.0,
        "costo2":       175000.0,
        "precio_venta": 310000.0,
        "mejor_prov":   "Proveedor 2",
        "mejor_costo":  175000.0,
        "ganancia":     135000.0,
        "rentabilidad": 77.14,
        "disponible":   False
    }
]
# NOTA: Los datos precargados sirven para demostrar el sistema sin necesidad
# de registrar productos manualmente al iniciar.
# NOTE: Preloaded data is used to demonstrate the system without needing
# to register products manually at startup.


# =============================================================================
# FUNCIONES UTILITARIAS / UTILITY FUNCTIONS
# =============================================================================

def limpiar():
    # os.system ejecuta un comando del sistema operativo
    # os.system executes an operating system command
    # 'cls' limpia en Windows, 'clear' limpia en Mac/Linux
    # 'cls' clears on Windows, 'clear' clears on Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')
# NOTA: Esta funcion limpia la pantalla antes de mostrar el menu.
# NOTE: This function clears the screen before showing the menu.


def estandarizar_dato(texto_entrada):
    # .strip() elimina espacios al inicio y al final del texto
    # .strip() removes spaces at the beginning and end of the text
    # .lower() convierte todo el texto a minusculas
    # .lower() converts all text to lowercase
    return texto_entrada.strip().lower()
# NOTA: Se usa para comparar textos sin importar mayusculas o espacios.
# NOTE: Used to compare texts regardless of uppercase or spaces.


def formatear_nombre(texto_entrada):
    # .strip() quita espacios innecesarios / removes unnecessary spaces
    # .title() pone la primera letra de cada palabra en mayuscula
    # .title() capitalizes the first letter of each word
    return texto_entrada.strip().title()
# NOTA: Se usa para guardar los nombres de productos con formato correcto.
# NOTE: Used to save product names with correct formatting.


def pedir_numero(mensaje):
    # este ciclo while se repite hasta que el usuario ingrese un numero valido
    # this while loop repeats until the user enters a valid number
    while True:
        try:
            # float() convierte el texto del usuario a numero decimal
            # float() converts the user's text to a decimal number
            valor = float(input(mensaje))

            # validacion: el valor debe ser mayor a cero
            # validation: the value must be greater than zero
            if valor <= 0:
                print("  El valor debe ser mayor a 0 / Value must be greater than 0")
            else:
                return valor  # retorna el valor valido / returns the valid value

        except ValueError:
            # ValueError ocurre cuando el usuario escribe letras en vez de numeros
            # ValueError occurs when the user types letters instead of numbers
            print("  Debes ingresar un numero / You must enter a number")
# NOTA: Esta funcion garantiza que nunca se guarde un valor invalido.
# Si el usuario escribe mal, el programa avisa y vuelve a preguntar sin cerrarse.
# NOTE: This function ensures an invalid value is never saved.
# If the user types wrong, the program warns and asks again without closing.


# =============================================================================
# LOGICA DE NEGOCIO / BUSINESS LOGIC
# =============================================================================

def calcular(costo1, costo2, precio_venta):
    # PASO 1: comparar los dos costos para saber cual proveedor conviene mas
    # STEP 1: compare the two costs to know which supplier is best
    if costo1 < costo2:
        # proveedor 1 es mas barato / supplier 1 is cheaper
        mejor = "Proveedor 1"
        costo_mejor = costo1

    elif costo2 < costo1:
        # proveedor 2 es mas barato / supplier 2 is cheaper
        mejor = "Proveedor 2"
        costo_mejor = costo2

    else:
        # ambos tienen el mismo costo / both have the same cost
        mejor = "Empate"
        costo_mejor = costo1

    # PASO 2: calcular la ganancia restando el mejor costo al precio de venta
    # STEP 2: calculate profit by subtracting best cost from sale price
    ganancia = precio_venta - costo_mejor

    # PASO 3: calcular el porcentaje de rentabilidad
    # STEP 3: calculate the profitability percentage
    # Formula: (ganancia / costo) * 100
    # Example: (70000 / 80000) * 100 = 87.5%
    rentabilidad = (ganancia / costo_mejor) * 100

    # retorna 4 valores a la vez / returns 4 values at once
    return mejor, costo_mejor, ganancia, rentabilidad
# NOTA: Esta es la funcion mas importante del sistema. Contiene toda la
# logica de negocio: comparacion de proveedores y calculos matematicos.
# Recibe 3 parametros y retorna 4 resultados.
# NOTE: This is the most important function in the system. It contains all
# the business logic: supplier comparison and mathematical calculations.
# It receives 3 parameters and returns 4 results.


# =============================================================================
# MODULO 1 - REGISTRAR PRODUCTO / REGISTER PRODUCT
# =============================================================================

def registrar_producto():
    # global permite modificar las variables declaradas fuera de la funcion
    # global allows modifying variables declared outside the function
    global productos, contador_id

    print("\n--- Registrar Producto / Register Product ---")

    # pedir el nombre y limpiarlo con formatear_nombre()
    # ask for the name and clean it with formatear_nombre()
    nombre_raw = input("Nombre del producto / Product name: ")
    nombre = formatear_nombre(nombre_raw)  # quita espacios y capitaliza / removes spaces and capitalizes

    # validacion: el nombre no puede estar vacio
    # validation: the name cannot be empty
    if nombre == "":
        print("El nombre no puede estar vacio / Name cannot be empty")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return  # sale de la funcion sin registrar / exits the function without registering

    # validacion: el nombre no puede ser solo numeros
    # validation: the name cannot be only numbers
    if nombre.replace(" ", "").isdigit():
        print("El nombre no puede ser solo numeros / Name cannot be only numbers")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # pedir los costos y el precio usando pedir_numero() que valida automaticamente
    # ask for costs and price using pedir_numero() which validates automatically
    costo1 = pedir_numero("Costo proveedor 1 ($) / Supplier 1 cost: ")
    costo2 = pedir_numero("Costo proveedor 2 ($) / Supplier 2 cost: ")
    precio = pedir_numero("Precio de venta ($)   / Sale price      : ")

    # validacion extra: el precio de venta debe ser mayor al mejor costo
    # extra validation: the sale price must be greater than the best cost
    costo_minimo = min(costo1, costo2)
    if precio <= costo_minimo:
        print("  Advertencia / Warning: el precio de venta es menor o igual al costo.")
        print("  Warning: the sale price is less than or equal to the cost.")
        print("  El producto tendra ganancia negativa / The product will have negative profit.")

    # llamar a calcular() enviando los 3 valores como argumentos
    # call calcular() sending the 3 values as arguments
    mejor, costo_mejor, ganancia, rentabilidad = calcular(costo1, costo2, precio)

    # construir el diccionario del producto con todos sus atributos
    # build the product dictionary with all its attributes
    producto = {
        "id":           contador_id,   # int   - ID unico autoasignado / auto-assigned unique ID
        "nombre":       nombre,         # str   - nombre formateado / formatted name
        "costo1":       costo1,         # float - costo proveedor 1 / supplier 1 cost
        "costo2":       costo2,         # float - costo proveedor 2 / supplier 2 cost
        "precio_venta": precio,         # float - precio de venta / sale price
        "mejor_prov":   mejor,          # str   - resultado de la comparacion / comparison result
        "mejor_costo":  costo_mejor,    # float - el costo mas bajo / the lowest cost
        "ganancia":     ganancia,       # float - ganancia calculada / calculated profit
        "rentabilidad": rentabilidad,   # float - porcentaje / percentage
        "disponible":   True            # bool  - activo por defecto / active by default
    }

    # agregar el diccionario a la lista global de productos
    # add the dictionary to the global product list
    productos.append(producto)

    # incrementar el contador para que el proximo producto tenga un ID diferente
    # increment the counter so the next product has a different ID
    contador_id = contador_id + 1

    # mostrar el resultado en pantalla con f-strings alineados
    # show the result on screen with aligned f-strings
    print()
    print(f"  {'-'*42}")
    print(f"  {'Producto registrado! / Product registered!'}")
    print(f"  {'-'*42}")
    print(f"  {'ID':<28} {producto['id']}")
    print(f"  {'Nombre / Name':<28} {nombre}")
    print(f"  {'Mejor proveedor / Best supplier':<28} {mejor}")
    print(f"  {'Costo mejor / Best cost':<28} ${costo_mejor:,.2f}")
    print(f"  {'Ganancia / Profit':<28} ${ganancia:,.2f}")
    print(f"  {'Rentabilidad / Profitability':<28} {rentabilidad:.2f}%")
    print(f"  {'Disponible / Available':<28} {producto['disponible']}")
    print(f"  {'-'*42}")

    input("\nPresiona Enter para continuar / Press Enter to continue...")
# NOTA: Esta funcion recopila los datos del usuario, los valida, llama a
# calcular() para obtener los resultados y guarda el producto como un
# diccionario en la lista global 'productos'.
# NOTE: This function collects user data, validates it, calls calcular()
# to get results and saves the product as a dictionary in the global list.


# =============================================================================
# CRUD - CONSULTAR (for loop) / QUERY (for loop)
# =============================================================================
# Avance 6: Funcion explicita de consulta que recorre la lista con un ciclo for
# Advance 6: Explicit query function that loops through the list with a for loop

def consultar_productos():
    """
    Consulta todos los productos de la lista usando un ciclo for.
    Query all products in the list using a for loop.
    Operacion CRUD: Consultar / CRUD Operation: Read
    """
    # -------------------------------------------------------------------------
    # ENCABEZADO / HEADER
    # Lista de Productos Registrados / List of Registered Products
    # -------------------------------------------------------------------------
    print()
    print("=" * 55)
    print(f"  {'Lista de Productos / Product List':^51}")
    print("=" * 55)
    print(f"  {'Campo / Field':<28} {'Valor / Value'}")
    print("-" * 55)

    # validar que existan datos / validate data exists
    if len(productos) == 0:
        print("  No hay productos registrados / No products registered")
        print("=" * 55)
        return

    # recorrer la lista con un ciclo for y mostrar cada producto
    # loop through the list with a for loop and display each product
    for p in productos:
        print()
        print(f"  {'ID':<28} {p['id']}")
        print(f"  {'Nombre / Name':<28} {p['nombre']}")
        print(f"  {'Costo Prov.1 / Supplier 1 Cost':<28} ${p['costo1']:,.2f}")
        print(f"  {'Costo Prov.2 / Supplier 2 Cost':<28} ${p['costo2']:,.2f}")
        print(f"  {'Precio Venta / Sale Price':<28} ${p['precio_venta']:,.2f}")
        print(f"  {'Mejor Proveedor / Best Supplier':<28} {p['mejor_prov']}")
        print(f"  {'Ganancia / Profit':<28} ${p['ganancia']:,.2f}")
        print(f"  {'Rentabilidad / Profitability':<28} {p['rentabilidad']:.2f}%")
        print(f"  {'Disponible / Available':<28} {'Si / Yes' if p['disponible'] else 'No'}")
        print("  " + "-" * 53)

    print(f"\n  {'Total registros / Total records':<28} {len(productos)}")
    print("=" * 55)
# NOTA: Esta funcion implementa la operacion C-R-U-D de Consulta (Read).
# Usa un ciclo for para recorrer la lista de productos y mostrar cada
# diccionario con sus campos en formato bilingüe (Español / English).
# NOTE: This function implements the C-R-U-D Read operation.
# It uses a for loop to traverse the product list and display each
# dictionary with its fields in bilingual format (Spanish / English).


# =============================================================================
# MODULO 2 - VER PRODUCTOS / VIEW PRODUCTS
# =============================================================================

def ver_productos():
    print("\n--- Productos Registrados / Registered Products ---")

    # verificar que haya productos antes de mostrar la tabla
    # verify there are products before showing the table
    if len(productos) == 0:
        print("No hay productos aun / No products yet")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # preguntar como ordenar la lista antes de mostrarla
    # ask how to sort the list before showing it
    print("\n  Ordenar por / Sort by:")
    print("  1. Nombre / Name")
    print("  2. Rentabilidad / Profitability")
    print("  3. Ganancia / Profit")
    print("  4. Sin ordenar / No sort")
    orden = input("  Opcion / Option: ").strip()

    # .sort() con key= ordena la lista segun el criterio elegido
    # .sort() with key= sorts the list according to the chosen criterion
    if orden == "1":
        # ordenar alfabeticamente por nombre usando lambda
        # sort alphabetically by name using lambda
        productos.sort(key=lambda p: p["nombre"].lower())
        print("  Ordenado por nombre / Sorted by name")
    elif orden == "2":
        # ordenar de mayor a menor rentabilidad / sort from highest to lowest profitability
        # reverse=True invierte el orden para que el mayor quede primero
        # reverse=True reverses the order so the highest comes first
        productos.sort(key=lambda p: p["rentabilidad"], reverse=True)
        print("  Ordenado por rentabilidad / Sorted by profitability")
    elif orden == "3":
        # ordenar de mayor a menor ganancia / sort from highest to lowest profit
        productos.sort(key=lambda p: p["ganancia"], reverse=True)
        print("  Ordenado por ganancia / Sorted by profit")
    # opcion 4 o cualquier otra no aplica ordenamiento / option 4 or any other applies no sorting

    # encabezado de tabla con f-strings y modificadores de ancho
    # table header with f-strings and width modifiers
    # :<5 alinea a la izquierda con 5 espacios / left-aligns with 5 spaces
    # :>10 alinea a la derecha con 10 espacios / right-aligns with 10 spaces
    print()
    print(f"  {'ID':<5} {'Nombre / Name':<22} {'Mejor Prov.':<14} {'Ganancia':>10} {'Rentab.':>10} {'Activo':>8}")
    print("  " + "-" * 72)

    # recorrer cada producto de la lista y mostrarlo en una fila
    # loop through each product in the list and display it in a row
    for i in range(len(productos)):
        p = productos[i]  # p es el diccionario del producto actual / p is the current product dictionary

        # truncar el nombre si es muy largo para que no rompa la tabla
        # truncate the name if too long so it doesn't break the table
        nombre_corto = p["nombre"][:20]

        # convertir el booleano a texto legible / convert boolean to readable text
        activo = "Si/Yes" if p["disponible"] else "No"

        # imprimir la fila con todos los datos alineados
        # print the row with all data aligned
        print(f"  {p['id']:<5} {nombre_corto:<22} {p['mejor_prov']:<14} "
              f"${p['ganancia']:>8,.2f} {p['rentabilidad']:>8.2f}% {activo:>8}")

    print("  " + "-" * 72)

    # calcular el promedio de rentabilidad de todos los productos
    # calculate the average profitability of all products
    total_rent = 0
    for p in productos:
        total_rent = total_rent + p["rentabilidad"]  # sumar todas las rentabilidades / add all profitabilities
    promedio = total_rent / len(productos)  # dividir entre el total / divide by total

    # mostrar resumen al final de la tabla / show summary at the end of the table
    print(f"\n  {'Total productos / Total products':<35} {len(productos)}")
    print(f"  {'Rentabilidad promedio / Avg profitability':<35} {promedio:.2f}%")

    input("\nPresiona Enter para continuar / Press Enter to continue...")
# NOTA: Esta funcion muestra todos los productos en una tabla alineada.
# Usa f-strings con modificadores de ancho para que las columnas queden
# rectas sin importar el largo del texto.
# NOTE: This function shows all products in an aligned table.
# It uses f-strings with width modifiers so columns stay straight
# regardless of text length.


# =============================================================================
# MODULO 3 - BUSCAR PRODUCTO / SEARCH PRODUCT
# =============================================================================

def buscar_producto():
    print("\n--- Buscar Producto / Search Product ---")

    # validar que haya productos para buscar / validate there are products to search
    if len(productos) == 0:
        print("No hay productos para buscar / No products to search")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # pedir el termino de busqueda y estandarizarlo
    # ask for the search term and standardize it
    termino_raw = input("Nombre a buscar / Name to search: ")

    # validar que no este vacio / validate it is not empty
    if termino_raw.strip() == "":
        print("Debes ingresar un termino de busqueda / You must enter a search term")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # estandarizar: quitar espacios y pasar a minusculas para comparar sin importar mayusculas
    # standardize: remove spaces and convert to lowercase to compare regardless of uppercase
    termino = estandarizar_dato(termino_raw)

    print(f"\n  Buscando / Searching: '{termino}'...")
    print()

    # lista donde se guardan los productos que coincidan con la busqueda
    # list where products matching the search are saved
    encontrados = []

    # recorrer todos los productos y comparar el nombre estandarizado
    # loop through all products and compare the standardized name
    for p in productos:
        # estandarizar el nombre del producto tambien para comparar igual con igual
        # standardize the product name too to compare like with like
        if termino in estandarizar_dato(p["nombre"]):
            encontrados.append(p)  # agregar a encontrados si coincide / add to found if it matches

    # mostrar resultados o mensaje de no encontrado
    # show results or not found message
    if len(encontrados) == 0:
        print(f"  No se encontro ningun producto con: '{termino}'")
        print(f"  No product found with: '{termino}'")
    else:
        print(f"  {'ID':<5} {'Nombre / Name':<22} {'Mejor Prov.':<14} {'Ganancia':>10} {'Rentab.':>10}")
        print("  " + "-" * 63)
        for p in encontrados:
            print(f"  {p['id']:<5} {p['nombre']:<22} {p['mejor_prov']:<14} "
                  f"${p['ganancia']:>8,.2f} {p['rentabilidad']:>8.2f}%")
        print(f"\n  Resultados encontrados / Results found: {len(encontrados)}")

    input("\nPresiona Enter para continuar / Press Enter to continue...")
# NOTA: La busqueda ignora mayusculas y espacios gracias a estandarizar_dato().
# Esto significa que buscar "auriculares", "AURICULARES" o " Auriculares "
# dara el mismo resultado.
# NOTE: The search ignores uppercase and spaces thanks to estandarizar_dato().
# This means searching "auriculares", "AURICULARES" or " Auriculares "
# will give the same result.


# =============================================================================
# MODULO 4 - ACTUALIZAR PRODUCTO / UPDATE PRODUCT
# =============================================================================

def actualizar_producto():
    global productos

    print("\n--- Actualizar Producto / Update Product ---")

    # validar que haya productos para actualizar / validate there are products to update
    if len(productos) == 0:
        print("No hay productos para actualizar / No products to update")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # mostrar lista de productos con sus IDs para que el usuario elija
    # show list of products with their IDs for the user to choose
    print()
    for p in productos:
        activo = "Si/Yes" if p["disponible"] else "No"
        print(f"  ID {p['id']} - {p['nombre']:<22} - Activo / Active: {activo}")

    try:
        # pedir el ID del producto a actualizar / ask for the ID of the product to update
        id_buscar = int(input("\nID del producto a actualizar / Product ID to update (0 cancelar/cancel): "))

        # si el usuario escribe 0 se cancela la operacion / if user types 0 the operation is cancelled
        if id_buscar == 0:
            return

        # buscar el producto cuyo ID coincida con el ingresado
        # search for the product whose ID matches the one entered
        producto_encontrado = None
        for p in productos:
            if p["id"] == id_buscar:
                producto_encontrado = p  # guardar referencia al diccionario / save reference to dictionary
                break  # salir del ciclo cuando se encuentre / exit loop when found

        # validar que el ID exista en la lista / validate the ID exists in the list
        if producto_encontrado is None:
            print(f"  No se encontro ningun producto con ID: {id_buscar}")
            print(f"  No product found with ID: {id_buscar}")
            input("\nPresiona Enter para continuar / Press Enter to continue...")
            return

        # mostrar opciones de que se puede actualizar / show options of what can be updated
        print(f"\n  Producto seleccionado / Selected product: {producto_encontrado['nombre']}")
        print("  1. Cambiar nombre         / Change name")
        print("  2. Cambiar precio venta   / Change sale price")
        print("  3. Cambiar disponibilidad / Change availability")

        opcion = input("\n  Que deseas actualizar / What do you want to update: ")

        if opcion == "1":
            # pedir nuevo nombre y validar que no este vacio
            # ask for new name and validate it is not empty
            nuevo_nombre = formatear_nombre(input("  Nuevo nombre / New name: "))
            if nuevo_nombre == "":
                print("  El nombre no puede estar vacio / Name cannot be empty")
            else:
                # .update() modifica el valor de la llave indicada en el diccionario
                # .update() modifies the value of the indicated key in the dictionary
                producto_encontrado.update({"nombre": nuevo_nombre})
                print(f"  Nombre actualizado / Name updated: {nuevo_nombre}")

        elif opcion == "2":
            # pedir nuevo precio y recalcular ganancia y rentabilidad
            # ask for new price and recalculate profit and profitability
            nuevo_precio = pedir_numero("  Nuevo precio de venta / New sale price: ")

            # advertir si el precio es menor al costo / warn if price is less than cost
            if nuevo_precio <= producto_encontrado["mejor_costo"]:
                print("  Advertencia / Warning: precio menor o igual al costo / price less than or equal to cost")

            # recalcular con la funcion calcular() / recalculate with calcular() function
            mejor, costo_mejor, ganancia, rentabilidad = calcular(
                producto_encontrado["costo1"],
                producto_encontrado["costo2"],
                nuevo_precio
            )

            # actualizar multiples llaves a la vez con .update()
            # update multiple keys at once with .update()
            producto_encontrado.update({
                "precio_venta": nuevo_precio,
                "ganancia":     ganancia,
                "rentabilidad": rentabilidad
            })
            print(f"  Precio actualizado / Price updated  : ${nuevo_precio:,.2f}")
            print(f"  Nueva ganancia / New profit         : ${ganancia:,.2f}")
            print(f"  Nueva rentabilidad / New profitab.  : {rentabilidad:.2f}%")

        elif opcion == "3":
            # invertir el valor booleano: True pasa a False y False pasa a True
            # invert the boolean value: True becomes False and False becomes True
            nuevo_estado = not producto_encontrado["disponible"]
            producto_encontrado.update({"disponible": nuevo_estado})
            estado_texto = "Activo / Active" if nuevo_estado else "Inactivo / Inactive"
            print(f"  Disponibilidad actualizada / Availability updated: {estado_texto}")

        else:
            print("  Opcion invalida / Invalid option")

    except ValueError:
        # ocurre si el usuario escribe letras en vez del ID numerico
        # occurs if the user types letters instead of the numeric ID
        print("  Debes ingresar un numero / You must enter a number")

    input("\nPresiona Enter para continuar / Press Enter to continue...")
# NOTA: Esta funcion busca un producto por su ID (llave unica) y permite
# actualizar nombre, precio o disponibilidad usando el metodo .update()
# del diccionario. Al cambiar el precio, recalcula ganancia y rentabilidad.
# NOTE: This function searches a product by its ID (unique key) and allows
# updating name, price or availability using the dictionary's .update() method.
# When price changes, it recalculates profit and profitability.


# =============================================================================
# MODULO 5 - ELIMINAR PRODUCTO / DELETE PRODUCT
# =============================================================================

def eliminar_producto():
    global productos

    print("\n--- Eliminar Producto / Delete Product ---")

    # validar que haya productos / validate there are products
    if len(productos) == 0:
        print("No hay productos para eliminar / No products to delete")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    # mostrar lista numerada de productos / show numbered list of products
    print()
    for i in range(len(productos)):
        print(f"  {i+1}. ID {productos[i]['id']} - {productos[i]['nombre']}")

    try:
        num = int(input("\nNumero a eliminar (0 cancelar) / Number to delete (0 cancel): "))

        # 0 cancela la operacion / 0 cancels the operation
        if num == 0:
            return

        # validar que el numero este dentro del rango valido
        # validate the number is within the valid range
        if num >= 1 and num <= len(productos):
            nombre = productos[num - 1]["nombre"]  # guardar nombre antes de eliminar / save name before deleting
            confirmar = input(f"  Confirmas eliminar '{nombre}'? (s/n): ")

            # estandarizar la respuesta para aceptar 'S', 's', ' s ' etc.
            # standardize the response to accept 'S', 's', ' s ' etc.
            if estandarizar_dato(confirmar) == "s":
                productos.pop(num - 1)  # .pop() elimina el elemento en esa posicion / removes element at that position
                print(f"  Producto eliminado / Product deleted: {nombre}")
            else:
                print("  Cancelado / Cancelled")
        else:
            # el numero no corresponde a ningun producto / the number doesn't match any product
            print(f"  Numero invalido. Elige entre 1 y {len(productos)} / Invalid number. Choose between 1 and {len(productos)}")

    except ValueError:
        print("  Debes ingresar un numero / You must enter a number")

    input("\nPresiona Enter para continuar / Press Enter to continue...")
# NOTA: Esta funcion elimina un producto de la lista por su posicion.
# Pide confirmacion antes de eliminar para evitar borrados accidentales.
# NOTE: This function removes a product from the list by its position.
# It asks for confirmation before deleting to avoid accidental deletions.


# =============================================================================
# MODULO 6 - GUARDAR DATOS / SAVE DATA
# =============================================================================

def guardar_datos():
    print("\n--- Guardar Datos / Save Data ---")

    # validar que haya datos para guardar / validate there is data to save
    if len(productos) == 0:
        print("No hay datos para guardar / No data to save")
        input("\nPresiona Enter para continuar / Press Enter to continue...")
        return

    try:
        # abrir el archivo en modo escritura 'w' / open file in write mode 'w'
        # encoding utf-8 para soportar caracteres especiales / utf-8 encoding to support special characters
        archivo = open("rentabilidad.json", "w", encoding="utf-8")

        # json.dump() convierte la lista de diccionarios a formato JSON y la escribe
        # json.dump() converts the list of dictionaries to JSON format and writes it
        # indent=2 hace el archivo legible con sangria / indent=2 makes the file readable with indentation
        json.dump(productos, archivo, ensure_ascii=False, indent=2)

        archivo.close()  # siempre cerrar el archivo despues de usarlo / always close the file after using it

        # -------------------------------------------------------------------------
        # CONFIRMACION DE GUARDADO / SAVE CONFIRMATION
        # -------------------------------------------------------------------------
        print()
        print("  " + "=" * 45)
        print(f"  {'Datos guardados exitosamente!':^43}")
        print(f"  {'Data saved successfully!':^43}")
        print("  " + "=" * 45)
        print(f"  {'Archivo / File':<30} rentabilidad.json")
        print(f"  {'Registros guardados / Saved records':<30} {len(productos)}")
        print(f"  {'Formato / Format':<30} JSON (UTF-8)")
        print("  " + "-" * 45)

    except Exception as e:
        # captura cualquier error inesperado al escribir el archivo
        # captures any unexpected error when writing the file
        print(f"  Error al guardar / Error saving: {e}")

    input("\nPresiona Enter para continuar / Press Enter to continue...")
# NOTA: Guarda la lista completa de productos en un archivo JSON.
# El archivo se puede abrir con cualquier editor de texto para ver los datos.
# NOTE: Saves the complete product list to a JSON file.
# The file can be opened with any text editor to view the data.


# =============================================================================
# MODULO 7 - CARGAR DATOS / LOAD DATA
# =============================================================================

def cargar_datos():
    global productos

    print("\n--- Cargar Datos / Load Data ---")

    try:
        # abrir el archivo en modo lectura 'r' / open file in read mode 'r'
        archivo = open("rentabilidad.json", "r", encoding="utf-8")

        # json.load() lee el archivo y lo convierte de vuelta a lista de diccionarios
        # json.load() reads the file and converts it back to a list of dictionaries
        datos = json.load(archivo)

        archivo.close()  # cerrar el archivo / close the file

        # validar que el archivo contenga una lista / validate the file contains a list
        if not isinstance(datos, list):
            print("  El archivo tiene un formato invalido / File has an invalid format")
            input("\nPresiona Enter para continuar / Press Enter to continue...")
            return

        # reemplazar la lista actual con los datos del archivo
        # replace the current list with the data from the file
        productos = datos
        print(f"  Datos cargados correctamente / Data loaded successfully")
        print(f"  Productos cargados / Loaded products: {len(productos)}")

    except FileNotFoundError:
        # ocurre cuando el archivo rentabilidad.json no existe todavia
        # occurs when the rentabilidad.json file does not exist yet
        print("  Archivo no encontrado. Guarda primero los datos.")
        print("  File not found. Save the data first.")

    except Exception as e:
        print(f"  Error al cargar / Error loading: {e}")

    input("\nPresiona Enter para continuar / Press Enter to continue...")
# NOTA: Carga los datos guardados previamente desde el archivo JSON.
# Si el archivo no existe muestra un mensaje claro en vez de cerrarse.
# NOTE: Loads previously saved data from the JSON file.
# If the file doesn't exist it shows a clear message instead of closing.


# =============================================================================
# MENU PRINCIPAL / MAIN MENU
# =============================================================================

def main():
    # ciclo principal que mantiene el programa activo hasta que el usuario salga
    # main loop that keeps the program active until the user exits
    while True:

        limpiar()  # limpiar pantalla antes de mostrar el menu / clear screen before showing menu

        # encabezado del menu / menu header
        print("=" * 45)
        print(f"  {'SISTEMA DE ANALISIS DE RENTABILIDAD':^41}")
        print(f"  {'Profitability Analysis System':^41}")
        print("=" * 45)
        print(f"  {'Productos registrados / Registered':<30} {len(productos)}")
        print("-" * 45)

        # opciones del menu / menu options
        print(f"  1. Registrar producto  / Register product")
        print(f"  2. Consultar lista     / Query list (CRUD)")
        print(f"  3. Ver tabla productos / View products table")
        print(f"  4. Buscar producto     / Search product")
        print(f"  5. Actualizar producto / Update product")
        print(f"  6. Eliminar producto   / Delete product")
        print(f"  7. Guardar datos       / Save data")
        print(f"  8. Cargar datos        / Load data")
        print(f"  9. Salir               / Exit")
        print("-" * 45)

        # leer la opcion del usuario / read the user's option
        opcion = input("Elige una opcion / Choose an option: ")

        # estructura if/elif que dirige al modulo correspondiente segun la opcion
        # if/elif structure that directs to the corresponding module based on the option
        if opcion == "1":
            registrar_producto()    # CRUD Agregar / Add - usa .append()

        elif opcion == "2":
            consultar_productos()   # CRUD Consultar / Read - usa ciclo for
            input("\nPresiona Enter para continuar / Press Enter to continue...")

        elif opcion == "3":
            ver_productos()         # tabla con ordenamiento / table with sorting

        elif opcion == "4":
            buscar_producto()       # busqueda por cadena / string search

        elif opcion == "5":
            actualizar_producto()   # CRUD Actualizar / Update

        elif opcion == "6":
            eliminar_producto()     # CRUD Eliminar / Delete

        elif opcion == "7":
            guardar_datos()         # persistencia JSON / JSON persistence

        elif opcion == "8":
            cargar_datos()          # cargar desde JSON / load from JSON

        elif opcion == "9":
            print("\n  Hasta luego! / Goodbye!")
            break  # break sale del ciclo while y termina el programa / break exits the while loop

        else:
            # cualquier otra entrada es invalida / any other input is invalid
            print("  Opcion invalida. Elige entre 1 y 9 / Invalid option. Choose between 1 and 9")
            input("  Presiona Enter para continuar / Press Enter to continue...")

# NOTA: main() es la funcion principal que coordina todo el programa.
# Usa un ciclo while True para que el menu se muestre continuamente.
# Solo termina cuando el usuario elige la opcion 9 que ejecuta break.
# El diseno Top-Down hace que main() solo coordine y cada funcion ejecute.
# NOTE: main() is the main function that coordinates the entire program.
# It uses a while True loop so the menu is displayed continuously.
# It only ends when the user chooses option 9 which executes break.
# The Top-Down design makes main() only coordinate and each function execute.


# =============================================================================
# PUNTO DE ENTRADA / ENTRY POINT
# =============================================================================

# esta linea inicia el programa llamando a main()
# this line starts the program by calling main()
main()
