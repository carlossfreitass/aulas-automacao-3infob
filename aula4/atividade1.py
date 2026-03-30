verificador = True

while verificador:
  usuario = input('Digite o nome de usuário: ')
  senha = input('Digite a senha: ')

  if (usuario == 'admin' and senha == 'admin123'):
    print('Bem Vindo')
    verificador = False