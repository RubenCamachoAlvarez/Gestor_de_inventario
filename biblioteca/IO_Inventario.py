
"""
Este modulo de Python incorpora la implementacion de las dos funciones de entrada y salida necesarias para escribir y leer
datos a partir del archivo especificado como el archivo de inventario que almacenara los datos de los diferentes productos.

"""


def escribir_registros_productos(lista_productos, ruta_archivo):

    """Esta funcion recibe como argumento una lista que contiene diferentes diccionarios con datos de productos
    los cuales finalmente son escritos dentro del archivo especificado en la ruta recibido como segundo argumento,
    de este modo garantizamos la persistencia de los datos al salir de la aplicacion."""

    #Abrimos el archivo donde queremos realizar la escritura de los datos para sus persistencia.

    with open(ruta_archivo, "w") as inventario:

        #Iteramos sobre cada uno de los productos que se desean escribir.

        for producto in lista_productos:


            #Escribimos dentro del archivo el registro que almacena los datos del producto.

            inventario.write(f"{producto['id']},{producto['nombre']},{producto['descripcion']},{producto['cantidad_stock']},{producto['precio']}\n")


        #Finalmente una vez iterados y escritos los datos de cada uno de los productos de la lista, el flujo de datos abierto hacia el archivo es cerrado por el sistema operativo.


def leer_registros_productos(ruta_archivo):

    """Esta función tiene el objetivo de leer los registros de productos almacenados en el archivo de la ruta especificada
    como argumento, almacenar los datos de cada uno de estos registros dentro de un diccionario y finalmente retornar
    una lista con todos los diccionarios que almacenan los datos de los distintos productos almacenados en el archivo
    de inventario."""

    #Comenzamos definiendo una lista donde almacenaremos cada uno de los diccionario con los datos de cada producto respectivamente.

    lista_productos = []

    #Abrimos un flujo de datos en modo de lectura para recuperar los registros de productos almacenados dentro del archivo de inventario.

    with open(ruta_archivo, "r") as inventario:

        for registro in inventario:

            datos = [campo.strip() for campo in registro.strip().split(",")]

            producto = {"id": datos[0], "nombre": datos[1], "descripcion": datos[2], "cantidad_stock": datos[3], "precio": datos[4]}

            lista_productos.append(producto)


        #Se cierra de manera implicita el flujo de datos establecido por el sistema operativo entre el archivo y la aplicacion.

