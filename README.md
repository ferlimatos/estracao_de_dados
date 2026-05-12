# Portal de Extração de Dados da EFG

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de automatizar a coleta de informações de cursos disponíveis no site da EFG.

A aplicação utiliza **Web Scraping** para acessar a página de cursos da EFG, extrair os dados automaticamente e disponibilizá-los através de uma API construída com Flask.

Na primeira versão, os dados eram coletados no momento em que o usuário acessava a rota da API. Isso fazia com que a resposta demorasse alguns segundos, pois o sistema precisava acessar o site da EFG, ler o HTML e extrair os cursos antes de mostrar o resultado.

Na nova versão, a coleta passa a acontecer antes, por meio de um script separado. Esse script salva os cursos em um arquivo JSON. Depois, o Flask apenas lê esse arquivo pronto e retorna os dados instantaneamente.

## Tecnologias utilizadas

### Python

Linguagem principal utilizada no projeto.

### Flask

Framework web utilizado para criar a aplicação e as rotas da API.

```python
@app.route("/api/cursos")
def cursos():
    return jsonify(service.listar_cursos())
```

### Web Scraping

Web Scraping é o processo de extrair informações automaticamente de páginas da web.

Bibliotecas utilizadas:

#### Requests

```python
requests.get(url)
```

#### BeautifulSoup

```python
soup.find_all()
```

## Estrutura do projeto

```text
estracao_de_dados/
├── app.py
├── domain/
│   └── curso.py
├── scraper/
│   ├── curso_scraper.py
│   └── curso_service.py
├── templates/
│   └── index.html
└── static/
    └── estilo.css
```

## Fluxo da aplicação

```text
Site da EFG
     ↓
Scraper coleta os dados
     ↓
Python organiza os cursos
     ↓
Flask disponibiliza os dados
     ↓
API retorna JSON
```

## Explicando cada parte

### `app.py`

Arquivo principal da aplicação Flask.

Responsável por:

- iniciar o servidor;
- criar as rotas;
- retornar as respostas da API.

### `domain/curso.py`

Contém a classe `Curso`, que representa cada curso encontrado no site.

Essa classe guarda informações como:

- modalidade;
- nível;
- nome do curso;
- localização;
- idade mínima;
- carga horária;
- links.

### Método `to_dict()`

O método `to_dict()` transforma um objeto `Curso` em um dicionário.

Isso é importante porque o Flask consegue converter dicionários em JSON.

### `scraper/curso_scraper.py`

Responsável pela extração dos dados.

Ele:

1. acessa a página da EFG;
2. lê o HTML;
3. procura os cards dos cursos;
4. extrai os dados;
5. cria objetos da classe `Curso`.

### `scraper/curso_service.py`

Funciona como uma camada intermediária entre o Flask e o scraper.

```text
Flask ↔ Service ↔ Scraper
```

Ela chama o scraper, recebe os cursos, transforma os objetos em dicionários e devolve os dados prontos para a API.

## API REST

A aplicação possui uma API simples para listar os cursos coletados.

### Endpoint

```http
GET /api/cursos
```

Exemplo de resposta:

```json
[
  {
    "nome": "Curso de Python",
    "modalidade": "Online"
  }
]
```

## JSON

JSON é um formato usado para troca de informações entre sistemas.

Exemplo:

```json
{
  "nome": "Curso de Python",
  "modalidade": "Online"
}
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/ferlimatos/estracao_de_dados.git
```

### 2. Entrar na pasta

```bash
cd estracao_de_dados
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install flask requests beautifulsoup4
```

### 6. Executar o projeto

```bash
flask run
```

ou:

```bash
python app.py
```

## Possíveis melhorias futuras

- Salvar os dados em banco de dados;
- Criar filtros de busca;
- Adicionar paginação;
- Criar uma interface completa;
- Automatizar a atualização dos cursos;
- Consumir múltiplos sites além da EFG.

## Conceitos praticados

- Python;
- Flask;
- Rotas;
- APIs REST;
- JSON;
- Web Scraping;
- Requests;
- BeautifulSoup;
- Programação Orientada a Objetos;
- Organização em camadas;
- Serialização de objetos.

## Créditos

Projeto desenvolvido com base em uma estrutura de referência apresentada em aula pelo professor [André][https://github.com/anderTron1], sendo adaptado e expandido para fins de estudo.
