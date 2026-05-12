# 'curso_scraper.py' é o arquivo responsável por extrair os dados dos cursos de uma página web.
# O requests acessa o site da EFG, e o BeautifulSoup lê o HTML da página para encontrar os cards dos cursos.
import requests
from bs4 import BeautifulSoup
from domain.curso import Curso

class CursoScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0"}

    # Método para coletar os dados dos cursos da página web. Ele faz uma requisição GET para a URL especificada, analisa o conteúdo HTML e extrai as informações relevantes para criar objetos do tipo 'Curso'.
    def coletar(self):
        # realiza a requisição para a página e cria um objeto BeautifulSoup para analisar o HTML
        response = requests.get(self.url, headers=self.headers)
        # O BeautifulSoup é usado para analisar o conteúdo HTML da resposta e facilitar a extração dos dados dos cursos.
        soup = BeautifulSoup(response.text, "html.parser")

        # A variável 'cursos' é uma lista que armazenará os objetos 'Curso' criados a partir dos dados extraídos da página.
        cursos = []

        # Loop para percorrer cada card de curso encontrado na página. Para cada card, ele extrai as informações de modalidade, nível, nome do curso, localização, idade mínima, carga horária e os links dos botões disponíveis.
        for cards in soup.select(".col-md-4"):
            modalidade = cards.select_one(".cci-modalidade")

            titulos = cards.select(".ccc-titulo")
            nivel = titulos[0] if len(titulos) > 0 else ""
            curso = titulos[1] if len(titulos) > 1 else ""

            localizacao = cards.select_one(".ccc-colegios")

            outros = cards.select_one(".ccc-outros")
            spans = outros.find_all("span") if outros else []

            idade = None
            carga = None

            if len(spans) > 0:
                idade = spans[0].get_text(strip=True)
                idade = idade.replace("anos", " anos")
                idade = idade.split("anos")[0].split()[-1] if "anos" in idade else None

            if len(spans) > 1:
                carga = spans[-1].get_text(strip=True)

            botoes = {btn.text.strip(): btn.get("href") for btn in cards.find_all("a", class_="btn")}
            status = "Aberto"
            texto_botoes = " ".join(botoes.keys()).lower()
            if "inscrições indisponíveis" in texto_botoes or "avise-me" in texto_botoes:
                status = "Indisponível"
            elif not botoes:
                # Caso o curso não tenha botão nenhum, talvez seja melhor marcar como indisponível
                status = "Indisponível"

            # curso_obj é criado como uma instância da classe 'Curso', utilizando os dados extraídos do card.
            curso_obj = Curso(
    nome=curso.text.strip() if curso else "Não informado",
    categoria="Geral",
    nivel=nivel.text.strip() if nivel else "",
    modalidade=modalidade.text.strip() if modalidade else "",
    unidade=localizacao.text.strip() if localizacao else "",
    status=status,
    carga_horaria=carga,
    botoes=botoes
)

            # O objeto 'curso_obj' é adicionado à lista 'cursos', que será retornada ao final do método.
            cursos.append(curso_obj)

        # O método retorna uma lista de objetos 'Curso' com os dados coletados.
        return cursos
