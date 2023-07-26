opcao = int(input("Informe uma opção: \n [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo extrato")

else:
    sys.exit("Opção inválida")


saldo = 2000
saque = float(input("Informe o valor do saque: "))


if saldo >= saque:
    print("Realizando saque!")

# if saldo < saque:
#     print("Saldo insuficiente")

else:
    print("Saldo insuficiente")