# TP integrador — AyED C2 2026

Repositorio del grupo. Partir de este esqueleto. No borrar la estructura de `src/` ni de `docs/`.

## Integrantes

| Nombre | Mail | GitHub |
| --- | --- | --- |
| Rodrigo Matias Lopez | rodlopez003@gmail.com | rodrigomatiaslopez |
| Camila Belen Passini | camilitapass@yahoo.com.ar | camipass |
| Emiliano Nicolas Blanco | emilianonicblanco@gmail.com | Longchamps27 |

**Tema elegido:** Biblioteca musical

## Cómo ejecutar

Desde la raíz del repo, con Python 3.10 o superior:

```text
python -m src.main
```

En Windows, si `python` no anda: `py -3 -m src.main`.

Solo biblioteca estándar. No hay `requirements.txt` a propósito.

## Que hace
Menu de catálogo de una biblioteca musical con las siguientes 9 operaciones:
-Listar el catálogo
-Ver detalles de una canción del catálogo
-Buscar (lineal y binaria)
-Ordenar (selección e inserción)
-Operación recursiva (Detección de todas las versiones de una cancion) 
-Armado de playlist con tope de 10
-Historial (pila de la playlist)
-Cola
-Guardado y lectura de la biblioteca musical en .txt y binario con struct

## Que no hace
Los archivos de prueba para errores del guardado y lectura en .txt y binario fueron armados a mano,
el programa no los puede generar. Si puede crear una playlist vacia en caso de que no exista ninguna.

## Entregas

Cada vencimiento se marca con un tag. Ver `GIT.md`.

| Tag | Vence |
| --- | --- |
| `preentrega` (opcional, solo repo) | domingo 30-ago-2026 23:59 |
| `entrega-1` | domingo 06-sep-2026 23:59 |
| `entrega-2` | domingo 20-sep-2026 23:59 |
| `entrega-3` | domingo 04-oct-2026 23:59 |
| `entrega-4` | domingo 01-nov-2026 23:59 |
| `entrega-5` | domingo 15-nov-2026 23:59 |
| `entrega-6` | domingo 22-nov-2026 23:59 |

Defensa oral (reemplaza el 2do parcial): 25 y 27-nov-2026.

La cátedra corrige el **tag**, no el último commit suelto de `main`.

El grupo se avisa por mail a diego.ambrossio@unab.edu.ar **y** angel.bianco@unab.edu.ar. Ver `GIT.md`.
