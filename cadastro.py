from aluno import Aluno
from professor import Professor
from disciplina import Disciplina
from persistencia import (salvar_alunos, salvar_professores, salvar_disciplinas, caminho_arquivo_alunos, caminho_arquivo_professores, caminho_arquivo_disciplinas)

def cadastrar_aluno(lista_alunos, nome, cpf, data_nascimento, matricula):
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

def cadastrar_professor(lista_professores, nome, cpf, data_nascimento, siape):
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