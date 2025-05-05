from flask import Blueprint, render_template, request, redirect, url_for
from functions.calculos import perdaDeCarga
from data.diametros import diametros_serie_40
main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def inicio():
    return render_template("inicio.html")

@main_bp.route("/succao")
def succao():
    return render_template("succao.html")

@main_bp.route("/recalque")
def recalque():
    tipo = request.args.get("tipo")
    return render_template("recalque.html", tipo=tipo)

@main_bp.route("/espessura")
def espessura():
    diametro = request.args.get("diametro")
    return render_template("espessura.html", diametro=diametro)

@main_bp.route("/vao_suportes")
def vao_suportes():
    espessura_real = request.args.get("espessura_real")
    diametro_vao = request.args.get("diametro_vao")
    return render_template("vao_suportes.html", espessura_real=espessura_real, diametro_vao=diametro_vao)

""" @vao_bp.route("/vao_suportes")
def vao_suportes():
    return render_template("vao_suportes.html")
 """
@main_bp.route("/diametro_espessura")
def diametro_espessura():
    tipo = request.args.get("tipo")

    return render_template("diametro_espessura.html", tipo=tipo)

@main_bp.route("/selecao", methods=["POST"])
def selecao():
    tipo_tubulacao = request.form["tipoDeTubulacao"]
    return redirect(url_for(f"main.diametro_espessura", tipo=tipo_tubulacao))




