# 'app.py' é o arquivo principal da aplicação Flask. Ele é responsável por criar o servidor web, definir as rotas e integrar o serviço de cursos.
from flask import Flask, jsonify, render_template
from scraper.curso_service import CursoService

# Criação da aplicação Flask
app = Flask(__name__)

# Instanciação do serviço de cursos
service = CursoService()

# Rota para a página inicial, que renderiza o template 'index.html'.
@app.route("/")
def home():
    return render_template("index.html")

# Rota para obter a lista de cursos em formato JSON.
@app.route("/api/cursos")
def cursos():
    cursos = service.listar_cursos()

    return jsonify(cursos)

@app.route("/api/atualizar-cursos")
def cursos_atualizados():
    service.atualizar_cursos()

    return jsonify({"message": "Cursos atualizados com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
