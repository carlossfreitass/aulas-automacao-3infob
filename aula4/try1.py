while True:
  try:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print(f'O resultado da divisão é: {n1 / n2}')
    break
  except ValueError:
    print('O valor digitado é inválido')
  except ZeroDivisionError:
    print('Você não pode dividir por 0')
  except Exception as e:
    print(f'Ocorreu um erro: {e}')