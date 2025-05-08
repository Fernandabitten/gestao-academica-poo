def carregar_alunos(arquivo):
    alunos = []
    with open(arquivo, 'r') as f:
        for linha in f:
            dados = linha.strip().split(',')
            nome = dados[0]
            n1 = float(dados[1])
            n2 = float(dados[2])
            media = float(dados[3])
            status = 'Aprovado' if media >= 7 else 'Reprovado'
            alunos.append({'nome': nome, 'n1': n1, 'n2': n2, 'media': media, 'status': status})
    return alunos

def carregar_professores(arquivo):
    professores = []
    with open(arquivo, 'r') as f:
        for linha in f:
            dados = linha.strip().split(',')
            nome = dados[0]
            disciplina = dados[1]
            qtd_alunos = int(dados[2])
            professores.append({'nome': nome, 'disciplina': disciplina, 'qtd_alunos': qtd_alunos})
    return professores

def relatorio_alunos_aprovados(alunos):
    aprovados = [a for a in alunos if a['status'] == 'Aprovado']
    print(f"Alunos aprovados ({len(aprovados)}):")
    for a in aprovados:
        print(f" - {a['nome']} (Média: {a['media']})")
    print()

def relatorio_alunos_reprovados(alunos):
    reprovados = [a for a in alunos if a['status'] == 'Reprovado']
    print(f"Alunos reprovados ({len(reprovados)}):")
    for a in reprovados:
        print(f" - {a['nome']} (Média: {a['media']})")
    print()

def professores_com_muitos_alunos(professores, limite):
    print(f"Professores com mais de {limite} alunos:")
    for p in professores:
        if p['qtd_alunos'] > limite:
            print(f" - {p['nome']} ({p['disciplina']}) - {p['qtd_alunos']} alunos")
    print()

def estatisticas_gerais(alunos, professores, disciplinas):
    total_alunos = len(alunos)
    total_professores = len(professores)
    total_disciplinas = len(set([p['disciplina'] for p in professores]))
    # Média geral por disciplina
    medias_por_disciplina = {}
    for disciplina in disciplinas:
        notas = [a['media'] for a in alunos if a.get('disciplina') == disciplina]
        if notas:
            medias_por_disciplina[disciplina] = sum(notas) / len(notas)
        else:
            medias_por_disciplina[disciplina] = 0
    print("Estatísticas Gerais:")
    print(f" - Número total de alunos: {total_alunos}")
    print(f" - Número total de professores: {total_professores}")
    print(f" - Número total de disciplinas: {total_disciplinas}")
    print("Média geral por disciplina:")
    for disciplina, media in medias_por_disciplina.items():
        print(f"  * {disciplina}: {media:.2f}")
    print()
