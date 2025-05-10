# Sistema de Gestão Acadêmica

O Sistema de Gestão Acadêmica é um projeto desenvolvido para a disciplina de Programação Orientada a Objetos do curso Técnico Subsequente em Informática para Internet do IFCE. O objetivo é criar uma aplicação modular para gerenciar alunos, professores e disciplinas, utilizando conceitos avançados de POO, persistência em arquivos e interface textual via menus interativos.

O sistema permite cadastrar, listar, buscar e gerenciar alunos, professores e disciplinas, além de gerar relatórios acadêmicos e estatísticas relevantes. Os dados são persistidos em arquivos .txt fornecidos como ponto de partida.

## Funcionalidades

- Cadastro, listagem e busca de alunos, professores e disciplinas

- Matrícula e desmatrícula de alunos em disciplinas

- Lançamento e cálculo de notas por disciplina

- Atribuição e remoção de disciplinas para professores

- Persistência automática dos dados em arquivos .txt

- Relatórios de:
  - Alunos aprovados e reprovados
  - Professores com mais alunos
  - Estatísticas gerais (totais e médias)
- Menus interativos para navegação e operações

## Estrutura do projeto

```

  ├── main.py                  # Ponto de entrada do sistema
  ├── cadastro.py              # Funções para cadastro de   entidades
  ├── menus.py                 # Menus interativos do sistema
  ├── relatorios.py            # Geração de relatórios acadêmicos
  ├── persistencia.py          # Leitura e gravação de dados
  ├── pessoa.py                # Classe Pessoa
  ├── aluno.py                 # Classe Aluno
  ├── professor.py             # Classe Professor
  ├── disciplina.py            # Classe Disciplina
  ├── disciplina.txt           # Dados persistidos de alunos
  ├── professores.txt          # Dados persistidos de professores
  ├── disciplinas.txt          # Dados persistidos de disciplinas

```

## Como executar

1. Pré-requisitos:

- Certifique-se de ter o Python 3 instalado.

2. Clone ou baixe o repositório.

```
git clone https://github.com/Fernandabitten/gestao-academica-poo.git
cd gestao-academica
```

3. No terminal, execute o comando:
   `python main.py`

## Como utilizar

Ao rodar o sistema, utilize o menu principal para navegar entre as opções:

- Menu Principal
  - Menu de Alunos
  - Menu de Professores
  - Menu de Disciplinas
  - Menu de Relatórios
  - Sair

Cada submenu permite cadastrar, listar, buscar, matricular/desmatricular, lançar notas e gerar relatórios.
Os dados são salvos automaticamente nos arquivos .txt após cada operação.

# Equipe

Projeto desenvolvido por:

[Fernanda Bittencourt](https://github.com/Fernandabitten)
[Grazielle Carvalho](https://github.com/grazyac)
[Maria Oliveira](https://github.com/Maria0oliveira)

## Licença

Este projeto é acadêmico e sem fins lucrativos.

> **Observações:**
>
> - Os arquivos de dados fornecidos (alunos.txt, professores.txt, disciplinas.txt) devem ser mantidos no formato original para correto funcionamento.
> - Em caso de dúvidas ou erros, consulte a documentação interna do código e os comentários explicativos.
