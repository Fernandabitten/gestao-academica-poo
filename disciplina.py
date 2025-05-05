class Disciplina:
    def __init__(self, codigo, nome, professor_responsavel=None, alunos_matriculados=None):
        self.codigo = codigo
        self.nome = nome
        self.professor_responsavel = professor_responsavel  # objeto Professor
        self.alunos_matriculados = alunos_matriculados if alunos_matriculados is not None else []

    def exibir_dados(self):
        print(f"Disciplina: {self.nome} ({self.codigo})")
        print(f"Professor Responsável: {self.professor_responsavel.nome if self.professor_responsavel else 'N/A'}")
        print("Alunos Matriculados:")
        for aluno in self.alunos_matriculados:
            print(f"  {aluno.nome}")
