from persistencia import (
    carregar_professores, carregar_alunos, carregar_disciplinas, vincular_disciplinas, definir_caminho
)

# Definindo os caminhos dos arquivos de dados
caminho_arquivo_professores = definir_caminho('bd', 'professores.txt')
caminho_arquivo_alunos = definir_caminho('bd', 'alunos.txt')
caminho_arquivo_disciplinas = definir_caminho('bd', 'disciplinas.txt')

# Carrega professores e alunos (referências a disciplinas são resolvidas depois)
professores = carregar_professores(caminho_arquivo_professores)
alunos = carregar_alunos(caminho_arquivo_alunos)

# Carrega disciplinas, já vinculando professores e alunos por nome
disciplinas = carregar_disciplinas(caminho_arquivo_disciplinas, professores, alunos)

# Vincula as disciplinas aos professores e alunos
vincular_disciplinas(professores, alunos, disciplinas)

# Exibe todos os professores e suas disciplinas
print("=== Professores ===")
for prof in professores:
    prof.exibir_dados()
    print()

# Exibe todos os alunos e suas disciplinas/notas
print("=== Alunos ===")
for aluno in alunos:
    aluno.exibir_dados()
    print()

#  Exibe todas as disciplinas, professores e alunos matriculados
print("=== Disciplinas ===")
for disc in disciplinas:
    disc.exibir_dados()
    print()


