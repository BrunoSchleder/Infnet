#Q5

#A)
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
