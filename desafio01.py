alunos = []

print('******** PYTHON **********')


def montaOpcoes():
    print('1) Acrescentar nome')
    print('2) Listar nomes')
    print('3) Sair')
    return int(input())

def adicionaAluno():
    nome = str(input('Digite o nome: '))
    alunos.append(nome)
    
    print('Deseja adicionar outro nome? ')
    print('Escolha 1 para continuar e 0 para cancelar')
    return int(input())

# --------------------------------------
i = 0
while(i == 0):    
    op = montaOpcoes()
    if op == 1:
        op2 = adicionaAluno()
        while(op2 == 1):
           op2 = adicionaAluno()
    
    if op == 2:
        if len(alunos) < 1:
            print('************************')
            print('Não existe alunos')
            print('************************')
        else:
            print('******** NOMES ************')
            for i in range(len(alunos)):
                print('[{}]: Aluno = {}'.format(i, alunos[i]))
            print('************************')
            montaOpcoes()   
             
    if op == 3:
        print('Obrigado por usar o sistema!')
        i = 1
    
    if(op > 3):
        print('Opção invalida!')
        i = 1

