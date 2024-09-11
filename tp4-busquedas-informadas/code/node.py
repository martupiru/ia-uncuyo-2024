from collections import deque
from queue import PriorityQueue
class Nodo:
    def __init__(self, estado, parent=None, action_number = None,path_cost = None):
        self.estado = estado #posicion
        self.parent = parent #nodo padre
        self.action_number = action_number #accion del nodo padre que lo llevo a llegar a este nodo hijo
        self.path_cost = path_cost
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __repr__(self):
        return f'Nodo(estado={self.estado})'
        #return {self.estado}


    def goal_test(self, final_state):
        return self.estado == final_state

    def possible_actions(self, env):
        # Xij = fila, columna
        actions = deque()
        action_number = deque()
        long = env.size
        # Derecha: 
        if self.estado[1] + 1 < long and env.map_list[self.estado[0]][self.estado[1] + 1] != 'H': 
            actions.append((self.estado[0], self.estado[1] + 1))
            action_number.append(2)
        
        # Izquierda: 
        if self.estado[1] - 1 >= 0 and env.map_list[self.estado[0]][self.estado[1] - 1] != 'H':
            actions.append((self.estado[0], self.estado[1] - 1))
            action_number.append(0)
        
        # Arriba: 
        if self.estado[0] - 1 >= 0 and env.map_list[self.estado[0] - 1][self.estado[1]] != 'H':
            actions.append((self.estado[0] - 1, self.estado[1]))
            action_number.append(3)
        
        # Abajo: 
        if self.estado[0] + 1 < long and env.map_list[self.estado[0] + 1][self.estado[1]] != 'H': #100
            actions.append((self.estado[0] + 1, self.estado[1]))
            action_number.append(1)
        
        return actions, action_number
    
    def possible_actions_p(self, env):
        # Xij = fila, columna
        actions = []
        long = env.size
        amount_action = 0
        # Izquierda: 
        if self.estado[1] - 1 >= 0 and env.map_list[self.estado[0]][self.estado[1] - 1] != 'H':
            actions.append((0,(self.estado[0], self.estado[1] - 1)))
            amount_action += 1
        # Abajo: 
        if self.estado[0] + 1 < long and env.map_list[self.estado[0] + 1][self.estado[1]] != 'H': #100
            actions.append((1,(self.estado[0] + 1, self.estado[1])))
            amount_action += 1
        # Derecha: 
        if self.estado[1] + 1 < long and env.map_list[self.estado[0]][self.estado[1] + 1] != 'H': 
            actions.append((2,(self.estado[0], self.estado[1] + 1)))
            amount_action += 1
        # Arriba: 
        if self.estado[0] - 1 >= 0 and env.map_list[self.estado[0] - 1][self.estado[1]] != 'H':
            actions.append((3,(self.estado[0] - 1, self.estado[1])))
            amount_action += 1

        return actions, amount_action