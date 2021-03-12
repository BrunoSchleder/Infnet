#Questão 2

#Informe a idade: 25
#Tem obrigação de votar.
def obrigacao_votar():
  idade = int(input("Informe a Idade "))
  while idade <= 0:
    print("Idade Inválida")
    idade = int(input("Informe a Idade"))
  

#Informe a idade: 75
#Não tem obrigação de votar.
  if idade >= 16 and idade < 18 or idade > 70:
    print("Voto Facultativo")

#Informe a idade: 12
#Não tem direito a voto.
  elif idade <16:
    print("Não Pode Votar")
  else:
    print("Voto Obrigatório")

obrigacao_votar()
