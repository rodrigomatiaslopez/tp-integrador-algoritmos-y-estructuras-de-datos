from config import TEMA
from dominio.Fonoteca import Fonoteca, Reproductor
from excepciones import *
from algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from persistencia import binario, texto
from persistencia.texto import cargar_texto, guardar_texto
from persistencia.binario import guardar_binario, cargar_binario, posicion_del_id, alta_binario, baja_binario, actualizar_registro
from dominio.cancion import Cancion, armar_catalogo_desde_txt
from pathlib import Path
import time


fonoteca = Fonoteca()
reproductor = Reproductor(catalogo=fonoteca, tope = 10)

RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data"

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}
ENCABEZADOS = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]
RUTA_TXT = DATA / "canciones.csv"
RUTA_BIN = DATA / "canciones.bin"
RUTA_TXT_PLAY = DATA / "playlist.csv"
RUTA_BIN_PLAY = DATA / "playlist.bin"

def filas_del_catalogo(catalogo):
    """Convierte los objetos del dominio en dicts para guardar_texto."""
    filas = []
    for c in catalogo: # usa el ITERADOR de la lista (E3)
        filas.append({
            "id": c.cancion_id,
            "titulo": c.nombre,
            "artista": c.autor,
            "album": c.album,
            "genero": c.genero,
            "anio": c.anio,
            "duracion_seg": c.duracion_seg
        })
    return filas

def guardar_todo(catalogo):
    """Guarda el catálogo en los dos formatos. Memoria y archivos quedan iguales."""
    guardar_texto(RUTA_TXT, filas_del_catalogo(catalogo), ENCABEZADOS)
    guardar_binario(RUTA_BIN, catalogo)


def listar_canciones():
    fonoteca.listar()

def mostrar_detalle (id_cancion):
    fonoteca.mostrar_detalle (id_cancion)


def operacion_recursiva (): 
    idc = None
    while idc == None: #Elegimos la cancion de la cual queremos ver las versiones existentes y se imprime el resultado
        print("Ingrese el id de la cancion de la cual desee conocer las versiones: ")
        idc = int (input())
        resultado_recursivo = fonoteca.versiones_deriv(idc)
        for can_ver in resultado_recursivo:
            print(can_ver)

def medir_tiempo(funcion, datos, *args, **kwargs):
    # Medición con dataset original (n)
    inicio = time.perf_counter()
    resultado_original = funcion(datos, *args, **kwargs)
    fin = time.perf_counter()
    t_original = fin - inicio

    # Medición con dataset 10 veces más grande (10n)
    datos_grandes = datos * 10
    inicio_grande = time.perf_counter()
    funcion(datos_grandes, *args, **kwargs)
    fin_grande = time.perf_counter()
    t_grande = fin_grande - inicio_grande

    # Imprimimos los tiempos en consola
    print(f"⏱ Tiempo (n={len(datos)}): {t_original:.6f} s")
    print(f"⏱ Tiempo (n={len(datos_grandes)}): {t_grande:.6f} s\n")

    return resultado_original

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"==== {nombre} — AyED C2 2026 ====")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():

    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    catalogo_ordenado_por = None
 
    while opcion != 0:
        mostrar_menu()
        opcion = int (input("> ").strip())

        if opcion == 0:
            print("Chau.")

        elif opcion == 1:
            listar_canciones()

        elif opcion == 2:
            id_cancion = int (input("Ingrese el ID de la cancion: "))
            mostrar_detalle(id_cancion)

        elif opcion == 3:
            subopcion_1 = None
        
            while subopcion_1 != 0:
                print ("\nBuscar por: [1] Nombre (lineal) | [2] Nombre (binaria) | [0] Salir")
                subopcion_1 = int (input ("Ingrese opcion: "))

                if subopcion_1 == 1:
                    nombre = str (input ("Ingresa el nombre: "))
                    resultado_lineal = medir_tiempo(
                        busqueda_lineal, 
                        list(fonoteca.fonoteca), 
                        nombre, 
                        obtener_clave=lambda x: x.nombre
                    )
                    if resultado_lineal :
                        print (f"\nEncontrado: {resultado_lineal}")
                    else:
                        print ("No se encontro el elemento.\n")

                elif subopcion_1 == 2:
                # Validar que el catálogo esté ordenado previamente
                    if catalogo_ordenado_por != "nombre":
                        print("\n[ALERTA] No se puede ejecutar Búsqueda Binaria.")
                        print("El catálogo no está ordenado por nombre. Por favor, ordénelo primero desde la opción 4.\n")
                    else:
                        nombre = str (input ("Ingresa el nombre: "))
                        resultado_binaria = medir_tiempo(
                            busqueda_binaria, 
                            list(fonoteca.fonoteca), 
                            nombre, 
                            obtener_clave=lambda i: i.nombre
                        )
                        if resultado_binaria :
                            print (f"Encontrado: {resultado_binaria}\n")
                        else:
                            print ("No se encontro el elemento.\n")
                    
                elif subopcion_1 == 0:
                    break

                else:
                    print ("Ingrese una opcion correcta.")

        elif opcion == 4:
            subopcion_2 = None

            while subopcion_2 != 0 :
                print ("\nOrdenar por: [1] Nombre | [2] Autor | [0] Salir")
                subopcion_2 = int (input ("Ingresa la opcion: "))

                if subopcion_2 == 1 :
                    coleccion = int (input ("[1] Seleccion.... | [2] Insercion | [0] Salir: "))
                    if coleccion == 1:
                        resultado_seleccion = medir_tiempo(
                            ordenar_seleccion, 
                            list(fonoteca.fonoteca), 
                            obtener_clave=lambda j: j.nombre
                        )
                                                
                        # Guardamos el resultado ordenado en el catálogo para que persista
                        fonoteca.fonoteca = resultado_seleccion
                        catalogo_ordenado_por = "nombre"
                                                
                        print("---- Catálogo ordenado por Selección ----")
                        fonoteca.listar()

                    elif coleccion == 2:
                        resultado_insercion = medir_tiempo(
                            ordenar_insercion, 
                            list(fonoteca.fonoteca), 
                            obtener_clave=lambda p: p.nombre
                        )
                        
                        fonoteca.fonoteca = resultado_insercion
                        catalogo_ordenado_por = "nombre"
                        
                        print("---- Catálogo ordenado por Inserción ----")
                        fonoteca.listar()

                    elif coleccion == 0:
                        pass
                    else: 
                        print("Opción incorrecta.")

                    
                elif subopcion_2 == 2:
                    coleccion = int (input ("[1] Seleccion.... | [2] Insercion : "))
                    if coleccion == 1:
                        resultado_seleccion = medir_tiempo(
                            ordenar_seleccion, 
                            list(fonoteca.fonoteca), 
                            obtener_clave=lambda j: j.autor
                        )
                                                
                        # Guardamos el resultado ordenado en el catálogo para que persista
                        fonoteca.fonoteca = resultado_seleccion
                        catalogo_ordenado_por = "autor"
                                                
                        print("---- Catálogo ordenado por Selección ----")
                        fonoteca.listar()

                    elif coleccion == 2:
                        resultado_insercion = medir_tiempo(
                            ordenar_insercion, 
                            list(fonoteca.fonoteca), 
                            obtener_clave=lambda p: p.autor
                        )
                        
                        fonoteca.fonoteca = resultado_insercion
                        catalogo_ordenado_por = "autor"
                        
                        print("---- Catálogo ordenado por Inserción ----")
                        fonoteca.listar()


                elif subopcion_2 == 0:
                    break

                else: 
                    print ("Ingrese una opcion correcta.")


        elif opcion == 5:
            operacion_recursiva ()

        elif opcion == 6:
        # Colección principal con tope (Playlist)
            subopcion_3 = None
            while subopcion_3 != 0:
                print ("\n==== Menu: [1] Agregar cancion a la playlist  [2] Eliminar cancion de la playlist  [3] Cargar playlist [4] Reemplazar cancion de la playlist [0] Salir ====")
                subopcion_3 = int (input ("Ingrese opcion: "))

                if subopcion_3 == 1 :
                    id_ingresado_1 = None
                    while id_ingresado_1 != 0 : 
                        id_ingresado_1 = int(input("Ingresá el ID de la canción para agregar [0 para finalizar]: "))
                        
                        if id_ingresado_1 == 0 :
                                    break
                       
                        try:
                            reproductor.agregar_playlist(id_ingresado_1)
                            nuev_cancion = reproductor._fonoteca.buscar(id_ingresado_1)
                            alta_binario(RUTA_BIN_PLAY, nuev_cancion)
                            print("+ Canción agregada exitosamente a tu playlist.")
                        except ValueError:
                            print("- Por favor, ingresá un ID numérico válido.")
                        except ItemNoEncontradoError as e:
                            print(f"- {e}")
                            break
                        except ColeccionLlenaError as e:
                            print(f"- {e}")
                            break
    
                elif subopcion_3 == 2 :
                    id_ingresado_2 = None
                    while id_ingresado_2 != 0 : 
                        id_ingresado_2 = int(input("Ingresá el ID de la canción para eliminar [0 para finalizar]: "))
                        
                        if id_ingresado_2 == 0 :
                            break
                        
                        try:
                            posicion = posicion_del_id(reproductor._playlist, id_ingresado_2)
                            reproductor.eliminar(id_ingresado_2)
                            baja_binario(RUTA_BIN_PLAY, posicion)
                            print("+ Canción eliminada exitosamente de tu playlist.")
                        except ValueError:
                            print("- Por favor, ingresá un ID numérico válido.")
                            break
                        except ItemNoEncontradoError as e:
                            print(f"- {e}")
                            break

                #elif subopcion_3 == 3 :
                 #   try:
                  #      lista = cargar_binario(RUTA_BIN_PLAY)
                   #     for cancion in lista:
                    #        reproductor.agregar_playlist(cancion.cancion_id)
                    #except ArchivoInvalidoError as error:
                     #   print(f"Archivo inválido: {error}")
                elif subopcion_3 == 3:
                    try:
                        lista = cargar_binario(RUTA_BIN_PLAY)

                        print(f"El archivo tiene {lista.tamanio()} canciones.")

                        cargadas = 0
                        for cancion in lista:
                            try:
                                reproductor.agregar_playlist(cancion.cancion_id)
                                cargadas += 1
                            except ColeccionLlenaError as e:
                                print(f"- Playlist llena tras {cargadas} canciones: {e}")
                                break
                            except ItemNoEncontradoError as e:
                                print(f"- ID {cancion.cancion_id} no está en la fonoteca: {e}")

                        print(f"+ {cargadas} canciones cargadas. Playlist actual: {reproductor._playlist.tamanio()} canciones.")

                    except ArchivoInvalidoError as error:
                        print(f"Archivo inválido: {error}")
                
                elif subopcion_3 == 4:
                    try:
                        reproductor.listar_playlist()
                        posicion = int(input("Posición de la canción a reemplazar: "))
                        id_nuev = int(input("Ingresá el ID de la canción por la que se reemplazará: "))
                        nuev_cancion = reproductor._fonoteca.buscar(id_nuev)
                        if nuev_cancion is None:
                            raise ItemNoEncontradoError(f"ID {id_nuevo} no está en la fonoteca.")
                        reproductor._playlist.reemplazar_en(posicion, nuev_cancion)
                        actualizar_registro(RUTA_BIN_PLAY, posicion, nuev_cancion)
                        print("+ Canción reemplazada exitosamente.")

                    except ValueError:
                            print("- Por favor, ingresá un ID numérico válido.")
                            break
                    except ItemNoEncontradoError as e:
                            print(f"- {e}")
                            break

                elif subopcion_3 == 0 :
                    break
                else:
                    print ("Opcion incorrecta.\n")


        elif opcion == 7:
            subopcion_4 = None
            while subopcion_4 != 0:
                print ("\n==== Menu: [1] Ver playlist [2] Cancion actual [3] Cancion anterior [0] Salir ====")
                subopcion_4 = int (input ("Ingrese opcion: "))

                if subopcion_4 == 1 :
                    reproductor.listar_playlist ()

                elif subopcion_4 == 2 :
                    try:
                        cancion_actual = reproductor.cancion_actual()
                        print(f"⏮ Estas escuchando: {cancion_actual.nombre} - {cancion_actual.autor}")
                    except PilaVaciaError as e:
                        print(f"- {e}")
                        break

                elif subopcion_4 == 3 :
                    try:
                        cancion_anterior = reproductor.cancion_anterior()
                        print(f"⏮ Volviendo a escuchar: {cancion_anterior.nombre} - {cancion_anterior.autor}")
                    except PilaVaciaError as e:
                        print(f"- {e}")
                        break

                elif subopcion_4 == 0 :
                    break
                else :
                    print ("Opcion incorrecta.\n")

        elif opcion == 8:
            subopcion_5 = None
            while subopcion_5 != 0 : 
                print ("\n==== [1] Encolar tema [2] Mostrar lista completa [3] Reproducir | Cancion siguiente [0] Salir ====")
                subopcion_5 = int (input ("Ingrese la opcion: "))
                if subopcion_5 == 1 :
                    id_ingresado_3 = None     
                    while id_ingresado_3 != 0 :
                        id_ingresado_3 = int(input ("Ingrese la ID de la cancion para agregar a la cola [0 para finalizar]: "))        
                        if id_ingresado_3 == 0:
                            break
                        else:
                            reproductor.encolar_tema (id_ingresado_3)

                elif subopcion_5 == 2:
                    try:
                        reproductor.listar_proximos ()
                    except ColaVaciaError as e:
                        print(f"- {e}")
                        break

                elif subopcion_5 == 3 :
                    try:
                        siguiente_cancion = reproductor.cancion_siguiente()
                        print(f"▶ Sonando ahora: {siguiente_cancion.nombre} - {siguiente_cancion.autor}")
                    except ColaVaciaError as e:
                        print(f"- {e}")
                        break

                
        elif opcion == 9:
            subopcion_6 = None
            while subopcion_6 != 0 :
                print ("\n[1] Cargar catálogo desde el .txt de la cátedra | [2] Guardar catálogo en .txt | [3] Guardar catálogo en binario (.bin) | [4] Cargar catálogo desde binario (.bin) | [0] Salir")
                subopcion_6 = int (input ("Seleccione una opcion: "))

                try:
                    if subopcion_6 == 1:
                        catalogo = armar_catalogo_desde_txt(RUTA_TXT)
                        print(f"Catálogo cargado: {catalogo.tamanio()} ítems.")
                        fonoteca.fonoteca = catalogo
                    elif subopcion_6 == 2:
                        guardar_texto(RUTA_TXT, filas_del_catalogo(catalogo), ENCABEZADOS)
                        print("Catálogo guardado en .txt.")
                    elif subopcion_6 == 3:
                        guardar_binario(RUTA_BIN, catalogo) # se define en §4
                        print("Catálogo guardado en .bin.")
                    elif subopcion_6 == 4:
                        catalogo = cargar_binario(RUTA_BIN) # se define en §4
                        print(f"Catálogo cargado desde .bin: {catalogo.tamanio()} ítems.")
                        fonoteca.fonoteca = catalogo
                    elif subopcion_6 == 0 :
                        break
                    else:
                        print("Opción inválida.")
                except ArchivoInvalidoError as error:
                    print(f"Archivo inválido: {error}")
                   

if __name__ == "__main__":
    main()
