# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- **Tema:** Biblioteca de Musica
- **Por qué lo eligieron (5–8 líneas):** Elegimos el tema de biblioteca musical para este trabajo práctico porque nos pareció una opción muy interesante y cercana a la realidad para aplicar los conceptos básicos de programación. Nos facilita la tarea de organizar elementos cotidianos, como las canciones, agrupando de forma ordenada sus atributos principales como el título, el artista y la duración. Además, consideramos que modelar un catálogo de música hace que el sistema sea más intuitivo de estructurar, permitiéndonos practicar de manera eficiente el manejo de colecciones y la interacción por consola que pide la materia.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

- **Item de catalogo**: La lista general del catálogo (permite agregar/quitar canciones) y los diccionarios de cada canción.
- **Mutable**: Lista de las canciones.
- **Inmutable**: Los strings (textos) con los nombres de títulos y artistas (EJ: {"titulo"}, {"artista"}).

- **Relacion (catalogo, coleccion principal y cola)**:
  * Catálogo / Colección principal: Lista que almacena todos los ítems disponibles.
  * Pila y cola: Se usarán más adelante para gestionar historiales y filas de reproducción.

```text
[ Menú / CLI ]
      │
      ▼
[ Catálogo ] (Colección Principal - Lista)
      │
      ├── [ Canción 1 ] (Diccionario mutable: título, artista, duración)
      ├── [ Canción 2 ] (Diccionario mutable: título, artista, duración)
      └── ...
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

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
