fonoteca = [
    {"cancion_id" : 1, "nombre" : "De musica ligera", "autor" : "Soda Stereo", "album" : "Cancion Animal", "genero" : "Rock"},
    {"cancion_id" : 2, "nombre" : "El pibe de los astilleros", "autor": "Patricio Rey y sus redonditos de ricota", "album": "La mosca y la sopa", "genero": "Rock"},
    {"cancion_id" : 3, "nombre" : "Hombre en U", "autor": "DIVIDIDOS", "album": "Amapola del 66", "genero": "Rock"},
    {"cancion_id" : 4, "nombre" : "El tren del cielo", "autor": "Soledad Pastorutti", "album": "Libre", "genero": "Folklore"},
    {"cancion_id" : 5, "nombre" : "Redemption Song", "autor": "Bob Marley and The Wailers", "album": "Uprising", "genero": "Roots Reggae"},
    {"cancion_id" : 6, "nombre" : "The Trooper", "autor": "Iron Maiden", "album": "Piece of Mind", "genero": "Heavy Metal"},       
    {"cancion_id" : 12, "nombre" : "Jijiji", "autor" : "Patricio Rey y sus Redonditos de Ricota", "album" : "Un Baion para el Ojo Idiota", "genero" : "Rock"},
    {"cancion_id" : 13, "nombre" : "Jijiji", "autor" : "Patricio Rey y sus Redonditos de Ricota", "album" : "En Directo", "genero" : "Rock"},
    {"cancion_id" : 16, "nombre" : "Sola en los Bares", "autor" : "Man Ray", "album" : "Perro de Playa", "genero" : "Pop Rock"},
    {"cancion_id" : 51, "nombre" : "Billie Jean", "autor" : "Michael Jackson", "album" : "Thriller", "genero" : "Pop"},
    {"cancion_id" : 52, "nombre" : "Billie Jean (Remix)", "autor" : "Michael Jackson", "album" : "Thriller 40", "genero" : "Pop"},
    {"cancion_id" : 61, "nombre" : "Sola en los Bares", "autor" : "Eruca Sativa", "album" : "Dopelganga", "genero" : "Rock"},
    {"cancion_id" : 62, "nombre" : "De musica ligera (Unplugged)", "autor" : "Soda Stereo", "album" : "Comfort y Musica Para Volar", "genero" : "Rock"}
]

import pandas as pd
from dominio.cancion import Cancion
from pathlib import Path

class Fonoteca:
    def __init__(self): #Funcion constructora de la Fonoteca, crea la fonoteca como una lista y el versiones.csv como un dataframe
        self.fonoteca = []
        for canc in fonoteca:
            new_can = Cancion(canc["cancion_id"], canc["nombre"], canc["autor"], canc["album"], canc["genero"])
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
    
