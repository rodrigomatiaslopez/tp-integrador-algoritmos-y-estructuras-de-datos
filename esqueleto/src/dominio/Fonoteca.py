import pandas as pd
from dominio.cancion import Cancion
from pathlib import Path

from tads import ListaEnlazada, Pila, Cola
from excepciones import *

fonoteca = [
    {"cancion_id" : 1, "titulo" : "De musica ligera", "autor" : "Soda Stereo", "album" : "Cancion Animal", "genero" : "Rock", "anio":1990, "duracion":213},
    {"cancion_id" : 2, "titulo" : "El pibe de los astilleros", "autor": "Patricio Rey y sus redonditos de ricota", "album": "La mosca y la sopa", "genero": "Rock", "anio":1986, "duracion":263},
    {"cancion_id" : 3, "titulo" : "Hombre en U", "autor": "DIVIDIDOS", "album": "Amapola del 66", "genero": "Rock", "anio":1988, "duracion":451},
    {"cancion_id" : 4, "titulo" : "El tren del cielo", "autor": "Soledad Pastorutti", "album": "Libre", "genero": "Folklore", "anio":2001, "duracion":210},
    {"cancion_id" : 5, "titulo" : "Redemption Song", "autor": "Bob Marley and The Wailers", "album": "Uprising", "genero": "Roots Reggae", "anio":1980, "duracion":227},
    {"cancion_id" : 6, "titulo" : "The Trooper", "autor": "Iron Maiden", "album": "Piece of Mind", "genero": "Heavy Metal", "anio":1983, "duracion":251},       
    {"cancion_id" : 12, "titulo" : "Jijiji", "autor" : "Patricio Rey y sus Redonditos de Ricota", "album" : "Un Baion para el Ojo Idiota", "genero" : "Rock", "anio":1986, "duracion":240},
    {"cancion_id" : 13, "titulo" : "Jijiji", "autor" : "Patricio Rey y sus Redonditos de Ricota", "album" : "En Directo", "genero" : "Rock", "anio":1992, "duracion":318},
    {"cancion_id" : 16, "titulo" : "Sola en los Bares", "autor" : "Man Ray", "album" : "Perro de Playa", "genero" : "Pop Rock", "anio":1991, "duracion":183},
    {"cancion_id" : 51, "titulo" : "Billie Jean", "autor" : "Michael Jackson", "album" : "Thriller", "genero" : "Pop", "anio":1982, "duracion":294},
    {"cancion_id" : 52, "titulo" : "Billie Jean (Remix)", "autor" : "Michael Jackson", "album" : "Thriller 40", "genero" : "Pop", "anio":2022, "duracion":292},
    {"cancion_id" : 61, "titulo" : "Sola en los Bares", "autor" : "Eruca Sativa", "album" : "Dopelganga", "genero" : "Rock", "anio":206, "duracion":2022},
    {"cancion_id" : 62, "titulo" : "De musica ligera (Unplugged)", "autor" : "Soda Stereo", "album" : "Comfort y Musica Para Volar", "genero" : "Rock", "anio":1996, "duracion":221}
]


class Fonoteca:
    def __init__(self): #Funcion constructora de la Fonoteca, crea la fonoteca como una lista y el versiones.csv como un dataframe
        self.fonoteca = []
        for canc in fonoteca:
            new_can = Cancion(canc["cancion_id"], canc["titulo"], canc["autor"], canc["album"], canc["genero"])
            self.fonoteca.append(new_can)
        base_dir = Path(__file__).resolve().parents[2]
        versiones_path = base_dir / "data" / "versiones.csv"
        self.versiones_list = pd.read_csv(versiones_path) 

    def listar(self): #Funcion que 
        for f in self.fonoteca:
            print(f)

    def buscar(self, id_ca): #Funcion que busca una id dada y nos devuelve la cancion correspondiente
        for can in self.fonoteca:
            if can.cancion_id == id_ca:
                return can
        else:
            return None
            #print("Esa cancion no existe")

    def versiones_deriv(self, idc_ori): #Le pasamos la id de la cancion original para ver si tiene versiones
        df_ver = self.versiones_list
        _versiones = self.buscar(idc_ori)
        if not _versiones: #CASO BASE
            return []
        resultado = [_versiones]
        for _, can in df_ver.iterrows(): #CASO RECURSIVO
            if _versiones.cancion_id == can["version_de_id"]:
                idv_deriv = can["cancion_id"]
                resultado += self.versiones_deriv(idv_deriv)
        return resultado

    def mostrar_detalle (self, cancion) : #funcion que busca la id de la cancion y devuelve los detalles
        for can in fonoteca :
            if can ["cancion_id"] == cancion:
                print (f"Año: {can["anio"]} | Duracion: {can["duracion"]} segundos | Titulo: {can ["titulo"]}")
                return
            
        print (f"ID ({cancion}) no existe en la lista de canciones")

    
class Reproductor:

    def __init__ (self, catalogo, tope = 10) : #constructor de reproductor para la playlist
        self._playlist = ListaEnlazada ()
        self._historial = Pila ()
        self._proximos = Cola ()
        self._tope = tope
        self._fonoteca = catalogo
        self._playlist_tamanio = 0

    def agregar_playlist(self, id_cancion) : #se agregan canciones a la playlist con tope maximo de 50
        cancion = self._fonoteca.buscar(id_cancion)
        if cancion is None:
            raise ItemNoEncontradoError(f"No se encontró ninguna canción con el ID ({id_cancion}) en el catálogo.")    
        elif self._playlist_tamanio >= self._tope:
            raise ColeccionLlenaError (f"La playlist esta llena (maximo {self._tope} canciones).")
        else:
            if cancion in self._playlist :
                print ("No se puede repetir la cancion.")
            else:
                print (f"{cancion} | Agregada a la playlist....")
                self._playlist.insertar_al_final (cancion)
                self._playlist_tamanio += 1

    def cancion_actual (self) :

        return self._historial.ver_tope ()

    def encolar_tema(self, id_cancion) : #agrega a la cola las proximas canciones
        cancion = self._fonoteca.buscar(id_cancion)
        if cancion is None:
            raise ItemNoEncontradoError(f"El ID '{id_cancion}' no existe en el catálogo.")

        else:
            print (f"{cancion} | Agregada a la lista de reproduccion....")
            self._proximos.encolar (cancion)


    def cancion_siguiente (self) : #saca la cancion de la cola y lo guarda en el historial
        cancion = self._proximos.desencolar ()
        self._historial.apilar(cancion)
        return cancion

    def cancion_anterior (self) : #
        return self._historial.desapilar()

    def eliminar(self, id_cancion) :

        self.listar_playlist()
        # 1. Buscamos el objeto Cancion original en la Fonoteca
        cancion = self._fonoteca.buscar(id_cancion)
        if cancion is None:
            raise ItemNoEncontradoError(f"El ID '{id_cancion}' no existe en el catálogo.")  
        # 2. Delegamos en buscar() de la ListaEnlazada para ver si está en la playlist
        if self._playlist.buscar(cancion) is None:
            raise ItemNoEncontradoError("La canción no se encuentra guardada en tu playlist.")
            
        # 3. Delegamos en eliminar() de la ListaEnlazada
        self._playlist.eliminar(cancion)

    def listar_playlist(self) : 
        contador = 0
        if self._playlist.esta_vacia():
            print("Tu playlist está vacía.")
            return
        else:
            print("--- Mi Playlist ---")
            for p in self._playlist:
                print (f"[{contador}] {p}")
                contador += 1

    def listar_proximos(self) : 
            contador = 0
            if self._proximos.esta_vacia():
                print("Tu lista de reproduccion está vacía.")
                return
            else:
                print("--- Lista de reproduccion ---")
                for p in self._proximos._items:
                    print (f"[{contador}] {p}")
                    contador += 1
