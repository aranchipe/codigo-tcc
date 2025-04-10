import numpy as np

# Dados aproximados extraídos do gráfico
diametros = np.array([25, 50, 100, 200, 500])  # mm
rugosidade_relativa = np.array([0.0008, 0.0005, 0.0003, 0.0002, 0.0001])

# Ajuste de uma reta (regressão linear)
coef = np.polyfit(diametros, rugosidade_relativa, 1)  # Grau 1 -> Linear
a, b = coef  # Coeficientes da equação y = ax + b

# Função para calcular rugosidade relativa
def rugosidade(d):
    return a * d + b

# Testando a função
d_teste = 102.2 
print(f"Para d = {d_teste} mm, ε/d ≈ {rugosidade(d_teste):.6f}")

# Exibir equação da reta
print(f"Equação ajustada: ε/d = {a:.6e} * d + {b:.6e}")
