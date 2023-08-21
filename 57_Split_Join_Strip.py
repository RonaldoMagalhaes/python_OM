"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""



frase = '   Olha só que   , coisa interessante          '

lista_palavras = frase.split()
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())


frases_unidas = "&".join("ABC")
print(frases_unidas)
