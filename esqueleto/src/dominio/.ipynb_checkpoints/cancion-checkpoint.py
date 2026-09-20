class Cancion: #Clase basica de una cancion, define su id, nombre, autor, album y genero
    def __init__(self, cancion_id, nombre, autor, album, genero):
        self.cancion_id = cancion_id
        self.nombre = nombre
        self.autor = autor
        self.album = album
        self.genero = genero

    def __str__(self): #Cuando se ejecuta print() sobre una canciones, se corre esta funcion
        resumen = self.nombre + " | " + self.autor + " | " + self.album + " | " + self.genero
        return resumen