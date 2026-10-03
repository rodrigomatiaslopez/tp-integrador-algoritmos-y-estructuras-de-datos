# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- **Tema:** Biblioteca de Musica
- **Por qué lo eligieron (5–8 líneas):** Elegimos el tema de biblioteca musical para este trabajo práctico porque nos pareció una opción muy interesante y cercana a la realidad para aplicar los conceptos básicos de programación. Nos facilita la tarea de organizar elementos cotidianos, como las canciones, agrupando de forma ordenada sus atributos principales como el título, el artista y la duración. Además, consideramos que modelar un catálogo de música hace que el sistema sea más intuitivo de estructurar, permitiéndonos practicar de manera eficiente el manejo de colecciones y la interacción por consola que pide la materia.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

- **Item de catalogo**: La lista general del catálogo (permite agregar/quitar canciones) y los diccionarios de cada canción.
- **Mutable**: Lista de las canciones. Son mutables para permitir la manipulación dinámica de los datos, pudiendo agregar o quitar elementos del catálogo.
- **Inmutable**: Los strings (textos) con los nombres de títulos y artistas (EJ: {"titulo"}, {"artista"}). Son inmutables para proteger la integridad de la información original.

```text
[ Menú / CLI ]
      │
      ▼
[ Fonoteca ] (Colección Principal - Lista)
      │
      ├── [ Canción 1 ] (Diccionario mutable: título, artista, duración)
      ├── [ Canción 2 ] (Diccionario mutable: título, artista, duración)
      └── ...
```

## 3. Recursión (E2)

* **Función:** Permite buscar de forma encadenada todas las versiones derivadas (covers, remixes, lives, etc.) a partir de una canción original, utilizando los datos provistos en el archivo CSV de relaciones.


* **Caso base:** La función busca las versiones asociadas a un ID y **no encuentra ningún registro derivado**. En ese momento, la función detiene las llamadas recursivas y retorna una lista vacía, evitando un bucle infinito.


* **Caso recursivo:** Se ejecuta cuando la función encuentra que una canción tiene una o más versiones asociadas en el archivo de datos. Por cada coincidencia encontrada, **la función se vuelve a invocar a sí misma** pasando el ID de la nueva versión derivada para explorar si a su vez posee más ramificaciones, acumulando los resultados.


#### **Traza de un ejemplo real del dataset:**
* **Punto de partida:** Tomamos como canción de origen el ID `1` (*"De música ligera"* de Soda Stereo).
* **Llamada 1:** Se ejecuta `fonoteca.versiones_deriv(1)`. El sistema busca en el archivo `versiones.csv` y detecta que la canción con ID `62` (*"De música ligera (Unplugged)"*) es una versión derivada de la original. Como encontró un derivado, se autoinvoca: `self.versiones_deriv(62)`.
* **Llamada 2 (Recursiva):** Se ejecuta `self.versiones_deriv(62)`. El sistema busca si la canción ID `62` tiene otras versiones derivadas a partir de ella.
* **Llegada al caso base:** Al no encontrar más registros derivados para la ID `62`, la función alcanza el caso base.
* **Resultado final:** La función devuelve la lista consolidada con la cadena de versiones encontradas a partir del ID inicial.


---

## 4. TADs (E3)

### 4. TADs (E3)

| TAD | Operaciones | Invariante |
| :--- | :--- | :--- |
| **ListaEnlazada** | `insertar_al_inicio(elem)`<br>`insertar_al_final(elem)`<br>`eliminar(elem)`<br>`tamanio()`<br>`esta_vacia()`<br>`__iter__()` | Secuencia lineal encadenada de nodos. Si `tamanio == 0`, `cabeza` es `None`; en caso contrario, `cabeza` referencia al primer nodo y el puntero siguiente del último nodo referencia a `None`. |
| **Pila** | `apilar(elem)`<br>`desapilar()`<br>`ver_tope()`<br>`esta_vacia()`<br>`tamanio()` | **LIFO (Last In, First Out):** El último elemento en ingresar es estrictamente el primero en salir. El acceso, inserción y remoción se realizan exclusivamente por el tope. |
| **Cola** | `encolar(elem)`<br>`desencolar()`<br>`frente()`<br>`esta_vacia()`<br>`tamanio()` | **FIFO (First In, First Out):** El primer elemento en ingresar es estrictamente el primero en salir. Las inserciones se realizan por el extremo final y las remociones por el frente. |

**Dónde se usa cada uno en el dominio:**

* **ListaEnlazada → Playlist (Colección Principal con Tope):** Se utiliza para almacenar y persistir la colección de canciones del usuario, permitiendo listar el contenido y controlar que no se sobrepase el límite máximo de capacidad (`ColeccionLlenaError`).
* **Pila → Historial de Reproducción:** Almacena de forma cronológica inversa las canciones ya reproducidas. Al ser LIFO, permite la funcionalidad de "retroceder" o volver a escuchar la pista inmediatamente anterior.
* **Cola → Fila de Reproducción ("A continuación"):** Gestiona los temas en espera de sonar. Al regirse por FIFO, asegura que las canciones se reproduzcan en el orden de llegada en que fueron agregadas.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
