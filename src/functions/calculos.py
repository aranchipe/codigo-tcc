from functions.grau_rugosidade import rugosidade
from functions.fator_de_atrito import fator_atrito
import math

def calculoNumeroDeReynolds(Q, d_int,visc):
        d_cm = d_int / 10
        area = (math.pi * (d_cm ** 2)) / 4
        vel = (Q / area) * 1000000
        return (d_cm * vel) / visc

def perdaDeCarga(Q, d_int, L_EQUIV, visc):
    d_int_cm = d_int / 10
    area = (math.pi * (d_int_cm ** 2)) / 4
    vel = (Q / area) * 1000000
    Re = calculoNumeroDeReynolds(Q, d_int, visc)
    grau_rugosidade = rugosidade(d_int)

    if Re < 2000:
        return (32 * L_EQUIV * visc * vel) / (981 * d_int_cm ** 2)
    else:
        f_calc = fator_atrito(grau_rugosidade, Re)
        return (f_calc * L_EQUIV * vel ** 2) / (2 * 981 * d_int_cm) 