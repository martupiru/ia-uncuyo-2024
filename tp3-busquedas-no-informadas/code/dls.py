import node as n
from collections import deque
import environment as e
import time

def depth_limited_search(env, limit):
    nombre = "DLS"
    start_time = time.time()
    
    # Crear el nodo inicial
    nodo = n.Nodo(env.initial_state, None)
    
    # Caso en que initial_state = final_state
    if nodo.goal_test(env.final_state):
        return nodo
    
    # Crear una pila LIFO (frontera) y establecer profundidad inicial en 0
    frontier = deque([(nodo, 0)])  # (nodo, profundidad)
    
    # Diccionario para almacenar los estados explorados
    explored = set()
    
    # Contadores
    first_cost = 0  # escenario 1
    second_cost = 0  # escenario 2
    
    while frontier:
        node, depth = frontier.pop()
        
        # Si el nodo ya está en el conjunto explorado, continuar con el siguiente nodo
        if node.estado in explored:
            continue
        
        # Añadir el estado al conjunto explorado
        explored.add(node.estado)
        
        # Si la profundidad límite ha sido alcanzada, no explorar más allá
        if depth >= limit:
            continue
        
        actions, action_number = node.possible_actions(env)
        first_cost += len(actions)  # escenario 1
        
        for action in actions:
            action_cost = action_number.popleft()
            child = n.Nodo(action, node, action_cost)
            second_cost += action_cost + 1  # escenario 2
            if child.estado not in explored and child.estado not in (nodo.estado for nodo, _ in frontier):
                if child.goal_test(env.final_state):
                    explored_amount = len(explored)
                    path, moves = solution(child)
                    end_time = time.time()
                    final_time = end_time - start_time
                    return path, moves, explored_amount, first_cost, second_cost, final_time, True, nombre
                
                # Añadir el nodo hijo a la frontera con profundidad incrementada
                frontier.append((child, depth + 1))
        
    end_time = time.time()
    final_time = end_time - start_time
    explored_amount = len(explored)
    path, moves = solution(node)
    return path, moves, explored_amount, first_cost, second_cost, final_time, False, nombre

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

env = e.Environment(100, 0.08, 9)  # Tamaño, tasa de agujeros, semilla
result = depth_limited_search(env, limit=10)

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

path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
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
    showMoves(moves, env)