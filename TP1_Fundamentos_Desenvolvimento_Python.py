#Q1.Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

print("***Bem-vindo ao programa de determinar números ímpares***")

Numero = int(input("Digite até  qual número (inclusive) você deseja somar os ímpares "))
def determinar_impar (Numero):
  soma = 0
  for i in range(0, Numero + 1):
    if (i % 2 != 0):
      soma += i

  return soma

determinar_impar(Numero)

##Q2.Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, meses e dias e retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.

import math

def calcular_idade (dia, mes, ano, dia_atual, mes_atual, ano_atual):

  idade_anos = ano_atual - ano
    
  if mes >= mes_atual:
    if mes == mes_atual:
      if dia > dia_atual:
        idade_anos -1 
    else:
      idade_anos -1  

  dias_passados =  (30 - dia) + ((12 - mes)*30) + ((mes_atual - 1)*30) + dia_atual + (idade_anos - 1)*365
  
  return dias_passados  

#Data de Nascimento
dia = int(input("Digite o dia de seu nascimento: "))
#Mês de Nascimento
mes = int(input("Digite seu mês de nascimento: "))
#Ano de Nascimento
ano = int(input("Digite seu ano de nascimento: "))

#Data atual
dia_atual = int(input("Digite o dia atual: "))
#Mês atual
mes_atual = int(input("Digite o mês atual: "))
#Ano atual
ano_atual = int(input("Digite o ano atual: "))

dias_passados = calcular_idade(dia, mes, ano, dia_atual, mes_atual, ano_atual)

modulo = 12 - int(math.fabs(mes_atual - mes))

if dia > dia_atual:
  modulo = modulo -1

print(f"Sua idade é de {ano_atual - ano - 1} anos e {modulo} meses.")
print(f"Você tem {dias_passados} dias.")

#Q3.Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120. Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.

print("***Bem vindo ao programa de calcular fatorial***")


def calcular_fatorial ():

  N = int(input("Digite um número para calcular o fatorial: "))
  fatorial = 1

  while N < 0:
    print("O número precisa ser maior ou igual a zero!")
    N = int(input("Digite um número para calcular o fatorial: "))
  
  if N == 0:
    print("O fatorial de zero é 1")

  else:
    for i in range(1, N + 1):
      fatorial *= i
  print(f"O valor do fatorial é {fatorial}")
  
calcular_fatorial()

#Q4.Escreva um programa em Python que calcule o fatorial de um dado número N usando um while. Use as mesmas especificações do item anterior.

numero = int(input("Fatorial de: "))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)

#Q5.Trabalhar com tuplas é muito importante! Crie 4 funções nas quais:

#A - Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo.
def obter_indice_elemento(elemento, parametro):
  if elemento in parametro:
    return parametro.index(elemento)
  print("O elemento não existe na tupla")

parametro = "maçã", "banana", "uva"
print(obter_indice_elemento("uva", parametro))
print(obter_indice_elemento("pêra", parametro))

#B - Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
def dividir_tupla(parametro):
  copiar = list(parametro)
  primeira_tupla = copiar[:len(copiar)//2]
  segunda_tupla = copiar[len(copiar)//2:]
  return primeira_tupla, segunda_tupla

parametro = "maçã", "banana", "uva", "pêra"
dividir_tupla(parametro)

#C - Dada uma tupla e um elemento, elimine esse elemento da tupla.
def deletar_elemento_indice(indice, parametro):
  copiar = list(parametro)
  del copiar[indice]
  novo = tuple(copiar)
  return novo

parametro = "maçã", "banana", "uva"
print(deletar_elemento_indice(0, parametro))
print(deletar_elemento_indice(2, parametro))

#D - Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.
def reverter(parametro):
  copiar = list(parametro)
  copiar.reverse()
  novo = tuple(copiar)
  return novo

parametro = "maçã", "banana", "uva"
print(reverter(parametro))

#Q6.Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores numa tupla e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, retorne qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo deve ser menor do que a soma do comprimento dos outros dois lados. Além disso, o programa deve identificar o tipo de triângulo formado observando as seguintes definições:

#Triângulo Equilátero: os comprimentos dos três lados são iguais.

#Triângulo Isósceles: os comprimentos de dois lados são iguais.

#Triângulo Escaleno: os comprimentos dos três lados são diferentes.

def possivel_triangulo(parametro):
  (x, y, z) = parametro
  if(x > (y+z)):
    return False
  if(y > (x+z)):
    return False
  if(z > (y+x)):
    return False
  return True

def encontrar_triangulo(parametro):
  (x, y, z) = parametro
  if x == y == z:
    return "equilátero"
  elif x != y != z:
    return "escaleno"
  else:
    return "isósceles"


print("Digite os comprimentos separados por virgula: ")
lados_triangulo = tuple(int(x.strip()) for x in input().split(','))

if possivel_triangulo(lados_triangulo):
  print(f"Esse triângulo é {encontrar_triangulo(lados_triangulo)}")
else:
  print("É impossível existir um triângulo com esses lados")
  
  #Q7.Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições para a esquerda. Assuma que a string tem pelo menos x caracteres.
  
  def rodar_string(mundo, rodar_tempo):  
  for x in range(rodar_tempo):
    mundo = mundo[-1] + mundo[:-1]
  return mundo

print(rodar_string("Brasil", 2))

#Q8.Escreva um código que leia 3 números do console e imprima o maior e o menor deles.

a = int(input('Entre com o primeiro numero: '))
b = int(input('Entre com o segundo numero: '))
if (a < b):
  menor = a
  maior = b
else:
  menor = b
  maior = a
c = int(input('Entre com o terceiro numero: '))
if (c < menor):
  menor = c
else:
  if (c > maior):
    maior = c

print('O menor numero eh ' + str(menor) + ' e o maior eh ' + str(maior))

#Q9.Refine o código anterior para ler primeiro a quantidade de números a serem lidos pelo console e depois imprima o maior e o menor.

quant = int(input('Quantos numeros serao lidos? '))
if (quant > 0):
  n = int(input('Entre com o numero: '))
  menor = n
  maior = n
for i in range(quant-1):
  n = int(input('Entre com o numero: '))
  if (n < menor):
    menor = n
  if (n > maior):
    maior = n

if (quant > 0):
  print('O menor numero eh ' + str(menor) + ' e o maior eh ' + str(maior))
  
  #Q10. Escreva um código que leia as 4 notas bimestrais de um aluno da escola pelo console e imprima a média final do aluno.
  
  nota1 = int(input('Entre com a nota1: '))
nota2 = int(input('Entre com a nota2: '))
nota3 = int(input('Entre com a nota3: '))
nota4 = int(input('Entre com a nota4: '))

def media(n1, n2, n3, n4):
  return (nota1+nota2+nota3+nota4)/4

print('A media final do aluno eh ' + str(media(nota1, nota2, nota3, nota4)))

#Q11.Refina o código anterior para obter a quantidade de notas a serem avaliadas pelo console e gerar o conceito final do aluno a partir da média aritmética calculada.

#Conceito A: entre 9 e 10 de média (incluindo os limites)

#Conceito B: entre 7 (inclusive) e abaixo de 9 de média

#Conceito C: entre 6 (inclusive) e abaixo de 7 de média

#Conceito D: abaixo de 6 de média

quantidade = int(input("Quantas notas serão levadas em consideração? "))

soma = 0;

for i in range(0, quantidade):   
  soma += (int(input(f"Digite a {i+1}ª nota: ")))

media = soma / quantidade

conceito = "A"

if (7 >= media < 9):
  conceito = "B"

if (6 >= media < 7):
  conceito = "C"

if (media < 6):
  conceito = "D"

print(f"A média foi {media}, portanto o conceito foi {conceito}")

#Q12.Escreva um código que some todos os números digitados pelo console até que o valor digitado seja ZERO (0).

oma = 0
base = 1


while (base != 0):
  numero = int(input("Digite o próximo número: "))
  soma += numero
  print(soma)
  base = numero
  
#Q13.Escreva uma função que calcula o salário líquido de um empregado a partir do salário bruto recebido como parâmetro. Base de cálculo:

#Letra A - Salário liquido = Salário bruto - desconto INSS - desconto IRRF Obs.: Vocês devem pesquisar as faixas de valores e as alíquotas de descontos do INSS para cada faixa e aplicar a alíquota conforme a faixa. O mesmo deve ser feito para o imposto de renda retido na fonte.
def pegar_INSS(salario):
  resultado = 0
  if salario <= 1100:
    resultado = salario * 0.075
  elif 1100 < salario <= 2203.48:
    resultado = salario * 0.09
  elif 2203.48 < salario <= 3305.22:
    resultado = salario * 0.12
  elif 3305.22 < salario <= 6433.57:
    resultado = salario * 0.14
  else:
    resultado = 751.99
  
  return round(resultado, 2)

def pegar_IRRF(salario):
  resultado = 0
  if salario <= 1903.98:
    resultado = 0
  elif 1903.98 < salario <= 2826.65:
    resultado = salario * 0.075 - 142.80
  elif 2826.65 < salario <= 3751.05:
    resultado = salario * 0.15 - 354.80
  elif 3751.05 < salario <= 4664.68:
    resultado = salario * 0.225 - 656.13
  else:
    resultado = salario * 0.275 - 869.36

  return round(resultado, 2)

salario = int(input("Digite o salário bruto: "))

INSS_desconto = pegar_INSS(salario)

salario_liquido_INSS = round(salario - INSS_desconto, 2)

IRRF_desconto = pegar_IRRF(salario_liquido_INSS)

salario_liquido = round(salario - IRRF_desconto - INSS_desconto, 2)

print(f"Desconto IRRF: R${IRRF_desconto}" )
print(f"Desconto INSS: R${INSS_desconto}" )
print(f"Salário líquido: R${salario_liquido}" )

#Para maiores informações consultar: https://www.calculadorafacil.com.br/trabalhista/calculo-salario-liquido

#Letra B - Refine o código anterior para incluir um parâmetro na função que represente o número de dependentes do trabalhador. Se o valor for omitido, assuma que ele não tem dependentes (valor 0 por default).
def pegar_INSS(salario):
  resultado = 0
  if salario <= 1100:
    resultado = salario * 0.075
  elif 1100 < salario <= 2203.48:
    resultado = salario * 0.09
  elif 2203.48 < salario <= 3305.22:
    resultado = salario * 0.12
  elif 3305.22 < salario <= 6433.57:
    resultado = salario * 0.14
  else:
    resultado = 751.99
  
  return round(resultado, 2)

def pegar_IRRF(salario):
  resultado = 0
  if salario <= 1903.98:
    resultado = 0
  elif 1903.98 < salario <= 2826.65:
    resultado = salario * 0.075 - 142.80
  elif 2826.65 < salario <= 3751.05:
    resultado = salario * 0.15 - 354.80
  elif 3751.05 < salario <= 4664.68:
    resultado = salario * 0.225 - 656.13
  else:
    resultado = salario * 0.275 - 869.36

  return round(resultado, 2)

salario = int(input("Digite o salário bruto: "))

INSS_desconto = pegar_INSS(salario)

salario_liquido_INSS = round(salario - INSS_desconto, 2)

IRRF_desconto = pegar_IRRF(salario_liquido_INSS)

salario_liquido = round(salario - IRRF_desconto - INSS_desconto, 2)

print(f"Desconto IRRF: R${IRRF_desconto}" )
print(f"Desconto INSS: R${INSS_desconto}" )
print(f"Salário líquido: R${salario_liquido}" )

#Q14.Implemente uma função que calcule as raízes de ume equação do segundo grau na forma ax2 + bx + c. O código deverá ler os valores de a, b e c do console e fazer as consistências, informando ao usuário nas seguintes situações:

#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

print("Com base nesta fórmula, ax2 + bx + c;")

a =float(input("Digite um valor para A: "))

if a == 0:
  print("Esta operação não condiz com uma equação de segundo grau.")
else:
  b = float(input("Digite um valor para B: "))
  c = float(input("Digite um valor para C: "))
  delta = (b**2)-(4*a*c)
if delta < 0:
  print("A equação não possui raízes reais.")
  print(" ")
  print(" Fim de execução. ")
else:
  x1=(-b + math.sqrt(delta) ) / (2*a)
  x2=(-b - math.sqrt(delta) ) / (2*a)
print("As duas raízes possíveis são: x1=" ,x1," e x2=" ,x2,"")
