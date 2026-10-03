from tads.lista_enlazada import ListaEnlazada
from excepciones import *

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        #Agrega un elemento al final de la cola
        self._items.insertar_al_final(dato)

    def desencolar(self):
        #Retira el primer elemento de la cola
        if self.esta_vacia():
            raise ColaVaciaError("La Cola no contiene elementos.")
        nod_sacad = self._items._head
        self._items.eliminar(nod_sacad._dato)
        return nod_sacad._dato

    def ver_frente(self):
        #Observa el primer elemento sin sacarlo
        if self.esta_vacia():
            raise ColaVaciaError("La Cola no contiene elementos.")
        return self._items._head._dato

    def esta_vacia(self):
        return self._items.esta_vacia()
