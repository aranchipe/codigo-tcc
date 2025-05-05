from flask import Blueprint, render_template, request
from sympy import symbols, Eq, solve, simplify
import math

vao_bp = Blueprint("vao", __name__) 

@vao_bp.route("/calculate_vao", methods=["POST"])
def calculate_vao():   
    espessura = float(request.form["espessura_real"])
    espessura_cm = espessura * 2.54
    diametro_vao= float(request.form["diametro_vao"])
    diametro_vao_cm = diametro_vao * 2.54
    q = float(request.form["q"])
    Q = float(request.form["Q"])
    W = float(request.form["W"])
    flecha = float(request.form["flecha"])
    S_v = float(request.form["S_v"])
    Z = float(request.form["Z"])
    E = float(request.form["E"])
    I = math.pi*((diametro_vao_cm/2)**4 - ((diametro_vao_cm/2)-espessura_cm)**4)/4


    numerador = -2*(Q + W) + math.sqrt((2*(Q + W))**2 + 4*q*10*Z*S_v)
    denominador = 2*q
    L_Sv = numerador / denominador

    L = symbols('L')
    equacao = Eq((q/4)*L**4 + ((Q + W)/3)*L**3 - (flecha * E * I)/2400, 0)
    solucoes = solve(equacao, L)

    L_flecha = next((simplify(sol) for sol in solucoes if sol.is_real and sol > 0), None)
    vao = round(min(L_Sv, L_flecha), 3)

    return render_template("vao_suportes_resultado.html", vao=vao, espessura=espessura)
