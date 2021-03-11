#Questão 1

#Informe o valor total do consumo: R$ 100.00
consumo = float(input("Valor Total do Consumo R$ "))

#Informe o total de pessoas: 2
numero = int(input("Total de Pessoas "))
while numero < 1:
  print("digite um valor válido")
  numero = int(input("Total de Pessoas "))

#Informe o percentual do serviço, entre 0 e 100: 10
taxa = int(input("Informe o Percentual de Serviço "))
while taxa < 0 or taxa  > 100:
  print("digite um valor válido")
  taxa = int(input("Informe o Percentual de Serviço "))

#O valor total da conta, com a taxa de serviço, será de R$ 110,00.
total_conta = consumo * (1 + taxa/100)

#Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ 55,00.
divisao = total_conta / numero
conta_real = numero * divisao

print(f"O valor da conta por pessoa é de {divisao}")
print(conta_real)
