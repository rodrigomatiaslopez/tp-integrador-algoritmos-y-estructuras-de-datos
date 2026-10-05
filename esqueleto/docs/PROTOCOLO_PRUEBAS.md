# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | pasa |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue | pasa |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa | pasa |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) | pasa |  |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | pasa |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | pasa |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | pasa |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | pasa |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |

# E2
* **Caso de prueba 1: Arranque y visualización del menú**
  
Verificar que al ejecutar el programa se cargue correctamente el archivo de configuración y se muestre en pantalla el título y las opciones del menú principal correspondientes al tema música.

*Resultado:* El menú se despliega indicando
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
  
Seleccionar la opción `1` del menú para listar las canciones disponibles en la fonoteca.

*Resultado:* Se imprimen en la consola todas las canciones cargadas inicialmente, mostrando de forma legible su nombre, autor, álbum y género.
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
  
Seleccionar la opción `2`, `3`, `4`, `6`, `7`, `8`, `9` del menú principal.

*Resultado:* El sistema responde ejecutando la función `pendiente()`, imprimiendo el mensaje 
  ```text
  Todavía no está implementado. Completar en la entrega que corresponde.
  ```
  sin romperse ni cerrarse.


* **Caso de prueba 4: Ejecución de la operación recursiva (con ID válido)**
  
Seleccionar la opción `5` e ingresar el ID numérico de una canción que posea versiones derivadas (por ejemplo, una canción original que tenga *covers* o *remixes* asociados).

*Resultado:* El sistema procesa la función recursiva de tu compañero (`versiones_deriv`), recorriendo las relaciones del archivo de datos y devolviendo la lista con todas las versiones derivadas encadenadas.     Ejemplo `1`
  ```text
  1 | De musica ligera |Soda Stereo |Cancion Animal |Rock
  62 |De musica ligera (Unplugged) |Soda Stereo |Comfort y Musica Para Volar | Rock
  ```


* **Caso de prueba 5: Operación recursiva (con ID inexistente o sin versiones)**
  
Seleccionar la opción `5` e ingresar un ID de canción que no exista en el sistema o que no tenga ninguna versión derivada registrada.

*Resultado:* El sistema detecta el caso base de la recursividad sin arrojar errores y retorna una lista vacía o un mensaje indicando que no hay derivados.
  ```text
  4 | El tren del cielo | Soledad Pastorutti | Libre | Folklore
  ```


* **Caso de prueba 6: Ingreso de opción de menú inválida**
  
Ingresar un número o letra que no esté contemplado en el menú principal (por ejemplo, escribir `99`).

*Resultado:* El sistema captura la opción por el bloque `else`, muestra el mensaje
  ```text
  Opción inválida.
  ```
  y vuelve a desplegar el menú para permitir un nuevo ingreso.

* **Caso de prueba 7: Salida correcta del programa**
  
Seleccionar la opción `0` del menú principal para salir del sistema.

*Resultadoo:* El programa imprime el mensaje de salida
   ```text
  Chau.
  ```
  y finaliza su ejecución de forma limpia interrumpiendo el bucle principal.

* **Caso de prueba 8: Comprobación de configuración del tema**
  
Modificar temporalmente el archivo `src/config.py` cambiando el valor de `TEMA` por un texto erróneo o vacío, e intentar correr el programa.

*Resultado:* El sistema valida la condición inicial del `main`, muestra la advertencia
  ```text
  Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.
  ```
  y frena la ejecución para evitar fallos mayores.

# E3
* **Caso de prueba 1: Agregar a la colección principal hasta el tope (Lista enlazada)**
  
Al seleccionar la opcion `6. Coleccion principal (playlist)` se desplega el menu interactivo para agregar una cancion, 

`1` cuando se agrega una cancion a la playlist el programa directamente no te deja agregar mas canciones.

`2` para eliminar una cancion de la playlist.
  ```text
  === Menu: [1] Agregar cancion a la playlist [2] Eliminar cancion de la playlist  [0] Salir ===
  Ingrese opcion: 1
  Ingresá el ID de la canción para agregar [0 para finalizar]: 1
  1 | De musica ligera | Soda Stereo | Cancion Animal | Rock || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 2
  2 | El pibe de los astilleros | Patricio Rey y sus redonditos de ricota | La mosca y la sopa | Rock || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 3
  3 | Hombre en U | DIVIDIDOS | Amapola del 66 | Rock || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 4
  4 | El tren del cielo | Soledad Pastorutti | Libre | Folklore || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 5
  5 | Redemption Song | Bob Marley and The Wailers | Uprising | Roots Reggae || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 6
  6 | The Trooper | Iron Maiden | Piece of Mind | Heavy Metal || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 12
  12 | Jijiji | Patricio Rey y sus Redonditos de Ricota | Un Baion para el Ojo Idiota | Rock || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 13
  13 | Jijiji | Patricio Rey y sus Redonditos de Ricota | En Directo | Rock || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 16
  16 | Sola en los Bares | Man Ray | Perro de Playa | Pop Rock || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 52
  52 | Billie Jean (Remix) | Michael Jackson | Thriller 40 | Pop || Agregada a la playlist....
  + Canción agregada exitosamente a tu playlist.
  Ingresá el ID de la canción para agregar [0 para finalizar]: 62
  - 
  La playlist esta llena (maximo 10 canciones).
  ```

* **Caso 2: Desapilar historial vacío (Pila)**
* 
Al seleccionar la opcion `7. Historial (pila)` se desplega el menu interactivo.

`1` para ver la playlist (agregada en opcion 6 (ref: caso 3.1) ), `2` para ver la cancion actual de la lista de reproduccion (cola), `3` para ver cancion anterior (pila) `0`.
  ```text
    === Menu: [1] Ver playlist [2] Cancion actual [3] Cancion anterior [0] Salir ===
    Ingrese opcion: 3
    - La Pila no tiene elementos.
  ```
  
* **Caso 3: Desencolar cola vacía**
  Al seleccionar la opcion `8. Cola` se desplega el menu interactivo.
  
  `1` para encolar un tema, `2` para mostrar la lista (cola) completa y `3` para reproducir y poner la siguiente cancion.

  Usamos la opcion `8` para desencolar la cola vacia.
  ```text
  === [1] Encolar tema [2] Mostrar lista completa [3] Reproducir | Cancion siguiente [0] Salir ===
    Ingrese la opcion: 3
    - La Cola no contiene elementos.
  ```

* **Caso 4: Listar colección con el iterador**
  Al seleccionar la opcion `7. Historial (pila)` se desplega el menu interactivo.
  
  `1` para ver la playlist, `2`, para ver la cancion actual  y `3` para la cancion anterior.

  Usamos `1` para ver la playlist coleccion con el iterador.
  ```text
  === Menu: [1] Ver playlist [2] Cancion actual [3] Cancion anterior [0] Salir ===
  Ingrese opcion: 1
  --- Mi Playlist ---
  [0] 1 | De musica ligera | Soda Stereo | Cancion Animal | Rock
  [1] 2 | El pibe de los astilleros | Patricio Rey y sus redonditos de ricota | La mosca y la sopa | Rock
  [2] 3 | Hombre en U | DIVIDIDOS | Amapola del 66 | Rock
  [3] 4 | El tren del cielo | Soledad Pastorutti | Libre | Folklore
  [4] 5 | Redemption Song | Bob Marley and The Wailers | Uprising | Roots Reggae
  [5] 6 | The Trooper | Iron Maiden | Piece of Mind | Heavy Metal
  [6] 12 | Jijiji | Patricio Rey y sus Redonditos de Ricota | Un Baion para el Ojo Idiota | Rock
  [7] 13 | Jijiji | Patricio Rey y sus Redonditos de Ricota | En Directo | Rock
  [8] 16 | Sola en los Bares | Man Ray | Perro de Playa | Pop Rock
  [9] 52 | Billie Jean (Remix) | Michael Jackson | Thriller 40 | Pop
  ```
