from flask import Blueprint, render_template, request
from data.diametros import diametros_serie_40, diametros
from functions.calculos import perdaDeCarga

diametro_bp = Blueprint("diametro", __name__)

@diametro_bp.route("/calculate_diametro", methods=["POST"])
def calculate_diametro():
    tipo_tubulacao = request.form["tipoDeTubulacao"]
    Q = float(request.form["q"]) / 3600
    L_EQUIV = float(request.form["l_equi"])
    H1 = float(request.form["h1"])
    H2 = float(request.form["h2"]) 
    peso_esp = float(request.form["peso_esp"])
    visc = float(request.form["visc"])

    if tipo_tubulacao == "succao":
        P_atm = float(request.form["p_atm"])
        P_vapor = float(request.form["p_vapor"])
        NPSH = float(request.form["npsh"])
        energ_disp = (P_atm * 0.9 / peso_esp) - ((H1 - H2) + (P_vapor / peso_esp) + NPSH)
    else:
        P1 = float(request.form["p1"])
        P2 = float(request.form["p2"])
        energ_disp = (H1 + P1 / peso_esp) - (H2 + P2 / peso_esp)

    """ for diametro, info in diametros_serie_40.items():
        perda_carga = perdaDeCarga(Q, info['d_int'], L_EQUIV, visc)
        if perda_carga < energ_disp:
            return render_template("resultado.html", diametro=diametro) """
    for diam_nominal, valores in diametros.items():
        for tubo in valores['tubos']:
            d_int = tubo['d_int_mm']
            perda_carga = perdaDeCarga(Q, d_int, L_EQUIV, visc)
            if perda_carga < energ_disp:
                return render_template("resultado.html", diametro=diam_nominal, schedule=tubo['schedule'])

    return "Nenhum diâmetro atende aos critérios."