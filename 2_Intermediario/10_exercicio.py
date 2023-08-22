# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def calculo(op):
    def operacao(num):
        return f"{num} x {op} = {num * op}"

    return operacao


duplica = calculo(2)
print(duplica(4))

print()

triplica = calculo(3)
print(triplica(3))

print()

quadruplica = calculo(4)
print(quadruplica(4))
