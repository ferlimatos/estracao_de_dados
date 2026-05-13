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

    def listar_cursos_validos(self, **filtros):
        """Retorna apenas cursos abertos com textos de botões tratados."""
        cursos = self.listar_cursos()

        # 1. Filtra apenas os abertos
        resultado = [c for c in cursos if c.get("status") == "Aberto"]

        # 2. Aplica filtros de busca dinâmicos
        for campo, valor in filtros.items():
            if valor:
                # CORREÇÃO DE MAPEAMENTO:
                # Se o JS manda 'termo', procuramos em 'nome' no JSON
                if campo == "termo":
                    chave = "nome"
                else:
                    # Se o JS manda 'unidade', 'nivel' ou 'modalidade',
                    # usamos o nome do campo direto
                    chave = campo

                valor_str = str(valor).lower()

                # Filtramos a lista baseada no campo atual
                resultado = [
                    c for c in resultado
                    if valor_str in str(c.get(chave, "")).lower()
                ]

                # O print ajuda a conferir no terminal se a chave bate com o JSON
                print(f"Filtrando campo JSON: {chave} | Valor buscado: {valor_str}")

        # 3. Tratamento de UX Writing nos botões
        for curso in resultado:
            curso["botoes"] = self.tratar_botoes_ux(curso.get("botoes"))

        return resultado

    def tratar_botoes_ux(self, botoes_crus):
        """Traduz os textos dos botões para padrões de UX Writing."""
        botoes_limpos = {}
        if not botoes_crus:
            return botoes_limpos

        for texto, link in botoes_crus.items():
            texto_min = texto.lower()

            # Aplica o UX Writing
            if "inscrev" in texto_min or "inscrição" in texto_min:
                novo_texto = "Fazer inscrição"
            elif any(palavra in texto_min for palavra in ["detalhes", "saiba", "edital", "disponíveis"]):
                novo_texto = "Ver detalhes"

            botoes_limpos[novo_texto] = link
        return botoes_limpos

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
            if termo.lower() in curso["nome"].lower()
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
