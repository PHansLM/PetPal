import matplotlib.pyplot as plt
import networkx as nx

def graficar_arbol(nodos, conexiones, niveles, solucion=None):
    G = nx.DiGraph()  # Usar un grafo dirigido para flechas
    
    # Agregar nodos al grafo
    for nodo in nodos:
        G.add_node(nodo)

    # Agregar conexiones al grafo
    for padre, hijo in conexiones:
        G.add_edge(padre, hijo)

    # Dibujar el grafo
    pos = nx.spring_layout(G)

    # Dibujar todos los nodos en gris
    nx.draw_networkx_nodes(G, pos, node_color='gray', node_size=500)

    # Dibujar todas las conexiones en gris
    nx.draw_networkx_edges(G, pos, edge_color='gray')

    # Si hay una solución, dibujarla en otro color
    if solucion:
        # Marcar nodos de la solución
        solucion_nodos = set(solucion)
        nx.draw_networkx_nodes(G, pos, nodelist=solucion_nodos, node_color='green', node_size=700)

        # Marcar las líneas de la solución con flechas
        solucion_conexiones = [(solucion[i], solucion[i + 1]) for i in range(len(solucion) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=solucion_conexiones, edge_color='blue', width=2, arrowstyle='-|>', arrowsize=20)

    # Etiquetas para los nodos
    labels = {nodo: f"{nodo}" for nodo in nodos}
    nx.draw_networkx_labels(G, pos, labels, font_size=10)

    plt.axis('off')  # Ocultar el eje
    plt.show()

# Función para graficar el entorno
def graficar_entorno(entorno, limpiador, title):
    ancho, largo = entorno.ancho, entorno.largo
    # Crear una matriz numérica para el entorno
    grid = [[0 for _ in range(ancho)] for _ in range(largo)]
    # Obstáculos en gris (valor 1)
    for (x, y) in entorno.obstaculos:
        grid[y][x] = 1
    # Desechos en naranja (valor 2)
    for (x, y) in entorno.desechos:
        grid[y][x] = 2
    # Limpiador en verde (valor 3)
    x, y = limpiador.posicion
    grid[y][x] = 3

    cmap = mcolors.ListedColormap(['white', 'gray', 'orange', 'green'])
    bounds = [0, 1, 2, 3, 4]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    
    # Ajustar el extent para que las celdas encajen perfectamente
    ax.imshow(grid, cmap=cmap, norm=norm, extent=[0, ancho, largo, 0], aspect='equal')

    # Configurar las etiquetas de los ticks
    ax.set_xticks(range(ancho))
    ax.set_yticks(range(largo))
    ax.set_xticklabels(range(ancho))
    ax.set_yticklabels(range(largo))
    # Evitar cortes
    ax.set_xlim(0, ancho)
    ax.set_ylim(largo, 0)  # Invertir el eje y
    
    plt.title(title)
    
    # Ajustar la grilla para que no se sobreponga con las celdas
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=0.5)
    
    plt.show()
