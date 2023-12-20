import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np

def taylor(f, a, n):
    x = sp.Symbol('x')
    serie = sp.series(f, x, a, n, "+").removeO()
    return serie

def plot_grafico(x, y, label):
    plt.plot(x, y, label=label)
    plt.xlabel("Comprimento de onda")
    plt.ylabel("Radiação do corpo negro")
    plt.legend()

def calcular_serie(f, a, n, label):
    lvetor = np.arange(0.00001, 0.00005, 0.000001)
    serievetor = [taylor(f(l), a, n) for l in lvetor]
    plot_grafico(lvetor, serievetor, label)

def calcular_diferenca_relativa():
    lvetor = range(1, 1001)
    difvetor = []

    for l in lvetor:
        f1 = lei_rayleigh_jeans(l)
        f2 = lei_planck(l)
        serie1 = taylor(f1, a, n)
        serie2 = taylor(f2, a, n)
        difrelativa = abs((serie1 - serie2) / serie1)
        difvetor.append(difrelativa)

    plt.plot(np.array(lvetor), np.array(difvetor))
    plt.xlabel("Comprimento de onda")
    plt.ylabel("Diferença relativa entre as Leis")

# Ponto fixo
a = 1
# Quantidade de termos fixo
n = 10
# Constante de Planck
h = 6.6262 * (10 ** -34)
# Velocidade da luz
c = 2.997925 * (10 ** 8)
# Constante de Boltzmann
k = 1.3807 * (10 ** -23)
# Fixando a temperatura em Kelvin
T = 283.15

print("\nENUNCIADO\nUse o Polinômio de Taylor para mostrar que, para comprimentos de onda longos, a Lei de Planck fornece aproximadamente os mesmos valores que a Lei de Rayleigh-Jeans.\n")

# Lei de Rayleigh-Jeans
def lei_rayleigh_jeans(l):
    return (8 * math.pi * k * T) / (l ** 4)

# Lei de Planck
def lei_planck(l):
    return (8 * math.pi * h * c * (l ** (-5))) / (math.exp(h * c / (l * k * T)) - 1)

# Plotando gráfico para a Lei de Rayleigh-Jeans
calcular_serie(lei_rayleigh_jeans, a, n, "Rayleigh-Jeans")

# Plotando gráfico para a Lei de Planck
calcular_serie(lei_planck, a, n, "Planck")
plt.show()

# Plotando gráfico para a diferença relativa entre as Leis
calcular_diferenca_relativa()
plt.show()
