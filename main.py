"""Este es el achivo principal del programa.

Este archivo hace la implementacion de las funciones de las diferentes opciones ofertadas por el programa para llevar a cabo
la gestion del inventario.

Del mismo modo, hace uso de los modulos para la captura de las entradas del usuario y para los mecanismo de entrada y salida
hacia el archivo que almacena los datos del inventario, que pertenecen al paquete 'biblioteca' """

from inventario import productos

from biblioteca import Entrada_Usuario


if __name__ == "__main__":

    control = True

    productos.leer_lista_productos()

    productos.mostrar_lista_productos()

    while control:

        # productos.agregar_nuevo_producto()

        # productos.buscar_producto_por_id_o_nombre()

        productos.eliminar_producto()

        control = Entrada_Usuario.confirmar_operacion("¿Desea repetir la operacion? ")

    productos.mostrar_lista_productos()
