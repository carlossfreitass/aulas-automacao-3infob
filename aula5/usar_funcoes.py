import aula4.funcao as funcao

funcao.imprimir('Digite o primeiro número: ')
n1 = funcao.ler()

funcao.imprimir('Digite o segundo número: ')
n2 = funcao.ler()

resposta = funcao.somar(n1, n2)
funcao.imprimir(f'O resultado é {resposta}')