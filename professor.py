from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, siape, disciplinas=None):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = disciplinas if disciplinas is not None else []

    @property
    def siape(self):
        return self.__siape

    def exibir_dados(self):
        print(f"Professor: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"SIAPE: {self.siape}")
        print("Disciplinas:")
        for disciplina in self.disciplinas:
            print(f"  {disciplina.nome}")
