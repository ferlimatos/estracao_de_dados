# Usado apenas quando quiser atualizar os dados dos cursos
import json
from scraper.curso_scraper import CursoScraper

scraper = CursoScraper("https://efg.org.br/cursos")

cursos = scraper.coletar()

cursos_dict = [curso.to_dict() for curso in cursos]

with open("data/cursos.json", "w", encoding="utf-8") as arquivo:
    json.dump(cursos_dict, arquivo, ensure_ascii=False, indent=4)

print("Cursos atualizados com sucesso!")
