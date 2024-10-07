import heapq
from utiles.graficador import graficar_arbol

def buscar(entorno, PetPal):
    frontera = []
    heapq.heappush(frontera, (0, entorno.copy(), PetPal.posicion, []))
    visitados = set()
    paso = 0
    nodos = []  # Almacenar nodos explorados
    conexiones = []  # Almacenar conexiones (nodo_padre, nodo_hijo)
    niveles = {}  # Diccionario para almacenar niveles de nodos

    print("Inicio de la búsqueda con heurística")

    while frontera:
        _, entorno_act, posicion_actual, path = heapq.heappop(frontera)

        estado_actual = (posicion_actual, frozenset(entorno_act.desechos))

        if estado_actual in visitados:
            continue
        
        visitados.add(estado_actual)
        niveles[posicion_actual] = paso

        if entorno_act.prueba_meta():
            print("¡Solución encontrada!\n")

            solucion = path + [posicion_actual]  # Ruta Solución

            solucion_pasos = [(posicion) for posicion in solucion]
            print("Posiciones de la solución:")
            for pos in solucion_pasos:
                print(f"Posición: {pos}")

            # Graficar el árbol con la solución
            graficar_arbol(nodos, conexiones, niveles, solucion=solucion)

            return path + [posicion_actual], nodos, conexiones, niveles

        PetPal.mover(posicion_actual)
        PetPal.limpiar(entorno_act)

        # Obtener sucesores
        sucesores = entorno_act.get_sucesores(posicion_actual)

        # Si hay sucesores, encontramos el sucesor con menor heurística
        if sucesores:
            # Aseguramos que hay desechos restantes
            if entorno_act.desechos:
                # Encontramos el sucesor con la menor distancia Manhattan a los desechos
                mejor_sucesor = min(sucesores, key=lambda s: min(distancia_manhattan(s, desecho) for desecho in entorno_act.desechos))
                nueva_h = min(distancia_manhattan(mejor_sucesor, desecho) for desecho in entorno_act.desechos)
            else:
                # Si no hay desechos restantes, la heurística es 0
                mejor_sucesor = sucesores[0]  # Cualquier sucesor
                nueva_h = 0

            # Expandimos el sucesor con menor heurística
            nuevo_estado = (mejor_sucesor, frozenset(entorno_act.desechos))
            if nuevo_estado not in visitados and entorno_act.posicion_valida(mejor_sucesor):
                heapq.heappush(frontera, (nueva_h, entorno_act.copy(), mejor_sucesor, path + [posicion_actual]))
                
            nodos.append(mejor_sucesor)
            conexiones.append((posicion_actual, mejor_sucesor))
            
            for sucesor in sucesores:
                nuevo_estado = (mejor_sucesor, frozenset(entorno_act.desechos))
                if sucesor != mejor_sucesor and sucesor not in visitados:
                    nodos.append(sucesor)
                    conexiones.append((posicion_actual, sucesor))
        paso += 1

    print("No se encontró solución.")
    return None, nodos, conexiones, niveles  # Si no se encontró solución

def distancia_manhattan(a, b):
    """Calcula la distancia Manhattan entre dos puntos (x1, y1) y (x2, y2)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
