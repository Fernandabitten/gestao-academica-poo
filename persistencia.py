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

def salvar_professores(professores, arquivo):
	with open(arquivo, 'w', encoding='utf-8') as f:
		for professor in professores:
			linha = '|'.join([
				professor._Professor__siape,
				professor.nome,
				professor._Pessoa__cpf,
				professor.data_nascimento,
				','.join([d if isinstance(d, str) else d.nome for d in professor.disciplinas])
			])
			f.write(linha + '\n')

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

def salvar_alunos(alunos, arquivo):
	with open(arquivo, 'w', encoding='utf-8') as f:
		for aluno in alunos:
			partes = [aluno.nome, aluno._Pessoa__cpf, aluno.data_nascimento, aluno._Aluno__matricula]
			for i, disciplina in enumerate(aluno.disciplinas):
				notas = aluno._Aluno__notas[i*3 : (i+1)*3]
				partes.append(f"{disciplina.nome},{','.join(map(str, notas))}")
			f.write('|'.join(partes) + '\n')

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

def salvar_disciplinas(lista_disciplinas, arquivo):
	with open(arquivo, 'w', encoding='utf-8') as f:
		for disciplina in lista_disciplinas:
			nome_prof = disciplina.professor_responsavel.nome if disciplina.professor_responsavel else "N/A"
			nomes_alunos = [aluno.nome for aluno in disciplina.alunos_matriculados]
			linha = f"{disciplina.codigo}|{disciplina.nome}|{nome_prof}|{','.join(nomes_alunos)}\n"
			f.write(linha)

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

def buscar_disciplina_por_codigo(lista_disciplinas, codigo_busca):
	for disciplina in lista_disciplinas:
		if disciplina.codigo == codigo_busca:
			return disciplina
	return None

# Definindo os caminhos dos arquivos de dados
caminho_arquivo_professores = definir_caminho('bd', 'professores.txt')
caminho_arquivo_alunos = definir_caminho('bd', 'alunos.txt')
caminho_arquivo_disciplinas = definir_caminho('bd', 'disciplinas.txt')

# Carrega professores e alunos (referências a disciplinas são resolvidas depois)
professores = carregar_professores(caminho_arquivo_professores)
alunos = carregar_alunos(caminho_arquivo_alunos)

# Carrega disciplinas
disciplinas = carregar_disciplinas(caminho_arquivo_disciplinas, professores, alunos)

# Vincula as disciplinas aos professores e alunos
vincular_disciplinas(professores, alunos, disciplinas)
