from abc import ABC, abstractmethod
import re
from datetime import datetime

class Pessoa(ABC):

  def __init__(self, nome, cpf, data_nascimento):
    self.nome = nome
    self.__cpf = cpf
    self.data_nascimento = data_nascimento

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
      datetime.strptime(data_nascimento, "%d/%m/%Y")
      return True
    except ValueError:
      return False

  @staticmethod
  def formatar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) == 11:
      return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf  
        
  @abstractmethod
  def exibir_dados(self):
    pass
