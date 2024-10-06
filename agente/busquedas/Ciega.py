from collections import deque

def buscar(entorno, limpiadorPetpal):
    # Incluimos también el estado de los desechos en el set de pasados
    frontera = deque([(entorno.copy(), limpiadorPetpal.posicion, [])])  # Cola para BFS
    pasados = set()  # Conjunto de estados explorados
    
    print("Inicio de la búsqueda en anchura")

    while frontera:
        temp_entorno, posicion_actual, path = frontera.popleft()

        # Estado actual del agente y desechos restantes
        estado_actual = (posicion_actual, frozenset(temp_entorno.desechos))
        
        # Si ya se exploró este estado (posición + desechos), lo saltamos
        if estado_actual in pasados:
            continue
        pasados.add(estado_actual)  # Marcamos este estado como explorado
        
        # Verifica si se ha alcanzado el objetivo (no queda más basura)
        if temp_entorno.prueba_meta():
            print("¡Solución encontrada!\n")
            return path + [posicion_actual]  # Retorna cuando toda la basura ha sido limpiada

        # Limpiar desechos adyacentes
        limpiadorPetpal.mover(posicion_actual)
        limpiadorPetpal.limpiar(temp_entorno)  # Limpia en la copia del entorno

        # Obtener sucesores
        sucesores = temp_entorno.get_sucesores(posicion_actual)

        # Expandir sucesores
        for sucesor in sucesores:
            # Solo expandimos si no hemos explorado este sucesor en el estado actual de desechos
            nuevo_estado = (sucesor, frozenset(temp_entorno.desechos))
            if nuevo_estado not in pasados:
                # Solo copiamos el entorno cuando es necesario expandir
                frontera.append((temp_entorno.copy(), sucesor, path + [posicion_actual]))

    print("No se encontró solución.")
    return None  # Si no se encontró solución
