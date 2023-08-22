# Exercício - sistema de perguntas e respostas

import os

os.system('clear')

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


num = len(perguntas)
qtd = 0
for p in perguntas:
    print("------------------------------------------")
    pergunta = p["Pergunta"]
    opcoes = p["Opções"]
    resp = p["Resposta"]
    print(f"{pergunta}")
    print()
    print("Opções: ")

    for ind, op in enumerate(opcoes):
        print(f"{ind}) {op}")

    escolha = input("Escolha uma opção: ")

    if opcoes[int(escolha)] == resp:
  #
        qtd += 1
        print("Acertou 👍")
    else:
        print("Resposta incorreta 👎 ")


print(f"Voce acertou {qtd}/{len(perguntas)}")
