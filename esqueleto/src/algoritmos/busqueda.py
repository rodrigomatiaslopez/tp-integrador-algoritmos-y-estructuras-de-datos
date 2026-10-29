def busqueda_lineal(coleccion, clave, obtener_clave = None):
    """Devuelve el ítem cuya clave coincide, o None."""

    for elemento in coleccion:
        if obtener_clave is None:
            return elemento
        elif obtener_clave (elemento) == clave:
            return elemento
    return None #no encontrado: el CLI avisa, no explota
    
    # raise NotImplementedError


def busqueda_binaria(coleccion, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""
    izq = 0
    der = len (coleccion) - 1
    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave (coleccion[medio])
        if valor == clave:
            return coleccion [medio]
        elif valor < clave:
            izq = medio + 1 #la clave esta en la mitad derecha
        else:
            der = medio - 1 #la clave esta en la mitad izquierda
    return None #recorrimos todo y no esta
    
    # raise NotImplementedError
