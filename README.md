# Portal Go Cursos

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de centralizar cursos gratuitos disponíveis em todo o estado de Goiás, facilitando o acesso da população a oportunidades de educação, capacitação e desenvolvimento profissional.

Atualmente, essas oportunidades estão espalhadas em diferentes sites e instituições (como EFG, IFG, Senai, entre outros), o que dificulta encontrar cursos com inscrições abertas de forma rápida e organizada.

A proposta do portal é reunir essas informações em um único lugar, tornando a busca por cursos mais acessível, simples e eficiente.

O projeto foi desenvolvido como parte da 1ª APA (Aprendizagem por Projeto Aplicada) do curso técnico em Desenvolvimento Web & Mobile na EFG José Luiz Bittencourt, inspirado pelo Dia Internacional da Educação, celebrado em 24 de janeiro e reconhecido pela ONU como uma data voltada à valorização da educação como ferramenta de transformação social e desenvolvimento.

---

## Evolução da coleta de dados

* [v1-mvp](https://github.com/ferlimatos/estracao_de_dados/tree/v1-mvp): na primeira versão do projeto, os dados eram coletados no momento em que o usuário acessava a rota da API.

Isso fazia com que a resposta demorasse alguns segundos, pois o sistema precisava:

1. acessar o site da EFG;
2. ler o HTML da página;
3. extrair os cursos;
4. organizar os dados;
5. retornar o resultado.

Na versão atual, a coleta passou a acontecer separadamente, por meio de um script próprio de scraping.

Esse script é executado manualmente pelo desenvolvedor e salva os cursos em um arquivo `JSON`.

Depois disso, o Flask apenas lê o arquivo já pronto e retorna os dados instantaneamente, melhorando significativamente o desempenho da aplicação.

O fluxo atual funciona da seguinte forma:

```text
Scraper → cursos.json → Flask → HTML
```

---

## Sobre a identificação dos cursos

O site da EFG não informa explicitamente o status dos cursos no HTML da página.

Por isso, o projeto utiliza algumas verificações para identificar automaticamente quais cursos possuem inscrições disponíveis.

Atualmente, um curso é considerado como `"Aberto"` quando o card possui:

- localização;
- idade mínima;
- carga horária;
- botão de inscrição.

Já os cursos que apresentam mensagens relacionadas à indisponibilidade de inscrições são classificados como `"Indisponível"`.

---

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- JSON
- Requests
- BeautifulSoup
- JavaScript (apenas quando necessário)

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

### app.py

Arquivo principal da aplicação Flask.

Responsável por:

* iniciar o servidor;
* criar as rotas;
* retornar as respostas da API.

### domain/curso.py

Contém a classe Curso, que representa cada curso encontrado no site.

Essa classe guarda informações como:

* modalidade;
* nível;
* nome do curso;
* localização;
* idade mínima;
* carga horária;
* links.

### Método to_dict()

O método to_dict() transforma um objeto Curso em um dicionário.

Isso é importante porque o Flask consegue converter dicionários em JSON.

### scraper/curso_scraper.py

Responsável pela extração dos dados.

1. acessa a página da EFG;
2. lê o HTML;
3. procura os cards dos cursos;
4. extrai os dados;
5. cria objetos da classe Curso.

### scraper/curso_service.py

Funciona como uma camada intermediária entre o Flask e o scraper. Aqui também é onde são colocado as regras de negócio.

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

* Salvar os dados em banco de dados;
* Adicionar paginação;
* Criar uma interface completa;
* Automatizar a atualização dos cursos;
* Consumir múltiplos sites além da EFG.

## Conceitos praticados

* Python;
* Flask;
* Rotas;
* APIs REST;
* JSON;
* Web Scraping;
* Requests;
* BeautifulSoup;
* Programação Orientada a Objetos;
* Organização em camadas;
* Serialização de objetos.

## Créditos

Projeto desenvolvido com base em uma estrutura de referência apresentada em aula pelo professor [André](https://github.com/anderTron1), sendo adaptado e expandido para fins de estudo.
