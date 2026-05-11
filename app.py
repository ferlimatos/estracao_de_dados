from flask import Flask, jsonify, render_template
from scraper.curso_service import CursoService

app = Flask(__name__)

service = CursoService()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/cursos")
def cursos():
    return jsonify(service.listar_cursos())

if __name__ == "__main__":
    app.run(debug=True)