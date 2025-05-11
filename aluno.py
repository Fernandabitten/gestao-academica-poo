from pessoa import Pessoa

class Aluno(Pessoa):
    total_alunos = 0    #atributo de classe

    def __init__(self, nome, cpf, data_nascimento, matricula, notas=None, disciplinas=None):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = notas if notas is not None else []
        self.disciplinas = disciplinas if disciplinas is not None else []

    #Para acessar os atributos privados
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, nova_matricula):  
        self.__matricula = nova_matricula
    
    @property
    def notas(self):
        return self.__notas 
    
    @classmethod
    def exibir_total_cadastrados(cls):
        print(f"Total de alunos cadastrados: {cls.total_alunos}")
    
    def matricular_em_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            self.__notas.extend([0.0, 0.0, 0.0])  # adiciona 3 notas para a nova disciplina
        if hasattr(disciplina, 'alunos_matriculados') and self not in disciplina.alunos_matriculados:
            disciplina.alunos_matriculados.append(self)
            print(f"Matriculado na disciplina {disciplina.nome} com sucesso.")
        else:
            print(f"Aluno já está matriculado na disciplina {disciplina.nome}.")
    
    def desmatricular_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            index = self.disciplinas.index(disciplina)
            self.disciplinas.remove(disciplina)

            # Remove as 3 notas correspondentes à disciplina
            del self.__notas[index * 3 : index * 3 + 3]

            # Remove o aluno da lista da disciplina (se existir)
            if hasattr(disciplina, 'alunos_matriculados') and self in disciplina.alunos_matriculados:
                disciplina.alunos_matriculados.remove(self)
            print(f"Desmatriculado da disciplina {disciplina.nome} com sucesso.")

    def adicionar_nota(self, disciplina, nota, indice):
        """
        Adiciona ou altera uma das 3 notas do aluno em uma disciplina específica.        
        :param disciplina: objeto Disciplina
        :param nota: valor da nota (float)
        :param indice: posição da nota (0, 1 ou 2)
        """
        if not isinstance(nota, (int, float)):
            print("Nota deve ser um número.")
            return

        if nota < 0 or nota > 10:
            print("Nota deve estar entre 0 e 10.")
            return

        # Verifica se o aluno está matriculado na disciplina
        # e se a disciplina tem 3 notas
        if disciplina in self.disciplinas:
            if indice not in [0, 1, 2]:
                print("Índice de nota inválido. Use 0, 1 ou 2.")
                return

            posicao_disciplina = self.disciplinas.index(disciplina)
            self.__notas[posicao_disciplina * 3 + indice] = nota # Atualiza a nota na posição correta Se pos = 1 (segunda disciplina) e indice = 2 (terceira nota), então a posição será 1 * 3 + 2 = 5.
                                                                  # Assim, a sexta posição da lista __notas será atualizada com o valor de nota
            print(f"Nota {indice + 1} da disciplina '{disciplina.nome}' atualizada para {nota}.")
        else:
            print("Aluno não está matriculado nessa disciplina.")


    def calcular_media_geral(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)
    
    def calcular_media_por_disciplina(self):
        medias = {}
        for i, disciplina in enumerate(self.disciplinas):
            notas_disciplina = self.__notas[i*3:(i+1)*3] # pega o "pedaço" correspondente à disciplina.
            if notas_disciplina:
                media = sum(notas_disciplina) / len(notas_disciplina)
                medias[disciplina.nome] = media
            else:
                medias[disciplina.nome] = 0.0
        return medias
    
    def exibir_dados(self):
        print(f"Aluno: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Matrícula: {self.matricula}")
        print("Disciplinas:")
        for i, disciplina in enumerate(self.disciplinas):
            notas_disciplina = self.__notas[i*3:(i+1)*3]
            print(f"  {disciplina.nome}: Notas: {notas_disciplina}")

        print(f"Média Geral: {self.calcular_media_geral():.2f}")
        medias = self.calcular_media_por_disciplina()
        for disciplina in self.disciplinas:
            media = medias.get(disciplina.nome, 0.0)
            print(f"Média em {disciplina.nome}: {media:.2f}")