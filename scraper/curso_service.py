import json
from scraper.curso_scraper import CursoScraper


class CursoService:
    def __init__(self):
        self.scraper = CursoScraper("https://efg.org.br/cursos")
        self.caminho_arquivo = "data/cursos.json"

    def listar_cursos(self):
        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            cursos = json.load(arquivo)

        return cursos

    def listar_cursos_validos(self, filtros):
        """Retorna apenas cursos com status 'Aberto' por padrão para o MVP."""
        cursos = self.listar_cursos() # Lê o JSON

        # Filtra apenas os abertos primeiro
        abertos = [c for c in cursos if c.get("status") == "Aberto"]

        # Se houver outros filtros (unidade, nome), aplica sobre os abertos
        resultado = abertos
        for campo, valor in filtros.items():
            if valor:
                resultado = [
                    c for c in resultado
                    if valor.lower() in str(c.get(campo, "")).lower()
                ]
        return resultado

    def atualizar_cursos(self):
        cursos = self.scraper.coletar()

        cursos_dict = [curso.to_dict() for curso in cursos]

        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(cursos_dict, arquivo, ensure_ascii=False, indent=4)

            return cursos_dict

    def buscar_por_nome(self, termo):
        cursos = self.listar_cursos()

        return [
            curso for curso in cursos
            if termo.lower() in curso["nome_curso"].lower()
        ]

    def buscar_por_modalidade(self, modalidade):
        cursos = self.listar_cursos()

        return [
            curso for curso in cursos
            if modalidade.lower() in curso["modalidade"].lower()
        ]

    def buscar_por_nivel(self, nivel):
        cursos = self.listar_cursos()

        return [
            curso for curso in cursos
            if nivel.lower() in curso["nivel"].lower()
        ]

    def buscar_por_unidade(self, unidade):
        cursos = self.listar_cursos()

        return [
            curso for curso in cursos
            if unidade.lower() in curso["unidade"].lower()
        ]

    def buscar_por_area(self, area):
        cursos = self.listar_cursos()

        return [
            curso for curso in cursos
            if area.lower() in curso["area"].lower()
        ]
