from flask import Blueprint, render_template, request 
from data.diametros import diametros

espessura_bp = Blueprint("espessura", __name__)

@espessura_bp.route("/calculate_espessura", methods=["POST"])
def calculate_espessura():
    diametro = float(request.form["diametro"]) 
    d_ext = diametros[diametro]["d_ext"]
    p_proj = float(request.form["p_proj"])
    C = float(request.form["margem_corrosao"])
    E = float(request.form["E"])
    Y = float(request.form["Y"])
    Sh = float(request.form["Sh"])

    espessura = (p_proj*d_ext)/(2*(Sh*E + p_proj*Y)) + C
    espessura = round(espessura*1.143, 3)

    tubo_compatível = None
    for tubo in diametros[diametro]["tubos"]:
        if tubo["espessura_pol"] >= espessura:
            tubo_compatível = tubo
            break

    if tubo_compatível:
        return render_template(
            "espessura_resultado.html",
            espessura=espessura,
            schedule=tubo_compatível["schedule"],
            espessura_real=tubo_compatível["espessura_pol"]
        )
    else:
        return render_template(
            "espessura_resultado.html",
            espessura=espessura,
            schedule=None,
            espessura_real=None,
            mensagem="Nenhum tubo disponível atende à espessura mínima."
        )
    
    """ return render_template("espessura_resultado.html", espessura=espessura) """
