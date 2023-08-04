from datetime import date
import datetime

# ================================PARTE 1==============================================
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

# ================================PARTE 2==============================================
# Criar funcoes para operações: Sacar, depositar e visualizar histórico
# funcao saque deve receber argumentos apensa por nome (keyword only)
# funcao deposito deve receber os argumentos apenas por posição (positional only) (só passar os argumentos)
# funcao visualizar extrato (positional only e keyword only)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------- NOVAS FUNÇÕES ---------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------
# Criar função usuário - deve armazenar os usuarios em uma lista. Ele é composto por nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, numero - bairro - cidade/sigla - estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF

# Criar conta corrente (vincular com o usuário) - O programa deve armazenar contas em uma lista. Ela deve ser composta por: Agência, número da conta e usuário. o número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a 1 usuário
# opcional: criar funcao listar contas


options ="""
================ Bem vindo ao banco! ================
      
  Selecione uma das opções abaixo:

  [1] - Depósito
  [2] - Saque
  [3] - Extrato
  [4] - Criar usuário
  [5] - Criar conta corrente
  [6] - Listar usuários
  [7] - Listar contas
  [8] - Sair
      
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

saldo = 1000.92
alteracoes_conta = {}
max_saques = 3
usuarios = []
contas = []
user_counter = 1
conta = 1  

def time():
  horas = datetime.datetime.now()
  hora_atual = horas.strftime("%H:%M:%S")
  savehour = f"{date.today()} - {hora_atual}"
  return savehour
def deposito():
    global saldo, alteracoes_conta
    print(enter_deposit_text)
    valor_depositado = float(input("Digite ao lado o valor que deseja depositar na sua conta:"))
    saldo += valor_depositado
    alteracoes_conta[f"{time()} - depósito"] = f" R$ {valor_depositado}"
    print(f"Seu saldo agora é de {saldo:.2f}")
def saque():
  global max_saques, saldo, alteracoes_conta
  if max_saques == 0:
      print("Você ja realizou o máximo de saques diários, volte outro dia")
      return
  print(enter_deposit_text)
  valor_sacado = float(input("Digite ao lado o valor de no máximo R$500 reais a ser retirado do seu saldo: "))
  if(valor_sacado > 500):
      print("O valor selecionado é maior que o permitido")
  elif(valor_sacado < 0):
      print("O valor selecionado é menor que o permitido")
  elif saldo - valor_sacado <= 0:
      print("Saldo insuficiente")
  else:
      saldo -= valor_sacado
      alteracoes_conta[f"{time()} - Saque"] = f"R$ {valor_sacado}"
      max_saques -= 1
      print("Transação realizada com sucesso!")
      print(f"\nSeu saldo atual é de R${saldo:.2f}")
def extrato():
    global alteracoes_conta, saldo
    print("================ Seu extrato! ================\n")
    print(f"Salto total de R$ {saldo:.2f}")
    if len(alteracoes_conta) == 0:
      print("ATENÇÃO:Não foram realizadas nenhum tipo de transação!\n")
    else:
      for chave, valor in alteracoes_conta.items():
        print(f"{chave} {valor}")
    print("==============================================")
def criar_usuario():
  global usuarios
  cpf = input("Insira ao lado o seu CPF: ")
  for usuario in usuarios:
     if cpf in usuario:
        print("Usuário já cadastrado")
        return
  nome = input("Insira seu nome completo ao lado: ")
  nascimento = input("Insira a sua data de nascimento: ")
  logradouro = input("Insira o nome da sua rua: ")
  numero = input("Insira o número: ")
  bairro = input("Insira o bairro em que reside: ")
  cidade = input("Insira a sua cidade: ")
  estado = input("Insira o estado: ")
  dados = {
    "nome": nome,
    "nascimento": nascimento,
    "endereço": f"{logradouro},{numero} - {bairro} - {cidade} - {estado}"
  }
  user = {
      cpf: dados
  }
  usuarios.append(user)
  print(usuarios[0])
def listar_usuarios():
   global usuarios
   for usuario in usuarios:
      print(usuario)
def criar_conta_corrente():
  global usuarios, conta
  agencia = "0001"
  user = {}
  user_found = False
  listar_usuarios()
  user_cpf = input("Digite ao lado o cpf cadastrado no sistema que deseja utilizar: ")
  for usuario in usuarios:
     if user_cpf in usuario:
        user = usuario.copy()
        user_found = True
  if not user_found:
        print("Usuário não encontrado, realizar cadastro do mesmo no sistema")
        return
  
  acc_bancaria = {
     "conta": conta,
     "agencia": agencia,
     "usuario": user
  }
  contas.append(acc_bancaria)
  conta += 1
  print(contas)
def listar_contas():
  for conta in contas:
     print(conta)

while True:
  choise = int(input(options))

  if choise <= 0 or choise > 8: 
    print("Selecione uma das opções entre 1 e 8")

  elif choise == 1: # DEPOSITO
    deposito()
  elif choise == 2: # SAQUE
   saque()
  elif choise == 3: # EXTRATO
    extrato()
  elif choise == 4: #Criar usuário
     criar_usuario()
  elif choise == 5: #Criar conta corrente
     criar_conta_corrente()
  elif choise == 6: #Criar conta corrente
     listar_usuarios()
  elif choise == 7: # listar contas
    listar_contas()
  elif choise == 8: # SAIR
    print(exit)
    break

