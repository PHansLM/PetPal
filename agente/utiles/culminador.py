def resultado(agente, entorno, solucion, nodos_explorados):
    if solucion is not None:
        print("Imprimiendo los pasos:")
        # Simula el proceso de moverse y limpiar
        for paso in solucion:
            agente.mover(paso)
            agente.limpiar(entorno)  # Limpia las casillas adyacentes con basura
            entorno.imprimirEntorno(agente.posicion)  # Imprime cada paso
            complejidad = len(nodos_explorados)

        print("--MEDIDAS DE RENDIMIENTO--")
        print("Completitud: Si \nOptima: Si (dado el metodo de busqueda)")
        print("Complejidad Temporal: {} u/t".format(complejidad))
        print("Complejidad Espacial: {} u/e".format(complejidad))         
    else:
        print("No se encontró solución \n")
        print("--MEDIDAS DE RENDIMIENTO--")
        print("Completitud: NO \nOptima: - \n")
        print("Complejidad Temporal: - \n")
        print("Complejidad Espacial: -")