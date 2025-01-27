"""
Este modulo contiene la definicion e implementacion de las diferentes funciones que dan soporte a las operaciones fundamentales sobre los productos
que realiza el programa principal.

Se escogio desacoplar las funciones para realizar las operaciones sobre los productos, del archivo principal para tener una mayor claridad en el codigo
y para que sea facilmente escalable el programa en caso de necesitarlo.

Por ejemplo, si quisieramos agregar una interfaz grafica de usuario en lugar de gestionar toda la aplicacion en modo texto, entonces simplementemente
tenemos que escribir el modulo que represente la GUI y conectarla con esta interfaz para dar la funcionalidad concreta a los diferentes elementos
graficos que la compongan.
"""

from biblioteca import Entrada_Usuario

from biblioteca import IO_Inventario

_ID_ultimo_producto = 0

_lista_productos = []

_ruta_archivo_inventario_productos = "./Inventario_Productos.dat"


def agregar_nuevo_producto():

    global _ID_ultimo_producto

    global _ruta_archivo_inventario_productos

    global _lista_productos

    maximo_numero_caracteres_nombre = 15

    maximo_numero_caracteres_descripcion = 30

    print("\nRegistro de nuevo producto\n")

    nombre = Entrada_Usuario.leer_cadena(f"Nombre (Maximo {maximo_numero_caracteres_nombre} caracteres): ", maximo_numero_caracteres_nombre)

    descripcion = Entrada_Usuario.leer_cadena(f"Descripcion (Maximo {maximo_numero_caracteres_descripcion} caracteres): ", maximo_numero_caracteres_descripcion)

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

        formato_renglon = f"|{ID: ^{maximo_numero_caracteres_ID}}|{nombre: ^{maximo_numero_caracteres_nombre}}|{descripcion: ^{maximo_numero_caracteres_descripcion}}|{cantidad_stock: ^{maximo_numero_caracteres_cantidad_stock}}|{precio: ^{maximo_numero_caracteres_precio}}|"

        print(formato_renglon)

        print(separador)
