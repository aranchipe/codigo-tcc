from flask import Flask, request, render_template
import math

app = Flask(__name__)

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    L_EQUIV = float(request.form["l_equi"])

    Q = float(request.form["q"])
    Q_real = Q/3600

    H1 = float(request.form["h1"])
    H2 = float(request.form["h2"])
    P1 = float(request.form["p1"])
    hr = float(request.form["hr"])
    Pr = float(request.form["pr"])
    peso_esp = float(request.form["peso_esp"])
    visc = float(request.form["visc"])
    vel_eco = float(request.form["vel_eco"])

        # calculo de P2
    P2 = Pr + hr*peso_esp

    # calculo da energia disponivel
    energ_disp = (H1 + P1/peso_esp) - (H2 + P2/peso_esp)


    d_arbitrado = math.sqrt(4*Q_real/(math.pi*int(vel_eco)))
    d_arb_pol = d_arbitrado * 39.37

    # Verifica  primeiro diametro nominal a ser testado
    for diametro, info in diametros_serie_40.items():
        if(d_arb_pol >= diametro):
            d_usado = diametro 
        else:
            break       

    d_int = diametros_serie_40[d_usado]['d_int']
    d_int_cm = d_int/10

    print(f'O diametro a ser usado deve ser {d_usado}')
    print(f'O diametro interno vale: {round(d_int_cm,1)} cm')

    area = (math.pi * (d_int_cm/100)**2)/4
    vel = (Q/3600)/area

    vel_cm = vel*100  # cm/s

    J_cm = 32*L_EQUIV*visc*vel_cm/(9.81*(d_int_cm**2))  # cm   
    J_m = J_cm/100


    
    return f"Seu IMC é: {J_m}"

if __name__ == "__main__":
    app.run()