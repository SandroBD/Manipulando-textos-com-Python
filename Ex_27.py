n = input('Informe seu nome: ').strip()
nome = n.split()
print(' {} \n Primeiro nome: {} \n Último nome: {}'.format(n, nome[0], nome[len(nome) - 1]))
