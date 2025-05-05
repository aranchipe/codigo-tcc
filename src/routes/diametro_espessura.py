from flask import Blueprint, render_template, request 
from data.diametros import diametros
from functions.calculos import perdaDeCarga
from data.tensoes_admissiveis import tensoes_admissiveis


diametro_espessura_bp = Blueprint("diametro_espessura", __name__)

@diametro_espessura_bp.route("/calculate_diametro_espessura", methods=["POST"])
def calculate_diametro_espessura(): 
    tipo_tubulacao = request.form["tipo"]
    material = request.form["material"]
    temp = float(request.form["temp"])

    p_proj = float(request.form["p_proj"])
    C = float(request.form["margem_corrosao"])
    E = float(request.form["E"])
    Y = float(request.form["Y"])

    tensoes = tensoes_admissiveis[material]["tensoes_ksi"]

    temperaturas_possiveis = [t for t in tensoes if t >= temp]

    if temperaturas_possiveis:
        temperatura_usada = min(temperaturas_possiveis) 
        Sh = tensoes[temperatura_usada]*1000
    else:
        error_temp = "Temperatura acima do limite para este material"
        return render_template("resultado_diametro_espessura.html", error_temp=error_temp)

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

    for diam_nominal, valores in diametros.items():
        d_ext = valores['d_ext']
        for tubo in valores['tubos']:
            espessura = (p_proj*d_ext)/(2*(Sh*E + p_proj*Y)) + C
            espessura = round(espessura*1.143, 3)
            d_int = tubo['d_int_mm']
            esp = tubo['espessura_pol']
            perda_carga = perdaDeCarga(Q, d_int, L_EQUIV, visc)
            
            if perda_carga < energ_disp and esp > espessura:
                return render_template("resultado_diametro_espessura.html", diametro=diam_nominal, schedule=tubo['schedule'], espessura_real=esp,espessura=espessura, material=material)
                    
