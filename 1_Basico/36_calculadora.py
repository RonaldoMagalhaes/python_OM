# calculadora com while

while True:
    sair = input("Quer sair? [S]/[N]: ").lower()
    if sair == 's':
        break
    else:
        try:
            n1_str = input("Entre com o N1: ")
            n1 = float(n1_str)
            n2_str = input("Entre com o N2: ")
            n2 = float(n2_str)
            op = input("Escolha a operacao: (+,-,/,*): ")
            resp = None
            operadores_permitidos = ["+","-","/","*"]
            if op not in operadores_permitidos:
                print("Operador inválido")
                continue

            elif op == "+":
                resp = n1+n2
            elif op == "-":
                resp = n1-n2
            elif op == "/":
                if n2 != 0:
                    resp = n1/n2
                else:
                    resp = "Erro, divisao por zero"
            elif op == "*":
                resp = n1*n2
            print(f"{n1} {op} {n2} = {resp}")
        except:
            print("Valor invalido")

