from tads.lista_enlazada import ListaEnlazada
from persistencia.texto import cargar_texto

class Cancion: #Clase basica de una cancion, define su id, nombre, autor, album y genero
    def __init__(self, cancion_id, nombre, autor, album, genero, anio = 0, duracion_seg = 0):
        self.cancion_id = int (cancion_id)
        self.nombre = nombre
        self.autor = autor
        self.album = album
        self.genero = genero
        self.anio = int (anio)
        self.duracion_seg = float (duracion_seg)

    def __str__(self): #Cuando se ejecuta print() sobre una canciones, se corre esta funcion
        resumen = f"{self.cancion_id} | {self.nombre} | {self.autor} | {self.album} | {self.genero} | {self.anio} | {self.duracion_seg}"
        return resumen

    
def armar_catalogo_desde_txt(ruta):
    """Lee el .txt y devuelve la ListaEnlazada con objetos del dominio."""
    catalogo = ListaEnlazada()
    for fila in cargar_texto(ruta):
        fonoteca = Cancion(
            cancion_id=int(fila["id"]), # acá se convierten los números
            nombre=fila["titulo"],
            autor=fila["artista"],
            album=fila["album"] or None, # si viene vacío → None
            genero=fila["genero"],
            anio=int(fila["anio"]),
            duracion_seg=float(fila["duracion_seg"])
        )
        catalogo.insertar_al_final(fonoteca)
    return catalogo

def armar_evoluciones_desde_txt(ruta):
    """Devuelve un dict {origen_id: [destino_id, ...]} para la recursión de E2."""
    evoluciones = {}
    for fila in cargar_texto(ruta):
        origen = int(fila["cancion_id"])
        destino = int(fila["version_de_id"])
        evoluciones.setdefault(origen, []).append(destino)
    return evoluciones
