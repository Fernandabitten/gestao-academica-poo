from relatorios import *
from cadastro import *
from persistencia import *

def menu_alunos(lista_alunos, lista_disciplinas):
  while True:
    print("\nMenu de Alunos:")
    print("1. Cadastrar novo aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno por matrícula")
    print("4. Matricular aluno em disciplina")
    print("5. Desmatricular aluno de uma disciplina")
    print("6. Adicionar nota")
    print("7. Calcular média por disciplina")
    print("8. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print()
      print("1. Cadastrar novo aluno")
      print()      
      nome = input("Nome: ").title()
      cpf = input("CPF: ")
      data = input("Data de nascimento (dd/mm/aaaa): ")
      matricula = input("Matrícula: ")
      cadastrar_aluno(lista_alunos, nome, cpf, data, matricula)
    elif opcao == "2":
      print()
      print("===2. Listar Alunos ===")
      print()
      for aluno in lista_alunos:
        print('========================')
        aluno.exibir_dados()
        print()
    elif opcao == "3":
      print()
      print("3. Buscar aluno por matrícula")
      print() 
      mat = input("Informe a matrícula: ")
      for aluno in lista_alunos:
        if aluno.matricula == mat:
          print('========================')
          aluno.exibir_dados()
          print()
          break
      else:
        print("Aluno não encontrado.")
    elif opcao == "4":
      print()
      print("4. Matricular aluno em disciplina")
      print()
      matricula = input("Informe a matrícula do aluno: ")
      codigo_disciplina = input("Código da disciplina: ").upper()
      if matricular_aluno_em_disciplina(lista_alunos, lista_disciplinas, matricula, codigo_disciplina):
        salvar_alunos(lista_alunos, caminho_arquivo_alunos)
        salvar_disciplinas(lista_disciplinas, caminho_arquivo_disciplinas)
        print("Aluno matriculado com sucesso.")
      else:
        print("Erro ao matricular.")
    elif opcao == "5":
      print()
      print("5. Desmatricular aluno de uma disciplina")
      print()
      matricula = input("Informe a matrícula do aluno: ")
      codigo_disciplina = input("Código da disciplina: ").upper()
      if desmatricular_aluno_de_disciplina(lista_alunos, lista_disciplinas, matricula, codigo_disciplina):
        salvar_alunos(lista_alunos, caminho_arquivo_alunos)
        salvar_disciplinas(lista_disciplinas, caminho_arquivo_disciplinas)
        print("Aluno desmatriculado com sucesso.")
      else:
        print("Erro ao desmatricular.")
    elif opcao == "6":
      print()
      print("6. Adicionar nota")
      print() 
      matricula = input("Informe a matrícula do aluno: ")     
      codigo_disciplina = input("Código da disciplina: ").upper()
      indice = int(input("Qual nota deseja alterar (1, 2 ou 3)? ")) - 1
      nota = float(input("Digite a nova nota: ").replace(',', '.'))

      if adicionar_nota_para_aluno(lista_alunos, lista_disciplinas, matricula, codigo_disciplina, indice, nota):
        salvar_alunos(lista_alunos, caminho_arquivo_alunos)
        print("Nota adicionada com sucesso.")
      else:
        print("Não foi possível adicionar a nota.")
    elif opcao == "7":
      print()
      print("7. Calcular média por disciplina")
      print()
      matricula = input("Informe a matrícula do aluno: ")
      aluno = next((a for a in lista_alunos if a.matricula == matricula), None)

      if aluno:
          medias = aluno.calcular_media_por_disciplina()
          print()
          print(f"\nMédias do aluno {aluno.nome}:")
          print('================================')
          for nome_disciplina, media in medias.items():
            print(f"{nome_disciplina}: {media:.2f}")
            print('---------------------------------')
      else:
        print("Aluno não encontrado.")
    elif opcao == "8":
      print("Voltando ao menu principal...")
      break
def menu_professores(lista_professores, lista_disciplinas):
  while True:
    print("\nMenu de Professores:")
    print("1. Cadastrar novo professor")
    print("2. Listar professores")
    print("3. Buscar professor por SIAPE")
    print("4. Adicionar disciplina ao professor")
    print("5. Remover disciplina do professor")
    print("6. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print()
      print("1. Cadastrar novo professor")
      print()
      nome = input("Nome: ").title()
      cpf = input("CPF: ")
      data = input("Data de nascimento (dd/mm/aaaa): ")
      siape = input("SIAPE: ")
      cadastrar_professor(lista_professores, nome, cpf, data, siape)
    elif opcao == "2":
      print()
      print("2. Listar professores")
      print()
      for prof in lista_professores:
        print('========================')
        prof.exibir_dados()
        print()
    elif opcao == "3":
      print()
      print("3. Buscar professor por SIAPE")
      print()
      siape = input("Informe o SIAPE: ")
      for prof in lista_professores:
        if prof.siape == siape:
          print('========================')
          prof.exibir_dados()
          print()
          break
      else:
        print("Professor não encontrado.")
    elif opcao == "4":
      print()
      print("4. Adicionar disciplina ao professor")
      print()
      siape = input("Informe o SIAPE do professor: ")
      professor_encontrado = next((p for p in lista_professores if p.siape == siape), None)
      if professor_encontrado:
        codigo_disciplina = input("Código da disciplina: ").upper()
        disciplina_encontrada = next((d for d in lista_disciplinas if d.codigo.upper() == codigo_disciplina), None)
        if disciplina_encontrada:
          # Usa o método da disciplina, que garante consistência e desvincula professor anterior
          disciplina_encontrada.adicionar_professor(professor_encontrado)
          salvar_professores(lista_professores, caminho_arquivo_professores) 
          salvar_disciplinas(lista_disciplinas, caminho_arquivo_disciplinas) 
        else:
          print("Disciplina não encontrada.")
      else:
        print("Professor não encontrado.")
    elif opcao == "5":
      print()
      print("5. Remover disciplina do professor")
      print()
      siape = input("Informe o SIAPE do professor: ")
      professor_encontrado = next((p for p in lista_professores if p.siape == siape), None)
      if professor_encontrado:
        codigo_disciplina = input("Código da disciplina: ").upper()
        disciplina_encontrada = next((d for d in lista_disciplinas if d.codigo.upper() == codigo_disciplina), None)
        if disciplina_encontrada:
          # Verifica se o professor realmente é o responsável pela disciplina
          if disciplina_encontrada.professor_responsavel == professor_encontrado:
            disciplina_encontrada.remover_professor()
            salvar_professores(lista_professores, caminho_arquivo_professores)
            salvar_disciplinas(lista_disciplinas, caminho_arquivo_disciplinas)  
          else:
            print(f"O professor {professor_encontrado.nome} não é responsável pela disciplina {disciplina_encontrada.nome}.")         
        else:
          print("Disciplina não encontrada.")
      else:
        print("Professor não encontrado.")
    elif opcao == "6":
      print("Voltando ao menu principal...")
      break
    else:
      print("Opção inválida.")

def menu_disciplinas(lista_disciplinas, lista_professores):
  while True:
    print("\nMenu de Disciplinas:")
    print("1. Cadastrar nova disciplina")
    print("2. Listar disciplinas")
    print("3. Buscar disciplina por código")
    print("4. Atribuir professor a uma disciplina")
    print("5. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print()
      print("1. Cadastrar nova disciplina")
      print()
      codigo = input("Código: ").upper()
      nome = input("Nome: ").title().replace(" ", "_")
      cadastrar_disciplina(lista_disciplinas, codigo, nome)
    elif opcao == "2":
      print()
      print("2. Listar disciplinas")
      print()
      for disc in lista_disciplinas:
        print('========================')
        disc.exibir_dados()
        print()
    elif opcao == "3":
      print()
      print("3. Buscar disciplina por código")
      print()
      codigo = input("Informe o código da disciplina: ").upper()
      for disc in lista_disciplinas:
        if disc.codigo.upper() == codigo:
          print('========================')
          disc.exibir_dados()
          print()
          break
      else:
        print("Disciplina não encontrada.")
    elif opcao == "4":
      print()
      print("5. Atribuir professor a uma disciplina")
      print()
      codigo_disciplina = input("Informe o código da disciplina: ").upper()
      disciplina_encontrada = next((d for d in lista_disciplinas if d.codigo.upper() == codigo_disciplina), None)      
      if disciplina_encontrada:
        siape = input("Informe o SIAPE do professor: ")
        professor_encontrado = next((p for p in lista_professores if p.siape == siape), None)        
        if professor_encontrado:
          disciplina_encontrada.adicionar_professor(professor_encontrado)
          salvar_professores(lista_professores, caminho_arquivo_professores)
          salvar_disciplinas(lista_disciplinas, caminho_arquivo_disciplinas) 
        else:
          print("Professor não encontrado.")
      else:
        print("Disciplina não encontrada.")
    elif opcao == "5":
      print("Voltando ao menu principal...")
      break
    else:
      print("Opção inválida.")

def menu_relatorios(lista_alunos, lista_professores, lista_disciplinas):
  while True:
    print("\nMenu de Relatórios:")
    print("1. Alunos aprovados")
    print("2. Alunos reprovados")
    print("3. Professores com muitos alunos")
    print("4. Estatísticas gerais")
    print("5. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print()
      print("1. Alunos aprovados")
      print()
      for nome, disciplina, media in alunos_aprovados(lista_alunos):
        print(f"{nome} - {disciplina} - Média: {media:.2f}")
    elif opcao == "2":
      print()
      print("2. Alunos reprovados")
      print()
      for nome, disciplina, media in alunos_reprovados(lista_alunos):
        print(f"{nome} - {disciplina} - Média: {media:.2f}")
    elif opcao == "3":
      print()
      print("3. Professores com muitos alunos")
      print()
      for nome, total in professores_com_muitos_alunos(lista_professores):
        print(f"{nome} - Total de alunos: {total}")
    elif opcao == "4":
      print()
      print("4. Estatísticas gerais")
      print()
      estat = estatisticas_gerais(lista_alunos, lista_professores, lista_disciplinas)
      print(f"Total de alunos: {estat['total_alunos']}")
      print(f"Total de professores: {estat['total_professores']}")
      print(f"Total de disciplinas: {estat['total_disciplinas']}")
      print("Médias por disciplina:")
      for disc, media in estat['medias_por_disciplina'].items():
        print(f"- {disc}: {media:.2f}")
    elif opcao == "5":
      print("Voltando ao menu principal...")
      break
    else:
      print("Opção inválida.")

def menu_principal(lista_alunos, lista_professores, lista_disciplinas):
  while True:
    print("\nMenu Principal:")
    print("1. Menu de Alunos")
    print("2. Menu de Professores")
    print("3. Menu de Disciplinas")
    print("4. Menu de Relatórios")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      menu_alunos(lista_alunos, lista_disciplinas)
    elif opcao == "2":
      menu_professores(lista_professores, lista_disciplinas)
    elif opcao == "3":
      menu_disciplinas(lista_disciplinas, lista_professores)
    elif opcao == "4":
      menu_relatorios(lista_alunos, lista_professores, lista_disciplinas)
    elif opcao == "5":
      print("Salvando dados e saindo...")
      salvar_alunos(lista_alunos, caminho_arquivo_alunos)
      salvar_professores(lista_professores, caminho_arquivo_professores)
      salvar_disciplinas(lista_disciplinas, caminho_arquivo_disciplinas)
      print("Dados salvos com sucesso. Até logo!")
      break
    else:
      print("Opção inválida.")


