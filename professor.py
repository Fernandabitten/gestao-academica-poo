from pessoa import Pessoa
from datetime import datetime

class Professor(Pessoa):
    total_professores = 0   #atributo de classe

    def __init__(self, nome, cpf, data_nascimento, siape, disciplinas=None):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = disciplinas if disciplinas is not None else []
        Professor.total_professores += 1

    @property
    def siape(self):
      return self.__siape
    
    @siape.setter
    def siape(self, novo_siape): 
        self.__siape = novo_siape

    @classmethod
    def exibir_total_cadastrados(cls):
      return print(f"Total de professores cadastrados: {cls.total_professores}")

    def adicionar_disciplina(self, disciplina):
      if disciplina not in self.disciplinas:
        self.disciplinas.append(disciplina)
        print(f"Disciplina '{disciplina.nome}' adicionada com sucesso ao professor {self.nome}.")
      else:
        print(f"Professor {self.nome} já ministra a disciplina '{disciplina.nome}'.")

    def remover_disciplina(self, disciplina):
      if disciplina in self.disciplinas:
        self.disciplinas.remove(disciplina)
        print(f"Disciplina {disciplina.nome} removida do professor {self.nome}..")
      else:
        print(f"Disciplina não encontrada na lista do professor {self.nome}.")
        return self.__siape

    def exibir_dados(self):
      print(f"Professor: {self.nome}")
      print(f"CPF: {self.cpf}")
      try:
        data_formatada = datetime.strptime(self.data_nascimento, "%Y-%m-%d").strftime("%d/%m/%Y")
      except ValueError:
        data_formatada = self.data_nascimento  
      print(f"Data de Nascimento: {data_formatada}")
      print(f"SIAPE: {self.siape}")
      print("Disciplinas:")
      for disciplina in self.disciplinas:
          print(f"  {disciplina.nome}")
