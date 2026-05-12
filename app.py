# 'app.py' é o arquivo principal da aplicação Flask. Ele é responsável por criar o servidor web, definir as rotas e integrar o serviço de cursos.
from flask import Flask, jsonify, render_template, request
from scraper.curso_service import CursoService

# Criação da aplicação Flask
app = Flask(__name__)
app.json.sort_keys = False

# Instanciação do serviço de cursos
service = CursoService()

# Rota para a página inicial, que renderiza o template 'index.html'.
@app.route("/")
def home():
    return render_template("index.html")

# Rota para obter a lista de cursos em formato JSON.
@app.route("/api/cursos")
def cursos():
    modalidade = request.args.get("modalidade")
    nivel = request.args.get("nivel")
    unidade = request.args.get("localizacao")

    cursos = service.listar_cursos()

    if modalidade:
        cursos = service.buscar_por_modalidade(modalidade)
    if nivel:
        cursos = service.buscar_por_nivel(nivel)
    if unidade:
        cursos = service.buscar_por_unidade(unidade)

    return jsonify(cursos)

if __name__ == "__main__":
    app.run(debug=True)
