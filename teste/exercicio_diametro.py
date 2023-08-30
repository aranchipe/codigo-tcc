import math

L1 = 4  # m
L2 = 88  # m
L3 = 75  # m
L4 = 7  # m
Q = 200  # m^3/h
Q_real = Q/3600
H1 = 0.85  # m
H2 = 13.70  # m
P1 = 316  # kPa
hr = 9  # m
Pr = 70.3  # kPa
peso_esp = 9.5  # N/dm^3
visc = 5.5  # stokes

# calculo de P2
P2 = Pr + hr*peso_esp

# calculo da energia disponivel
energ_disp = (H1 + P1/peso_esp) - (H2 + P2/peso_esp)
comp_acid = 41.5
comp_trec_reto = L1+L2+L3+L4

comp_equiv = comp_acid+comp_trec_reto

# calculo do diametro a ser arbitrado
vel_eco = input("digite a velocidade econômica(m/s) - tabela 2.1: \n")
d_int = 0
fim = False

while fim == False:
    primeira_vez = input(
        "digite 'sim' se for a primeira tentativa e 'nao' se nao for: \n")
    if primeira_vez == "sim":

        d_arbitrado = math.sqrt(4*Q_real/(math.pi*int(vel_eco)))
        d_arb_pol = d_arbitrado * 39.37

        if d_arb_pol >= 24:
            d_arb_pol = 24
        elif d_arb_pol >= 20:
            d_arb_pol = 20
        elif d_arb_pol >= 18:
            d_arb_pol = 18
        elif d_arb_pol >= 16:
            d_arb_pol = 16
        elif d_arb_pol >= 14:
            d_arb_pol = 14
        elif d_arb_pol >= 12:
            d_arb_pol = 12
        elif d_arb_pol >= 10:
            d_arb_pol = 10
        elif d_arb_pol >= 8:
            d_arb_pol = 8
        elif d_arb_pol >= 6:
            d_arb_pol = 6
        elif d_arb_pol >= 4:
            d_arb_pol = 4
        elif d_arb_pol >= 3:
            d_arb_pol = 3
        elif d_arb_pol >= 2:
            d_arb_pol = 2
        elif d_arb_pol >= 1.5:
            d_arb_pol = 1.5
        elif d_arb_pol >= 1:
            d_arb_pol = 1
        elif d_arb_pol >= 0.75:
            d_arb_pol = 0.75
        print(f'o primeiro diâmetro a ser testado deve ser de {d_arb_pol}" ')
        d_int = float(input(
            "digite o diametro interno referente a séria escolhida (em cm): \n"))
    else:
        d_int = float(input(
            "digite o diametro interno referente a séria escolhida (em cm) - deve ser referente ao diâmetro nominal exatamente superior ao anterior: \n"))

    A = (math.pi * (d_int/100)**2)/4
    vel = (Q/3600)/A

    vel_cm = vel*100  # cm/s

    Re = (d_int * (vel*100))/visc

    J_cm = 32*comp_equiv*visc*vel_cm/(9.81*(d_int**2))  # cm
    J_m = J_cm/100

    if J_m > energ_disp:
        print("O diâmetro arbitrado é insuficiente, escolha um maior")
    else:
        print("O diâmetro arbitrado serve para o problema")
        fim = True
