

class Entorno:
    def __init__(self, ancho, largo, obstaculos, desechos):
        self.ancho = ancho
        self.largo = largo
        self.obstaculos = set(obstaculos)  # Posiciones donde hay obstáculos
        self.desechos = set(desechos)            # Posiciones donde hay desechos por limpiar
        self.limpiados = set()  # Agregar conjunto para posiciones limpiadas


    def prueba_meta(self):
        return len(self.desechos) == 0

    def get_sucesores(self, posicion):
        # Devuelve los movimientos posibles (arriba, abajo, izquierda, derecha) desde la posición actual
        posibles_movimientos = [
            (0, 1), (0, -1), (1, 0), (-1, 0)  # Arriba, Abajo, Derecha, Izquierda
        ]
        sucesores = []
        for movimiento in posibles_movimientos:
            nueva_posicion = (posicion[0] + movimiento[0], posicion[1] + movimiento[1])
            if self.posicion_valida(nueva_posicion):
                sucesores.append(nueva_posicion)
        return sucesores

    def posicion_valida(self, posicion):
        # Verifica si la posición es válida (dentro de los límites y no es un obstáculo)
        x, y = posicion
        return 0 <= x < self.ancho and 0 <= y < self.largo and posicion not in self.obstaculos

    def limpiar_desecho(self, agent_position):
        posibles_movimientos = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]
        for movimiento in posibles_movimientos:
            adj_pos = (agent_position[0] + movimiento[0], agent_position[1] + movimiento[1])
            if adj_pos in self.desechos:
                self.desechos.remove(adj_pos)  # Limpia los desechos de la casilla adyacente
                self.limpiados.add(adj_pos)  # Agrega a la lista de limpiados
                return True
        return False

    def imprimirEntorno(self, agent_position):
        for y in range(self.largo):
            row = []
            for x in range(self.ancho):
                pos = (x, y)
                if pos == agent_position:
                    row.append('A')  # Petpal
                elif pos in self.obstaculos:
                    row.append('X')  # Obstáculo
                elif pos in self.desechos:
                    row.append('D')  # Desechos
                elif pos in self.limpiados:
                    row.append('L')  # Limpiados
                else:
                    row.append('.')
            print(" ".join(row))
        print("\n")

    def copy(self):
        # Retorna una copia del entorno (nueva instancia)
        return Entorno(self.ancho, self.largo, list(self.obstaculos), list(self.desechos))