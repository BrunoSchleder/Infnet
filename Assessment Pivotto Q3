#Q3
def renda_mensal ():
    salario = float(input("Renda Mensal: "))
    gasto_moradia = float(input("Gasto com moradia: "))
    gasto_educacao = float(input("Gasto com educacao: "))
    gasto_transporte = float(input("Gasto com transporte: "))
    percentual_moradia = (gasto_moradia / salario) * 100
    percentual_educacao = (gasto_educacao / salario) * 100
    percentual_transporte = (gasto_transporte / salario) * 100
    if percentual_moradia <= 30:
        print(f"Seus gastos com moradia estão dentro da margem recomendada. Você está gastando {round(percentual_moradia,2)}% do seu salário com moradia")
    else:
        print(f"Idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {salario * 0.3}. Você está gastando {round(percentual_moradia,2)}% do seu salário com moradia")
    if percentual_educacao <= 20:
        print(f"Seus gastos com educação estão dentro da margem recomendada. Você está gastando {round(percentual_educacao,2)}% do seu salário com moradia")
    else:
        print(f"Idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {salario * 0.2}. Você está gastando {round(percentual_educacao,2)}% do seu salário com educação")
    if percentual_transporte <= 15:
        print(f"Seus gastos com transporte estão dentro da margem recomendada. Você está gastando {round(percentual_transporte,2)}% do seu salário com moradia")
    else:
        print(f"Idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {salario * 0.15}. Você está gastando {round(percentual_transporte,2)}% do seu salário com transporte")


renda_mensal()
