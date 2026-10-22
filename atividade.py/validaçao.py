senha_correta = 'luluket123'
while True:
    senha = input('Digite sua senha:')
    if senha == senha_correta:
        print('Acesso permitido!')
        break
    else:
        print('Senha incorreta. Tente novamente.')