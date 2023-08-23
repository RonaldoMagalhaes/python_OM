import os

os.system('clear')

palavra_secreta = set("nir")
#print(palavra_secreta)
#tamanho = len(palavra_secreta)

letras_acertadas = set()

while True:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Digite apenas uma unica letra: ")



    if letra in palavra_secreta:
        letras_acertadas.add(letra)

    print(letras_acertadas)

    if letras_acertadas == palavra_secreta:
        print("Parabéns, voce ganhou o jogo....")
        break
