nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6:
  print('APROVADO!')
else:
  exame = float(input('Digite sua nota do Exame Final: '))
  media = (media + exame) / 2
  if media > 6:
    print('APROVADO!')
  else:
    print('REPROVADO!')