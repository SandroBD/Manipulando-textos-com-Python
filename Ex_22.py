nome = str(input('Informe seu nome? ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
div = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(div[0], len(div[0])))








