'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
temp = []
alunos = []
print('-=' * 5, 'ANÁLISE ESCOLA FELT DEV', '=-' * 5)
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota da av 1: ')))
    temp.append(float(input('Nota da av 2: ')))
    opção = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    alunos.append(temp[:])
    temp.clear()
    print('--' * 20)
    if 'N' in opção:
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for pos, l in enumerate(alunos):
    média = (l[1] + l[2]) / 2
    print(f'{pos:<4}{l[0]:<10} {média:>8.1f}')
print('--' * 20)
while True:
    num = int(input('Algum aluno(a) que você deseje verificar a nota?\n'
                      'Digite o número do(a) aluno(a) ou [999] para encerrar: '))
    if num >= 999:
        break
    if num <= len(alunos) - 1: # essa condição só vai imprimir o resultado se estiver dentro do range.
        # eu não adicionei essa condição e meu programa dava erro.
        # agora ele não tenta imprimir fora do range, ele imprime apenas se o numero for compativel com os alunos cadastrados.
        print('--' * 20)
        print(f'Aluno {num}: {alunos[num][0]} tirou {alunos[num][1]} e {alunos[num][2]}.')
    print('--' * 20)
print('-=' * 30)
print('-=' * 5, 'PROGRAMA ENCERRADO', '=-' * 5)