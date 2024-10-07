from utiles.graficador import graficar_entorno

def resultado(agente, entorno, solucion, nodos_explorados, Op):
    optima = "Si" if Op else "No"
    if solucion is not None:
        entorno_copia = entorno.copy()
        for i, paso in enumerate(solucion):
            # Mover el agente al siguiente paso
            agente.mover(paso)
            # Limpiar si hay basura cerca
            agente.limpiar(entorno_copia)
            # Graficar el entorno en cada paso
            title = f"Paso {i+1}: PetPal en {agente.posicion}"
            graficar_entorno(entorno_copia, agente, title)
        print("Imprimiendo los pasos:")
        # Simula el proceso de moverse y limpiar
        for paso in solucion:
            agente.mover(paso)
            agente.limpiar(entorno)  # Limpia las casillas adyacentes con basura
            entorno.imprimirEntorno(agente.posicion)  # Imprime cada paso
            complejidad = len(nodos_explorados)
        print("--MEDIDAS DE RENDIMIENTO--")
        print(f"Completitud: Si \nOptima: {optima} (dado el metodo de busqueda)")
        print("Complejidad Temporal: {} u/t".format(complejidad))
        print("Complejidad Espacial: {} u/e".format(complejidad))        
    else:
        print("No se encontró solución \n")
        print("--MEDIDAS DE RENDIMIENTO--")
        print("Completitud: NO \nOptima: - \n")
        print("Complejidad Temporal: - \n")
        print("Complejidad Espacial: -")
