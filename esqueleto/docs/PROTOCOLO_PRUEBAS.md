# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa |  |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) |  |  |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |

#E2
* **Caso de prueba 1: Arranque y visualización del menú**
- Verificar que al ejecutar el programa se cargue correctamente el archivo de configuración y se muestre en pantalla el título y las opciones del menú principal correspondientes al tema música.
- *Resultado:* El menú se despliega indicando
  ```text
  === Biblioteca musical — AyED C2 2026 ===
  1. Listar catálogo
  2. Ver detalle
  3. Buscar
  4. Ordenar
  5. Operación recursiva
  6. Colección principal (equipo / menú / playlist)
  7. Historial (pila)
  8. Cola
  9. Guardar / cargar archivos
  0. Salir
  ```
  junto a sus respectivas opciones numéricas.


* **Caso de prueba 2: Listar el catálogo completo**
- Seleccionar la opción `1` del menú para listar las canciones disponibles en la fonoteca.
- *Resultado:* Se imprimen en la consola todas las canciones cargadas inicialmente, mostrando de forma legible su nombre, autor, álbum y género.
```text
  1 | De musica ligera | Soda Stereo | Cancion Animal | Rock
  2 | El pibe de los astilleros | Patricio Rey y sus redonditos de ricota | La mosca y la sopa | Rock
  3 | Hombre en U | DIVIDIDOS | Amapola del 66 | Rock
  4 | El tren del cielo | Soledad Pastorutti | Libre | Folklore
  5 | Redemption Song | Bob Marley and The Wailers | Uprising | Roots Reggae
  6 | The Trooper | Iron Maiden | Piece of Mind | Heavy Metal
  12 | Jijiji | Patricio Rey y sus Redonditos de Ricota | Un Baion para el Ojo Idiota | Rock
  13 | Jijiji | Patricio Rey y sus Redonditos de Ricota | En Directo | Rock
  16 | Sola en los Bares | Man Ray | Perro de Playa | Pop Rock
  51 | Billie Jean | Michael Jackson | Thriller | Pop
  52 | Billie Jean (Remix) | Michael Jackson | Thriller 40 | Pop
  61 | Sola en los Bares | Eruca Sativa | Dopelganga | Rock
  62 | De musica ligera (Unplugged) | Soda Stereo | Comfort y Musica Para Volar | Rock
```


* **Caso de prueba 3: Menu en proceso**
- Seleccionar la opción `2`, `3`, `4`, `6`, `7`, `8`, `9` del menú principal.
- *Resultado:* El sistema responde ejecutando la función `pendiente()`, imprimiendo el mensaje 
  ```text
    Todavía no está implementado. Completar en la entrega que corresponde.
  ```
  sin romperse ni cerrarse.


* **Caso de prueba 4: Ejecución de la operación recursiva (con ID válido)**
- Seleccionar la opción `5` e ingresar el ID numérico de una canción que posea versiones derivadas (por ejemplo, una canción original que tenga *covers* o *remixes* asociados).
- *Resultado:* El sistema procesa la función recursiva de tu compañero (`versiones_deriv`), recorriendo las relaciones del archivo de datos y devolviendo la lista con todas las versiones derivadas encadenadas.
  ```text
  
  ```


* **Caso de prueba 5: Operación recursiva (con ID inexistente o sin versiones)**
-  Seleccionar la opción `5` e ingresar un ID de canción que no exista en el sistema o que no tenga ninguna versión derivada registrada.
- *Resultado:* El sistema detecta el caso base de la recursividad sin arrojar errores y retorna una lista vacía o un mensaje indicando que no hay derivados.
- 


* **Caso de prueba 6: Ingreso de opción de menú inválida**
- Ingresar un número o letra que no esté contemplado en el menú principal (por ejemplo, escribir `99` o una letra `abc`).
- *Resultado esperado:* El sistema captura la opción por el bloque `else`, muestra el mensaje *"Opción inválida."* y vuelve a desplegar el menú para permitir un nuevo ingreso.


* **Caso de prueba 7: Salida correcta del programa**
-  Seleccionar la opción `0` del menú principal para salir del sistema.
- *Resultado esperado:* El programa imprime el mensaje de salida (*"Chau."*) y finaliza su ejecución de forma limpia interrumpiendo el bucle principal.


* **Caso de prueba 8: Comprobación de configuración del tema**
- Modificar temporalmente el archivo `src/config.py` cambiando el valor de `TEMA` por un texto erróneo o vacío, e intentar correr el programa.
- *Resultado esperado:* El sistema valida la condición inicial del `main`, muestra la advertencia *"Seteá TEMA en src/config.py..."* y frena la ejecución para evitar fallos mayores.

