class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
        self._head = None
        self._size = 0

    def esta_vacia(self):
        if self._size == 0:
            return True
        else:
            return False

    def tamanio(self):
        return self._size

    def insertar_al_inicio(self, dato):
        nuev_nod = Nodo(dato, self._head)
        self._head = nuev_nod
        self._size += 1

    def insertar_al_final(self, dato):
        nuev_nod = Nodo(dato)
        if self.esta_vacia():
            self._head = nuev_nod
        else:
            nod_act = self._head
            while nod_act._next is not None:
                nod_act = nod_act._next
            nod_act._next = nuev_nod
        self._size += 1

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError

    def eliminar(self, dato):
        if self.esta_vacia():
            return
        elif self._head._dato == dato:
            self._head = self._head._next
            self._size -= 1
            return
        else:
            nod_act = self._head
            while nod_act._next is not None:
                if nod_act._next._dato == dato:
                    nod_act._next = nod_act._next._next
                    self._size -= 1
                    return
                nod_act = nod_act._next
            return

    def buscar(self, dato):
        nod_act = self._size
        while nod_act is not None:
            if nod_act._dato == dato:
                return nod_act
            nod_act = nod_act._next
        return None

    def __iter__(self):
        return self._Iterador(self._head)

    class _Iterador:
        #Clase interna del iterador
        def __init__(self, head):
            self._actual = head

        def __iter__(self):
            return self

        def __next__(self):
            if self._actual is None:
                raise StopIteration
            dato = self._actual_dato
            self._actual = self._actual._next
            return dato
