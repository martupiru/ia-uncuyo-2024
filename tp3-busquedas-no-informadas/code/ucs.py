import node as n
from collections import deque
import environment as e
import time
import heapq

def ucs(env):
    nombre = "UCS"
    start_time = time.time()
    
    # Crear el nodo inicial con costo 0
    nodo = n.Nodo(env.initial_state, None, None, 0)
    
    # Caso en que initial_state = final_state
    if nodo.goal_test(env.final_state):
        return nodo
    
    # Crear una cola de prioridad (frontera) basada en el costo acumulado
    frontier = []
    heapq.heappush(frontier, (nodo.path_cost, nodo))
    
    # Diccionario para almacenar el costo mínimo para alcanzar cada estado
    costs = {nodo.estado: nodo.path_cost}
    
    # Diccionario para almacenar los nodos explorados
    explored = set()
    
    # Contadores
    first_cost = 0  # escenario 1
    second_cost = 0  # escenario 2
    move_count = 0
    explored_amount = 0
    while frontier  and (move_count < 1000):
        # Extraer el nodo de menor costo de la frontera
        _, node = heapq.heappop(frontier)
        
        # Marcar el nodo como explorado
        if node.estado in explored:
            continue
        explored.add(node.estado)
        
        # Comprobar si se ha alcanzado el objetivo
        if node.goal_test(env.final_state):
            explored_amount = len(explored)
            path, moves = solution(node)
            end_time = time.time()
            final_time = end_time - start_time
            return path, moves, explored_amount, first_cost, second_cost, final_time, True, nombre
        
        actions, action_number = node.possible_actions(env)
        first_cost +=1  
        
        for action in actions:
            action_cost = action_number.popleft()
            new_cost = node.path_cost + action_cost + 1  # costo acumulado + costo de la acción
            child = n.Nodo(action, node, action_cost, new_cost)
            second_cost += action_cost + 1  # escenario 2
            
            if child.estado not in explored and (child.estado not in costs or new_cost < costs[child.estado]):
                costs[child.estado] = new_cost
                heapq.heappush(frontier, (new_cost, child))
        move_count+=1
    
    end_time = time.time()
    final_time = end_time - start_time
    path, moves = solution(node)
    return path, moves, len(explored), first_cost, second_cost, final_time, False, nombre

def solution(child):
    path = []
    moves = []
    # Añadir el estado del nodo objetivo
    path.append(child.estado)
    if child.action_number is not None:
        moves.append(child.action_number)
    # Recorrer hacia atrás hasta llegar al nodo raíz
    node = child.parent
    while node is not None:
        path.append(node.estado)
        if node.action_number is not None:
            moves.append(node.action_number)
        node = node.parent
    path.reverse()
    moves.reverse()
    return path, moves

# Ejemplo de uso
#env = e.Environment(100, 0.08, 9)  # Tamaño, tasa de agujeros, semilla
#result = ucs(env)

def showMoves(moves, env):
    # Restablecer el entorno para iniciar un nuevo episodio
    state = env.environment.reset()
    # Renderizar el entorno inicial
    env.environment.render()
    time.sleep(2)
    for move in moves:
        time.sleep(0.5)
        next_state, reward, done, truncated, info = env.environment.step(move)  
    env.environment.render()
    time.sleep(0.5)

"""path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
info = {
    'algorithm_name': nombre,
    'posición inicial agente': env.initial_state,
    'posición objetivo': env.final_state,
    'env_n': 0,
    'camino generado': path,
    'movimientos': moves,
    'states_n': explored_amount,
    'cost_e1': first_cost,  # escenario 1
    'cost_e2': second_cost,  # escenario 2
    'time': final_time,
    'solution_found': found
}
print(info)

if found:
    showMoves(moves, env)"""