from collections import deque
from utiles.graficador import graficar_arbol

def buscar(entorno, limpiadorPetpal):
    # Inicia la frontera con la posición inicial y nivel 0
    frontera = deque([(entorno.copy(), limpiadorPetpal.posicion, [], 0)])  
    pasados = set()  # Conjunto de estados explorados
    nodos = []  # Almacenar nodos explorados
    conexiones = []  # Almacenar conexiones (nodo_padre, nodo_hijo)
    niveles = {}  # Diccionario para almacenar niveles de nodos

    print("Inicio de la búsqueda en anchura")

    while frontera:
        temp_entorno, posicion_actual, path, nivel_actual = frontera.popleft()

        estado_actual = (posicion_actual, frozenset(temp_entorno.desechos))
        
        if estado_actual in pasados:
            continue
        
        # Agregar estado actual a los pasados y nodos explorados
        pasados.add(estado_actual)
        nodos.append(posicion_actual)

        # Solo asignar el nivel si no se ha asignado previamente
        if posicion_actual not in niveles:
            niveles[posicion_actual] = nivel_actual  # Asigna el nivel al nodo actual

        if temp_entorno.prueba_meta():
            print("¡Solución encontrada!\n")
            
            # Recopilar posiciones de la solución
            solucion = path + [posicion_actual]  # Aquí guardamos la ruta de la solución

            # Imprimir las posiciones con sus niveles
            solucion_pasos = [(posicion) for posicion in solucion]
            print("Posiciones de la solución:")
            for pos in solucion_pasos:
                print(f"Posición: {pos}")

            # Graficar el árbol con la solución
            graficar_arbol(nodos, conexiones, niveles, solucion=solucion)

            return path + [posicion_actual], nodos, conexiones, niveles  # Retorna nodos y niveles

        # Mover y limpiar
        limpiadorPetpal.mover(posicion_actual)
        limpiadorPetpal.limpiar(temp_entorno)

        # Obtener sucesores
        sucesores = temp_entorno.get_sucesores(posicion_actual)

        for sucesor in sucesores:
            nuevo_estado = (sucesor, frozenset(temp_entorno.desechos))
            if nuevo_estado not in pasados:
                # Asignar el nuevo nivel basado en el nivel actual
                frontera.append((temp_entorno.copy(), sucesor, path + [posicion_actual], nivel_actual + 1))  
                conexiones.append((posicion_actual, sucesor))

    print("No se encontró solución.")
    return None, nodos, conexiones, niveles  # Si no se encontró solución
