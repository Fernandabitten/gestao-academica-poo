from relatorios import *
from cadastro import *
# from persistencia import salvar_alunos

def menu_alunos(lista_alunos, lista_disciplinas):
  while True:
    print("\nMenu de Alunos:")
    print("1. Cadastrar novo aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno por matrícula")
    print("4. Matricular aluno em disciplina")
    print("5. Adicionar nota")
    print("6. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print()
      print("1. Cadastrar novo aluno")
      print()      
      nome = input("Nome: ")
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
          print(aluno.exibir_dados())
          break
        else:
          print("Aluno não encontrado.")
    elif opcao == "4":
      print()
      print("4. Matricular aluno em disciplina")
      print()
      matricula = input("Informe a matrícula do aluno: ")
      aluno_encontrado = None
      for aluno in lista_alunos:
        if aluno.matricula == matricula:
          aluno_encontrado = aluno
          break
      if aluno_encontrado:
        codigo = input("Código da disciplina: ")
        for disc in lista_disciplinas:
          if disc.codigo == codigo:
            aluno_encontrado.matricular_em_disciplina(disc)
            disc.adicionar_aluno(aluno_encontrado)
            print("Aluno matriculado com sucesso.")
            break
          else:
            print("Disciplina não encontrada.")
      else:
          print("Aluno não encontrado.")
    elif opcao == "5":
      print()
      print("5. Adicionar nota")
      print()      
      matricula = input("Informe a matrícula do aluno: ")
      aluno_encontrado = None
      for aluno in lista_alunos:
        if aluno.matricula == matricula:
            aluno_encontrado = aluno
            break
      if aluno_encontrado:
        codigo = input("Código da disciplina: ")
        for disc in aluno_encontrado.disciplinas:
          if disc.codigo == codigo:
            try:
              nota = float(input("Nota: "))
              aluno_encontrado.adicionar_nota(disc, nota)
              print("Nota adicionada com sucesso.")
            except ValueError:
              print("Nota inválida.")
            break
          else:
            print("Aluno não está matriculado nessa disciplina.")
      else:
        print("Aluno não encontrado.")
    elif opcao == "6":
      print("Voltando ao menu principal...")
      break
    else:
      print("Opção inválida.")

def menu_professores(lista_professores):
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
      nome = input("Nome: ")
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
      for prof in lista_professores:
        if prof.siape == siape:
          codigo = input("Código da disciplina a adicionar: ")
          nome = input("Nome da disciplina: ")
          from disciplina import Disciplina
          nova_disc = Disciplina(codigo, nome)
          prof.adicionar_disciplina(nova_disc)
          print("Disciplina adicionada ao professor.")
          break
      else:
        print("Professor não encontrado.")
    elif opcao == "5":
      print()
      print("5. Remover disciplina do professor")
      print()
      siape = input("SIAPE do professor: ")
      for prof in lista_professores:
        if prof.siape == siape:
          codigo = input("Código da disciplina a remover: ")
          prof.remover_disciplina(codigo)
          print("Disciplina removida.")
          break
      else:
        print("Professor não encontrado.")
    elif opcao == "6":
      print("Voltando ao menu principal...")
      break
    else:
      print("Opção inválida.")

def menu_disciplinas(lista_disciplinas):
  while True:
    print("\nMenu de Disciplinas:")
    print("1. Cadastrar nova disciplina")
    print("2. Listar disciplinas")
    print("3. Buscar disciplina por código")
    print("4. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print()
      print("1. Cadastrar nova disciplina")
      print()
      codigo = input("Código: ")
      nome = input("Nome: ")
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
      codigo = input("Informe o código da disciplina: ")
      for disc in lista_disciplinas:
        if disc.codigo == codigo:
          print('========================')
          disc.exibir_dados()
          print()
          break
      else:
        print("Disciplina não encontrada.")
    elif opcao == "4":
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
      menu_professores(lista_professores)
    elif opcao == "3":
      menu_disciplinas(lista_disciplinas)
    elif opcao == "4":
      menu_relatorios(lista_alunos, lista_professores, lista_disciplinas)
    elif opcao == "5":
      print("Salvando dados e saindo...")
      # salvar_alunos("alunos.dat", lista_alunos)
      # salvar_alunos("professores.dat", lista_professores)
      # salvar_alunos("disciplinas.dat", lista_disciplinas)
      break
    else:
      print("Opção inválida.")


