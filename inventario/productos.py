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

__ID_ultimo_producto = 0

__lista_productos = []

def agregar_nuevo_producto():

    global __ID_ultimo_producto

    maximo_numero_caracteres_nombre = 20

    maximo_numero_caracteres_descripcion = 100

    print("Registro de nuevo producto", end="\n\n")

    nombre = Entrada_Usuario.leer_cadena(f"Nombre (Maximo {maximo_numero_caracteres_nombre} caracteres): ", maximo_numero_caracteres_nombre)

    descripcion = Entrada_Usuario.leer_cadena(f"Descripcion (Maximo {maximo_numero_caracteres_descripcion} caracteres): ", maximo_numero_caracteres_descripcion)

    cantidad_stock = Entrada_Usuario.leer_numero_entero("Cantidad en stock: ")

    precio = Entrada_Usuario.leer_numero_decimal("Precio: ")

    producto = {"id" : __ID_ultimo_producto, "nombre" : nombre, "descripcion" : descripcion, "cantidad_stock" : cantidad_stock, "precio" : precio}

    __lista_productos.append(producto)

    IO_Inventario.escribir_registros_productos(__lista_productos, "Inventario_Productos.dat")

    __ID_ultimo_producto += 1

