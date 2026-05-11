class Curso:
    def __init__(self, modalidade, nivel, curso, localizacao, idade, carga_horaria, botoes):
        self.modalidade = modalidade
        self.nivel = nivel
        self.curso = curso
        self.localizacao = localizacao
        self.idade = idade
        self.carga_horaria = carga_horaria
        self.botoes = botoes
    
    def to_dict(self):
        return {
            "modalidade": self.modalidade,
            "nivel": self.nivel,
            "curso": self.curso,
            "localizacao": self.localizacao,
            "idade": self.idade,
            "carga_horaria": self.carga_horaria,
            "botoes": self.botoes
        }