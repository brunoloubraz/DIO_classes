from datetime import date
import datetime

# Criar um sistema bancário que seja possívvel sacar, depositar e visualizar extrato
# 1 deposito: deve ser possível depositar valores POSITIVOS na conta
# 2 deposito: todos os depósitos devem ser armazenados em uma variável e exibidos na operacao extrato
# --
# 1 sacar: pode realizar 3 saques diários
# 2 saque pode ser no máximo de 500 reais
# 3 caso o usuario nao tenha saldo em conta, ele deve exibir uma mensagem informando o erro
# 4 todos os saques devem ser armazenados em uma variavel e exibidos na operacao de extrato
# --
# 1 extrato: deve mostrar todos os saques e depositos realizados  e deve vir no formato R$ 1500.45

options ="""
================ Bem vindo ao banco! ================
      
  Selecione uma das opções abaixo:

  [1] - Depósito
  [2] - Saque
  [3] - Extrato
  [4] - Sair
      
=====================================================
"""
enter_deposit_text = """
================ Você selecionou a aba de depósito! ================
"""
enter_saque_text = """
================ Você selecionou a aba de Saque! ================
"""
exit = """
================ Obrigado por utilizar os nossos serviços! ================
"""
saldo = 100.9002
alteracoes_conta = {}

max_saques = 3

def time():
  horas = datetime.datetime.now()
  hora_atual = horas.strftime("%H:%M:%S")
  savehour = f"{date.today()} - {hora_atual}"
  return savehour

while True:
  # horas = datetime.datetime.now()
  # hora_atual = horas.strftime("%H:%M:%S")
  # savehour = f"{date.today()} - {hora_atual}"

  choise = int(input(options))

  if choise <= 0 or choise > 4: 
    print("Selecione uma das opções entre 1 e 4")

# DEPOSITO
  elif choise == 1:
    print(enter_deposit_text)
    valor_depositado = float(input("Digite ao lado o valor que deseja depositar na sua conta:"))
    saldo += valor_depositado
    alteracoes_conta[f"{time()} - depósito"] = valor_depositado
    print(f"Seu saldo agora é de {saldo:.2f}")

# SAQUE
  elif choise == 2:
    if max_saques == 0:
      print("Você ja realizou o máximo de saques diários, volte outro dia")
    else:
      print(enter_deposit_text)
      valor_sacado = float(input("Digite ao lado o valor de no máximo R$500 reais a ser retirado do seu saldo: "))
      if(valor_sacado > 500):
        print("O valor selecionado é maior que o permitido")
        continue
      elif(valor_sacado < 0):
        print("O valor selecionado é menor que o permitido")
        continue
      elif saldo - valor_sacado <= 0:
        print("Saldo insuficiente")
        continue
      else:
        saldo -= valor_sacado
        alteracoes_conta[f"{time()} - Saque"] = valor_sacado
        max_saques -= 1
        print("Transação realizada com sucesso!")
        print(f"\nSeu saldo atual é de R${saldo:.2f}")

# EXTRATO
  elif choise == 3:
    print("================ Seu extrato! ================\n")
    print(f"Salto total de R$ {saldo:.2f}")
    # print(len(alteracoes_conta))
    if len(alteracoes_conta) == 0:
      print("Não foram realizadas nenhum tipo de transação!\n")
    else:
      print(alteracoes_conta)
    # for alteracoes_conta in alteracoes_conta:
    #   print(alteracoes_conta)
    print("==============================================")
  elif choise == 4:
    print(exit)
    break

