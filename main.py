"""Este es el achivo principal del programa.

Este archivo hace la implementacion de las funciones de las diferentes opciones ofertadas por el programa para llevar a cabo
la gestion del inventario.

Del mismo modo, hace uso de los modulos para la captura de las entradas del usuario y para los mecanismo de entrada y salida
hacia el archivo que almacena los datos del inventario, que pertenecen al paquete 'biblioteca' """

from inventario import productos

from biblioteca import Entrada_Usuario

def menu_opciones():

    print("\nMenu de opciones\n")

    print("1. Imprimir todos los productos del inventario")

    print("2. Agregar nuevo producto")

    print("3. Actualizar datos de producto")

    print("4. Eliminar producto")

    print("5. Imprimir reporte de productos con un bajo stock")

    print("6. Buscar producto por nombre o por ID")

    print("7. Salir de la aplicacion")


    opcion_menu = int(Entrada_Usuario.seleccionar_opcion("\nSeleccione una opcion del menu: ", ["1", "2", "3", "4", "5", "6", "7"]))

    return opcion_menu



def bucle_menu_principal():

    productos.leer_lista_productos()

    print("\nSISTEMA GESTOR DE INVENTARIO\n")

    while True:

        opcion_seleccionada = menu_opciones()

        if opcion_seleccionada == 1:

            productos.mostrar_lista_productos()

        elif opcion_seleccionada == 5:

            productos.reporte_productos_bajo_stock()

        elif opcion_seleccionada < 6:

            while True:

                if opcion_seleccionada == 2:

                    productos.agregar_nuevo_producto()

                elif opcion_seleccionada == 3:

                    productos.actualizar_datos_producto()

                elif opcion_seleccionada == 4:

                    productos.eliminar_producto()

                if not Entrada_Usuario.confirmar_operacion("¿Desea repetir la misma operacion? "):

                    break

        elif opcion_seleccionada == 6:

            productos.buscar_producto_por_id_o_nombre()
    
        elif opcion_seleccionada == 7:

            break

    print("\nHasta pronto\n")




if __name__ == "__main__":

    bucle_menu_principal()

