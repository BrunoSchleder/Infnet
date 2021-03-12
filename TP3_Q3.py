#Questão 3

#Informe nome do 1º participante: Zefrônio
#Informe nota do 1º participante: 8.5
#Informe nome do 2º participante: Oliúde
#Informe nota do 2º participante: 6.0
#Informe nome do 3º participante: Xonotrônfila
#Informe nota do 3º participante: 7.8
#Informe nome do 4º participante: Carbúncleo
#Informe nota do 4º participante: 8.6
#Informe nome do 5º participante: Zeugma
#Informe nota do 5º participante: 9.4
#O(a) vencedor(a) foi Zeugma com nota 9.4!

def escolhe_vencedor():
  for i in range(5):
    nome = input(f"Informe o nome do {i+1}º participante: ")
    nota = float(input(f"Informe a nota do {i+1}º participante: "))
    
    if i == 0 or nota > nota_vencedor:
      nome_vencedor = nome
      nota_vencedor = nota
    
  print(f"O vencedor foi {nome_vencedor} e com nota {nota_vencedor}")

escolhe_vencedor()
