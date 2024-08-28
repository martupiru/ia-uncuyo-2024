import random
import copy
from environment import *
from agent import  *

# Parámetros del entorno
size = int(input("Ingrese el tamaño: "))
init_posX = random.randint(0, size-1)
init_posY = random.randint(0, size-1)
dirt_rate= float(input("Ingrese porcentaje de suciedad en el tablero. Numero entre 0 y 1: "))
while dirt_rate<0 or dirt_rate>=1:
    dirt_rate= float(input("Ingrese porcentaje de suciedad en el tablero. Numero entre 0 y 1: "))

promRandom = 0
promReflex = 0
for i in range(10):
    print(i+1)
    
    # Crear el entorno agente reflexivo
    env = Environment(size,size, init_posX, init_posY, dirt_rate)
    # Creamos copia entorno para agente random
    env1=copy.deepcopy(env)

    #env1.print_environment()
    env.print_environment()

    #Creamos agente reflexivo
    agent_reflex = Agent(env)
    #Creamos agente random
    agent_random = Agent(env1)

    #Agente Random
    print("AGENTE RANDOM: ")
    
    for _ in range(1000):
        #env1.print_environment()
        action = random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha', 'Limpiar', 'NoHacerNada'])
        #print(f"Acción elegida: {action}")
        agent_action = agent_random.choose_action(action)
        #si elegimos la accion limpiar y el casillero está vacio, limpia
        if action == 'Limpiar' and env1.is_dirty: env1.accept_action('Limpiar')
        else: env1.accept_action(agent_action)
        
        
    print("Rendimiento final:", env1.get_performance())
    promRandom = promRandom + env1.get_performance()
    

    #Agente Reflexivo
    #print('--------------------------------------------')
    print("AGENTE REFLEXIVO: ")
    
    for _ in range(1000):
        #env.print_environment()
        action = random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha', 'NoHacerNada'])
        #print(f"Acción elegida: {action}")
        agent_action = agent_reflex.choose_action(action)
        #si el casillero está vacio entonces limpiamos
        if env.is_dirty : env.accept_action('Limpiar')
        env.accept_action(agent_action)
        
    print("Rendimiento final:", env.get_performance())
    promReflex = promReflex + env.get_performance()
    print('--------------------------------------------')
    print('--------------------------------------------')
print("EL PROMEDIO DEL AGENTE RANDOM ES: " , (promRandom/10))
print("EL PROMEDIO DEL AGENTE REFLEXIVO ES: " , (promReflex/10))

