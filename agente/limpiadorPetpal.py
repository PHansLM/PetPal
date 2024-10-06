class LimpiadorPetpal:
    def __init__(self, estacion_carga):
        self.posicion = estacion_carga
    
    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion

    def limpiar(self, entorno):
        # Limpia la basura en casillas adyacentes
        x, y = self.posicion
        adyacentes = [
            (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        ]
        for pos in adyacentes:
            if pos in entorno.desechos:
                entorno.desechos.remove(pos)  # Elimina la basura de la lista