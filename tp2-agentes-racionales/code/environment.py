import random

class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        # Ajustar el dirt_rate para tener una cantidad visible de suciedad
        self.grid = [[random.random() < dirt_rate for _ in range(sizeY)] for _ in range(sizeX)]
        self.agent_position = (init_posX, init_posY)
        self.performance = 0

    def accept_action(self, action):
        x, y = self.agent_position
        if action == 'Arriba' and x > 0:
            self.agent_position = (x - 1, y)
        elif action == 'Abajo' and x < self.sizeX - 1:
            self.agent_position = (x + 1, y)
        elif action == 'Izquierda' and y > 0:
            self.agent_position = (x, y - 1)
        elif action == 'Derecha' and y < self.sizeY - 1:
            self.agent_position = (x, y + 1)
        elif action == 'Limpiar':
            if self.is_dirty():
                self.grid[x][y] = False
                self.performance += 1

    def is_dirty(self):
        x, y = self.agent_position
        return self.grid[x][y]

    def get_performance(self):
        return self.performance

    def print_environment(self):
        for i in range(self.sizeX):
            row = ""
            for j in range(self.sizeY):
                if self.agent_position == (i, j):
                    row += "A "  # Representa al agente
                else:
                    row += "X " if self.grid[i][j] else ". "  # X para suciedad, . para limpio
            print(row)
        #print("\nPerformance:", self.performance)
