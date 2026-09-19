from config import TEMA
from dominio.Fonoteca import fonoteca

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def listar_canciones():
    for cancion in fonoteca:
        print(f"{cancion["nombre"]} | {cancion["autor"]} | {cancion["album"]} | {cancion["genero"]}")

def operacion_recursiva ():
    
    for cancion in fonoteca: #recorre la lista de canciones a ver si tiene distintas versiones
       
        if "versiones" in cancion and cancion ["versiones"]:
            print (f"* {cancion ["nombre"]} | {cancion ["nombre"]} | {cancion ["nombre"]} | {cancion ["nombre"]} | {cancion ["genero"]}")
            
            def recorrer (lista_versiones): #funcion recursiva para recorrer la lista
                if not lista_versiones:
                    return
                
                version = lista_versiones [0]
                print (f"  ---- {version ["nombre"]} | {version ["autor"]} | {version ["album"]} | {version ["genero"]}")
                              
            recorrer (cancion ["versiones"])
            print ()


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
    print("6. Colección principal (equipo / menú / playlist)")
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
            pendiente ()
        elif opcion == 3:
            pendiente ()
        elif opcion == 4:
            pendiente ()
        elif opcion == 5:
            operacion_recursiva ()
        elif opcion == 6:
            pendiente ()
        elif opcion == 7:
            pendiente ()
        elif opcion == 8:
            pendiente ()
        elif opcion == 9:
            pendiente ()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
