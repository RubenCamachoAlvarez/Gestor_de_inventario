"""
Este modulo de Python realiza las implementaciones de las funciones necesarias para capturar la entrada del usuario de una manera comoda y sobretodo segura, garantizando que el tipo de dato que se espera que el usuario ingrese sea la que sea retornada al flujo principal del programa para realizar las operaciones correspondientes.

"""
from sys import stderr


def leer_numero_entero(mensaje_entrada):

    """Como su nombre lo indica, esta funcion esta diseñada para solicitar al usuario ingresar un entero y esta funcion se
    mantiene en ejecucion hasta que el tipo de dato solicitado es ingresado correctamente.

    Del mismo modo, esta funcion recibe como argumento una cadena de caracteres indicando el mensaje que debe de mostrar
    como prompt para que el usuario conozca de antemano que finalidad tiene el dato que ingresara."""


    #Comenzamos creando un ciclo infinito que iterara de manera indefinida hasta capturar el tipo de dato solicitado de manera correcta.

    while True:

        #Establecemos un constructo try-except el cual nos permite capturar una excepcion de tipo TypeError en caso de que la funcion int() no pueda realizar la transformacion de los datos retornados por la funcion read() en un tipo de dato entero.

        try:

            #Solicitamos la entrada al usuario y procedemos a tratar de convertirla en un entero.

            numero_entero = int(input(mensaje_entrada))

            if(numero_entero < 0):

                print("No se aceptan numeros enteros negativos", file=stderr)

                continue

            #Si la cadena ingresa por el usuario es correctamente convertida a un tipo de dato entero, entonces salimos del bucle

            break

        except ValueError:

            #Si entrada del usuario no puede ser convertida a un entero, entonces se muestra el mensaje de error en la salida estandar de errores y se repite el ciclo nuevamente.

            print("El dato ingresado no corresponde a un numero entero.", file=stderr)

    return numero_entero



def leer_numero_decimal(mensaje_entrada):

    """Esta funcion se encarga de realizar la peticion al usuario de ingresar un numero decimal el cual es gestionado
    por medio del tipo de dato float."""

    #Ciclo infinito que se ejecuta hasta que el dato ingresado por el cliente pueda ser transformado al tipo de dato float.

    while True:

        #Constructo try-except que nos permite capturar la excepcion TypeError si la conversion del dato ingresado ha sido insatisfactoria.

        try:

            #Lectura del dato a partir de la entrada estandar y solicitud para que este sea transformado en un tipo de dato flotante.

            cadena_decimal = input(mensaje_entrada)

            cadena_decimal = cadena_decimal[1:] if cadena_decimal[0] == "$" else cadena_decimal

            numero_decimal = float(cadena_decimal)

            if(numero_decimal < 0.0):

                print("No se aceptan numeros decimales negativos.", file=stderr)

                continue

            #Si la entrada es transformada correctamente a su representacion como tipo de dato flotante, entonces salimos del ciclo.

            break

        except ValueError:

            #En caso de que el proceso de conversion falle, entonces procedemos a mostrar el siguiente mensaje en la salida estandar de error. Y a continuacion se realiza una nueva iteracion en el ciclo repitiendo todo el proceso.

            print("El dato ingresado no corresponde a un numero decimal.", file=stderr)

    #Cuando el usuario ingresa el dato adecuado, este es retornado al flujo de ejecucion principal del programa.

    return numero_decimal


def leer_cadena(mensaje_entrada, maximo_numero_caracteres):

    """Esta funcion tiene el proposito de unicamente solicitar la lectura de una cadena de caracter al usuario a partir de la
    entrada estandar asignada al proceso en el cual se ejecuta este programa.

    Un aspecto importante es que esta cadena recibe como segundo argumento el numero maximo de caracteres que deseamos que el usuario pueda ingresar en
    la entrada. Si el usuario excede este limite, entonces solo se tomaran los primeros n caracteres que corresponde a ese numero maximo de caracteres
    especificados."""

    cadena = input(mensaje_entrada).strip()[0:maximo_numero_caracteres]

    return cadena


def seleccionar_opcion(mensaje_seleccion, lista_opciones):

    """Esta funcion fue implementada para proporcionar un mecanismo general para poder seleccionar opciones de un menu.

    Generalmente cuando se trabaja con menu en aplicaciones de consola es normal que se solicite al usuario ingresar una opcion del menu
    que tipicamente estan representadas por numeros enteros o letras. Para esto mismo fue diseñado esta funcion.

    Inicialmente despliega un prompt con el mensaje especificado como argumento durante la llamada a la funcion, y a continuacion espera
    hasta que el usuario ingrese una entrada que debe de ser de un unico caracter (ya que en nuestro programa no tendremos menus con 2 o mas digitos,
    por ejemplo).

    Del mismo modo, el segundo argumento recibe una lista con todas las posibles opciones que el usuario puede ingresar. Una vez que el usuario introduzca
    una opcion de un solo caracter, esta se comparara con los elementos de la lista y si corresponde con alguno, finalmente la funcion termina y retorna
    la opcion seleccionada."""

    while True:

        opcion_seleccionada = input(mensaje_seleccion)

        if len(opcion_seleccionada) == 1 and opcion_seleccionada in lista_opciones:

            break

        else:

            print("Esta no es una opcion valida", file=stderr);

    return opcion_seleccionada


def confirmar_operacion(mensaje_confirmacion):

    """Esta funcion esta diseñada para solicitar al usuario confirmar la realizar de una determinada operacion esperando a que ingrese una 'S' o 's' para
    confirmar la operacion, o 'N' o 'n' para cancelarla o negar su ejecucion.

    Esta funcion sera utilizada para solicitar la confirmacion al usuario para la realizacion de operaciones criticas como la eliminacion o
    actualizacion de los datos de un producto."""

    opcion = seleccionar_opcion(mensaje_confirmacion + "[S/n]: ", ["s", "n", "S", "N"])

    return True if opcion.lower() == "s" else False
