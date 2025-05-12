from aluno import Aluno
from professor import Professor
from disciplina import Disciplina

def alunos_aprovados(lista_alunos):
    print("1. Alunos aprovados\n")
    for aluno in lista_alunos:
      medias = aluno.calcular_media_por_disciplina()
      for disciplina_nome, media in medias.items():
        if media >= 7.0:
          print(f"Aluno: {aluno.nome} | Disciplina: {disciplina_nome} | Média: {media:.2f}")

def alunos_reprovados(lista_alunos):
  print("2. Alunos reprovados\n")
  for aluno in lista_alunos:
    medias = aluno.calcular_media_por_disciplina()
    reprovado_em_alguma = False

    for disciplina, media in medias.items():
      if media < 7.0:
        if not reprovado_em_alguma:
          print(f"Aluno: {aluno.nome} (Matrícula: {aluno.matricula})")
          reprovado_em_alguma = True
        print(f"  Disciplina: {disciplina} | Média: {media:.2f}")

    if reprovado_em_alguma:
      print("-" * 40)

def professores_com_muitos_alunos(lista_professores, minimo_alunos):
    print()
    print(f"Professores com mais de {minimo_alunos} alunos nas disciplinas que ministram:")
    print()

    for professor in lista_professores:
      total_alunos = 0
      for disciplina in professor.disciplinas:
        if hasattr(disciplina, 'alunos_matriculados'):
          total_alunos += len(disciplina.alunos_matriculados)

      if total_alunos > minimo_alunos:
        print(f"Professor: {professor.nome}")
        print(f"Total de alunos: {total_alunos}")
        print("-" * 40)

def estatisticas_gerais(lista_alunos, lista_professores, lista_disciplinas):
  # Total de alunos, professores e disciplinas
  total_alunos = Aluno.exibir_total_cadastrados()  # A classe já tem esse atributo de classe
  total_professores = Professor.exibir_total_cadastrados()  # A classe já tem esse atributo de classe
  total_disciplinas = Disciplina.exibir_total_cadastrados()  # A classe já tem esse atributo de classe
  
  # Para acumular todas as médias e notas por disciplina
  medias_por_disciplina = {}

  for aluno in lista_alunos:
    for i, disciplina in enumerate(aluno.disciplinas):
      nome_disciplina = disciplina.nome
      notas = aluno.notas[i*3:(i+1)*3]  # Pega 3 notas da disciplina atual

      if nome_disciplina not in medias_por_disciplina:
        medias_por_disciplina[nome_disciplina] = []

      # Média do aluno na disciplina
      media = sum(notas) / len(notas) if notas else 0.0
      medias_por_disciplina[nome_disciplina].append(media)

  # Média das médias dos alunos por disciplina
  media_dos_alunos_por_disciplina = {
    nome: sum(medias) / len(medias) if medias else 0.0
    for nome, medias in medias_por_disciplina.items()
  }

  return {
    'total_alunos': total_alunos,
    'total_professores': total_professores,
    'total_disciplinas': total_disciplinas,
    'media_dos_alunos_por_disciplina': media_dos_alunos_por_disciplina,
  }