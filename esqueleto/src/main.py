from config import TEMA
from dominio.Fonoteca import Fonoteca, Reproductor
from excepciones import *
from algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
import time

fonoteca = Fonoteca()
reproductor = Reproductor(catalogo=fonoteca, tope = 10)
TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

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

def medir_tiempo (funcion, datos, *args, **kwargs) :
    inicio = time.perf_counter ()
    resultado_original = funcion (datos, *args, **kwargs)
    fin = time.perf_counter ()
    print (f"Tiempo de ejecucion Original: {fin - inicio:.6f} s")

    datos_grandes = datos * 10
    inicio_grande = time.perf_counter ()
    resultado_grande = funcion (datos_grandes, *args, **kwargs)
    fin_grande = time.perf_counter ()
    print (f"Tiempo de ejecucion Grande: {fin_grande - inicio_grande:.6f} s")

    return resultado_original

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
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
 
    while opcion != 0:
        mostrar_menu()
        opcion = int (input("> ").strip())
        if opcion == 0:
            print("Chau.")
        elif opcion == 1:
            listar_canciones ()
        elif opcion == 2:
            id_cancion = int (input("Ingrese el ID de la cancion: "))
            mostrar_detalle (id_cancion)
        elif opcion == 3:

            opcion_5 = None
            while opcion_5 != 0:

                print ("\nBuscar por: [1] Nombre (lineal) | [2] Nombre (binaria) | [0] Salir")
                id_ingresado_4 = int (input ("Ingrese opcion: "))

                if id_ingresado_4 == 1:
                    nombre = str (input ("Ingresa el nombre: "))
                    resultado_lineal = busqueda_lineal (fonoteca.fonoteca, nombre, lambda x: x.nombre)
                    if resultado_lineal :
                        print (f"\nEncontrado: {resultado_lineal}")
                    else:
                        print ("No se encontro el elemento.\n")
                    medir_tiempo (busqueda_lineal, fonoteca.fonoteca, nombre, obtener_clave = lambda p: p.nombre)

                elif id_ingresado_4 == 2:
                    nombre = str (input ("Ingresa el nombre: "))
                    resultado_binaria = busqueda_binaria (fonoteca.fonoteca, nombre, lambda i: i.nombre)
                    if resultado_binaria :
                        print (f"Encontrado: {resultado_binaria}\n")
                    else:
                        print ("No se encontro el elemento.\n")
                    medir_tiempo (busqueda_binaria, fonoteca.fonoteca, nombre, obtener_clave = lambda p: p.nombre)
                    
                elif id_ingresado_4 == 0:
                    break

                else:
                    print ("Ingrese una opcion correcta.")

        elif opcion == 4:
            opcion_6 = None
            while opcion_6 != 0 :
                print ("\nOrdenar por: [1] Nombre | [2] Tiempo / hp / duracion")
                id_ingresado_5 = int (input ("Ingresa la opcion: "))

                if id_ingresado_5 == 1 :
                    coleccion = int (input ("[1] Seleccion.... | [2] Insercion : "))
                    if coleccion == 1:
                        resultado_seleccion = ordenar_seleccion (fonoteca.fonoteca, lambda j: j.nombre)
                        print ("---- Catalogo ordenado por Seleccion ----")
                        for cancion in resultado_seleccion: 
                            print (cancion)
                        medir_tiempo (ordenar_seleccion, fonoteca.fonoteca, obtener_clave = lambda p: p.nombre)

                    elif coleccion == 2:
                        resultado_insercion = ordenar_insercion (fonoteca.fonoteca, lambda k: k.nombre)
                        print ("---- Catalogo ordenado por Insercion ----")
                        for cancion in resultado_insercion :
                            print (cancion)
                        medir_tiempo (ordenar_insercion, fonoteca.fonoteca, obtener_clave = lambda p: p.nombre)
                    
                    else: 
                        pass
                    
                elif id_ingresado_5 == 2:

                    pendiente ()

                elif id_ingresado_5 == 0:

                    break

                else: 
                    print ("Ingrese una opcion correcta.")


        elif opcion == 5:
            operacion_recursiva ()
        elif opcion == 6:
        # Colección principal con tope (Playlist)
            opcion_2 = None
            while opcion_2 != 0:
                print ("\n=== Menu: [1] Agregar cancion a la playlist [2] Eliminar cancion de la playlist  [0] Salir ===")
                opcion_2 = int (input ("Ingrese opcion: "))

                if opcion_2 == 1 :
                    id_ingresado = None
                    while id_ingresado != 0 : 
                        id_ingresado = int(input("Ingresá el ID de la canción para agregar [0 para finalizar]: "))
                        try:
                            reproductor.agregar_playlist(id_ingresado)
                            print("+ Canción agregada exitosamente a tu playlist.")
                        except ValueError:
                            print("- Por favor, ingresá un ID numérico válido.")
                        except ItemNoEncontradoError as e:
                            print(f"- {e}")
                            break
                        except ColeccionLlenaError as e:
                            print(f"- {e}")
                            break

                        if id_ingresado == 0 :
                            break

                elif opcion_2 == 2 :
                    id_ingresado_2 = None
                    while id_ingresado_2 != 0 : 
                        id_ingresado_2 = int(input("Ingresá el ID de la canción para eliminar [0 para finalizar]: "))
                        try:
                            reproductor.eliminar(id_ingresado_2)
                            print("+ Canción eliminada exitosamente a tu playlist.")
                        except ValueError:
                            print("- Por favor, ingresá un ID numérico válido.")
                            break
                        except ItemNoEncontradoError as e:
                            print(f"- {e}")
                            break

                        if id_ingresado_2 == 0 :
                            break

                elif opcion_2 == 0 :
                    break
                else:
                    print ("Opcion incorrecta.\n")

        elif opcion == 7:
            opcion_3 = None
            while opcion_3 != 0:
                print ("\n=== Menu: [1] Ver playlist [2] Cancion actual [3] Cancion anterior [0] Salir ===")
                opcion_3 = int (input ("Ingrese opcion: "))

                if opcion_3 == 1 :
                    reproductor.listar_playlist ()
                elif opcion_3 == 2 :
                    reproductor.cancion_actual ()
                    try:
                        cancion_actual = reproductor.cancion_actual()
                        print(f"⏮ Estas escuchando: {cancion_actual.nombre} - {cancion_actual.autor}")
                    except PilaVaciaError as e:
                        print(f"- {e}")
                        break

                elif opcion_3 == 3 :
                    try:
                        cancion_anterior = reproductor.cancion_anterior()
                        print(f"⏮ Volviendo a escuchar: {cancion_anterior.nombre} - {cancion_anterior.autor}")
                    except PilaVaciaError as e:
                        print(f"- {e}")
                        break

                elif opcion_2 == 0 :
                    break
                else :
                    print ("Opcion incorrecta.\n")

        elif opcion == 8:
            opcion_4 = None
            while opcion_4 != 0 : 
                print ("\n=== [1] Encolar tema [2] Mostrar lista completa [3] Reproducir | Cancion siguiente [0] Salir ===")
                opcion_4 = int (input ("Ingrese la opcion: "))
                if opcion_4 == 1 :
                    id_ingresado_3 = None     
                    while id_ingresado_3 != 0 :
                        id_ingresado_3 = int(input ("Ingrese la ID de la cancion para agregar a la cola [0 para finalizar]: "))        
                        if id_ingresado_3 == 0:
                            break
                        else:
                            reproductor.encolar_tema (id_ingresado_3)

                elif opcion_4 == 2:
                    try:
                        reproductor.listar_proximos ()
                    except ColaVaciaError as e:
                        print(f"- {e}")
                        break

                elif opcion_4 == 3 :
                    try:
                        siguiente_cancion = reproductor.cancion_siguiente()
                        print(f"▶ Sonando ahora: {siguiente_cancion.nombre} - {siguiente_cancion.autor}")
                    except ColaVaciaError as e:
                        print(f"- {e}")
                        break
                
        elif opcion == 9:
            pendiente ()
            
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
