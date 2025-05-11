class Disciplina:
    total_disciplinas = 0   #atributo de classe

    def __init__(self, codigo, nome, professor_responsavel=None, alunos_matriculados=None):
      self.codigo = codigo
      self.nome = nome
      self.professor_responsavel = professor_responsavel  # objeto Professor
      self.alunos_matriculados = alunos_matriculados if alunos_matriculados is not None else []

    def adicionar_professor(self, professor):
      if self.professor_responsavel:
        # Desvincula o professor anterior
        self.professor_responsavel.remover_disciplina(self)
        print(f"Professor {self.professor_responsavel.nome} foi desvinculado da disciplina {self.nome}.")
     
      @classmethod
      def exibir_total_cadastrados(cls):
        print(f"Total de disciplinas cadastradas: {cls.total_disciplinas}")

      # Atribui o novo professor
      self.professor_responsavel = professor
      professor.adicionar_disciplina(self)
      print(f"O professor {professor.nome} foi atribuído como responsável pela disciplina {self.nome}.")

    def remover_professor(self):
      if self.professor_responsavel:
        self.professor_responsavel.remover_disciplina(self)
        print(f"Professor {self.professor_responsavel.nome} removido da disciplina {self.nome}.")
        self.professor_responsavel = None
      else:
        print(f"A disciplina {self.nome} não possui professor atribuído.")

    def exibir_dados(self):
        print(f"Disciplina: {self.nome} ({self.codigo})")
        print(f"Professor Responsável: {self.professor_responsavel.nome if self.professor_responsavel else 'N/A'}")
        print("Alunos Matriculados:")
        for aluno in self.alunos_matriculados:
            print(f"  {aluno.nome}")        
