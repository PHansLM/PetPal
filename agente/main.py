from utiles.culminador import resultado
from entorno import Entorno
from limpiadorPetpal import LimpiadorPetpal
from busquedas import Heuristica, Ciega

def main():
    # Inicializa el entorno (por ejemplo, una sala de 10x6 con obstáculos y basura)
    entorno = Entorno(
        ancho=10, 
        largo=6, 
        obstaculos=[(0,0), (2,0), (3,0), (4,0), 
                    (0,2), (6,2), 
                    (0,3), (2,3), (3,3), (4,3), (6,3), 
                    (0,4),  
                    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (7,5), (8,5)], 
        desechos=[(0, 1), (7, 2), (2, 4), (9,5)]
    )
    entorno_h = entorno.copy()
    # Inicializa el agente en una posición inicial
    agente = LimpiadorPetpal(estacion_carga=(8, 0))
    print("Estado inicial del entorno:")
    entorno.imprimirEntorno(agente.posicion)

    # EJECUCION DE AMBAS BUSQUEDAS

    print("BUSQUEDA DE PRIMERO EN ANCHURA")

    #Iniciar búsqueda no informada
    solucion, nodos_explorados, conexiones, niveles = Ciega.buscar(entorno, agente)  
    
    #Devolver resultado del análisis de búsqueda no informada
    resultado(agente, entorno, solucion, nodos_explorados, True)
    
    print("BUSQUEDA DE HEURISTICA VORAZ")
    
    agente_h = LimpiadorPetpal(estacion_carga=(8, 0))
    
    #Iniciar búsqueda informada
    solucion_h, nodos_explorados_h, conexiones, niveles = Heuristica.buscar(entorno_h, agente_h)  
    
    #Devolver resultado del análisis de búsqueda informada
    resultado(agente_h, entorno_h, solucion_h, nodos_explorados_h, False)

if __name__ == "__main__":
    main()
