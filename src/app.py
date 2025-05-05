from flask import Flask
from routes import main_bp, vao_bp, diametro_espessura_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(vao_bp)
app.register_blueprint(diametro_espessura_bp)

if __name__ == "__main__":
    app.run(debug=True)
