from flask import Flask, request, render_template, redirect, url_for
from grau_rugosidade import rugosidade
from fator_de_atrito import fator_atrito
import math

app = Flask(__name__)

diametros_serie_40 = {
    0.5: {"d_int": 15.76},
    0.75: {"d_int": 20.96},
    1: {"d_int": 26.64},
    1.25: {"d_int": 35.08},
    1.5: {"d_int": 40.94},
    2: {"d_int": 52.48},
    2.5: {"d_int": 62.68},
    3: {"d_int": 77.92},
    3.5: {"d_int": 90.12},
    4: {"d_int": 102.26},
    5: {"d_int": 128.2},
    6: {"d_int": 154.08},
    8: {"d_int": 202.74},
    10: {"d_int": 254.51},
    12: {"d_int": 303.22},
    14: {"d_int": 350.22},
}

@app.route("/")
def tipo_de_tubo():
    return render_template("tipo_de_tubo.html")

@app.route("/succao")
def succao():
    return render_template("succao.html")

@app.route("/recalque")
def recalque():
    return render_template("recalque.html")

@app.route("/espessura")
def espessura():
    return render_template("espessura.html")

@app.route("/selecao", methods=["POST"])
def selecao():
    tipo_tubulacao = request.form["tipoDeTubulacao"]
    return redirect(url_for(tipo_tubulacao))

@app.route("/calculate", methods=["POST"])
def calculate_diametro():
    tipo_tubulacao = request.form["tipoDeTubulacao"]
    Q = float(request.form["q"]) / 3600  # Convertendo para m³/s
    L_EQUIV = float(request.form["l_equi"])
    H1 = float(request.form["h1"])
    H2 = float(request.form["h2"])
    peso_esp = float(request.form["peso_esp"])
    visc = float(request.form["visc"])
    

    if tipo_tubulacao == "succao":
        P_atm = float(request.form["p_atm"])
        P_vapor = float(request.form["p_vapor"])
        NPSH = float(request.form["npsh"])
        energ_disp = (P_atm * 0.9 / peso_esp) - ((H1 - H2) + (P_vapor / peso_esp) + NPSH) # 90% para previnir variações na P_atm

    else:  # Recalque
        P1 = float(request.form["p1"])
        P2 = float(request.form["p2"])

        energ_disp = (H1 + P1 / peso_esp) - (H2 + P2 / peso_esp)

    def calculoNumeroDeReynolds(Q, d_int):
        d_cm = d_int / 10
        area = (math.pi * (d_cm ** 2)) / 4
        vel = (Q / area) * 1000000
        return (d_cm * vel) / visc

    def perdaDeCarga(Q, d_int):
        d_int_cm = d_int / 10
        area = (math.pi * (d_int_cm ** 2)) / 4  # Área em m²
        vel = (Q / area) * 1000000 # vel em cm/s
        Re = calculoNumeroDeReynolds(Q, d_int)
        grau_rugosidade = rugosidade(d_int)
        
        if Re < 2000:  # Escoamento laminar

            return (32 * L_EQUIV * visc * vel) / (981 * d_int_cm ** 2)
        else:  # Escoamento turbulento
            f_calc = fator_atrito(grau_rugosidade,Re)
            return (f_calc * L_EQUIV * vel ** 2) / (2 * 981 * d_int_cm)

    for diametro, info in diametros_serie_40.items():
        perda_carga =  perdaDeCarga(Q, info['d_int'])
        
        if perda_carga < energ_disp:
            return f"O diâmetro adequado é {diametro} pol."

    return "Nenhum diâmetro atende aos critérios."

@app.route("/espessura", methods=["GET", "POST"])
def calculate_espessura():
    return "Cálculo da Espessura"

if __name__ == "__main__":
    app.run()
