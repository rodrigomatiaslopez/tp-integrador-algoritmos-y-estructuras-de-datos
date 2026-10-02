class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        #Agrega al inicio de la pila
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        #Retira el primer elemento de la pila
        if self.esta_vacia():
            raise PilaVaciaError("La Pila no contiene elementos.")
        nod_sacad = self._items.buscar(self._items._head._dato)
        self._items.eliminar(self._items._head._dato)
        return nod_sacad._dato

    def ver_tope(self):
        #Observa el primer elemento sin sacarlo
        if self.esta_vacia():
            raise PilaVaciaError("La Pila no contiene elementos.")
        return self._items._head._dato

    def esta_vacia(self):
        return self._items.esta_vacia()
