class LimpiadorPetpal:
    def __init__(self, estacion_carga):
        self.posicion = estacion_carga
    
    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion

    def limpiar(self, entorno):
        # Limpia una casilla adyacente si hay desechos cerca
        return entorno.limpiar_desecho(self.posicion)