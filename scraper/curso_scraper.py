# scraper/curso_scraper.py

import requests
from bs4 import BeautifulSoup
from domain.curso import Curso

class CursoScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def coletar(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        cursos = []

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

            botoes = {}
            for btn in cards.find_all("a", class_="btn"):
                botoes[btn.text.strip()] = btn.get("href")

            curso_obj = Curso(
                modalidade.text.strip() if modalidade else "",
                nivel.text.strip(),
                curso.text.strip(),
                localizacao.text.strip() if localizacao else "",
                idade,
                carga,
                botoes
            )

            cursos.append(curso_obj)

        return cursos