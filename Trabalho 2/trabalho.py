import numpy as np
import matplotlib.pyplot as plt

def solve_heat_conduction(delta_x, delta_t):
    # Parâmetros do problema
    L = 1.0  # Espessura da parede
    Ts = 300.0  # Temperatura da superfície
    Ti = 100.0  # Temperatura interna
    alpha = 0.1  # Difusividade

    # Número de nós no espaço
    num_nodes = int(L / delta_x) + 1

    # Número de passos de tempo
    num_steps = int(tf / delta_t) + 1

    # Inicialização da matriz de temperaturas
    T = np.zeros((num_nodes, num_steps))

    # Condições iniciais
    T[:, 0] = Ti
    T[0, :] = Ts
    T[-1, :] = Ts

    # Iteração pelos passos de tempo e nós espaciais
    for j in range(0, num_steps - 1):
        for i in range(1, num_nodes - 1):
            T[i, j+1] = T[i, j] + alpha * delta_t / (delta_x**2) * (T[i+1, j] - 2*T[i, j] + T[i-1, j])

    return T

# Parâmetros do problema
delta_x_1 = 0.05
delta_t_1 = 0.01
delta_x_2 = 0.05
delta_t_2 = 0.05
tf = 0.1

# Solução aproximada para delta_x = 0.05 e delta_t = 0.01
T_1 = solve_heat_conduction(delta_x_1, delta_t_1)

# Solução aproximada para delta_x = 0.05 e delta_t = 0.05
T_2 = solve_heat_conduction(delta_x_2, delta_t_2)

# Solução exata
x = np.linspace(0, 1, int(1/delta_x_1) + 1)
Ts = 300.0  # Temperatura da superfície
Ti = 100.0  # Temperatura interna
L = 1.0  # Espessura da parede
alpha = 0.1  # Difusividade
exact_solution = Ts + 2*(Ti - Ts) * np.sum(np.exp(-(np.pi**2 / L**2) * alpha * tf) * (1 - (-1)**np.arange(1, 100)) / (np.arange(1, 100) * np.pi) * np.sin(np.pi * np.arange(1, 100) * x[:, np.newaxis] / L), axis=1)

# Plotagem dos resultados
plt.plot(x, T_1[:, -1], label='Aprox. (delta_x = 0.05, delta_t = 0.01)')
plt.plot(x, T_2[:, -1], label='Aprox. (delta_x = 0.05, delta_t = 0.05)')
plt.plot(x, exact_solution, label='Exata')
plt.xlabel('Posição (x)')
plt.ylabel('Temperatura (oF)')
plt.title('Distribuição de Temperatura na Parede')
plt.legend()
plt.grid(True)
plt.show()
