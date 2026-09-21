from config import TEMA
from dominio.Fonoteca import Fonoteca

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def listar_canciones():
    fonoteca = Fonoteca()
    fonoteca.listar()

def operacion_recursiva (): 
    fonoteca = Fonoteca()
    idc = None
    while idc == None: #Elegimos la cancion de la cual queremos ver las versiones existentes y se imprime el resultado
        print("Ingrese el id de la cancion de la cual desee conocer las versiones: ")
        idc = int (input())
        resultado_recursivo = fonoteca.versiones_deriv(idc)
        for can_ver in resultado_recursivo:
            print(can_ver)

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
