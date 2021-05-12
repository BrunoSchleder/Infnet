#Questão 5

#A)
import matplotlib.pyplot as plt

arquivo = open("Assessment_PIBs.csv")
tabela_pib = arquivo.read()
arquivo.close()

tabela_pib = tabela_pib.splitlines()
head = tabela_pib[0]
head = head.split(',')
tabela_pib = tabela_pib[1:]
paises_pib = []
anos = head[1:]
for elemento in tabela_pib:
  elemento = elemento.split(',')
  paises_pib.append(elemento)

for elemento in tabela_pib:
  elemento = elemento.split(',')
  head.append(elemento)

paises = []

for linha in paises_pib:
  paises.append(linha[0])

for linha in range(0, len(paises_pib)):
  del paises_pib[linha][0]

pais = input("Informe um país: ")
if pais in paises:
  ano = input("Informe um ano entre 2013 e 2020: ")
  if ano in anos:
    print(f"PIB {pais} em {ano} é de US$ {paises_pib[paises.index(pais)][anos.index(ano)]} trilhões.")
  else:
    print("O ano não está disponível!")
else:
  print("País indisponível")

#B)
def variacaoperiodo(paises, anos, paises_pib):
  for linha in range(0, 15):
    variacao = (float(paises_pib[linha][7]) / float(paises_pib[linha][0]) -1) * 100
    comprimento = len(paises[linha])
    print(f"\n{paises[linha]}" + " "*(25 - comprimento) + f"Variação percentual {variacao:.2f} % no período de 2013 a 2020")

variacaoperiodo(paises, anos, paises_pib)

#C)
def graf_plot(paises_pib, anos, paises):
  pais = input("\nEscolha um país para ver o gráfico de variação do PIB (2013 a 2020): ")
  for i in range(0, 8):
    paises_pib[paises.index(pais)][i] = float(paises_pib[paises.index(pais)][i])
  plt.plot(anos, paises_pib[paises.index(pais)])
  plt.title("Desenvolvimento PIB")
  plt.xlabel("Anos")
  plt.ylabel("PIB em US$ Trilhões")
  plt.ylim([min(paises_pib[paises.index(pais)]), max(paises_pib[paises.index(pais)])])
  plt.show()

graf_plot(paises_pib, anos, paises)
