menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)
  if opcao == 'd':
    print("====================++ Depositar: ====================")
    valor_deposito = float(input("Digite o valor a ser depositado: "))
    if valor_deposito>0:
      saldo += valor_deposito
      extrato += f"Depósito no valor de R$ {valor_deposito:.2f}\nSaldo: R$ {saldo:.2f}\n"
      print(f"Deposito no valor de R$ {valor_deposito:.2f} realizado com sucesso!")
    else:
      print("Valor inválido para operação.")
#===============================================================================      
  elif opcao == 's':
    print("====================--Sacar: ====================")
    valor_saque = float(input("Digite o valor para saque: "))
    saldo_insuficiente = valor_saque > saldo
    excede_limite = valor_saque > limite
    excede_saques = numero_saques >= LIMITE_SAQUES
    if saldo_insuficiente:
      print(f"FALHA: Saldo insuficiente para o saque desejado. Seu saldo é de {saldo: .2f}")
    elif excede_limite:
      print("FALHA: O valor operação desejada excede o limite.")
    elif excede_saques:
      print("FALHA: Operação excede o limite de saques por dia.")
    elif valor_saque > 0:
      saldo -= valor_saque
      extrato += f"Saque no valor de R$ {valor_saque: .2f}\nSaldo: R$ {saldo:.2f}\n"
      numero_saques += 1
      print(f"Saque no valor de R$ {valor_saque:.2f} realizado com sucesso!")
    else:
      print("FALHA: valor inválido")
#===============================================================================
  elif opcao == 'e':
    print("==================== Extrato: ====================")
    print("Não foram realizadas operações.\n" if not extrato else extrato)
    #print(f"Saldo atual: R${saldo: .2f}")
    print("==================== Fim do Extrato ====================")
#===============================================================================
  elif opcao == 'q':
    break
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")

  