print('-'*8, '\nCadastro\n' + '-'*8)

#Repete a inserção do email até que seja válido
valido_email = False
while valido_email == False:
    email = str(input('Informe o seu e-mail: '))
    if '@' in email:
        print('E-mail cadastrado com sucesso!')
        valido_email = True
    else:
        print('O e-mail informado não é válido, tente novamente')

#Repete a inserção da senha até que seja válida
valido_senha = False
while valido_senha == False:
    senha1 = str(input('Informe a senha desejada: '))
    senha2 = str(input('Repita a senha informada: '))
    if senha1 == senha2:
        print('Senha cadastrada com sucesso')
        valido_senha = True
    else:
        print('A senha informada não é válida, tente novamente')

#Cadastra o nome do usuario e finaliza o programa com uma mensagem de boas vindas
usuario = str(input('Informe o seu nome de usuário: '))

print(f'Bem vindo, {usuario}! Você se cadastrou com sucesso!')
