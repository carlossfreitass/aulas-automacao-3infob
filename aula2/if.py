# Condição IF

def maior():
  idade = int(input('Digite sua idade: '))

  if (idade < 18):
    print('Menor de idade')
    return
  
  print('Maior de idade')

maior()