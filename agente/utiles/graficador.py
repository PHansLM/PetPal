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
