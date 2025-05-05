from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, matricula, notas=None, disciplinas=None):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = notas if notas is not None else []
        self.disciplinas = disciplinas if disciplinas is not None else []

    #Para acessar os atributos privados
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def notas(self):
        return self.__notas 

    def exibir_dados(self):
        print(f"Aluno: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Matrícula: {self.matricula}")
        print("Disciplinas:")
        for i, disciplina in enumerate(self.disciplinas):
            notas_disciplina = self.__notas[i*3:(i+1)*3]
            print(f"  {disciplina.nome}: Notas: {notas_disciplina}")
