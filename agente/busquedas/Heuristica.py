import heapq

def buscar(entorno, PetPal):
    frontera = []
    heapq.heappush(frontera, (0, entorno.copy(), PetPal.posicion, []))
    visitados = set()
    paso = 0

    print("Inicio de la búsqueda con heurística")

    while frontera:
        _, entorno_act, posicion_actual, path = heapq.heappop(frontera)

        estado_actual = (posicion_actual, frozenset(entorno_act.desechos))

        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)

        if entorno_act.prueba_meta():
            print("¡Solución encontrada!\n")
            return path + [posicion_actual]

        PetPal.mover(posicion_actual)
        PetPal.limpiar(entorno_act)

        # Obtener sucesores
        sucesores = entorno_act.get_sucesores(posicion_actual)
        print(f"Sucesores de {posicion_actual}: {sucesores}")

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
        paso += 1

    print("No se encontró solución.")
    return None  # Si no se encontró solución

def distancia_manhattan(a, b):
    """Calcula la distancia Manhattan entre dos puntos (x1, y1) y (x2, y2)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
