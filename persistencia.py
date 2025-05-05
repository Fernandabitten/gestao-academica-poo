from aluno import Aluno
from professor import Professor
from disciplina import Disciplina
import os

def definir_caminho(diretorio, nome_arquivo):
    return os.path.join(os.path.dirname(__file__), diretorio, nome_arquivo) 

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
        return linhas 
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler {nome_arquivo}: {e}")
        return []

def carregar_professores(arquivo):
    professores = []
    linhas = ler_arquivo(arquivo)
    for linha in linhas:
        try:
            dados = linha.strip().split('|')
            siape = dados[0]
            nome = dados[1]
            cpf = dados[2]
            data_nasc = dados[3]
            disciplinas_nomes = dados[4].split(',') if len(dados) > 4 else []
            prof = Professor(nome, cpf, data_nasc, siape, disciplinas=[])
            prof.disciplinas_nomes = disciplinas_nomes  # Temporário
            professores.append(prof)            
        except IndexError:
            print(f"Erro ao processar linha: {linha}")
        except ValueError:
            print(f"Erro ao processar disciplina: {linha}")
    return professores

def carregar_alunos(arquivo):
    alunos = []
    linhas = ler_arquivo(arquivo)
    for linha in linhas:
        try:
            dados = linha.strip().split('|')
            nome = dados[0]
            cpf = dados[1]
            data_nasc = dados[2]
            matricula = dados[3]
            notas = []
            disciplinas_nomes = []
            for entry in dados[4:]:
                partes = entry.split(',')
                disciplinas_nomes.append(partes[0])
                notas.extend(map(float, partes[1:]))
            aluno = Aluno(nome, cpf, data_nasc, matricula, notas, disciplinas=[])
            aluno.disciplinas_nomes = disciplinas_nomes  # Temporário
            alunos.append(aluno)
        except ValueError:
            print(f"Erro ao processar aluno: {linha}")
    return alunos

def carregar_disciplinas(arquivo, professores, alunos):
    disciplinas = []
    linhas = ler_arquivo(arquivo)
    try:
        for linha in linhas:
            dados = linha.strip().split('|')
            codigo = dados[0]
            nome = dados[1]
            prof_nome = dados[2]
            alunos_nomes = dados[3].split(',') if len(dados) > 3 else []
            # Resolver referências
            prof = next((p for p in professores if p.nome == prof_nome), None)
            alunos_objs = [a for a in alunos if a.nome in alunos_nomes]
            disc = Disciplina(codigo, nome, prof, alunos_objs)
            disciplinas.append(disc)
    except IndexError:
        print(f"Erro ao processar linha: {linha}")
    except ValueError:
        print(f"Erro ao processar disciplina: {linha}")
    return disciplinas

def vincular_disciplinas(professores, alunos, disciplinas):
    nome_para_disc = {d.nome: d for d in disciplinas}
    # Atualizar professores
    for prof in professores:
        prof.disciplinas = [nome_para_disc[nome] for nome in prof.disciplinas_nomes if nome in nome_para_disc]
        delattr(prof, 'disciplinas_nomes')
    # Atualizar alunos
    for aluno in alunos:
        aluno.disciplinas = [nome_para_disc[nome] for nome in aluno.disciplinas_nomes if nome in nome_para_disc]
        delattr(aluno, 'disciplinas_nomes')
