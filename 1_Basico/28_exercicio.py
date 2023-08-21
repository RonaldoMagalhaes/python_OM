"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num_str = input("Digite um numero inteiro: ")

# try:
#     num_int = int(num_str)
#     if num_int % 2 == 0:
#         print("O numero eh par")
#     else:
#         print("O numero eh impar")
#     print()

# except:
#     print(f"{num_str} nao eh um numero inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora_str = input("Que horas sao: ")

# try:

#     hora = int(hora_str)
#     if hora<12:
#         print("Bom dia 0-11")
#     elif hora<18:
#             print("Boa tarde 12-18")
#     elif hora <=24:
#         print("Boa noite 18-24")
#     else:
#         print("Horario invalido")

# except:

#     print("Entrada invalida")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite seu nome: ")
len_nome = len(nome)

if len_nome <= 4:
    print("Seu nome é curto")
elif len_nome <=6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
