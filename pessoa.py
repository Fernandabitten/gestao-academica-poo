from abc import ABC, abstractmethod
import re
from datetime import datetime

class Pessoa(ABC):
    total_pessoas = 0   #atributo de classe

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento

    @classmethod
    def exibir_total_cadastrados(cls):
        print(f"Total de pessoas cadastradas: {cls.total_pessoas}")

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):  
        self.__cpf = self.validar_cpf(novo_cpf)

    @staticmethod
    def validar_cpf (cpf):
        cpf = re.sub(r'\D','', cpf)
        return len (cpf) == 11 and cpf.isdigit()
    
    @staticmethod
    def validar_data (data_nascimento):
        try:
            datetime.strptime(data_nascimento, "%d/%m/%y")
            return True
        except ValueError:
            return False
           
    @abstractmethod
    def exibir_dados(self):
        pass
