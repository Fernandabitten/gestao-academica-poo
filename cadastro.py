from aluno import Aluno
from professor import Professor
from disciplina import Disciplina
from pessoa import Pessoa
from persistencia import (salvar_alunos, salvar_professores, salvar_disciplinas, caminho_arquivo_alunos, caminho_arquivo_professores, caminho_arquivo_disciplinas)
from datetime import datetime

def cadastrar_aluno(lista_alunos):
  print("\nCadastro de Aluno")
  nome = input("Nome: ").title()

  # Validar CPF
  while True:
    cpf = input("CPF (somente números ou com pontuação): ")
    if Pessoa.validar_cpf(cpf):
      cpf = Pessoa.formatar_cpf(cpf)
      print(f"CPF formatado e válido: {cpf}")
      break
    else:
      print("CPF inválido! Digite um CPF com 11 dígitos numéricos.")
  
  while True:
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    if Pessoa.validar_data(data_nascimento):
      data_nascimento =  datetime.strptime(data_nascimento, "%d/%m/%Y").strftime("%Y-%m-%d")
      break
    else:
      print("Data inválida! Use o formato dd/mm/aa.")

  ano_atual = datetime.now().year
  matricula = f"SI{ano_atual}{Aluno.total_alunos:05d}"

  novo_aluno = Aluno(
    nome=nome,
    cpf=cpf,
    data_nascimento=data_nascimento,
    matricula=matricula,
    notas=[],
    disciplinas=[]
  )
  novo_aluno.disciplinas_nomes = [d.nome for d in novo_aluno.disciplinas]  
  lista_alunos.append(novo_aluno)
  salvar_alunos(lista_alunos, caminho_arquivo_alunos)
  print(f"Aluno {nome} cadastrado com sucesso.")

def cadastrar_professor(lista_professores):
  print("\nCadastro de Professor")
  nome = input("Nome: ").title()
  # Validar CPF
  while True:
    cpf = input("CPF (somente números ou com pontuação): ")
    if Pessoa.validar_cpf(cpf):
      cpf = Pessoa.formatar_cpf(cpf)
      print(f"CPF formatado e válido: {cpf}")
      break
    else:
      print("CPF inválido! Digite um CPF com 11 dígitos numéricos.")
  
  while True:
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    if Pessoa.validar_data(data_nascimento):
      data_nascimento =  datetime.strptime(data_nascimento, "%d/%m/%Y").strftime("%Y-%m-%d")
      break
    else:
      print("Data inválida! Use o formato dd/mm/aa.")

  siape = gerar_siape()

  novo_professor = Professor(
  nome=nome,
  cpf=cpf,
  data_nascimento=data_nascimento,
  siape=siape,
  disciplinas=[]
  )
  novo_professor.disciplinas_nomes = [d.nome for d in novo_professor.disciplinas]
  lista_professores.append(novo_professor)
  salvar_professores(lista_professores, caminho_arquivo_professores)
  print(f"Professor {nome} cadastrado com sucesso.")

def cadastrar_disciplina(lista_disciplinas, codigo, nome):
    nova_disciplina = Disciplina(
        codigo=codigo,
        nome=nome,
        professor_responsavel=None,
        alunos_matriculados=[]
    )
    lista_disciplinas.append(nova_disciplina)
    salvar_disciplinas(lista_disciplinas, caminho_arquivo_disciplinas)
    print(f"Disciplina {nome} cadastrada com sucesso.")

def gerar_siape():
  base = 9870000
  return str(base + Professor.total_professores + 1)