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
        desechos=[(0, 1), (7, 2), (2, 4), (9,5)])
    
    # Inicializa el agente en una posición inicial
    agente = LimpiadorPetpal(estacion_carga=(8, 0))
    
    # EJECUCION DE AMBAS BUSQUEDAS
    
if __name__ == "__main__":
    main()
