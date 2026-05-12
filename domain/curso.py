# 'curso.py' é o arquivo que define a classe 'Curso', que representa um curso com suas características e métodos para converter seus dados em formato de dicionário.

OPCOES_VALIDAS = {
    "unidades": ["Artes Basileu França", "José Luiz Bittencourt", "Luiz Rassi", "Paulo Renato de Souza", "Raul Brandão de Castro", "Sarah L. L. Kubitschek de Oliveira"],
    "niveis": ["Capacitação", "Qualificação profissional", "Técnico de nível médio", "Curso Superior"],
    "modalidades": ["Presencial", "Online", "EAD"],
    "status": ["Aberto", "Indisponível"]
}

class Curso:
    def __init__(self, nome, categoria, nivel, modalidade, unidade, status, carga_horaria, botoes):
        self.nome = nome
        self.categoria = categoria
        self.carga_horaria = carga_horaria
        self.botoes = botoes

        # Validação e padronização dos atributos 'nivel', 'modalidade', 'unidade' e 'status' usando o método 'validar'.
        self.nivel = self.validar(nivel, OPCOES_VALIDAS["niveis"])
        self.modalidade = self.validar(modalidade, OPCOES_VALIDAS["modalidades"])
        self.unidade = self.validar(unidade, OPCOES_VALIDAS["unidades"])
        self.status = self.validar(status, OPCOES_VALIDAS["status"])


    def validar(self, valor, lista_opcoes):
        if not valor:
            return "Não informado"

        valor_limpo = valor.strip()
        for opcao in lista_opcoes:
            if valor_limpo.lower() == opcao.lower():
                return opcao

        return valor_limpo

    # Método para converter os atributos do curso em um dicionário, facilitando a serialização para JSON.
    def to_dict(self):
        return {
            "nome": self.nome,
            "categoria": self.categoria,
            "nivel": self.nivel,
            "modalidade": self.modalidade,
            "unidade": self.unidade,
            "carga_horaria": self.carga_horaria,
            "botoes": self.botoes,
            "status": self.status
        }

# if __name__ == "__main__":
#     print("--- INICIANDO TESTES DE VALIDAÇÃO ---")

#     # Caso 1: Dados com variações de caixa (MAIÚSCULA/minúscula) e espaços
#     # O site pode trazer "ead" ou "  EAD  ", mas sua lista tem "EAD"
#     c1 = Curso(
#         nome="Desenvolvimento Web",
#         categoria="Tecnologia",
#         nivel="curso técnico",      # Está em minúsculo na entrada
#         modalidade="  ead  ",       # Espaços e minúsculo
#         unidade="luiz rassi",       # Minúsculo
#         status="ABERTO",            # Maiúsculo
#         carga_horaria="1200h",
#         botoes=["Saiba Mais"]
#     )

#     # Caso 2: Dados que NÃO estão na lista (deve retornar o valor original limpo)
#     c2 = Curso(
#         nome="Pós-Graduação em IA",
#         categoria="Tecnologia",
#         nivel="Mestrado",           # Não existe em OPCOES_VALIDAS
#         modalidade="Híbrido",       # Não existe em OPCOES_VALIDAS
#         unidade="Unidade Marte",    # Não existe em OPCOES_VALIDAS
#         status="Encerrado",         # Não existe em OPCOES_VALIDAS
#         carga_horaria="360h",
#         botoes=[]
#     )

#     # Caso 3: Valores vazios ou None
#     c3 = Curso("Curso Vazio", "Geral", None, "", None, "", "0h", [])

#     def imprimir_resultado(obj, titulo):
#         print(f"\n> {titulo}:")
#         # Usando seu método de dicionário para visualizar
#         dados = obj.to_dict()
#         for chave, valor in dados.items():
#             print(f"  {chave.capitalize()}: {valor}")

#     imprimir_resultado(c1, "TESTE 1 (PADRONIZAÇÃO)")
#     imprimir_resultado(c2, "TESTE 2 (VALORES FORA DA LISTA)")
#     imprimir_resultado(c3, "TESTE 3 (VALORES NULOS)")
