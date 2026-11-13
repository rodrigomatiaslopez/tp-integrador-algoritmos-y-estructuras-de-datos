"""Registros de longitud fija con struct.

Layout sugerido (documentar el definitivo en docs/INFORME.md):

Header:
  magia     4s   b'AYED'
  tema      1s   b'P' | b'R' | b'M'
  cantidad  I    unsigned int

El registro depende del tema. Ejemplo Pokédex:
  id          I
  nombre     20s
  tipo1      12s
  tipo2      12s
  hp          H
  ataque      H
  defensa     H
  velocidad   H
  generacion  H
"""

import struct
from pathlib import Path
from excepciones import ArchivoInvalidoError
from dominio.cancion import Cancion
from tads.lista_enlazada import ListaEnlazada
from excepciones import *


FORMATO = struct.Struct("<I 20s 12s 12s 12s 4H") # 60 bytes por registro
HEADER = struct.Struct("<4s 1s I") # 9 bytes: magia, tema, cantidad
TEMA = b"M" # Pokédex: P · Recetario: R · Música: M

def _a_bytes(texto, ancho):
  return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")


def _a_texto(datos):
  return datos.rstrip(b"\x00").decode("utf-8")


def _item_a_tupla(c):
  """Objeto del dominio → tupla lista para FORMATO.pack. AJUSTÁ A TU TEMA."""
  return (
        int(c.cancion_id),
        _a_bytes(c.nombre, 20),
        _a_bytes(c.autor, 12),
        _a_bytes(c.album, 12),
        _a_bytes(c.genero, 12),
        int (c.anio),
        int (c.duracion_seg),
        0,
        0
  )


def _tupla_a_item(t):
  """Tupla que salió de FORMATO.unpack → objeto del dominio. AJUSTÁ A TU TEMA."""
  return Cancion(
        cancion_id=t[0],
        nombre=_a_texto(t[1]),
        autor=_a_texto(t[2]),
        album=_a_texto(t[3]),
        genero=_a_texto(t[4]),
        anio=int (t[5]),
        duracion_seg=float (t[6]),
    )


def guardar_binario(ruta, catalogo):
    """Escribe el archivo completo: header (magia + tema + cantidad) + registros."""
    with open(ruta, "wb") as archivo:
      archivo.write(HEADER.pack(b"AYED", TEMA, catalogo.tamanio()))
      for item in catalogo: # iterador de E3 otra vez
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))


def cargar_binario(ruta):
    """Lee el binario con validaciones. Devuelve la ListaEnlazada de ítems."""
    with open(ruta, "rb") as archivo:
      cabecera = archivo.read(HEADER.size)
      if len(cabecera) < HEADER.size:
        raise ArchivoInvalidoError("Binario truncado: ni siquiera tiene header completo.")
      magia, tema, cantidad = HEADER.unpack(cabecera)
      if magia != b"AYED":
        raise ArchivoInvalidoError("Magia incorrecta: este archivo no es de este TP.")
      if tema != TEMA:
        raise ArchivoInvalidoError(f"El tema del archivo ({tema!r}) no es el mío ({TEMA!r}).")
      catalogo = ListaEnlazada()
      for _ in range(cantidad):
        datos = archivo.read(FORMATO.size)
        if len(datos) < FORMATO.size:
          raise ArchivoInvalidoError(
        "Binario truncado: el header dice más registros de los que hay."
        )
        catalogo.insertar_al_final(_tupla_a_item(FORMATO.unpack(datos)))
    return catalogo

def actualizar_registro(ruta, posicion, item):
  """Pisa SOLO el registro número 'posicion' (0-based) sin tocar el resto."""
  with open(ruta, "r+b") as archivo: # r+b = leer Y escribir
    archivo.seek(HEADER.size + posicion * FORMATO.size) # el salto del dibujo
    archivo.write(FORMATO.pack(*_item_a_tupla(item)))

def posicion_del_id(catalogo, id_buscado):
  """Devuelve la posición (0-based) del ítem con ese id, usando el iterador."""
  for posicion, item in enumerate(catalogo):
    if item.id == id_buscado:
      return posicion
  raise ItemNoEncontradoError (f"No hay ítem con id {id_buscado}")
