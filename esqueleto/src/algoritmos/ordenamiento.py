 def ordenar_seleccion(coleccion, clave):
    """Ordenamiento por selección. Devuelve una nueva secuencia, no usa sorted."""
    n = len (coleccion)
    for i in range (n - 1):
        pos_min = i
        for j in range (i + 1, n) :
            if obtener_clave (coleccion [j] < obtener_clave (coleccion [pos_min]))
                pos_min = j
            coleccion [i], coleccion [pos_min] = coleccion [pos_min], coleccion [i]
         return coleecion

     
    # raise NotImplementedError


def ordenar_insercion(coleccion, clave):
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted."""
    for i in range (1, len (coleccion)):
        actual = coleccion [i]
        j = i - 1
        while j >= 0 and obtener_clave (coleccion [j]) > obtener_clave (actual):
            coleccion [j + 1] = coleccion [j] #desplaza el mayot a la derecha
            j -= 1
        coleccion [j + 1] = actual #inserta el elemento en su lugar
    return coleccion

    # raise NotImplementedError
