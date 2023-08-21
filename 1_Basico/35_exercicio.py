"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
#nova_string += '*L*u*i*z* *O*t*á*v*i*o'

cont = 0
while cont < tamanho_nome:
    nova_string += "*" + nome[cont]
    cont +=1

print(nome)
print(nova_string)
