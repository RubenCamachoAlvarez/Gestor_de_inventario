"""
Este modulo contiene la definicion e implementacion de las diferentes funciones que dan soporte a las operaciones fundamentales sobre los productos
que realiza el programa principal.

Se escogio desacoplar las funciones para realizar las operaciones sobre los productos, del archivo principal para tener una mayor claridad en el codigo
y para que sea facilmente escalable el programa en caso de necesitarlo.

Por ejemplo, si quisieramos agregar una interfaz grafica de usuario en lugar de gestionar toda la aplicacion en modo texto, entonces simplementemente
tenemos que escribir el modulo que represente la GUI y conectarla con esta interfaz para dar la funcionalidad concreta a los diferentes elementos
graficos que la compongan.
"""

from sys import stderr

from biblioteca import Entrada_Usuario

from biblioteca import IO_Inventario

_ID_ultimo_producto = 0

_lista_productos = []

_ruta_archivo_inventario_productos = "./Inventario_Productos.dat"

_maximo_numero_caracteres_nombre = 15

_maximo_numero_caracteres_descripcion = 30


def agregar_nuevo_producto():

    global _ID_ultimo_producto

    global _ruta_archivo_inventario_productos

    global _lista_productos

    print("\nRegistro de nuevo producto\n")

    nombre = Entrada_Usuario.leer_cadena(f"Nombre (Maximo {_maximo_numero_caracteres_nombre} caracteres): ", _maximo_numero_caracteres_nombre)

    descripcion = Entrada_Usuario.leer_cadena(f"Descripcion (Maximo {_maximo_numero_caracteres_descripcion} caracteres): ", _maximo_numero_caracteres_descripcion)

    cantidad_stock = Entrada_Usuario.leer_numero_entero("Cantidad en stock: ")

    precio = Entrada_Usuario.leer_numero_decimal("Precio: ")

    producto = {"id" : _ID_ultimo_producto, "nombre" : nombre, "descripcion" : descripcion, "cantidad_stock" : cantidad_stock, "precio" : precio}

    _lista_productos.append(producto)

    IO_Inventario.escribir_registros_productos(_lista_productos, _ruta_archivo_inventario_productos)

    _ID_ultimo_producto += 1



def leer_lista_productos():

    global _ID_ultimo_producto

    global _ruta_archivo_inventario_productos

    global _lista_productos

    _lista_productos = IO_Inventario.leer_registros_productos(_ruta_archivo_inventario_productos)

    if len(_lista_productos) > 0:

        for producto in _lista_productos:

            if producto['id'] > _ID_ultimo_producto:

                _ID_ultimo_producto = producto['id']

        _ID_ultimo_producto += 1


def mostrar_lista_productos():

    print("\nInventario de productos\n")

    global _lista_productos

    imprimir_tabla_productos(_lista_productos)


def imprimir_tabla_productos(lista_productos):
    
    maximo_numero_caracteres_ID = 6
    
    maximo_numero_caracteres_nombre = 20
    
    maximo_numero_caracteres_descripcion = 35
    
    maximo_numero_caracteres_cantidad_stock = 20
    
    maximo_numero_caracteres_precio = 10

    separador = f"+{'':-^{maximo_numero_caracteres_ID}}+{'':-^{maximo_numero_caracteres_nombre}}+{'':-^{maximo_numero_caracteres_descripcion}}+{'':-^{maximo_numero_caracteres_cantidad_stock}}+{'':-^{maximo_numero_caracteres_precio}}+"

    encabezado = f"|{'ID': ^{maximo_numero_caracteres_ID}}|{'Nombre': ^{maximo_numero_caracteres_nombre}}|{'Descripcion': ^{maximo_numero_caracteres_descripcion}}|{'Cantidad en Stock': ^{maximo_numero_caracteres_cantidad_stock}}|{'Precio': ^{maximo_numero_caracteres_precio}}|"

    print(separador)

    print(encabezado)

    print(separador)

    for producto in lista_productos:

        ID = producto['id']

        nombre = producto['nombre']

        descripcion = producto['descripcion']

        cantidad_stock = producto['cantidad_stock']

        precio = producto['precio']

        formato_renglon = f"|{ID: ^{maximo_numero_caracteres_ID}}|{nombre: ^{maximo_numero_caracteres_nombre}}|{descripcion: ^{maximo_numero_caracteres_descripcion}}|{cantidad_stock: ^{maximo_numero_caracteres_cantidad_stock}}|${precio: ^{maximo_numero_caracteres_precio-1}}|"

        print(formato_renglon)

        print(separador)


def buscar_producto_por_id(id_producto):

    global _lista_productos

    for producto in _lista_productos:

        if producto['id'] == id_producto:

            return producto


    return None


def buscar_producto_por_nombre(nombre_producto):

    global _lista_productos

    productos_coincidencia = []

    for producto in _lista_productos:

        if nombre_producto.lower() in producto['nombre'].lower():

            productos_coincidencia.append(producto)

    return productos_coincidencia


def buscar_producto_por_id_o_nombre():

    global _maximo_numero_caracteres_nombre

    print("\nBuscar producto por ID o nombre\n")

    print("1. Buscar por ID")

    print("2. Filtrar por nombre\n")

    opcion = int(Entrada_Usuario.seleccionar_opcion("Ingrese una opcion de busqueda: ", ["1", "2"]))

    productos_filtrados = []

    if opcion == 1:

        while True:

            id_producto = Entrada_Usuario.leer_numero_entero("Ingrese el ID del producto a buscar: ")

            producto = buscar_producto_por_id(id_producto)

            if producto != None:

                productos_filtrados.append(producto)

            else:

                print(f"\nNo hay ningun producto con ID '{id_producto}' almacenado actualmente en el inventario.\n", file=stderr)

                if Entrada_Usuario.confirmar_operacion("¿Deseas ingresar un ID diferente? "):

                    continue

            break

    elif opcion == 2:

        while True:

            nombre_producto = Entrada_Usuario.leer_cadena("Ingrese el nombre del producto: ", _maximo_numero_caracteres_nombre)

            productos_filtrados = buscar_producto_por_nombre(nombre_producto)

            if len(productos_filtrados) == 0:

                print(f"\nNo se ha encontrado ningun producto con el nombre '{nombre_producto}' actualmente almacenado en el inventario.\n", file=stderr)

                if Entrada_Usuario.confirmar_operacion("¿Deseas volver a buscar con un nombre diferente? "):

                    continue

            break


    if len(productos_filtrados) > 0:

        imprimir_tabla_productos(productos_filtrados)

    else:

        print("\nNINGUN PRODUCTO FUE FILTRADO\n")


def eliminar_producto():

    global _lista_productos

    print("\nEliminar producto de inventario\n")

    if len(_lista_productos):

        if Entrada_Usuario.confirmar_operacion("¿Desea mostrar los productos del inventario?"):

            mostrar_lista_productos()


        id_producto = Entrada_Usuario.lee_numero_entero("\nIngrese el ID del producto que desea eliminar del inventario: ")

        if buscar_producto_por_id(id_producto) != None and Entrada_Usuario.confirmar_operacion("¿Esta seguro de eliminar este producto permanentemente? "):



    else:

        print("\nNO HAY PRODUCTOS REGISTRADOS EN EL INVENTARIO\n", file=stderr)
