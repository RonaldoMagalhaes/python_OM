"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

index = 0

for _ in lista:
    print(f"{index} {lista[index]}")
    index += 1

print("*"*80)
for i,n in enumerate(lista):
    print(f"{i} {n}")