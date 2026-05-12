# Esse arquivo funciona como uma camada intermediária. Ele cria o scraper com a URL: "https://efg.org.br/cursos" e tem um método 'listar_cursos' que chama o método 'coletar' do scraper para obter os dados dos cursos, convertendo-os em dicionários para facilitar a serialização em JSON.

from scraper.curso_scraper import CursoScraper

class CursoService:
    def __init__(self):
        self.scraper = CursoScraper("https://efg.org.br/cursos")

    def listar_cursos(self):
        cursos = self.scraper.coletar()
        return [c.to_dict() for c in cursos]
