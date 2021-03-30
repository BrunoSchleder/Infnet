#Q4
#Valor inicial: R$ 10000
#Rendimento por período (%): 0.54
#Aporte a cada período: R$ 1000
#Total de períodos: 120

import matplotlib.pyplot as plt

valor_inicial = float(input("Valor de Investimento Inicial R$ "))
rendimento_periodo = float(input("Taxa de Juros % "))
aporte = float(input("Valor Mensal R$ "))
mês = 1
saldo = valor_inicial
periodos = int(input("Em quantos meses de aplicação "))
valor_rentabilidade = []
while mês <= periodos:
  rendimento = (saldo * (rendimento_periodo / 100))
  saldo = saldo + rendimento + aporte  
  valor_rentabilidade.append(saldo)
  print (f"Após {mês} períodos(s), o montante será de R$ {saldo:.2f} ")
  mês = mês + 1

plt.plot(valor_rentabilidade)
plt.show()
