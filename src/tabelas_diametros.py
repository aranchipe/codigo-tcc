import math

diametros_serie_40 = {
    0.5: {
        "d_int": 15.76
    },
    0.75: {
        "d_int": 20.96
    },
    1: {
        "d_int": 26.64
    },
    1.25: {
        "d_int": 35.08
    },
    1.5: {
        "d_int": 40.94
    },
    2: {
        "d_int": 52.48
    },
    2.5: {
        "d_int": 62.68
    },
    3: {               
        "d_int": 77.92
    },
    3.5: {                
        "d_int": 90.12
    },
    4: {                
        "d_int": 102.26
    },
    5: {               
        "d_int": 128.2
    },
    6: {                
        "d_int": 154.08
    },
    8: {               
        "d_int": 202.74
    },
    10: {              
        "d_int": 254.51
    },
    12: {       
        "d_int": 303.22
    }

}


diametros_serie_80 = {
    0.5: {
        "d_int": 13.84
    },
    0.75: {
        "d_int": 18.88
    },
    1: {
        "d_int": 24.30
    },
    1.25: {
        "d_int": 32.50
    },
    1.5: {
        "d_int": 38.14
    },
    2: {
        "d_int": 49.22
    },
    2.5: {
        "d_int": 58.98
    },
    3: {               
        "d_int": 73.66
    },
    3.5: {                
        "d_int": 85.44
    },
    4: {                
        "d_int": 97.18
    },
    5: {               
        "d_int": 122.26
    },
    6: {                
        "d_int": 146.36
    },
    8: {               
        "d_int": 193.7
    },
    10: {              
        "d_int": 242.85
    },
    12: {       
        "d_int": 288.90
    }

}

""" print(diametros_serie_40[6]['d_int']) """

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
L_EQUIV = 215 # m

# calculo de P2
P2 = Pr + hr*peso_esp

# calculo da energia disponivel
energ_disp = (H1 + P1/peso_esp) - (H2 + P2/peso_esp)

print(round(energ_disp,2))