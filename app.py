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
@app.route('/api/cursos')
def api_cursos():
    nome = request.args.get('nome', '')
    unidade = request.args.get('unidade', '')

    # O service agora só retorna o que está aberto
    cursos = service.listar_cursos_validos(filtros={'nome': nome, 'unidade': unidade})

    return jsonify(cursos)

if __name__ == "__main__":
    app.run(debug=True)
