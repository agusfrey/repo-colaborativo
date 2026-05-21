def registrar_habitos():
    """
    Permite al usuario ingresar actividades realizadas durante el día.

    La función solicita al usuario que ingrese actividades una por una,
    guardándolas en una lista. El ingreso finaliza cuando el usuario escribe 'fin'.

    Parámetros
    ----------
    No recibe parámetros.

    Returns
    -------
    list
        Lista de actividades ingresadas por el usuario.
    """

    habitos = []

    while True:
        actividad = input("Ingresá una actividad (o 'fin' para terminar): ")

        if actividad == "fin":
            break

        habitos.append(actividad)

    return habitos


def analizar_habitos(lista):
    """
    Analiza una lista de actividades y cuenta cuántas veces aparece cada una.

    Recorre la lista recibida y genera un diccionario donde las claves son
    las actividades y los valores son la cantidad de veces que se repiten.

    Parámetros
    ----------
    lista : list
        Lista de actividades (strings).

    Returns
    -------
    dict
        Diccionario con el conteo de cada actividad.
    """

    conteo = {}

    for actividad in lista:
        if actividad in conteo:
            conteo[actividad] += 1
        else:
            conteo[actividad] = 1

    return conteo
