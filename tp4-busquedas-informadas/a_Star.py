import node as n
from queue import PriorityQueue
import environment as e
import time

def a_star(env):
    nombre = "A*"
    start_time = time.time()
    
    # Crear el nodo inicial
    start_node = n.Nodo(env.initial_state, None, 0, 0)
    
    # Caso en que initial_state = final_state
    if start_node.goal_test(env.final_state):
        return start_node
    
    # Crear una cola de prioridad (frontera)
    frontier = PriorityQueue()
    frontier.put((start_node.path_cost + heuristic(start_node.estado, env.final_state), start_node))
    
    # Diccionario para almacenar el costo del mejor camino encontrado hasta un estado
    explored = {}
    
    # Contadores
    total_cost = 0
    
    while not frontier.empty():
        _, current_node = frontier.get()
        
        if current_node.estado in explored and explored[current_node.estado] <= current_node.path_cost:
            continue
        
        # Guardar el costo del camino más bajo encontrado hasta el estado
        explored[current_node.estado] = current_node.path_cost
        
        if current_node.goal_test(env.final_state):
            end_time = time.time()
            path, moves = solution(current_node)
            final_time = end_time - start_time
            return path, moves, len(explored), total_cost, final_time, True, nombre
        
        actions, action_number = current_node.possible_actions(env)
        total_cost += len(actions)
        
        for action, action_index in zip(actions, action_number):
            child_cost = current_node.path_cost + 1
            child = n.Nodo(action, current_node, action_index, child_cost)
            frontier.put((child.path_cost + heuristic(child.estado, env.final_state), child))
    
    end_time = time.time()
    final_time = end_time - start_time
    path, moves = solution(current_node)
    return path, moves, len(explored), total_cost, final_time, False, nombre

def heuristic(state, goal):
    # Heurística simple: distancia de Manhattan
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def solution(child):
    path = []
    moves = []
    # Añadir el estado del nodo objetivo
    path.append(child.estado)
    moves.append(child.action_number)
    # Recorrer hacia atrás hasta llegar al nodo raíz
    node = child.parent
    while node is not None:
        path.append(node.estado)
        moves.append(node.action_number)
        node = node.parent
    path.reverse()
    moves.reverse()
    return path, moves

# Ejemplo de uso
env = e.Environment(100, 0.08, 9) # Tamaño reducido para pruebas
result = a_star(env)

def showMoves(moves, env):
    # Resetear el entorno para iniciar un nuevo episodio
    state = env.environment.reset()
    # Renderizar el entorno inicial
    env.environment.render()
    time.sleep(2)
    for i in range(1, len(moves)):
        time.sleep(0.5)
        next_state, reward, done, truncated, info = env.environment.step(moves[i])
    env.environment.render()
    time.sleep(0.5)

path, moves, explored_amount, total_cost, final_time, found, nombre = result
info = {
    'algorithm_name': 'A*',
    'posición inicial agente': env.initial_state,
    'posición objetivo': env.final_state,
    'env_n': 0,
    'camino generado': path,
    'movimientos': moves,
    'states_n': explored_amount,
    'cost_total': total_cost,
    'time': final_time,
    'solution_found': found
}
print(info)

if found:
    showMoves(moves, env)