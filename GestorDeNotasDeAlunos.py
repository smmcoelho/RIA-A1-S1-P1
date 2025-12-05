
# Adicionar um novo aluno e nota.
def adicionarNovoAluno(d : dict, nome: str, nota: int) -> None:
    #TODO

# Atualizar a nota de um aluno existente.
def atualizarNota(d: dict, nome: str, nota: int) -> None:
    #TODO

# Exibir todos os alunos e notas (por ordem alfabética ou nota decrescente)
def exibirAlunos(d: dict) -> None:
    #TODO

def exibirAlunosRevertido(d: dict) -> None:
    #TODO

# Mostrar o aluno com a maior nota.
def exibirMelhor(d: dict) -> None:
    #TODO

# Mostrar aluno com menor nota
def exibirPior(d: dict) -> None:
    #TODO

def menu() -> int:
    print("1 - Adicionar um novo aluno e nota.")
    print("2 - Atualizar a nota de um aluno existente.")
    print("3 - Exibir todos os alunos e notas")
    print("4 - Mostrar o aluno com a maior nota.")
    print("5 - Mostrar aluno com menor nota")
    print("6 - Sair do programa.")
    i = int(input('Introduza uma opcao: '))
    return i

def menuAdicionarAluno():
    nome = input('Insira o nome: ')
    nota = int(input('Insira a nota: '))
    return nome, nota

if __name__ == '__main__':
    d = dict()
    while True:
        opcao = menu()
        match opcao :
            case 1:
                nome, nota = menuAdicionarAluno()
                adicionarNovoAluno(d, nome, nota)
            case 2:
                nome, nota = menuAdicionarAluno()
                atualizarNota(d, nome, nota)
            case 3:
                exibirAlunos(d)
                # exibirAlunosRevertido(d)
            case 4:
                exibirMelhor(d)
            case 5:
                exibirPior(d)
            case 6:
                print('\t Sair do programa')
                break
