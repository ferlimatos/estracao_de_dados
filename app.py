# 'app.py' é o arquivo principal da aplicação Flask. Ele é responsável por criar o servidor web, definir as rotas e integrar o serviço de cursos.
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from scraper.curso_service import CursoService

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)
app.json.sort_keys = False

# Instanciação do serviço de cursos
service = CursoService()

# Rota para a página inicial, que renderiza o template 'index.html'.
@app.route("/")
def home():
    return render_template("index.html")

# Rota para obter a lista de cursos em formato JSON.
@app.route('/api/cursos')
def api_cursos():
    nome = request.args.get('nome', '')
    nivel = request.args.get('nivel', '')
    unidade = request.args.get('unidade', '')
    modalidade = request.args.get('modalidade', '')

    # O service agora só retorna o que está aberto
    cursos = service.listar_cursos_validos(termo=nome, unidade=unidade, nivel=nivel, modalidade=modalidade)

    return jsonify(cursos)

if __name__ == "__main__":
    app.run(debug=True)
