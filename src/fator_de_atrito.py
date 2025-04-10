import math

def fator_atrito(rugosidade, Re):

# Equação de Haaland para calcular o fator de atrito f
    f = 1 / ( -1.8 * math.log10( ( (rugosidade) / 3.7 )**1.11 + (6.9 / Re) ) )**2

# Exibir resultado
    return f 