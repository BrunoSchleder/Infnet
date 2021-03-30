#Q5

#A)
arquivo = open("Assessment_PIBs.csv")
tabela_pib = arquivo.read()
arquivo.close()

tabela_pib = tabela_pib.splitlines()
head = tabela_pib[0]
head = head.split(',')
tabela_pib = tabela_pib[1:]
print(head)
print(tabela_pib)
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
  
  
#B)
