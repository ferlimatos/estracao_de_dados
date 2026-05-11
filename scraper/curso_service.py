# services/curso_service.py

from scraper.curso_scraper import CursoScraper

class CursoService:
    def __init__(self):
        self.scraper = CursoScraper("https://efg.org.br/cursos")

    def listar_cursos(self):
        cursos = self.scraper.coletar()
        return [c.to_dict() for c in cursos]