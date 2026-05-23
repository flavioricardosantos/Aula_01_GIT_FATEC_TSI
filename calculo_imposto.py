# FAZER UMA APLICAÇÃO QUE CALCULE O IMPOSTO DE RENDA DE UMA PESSOA
# JÁ QUE O IMPOSTO DE RENDA VARIA DEPENDENDO DO SALÁRIO
# REDUÇÃO E IMPOSTO DE RENDA (SÃO 2 TABELAS DIFERENTES)

# use esse site https://www.gov.br/secom/pt-br/acompanhe-a-secom/noticias/2026/01/nova-tabela-do-ir-veja-faixas-e-aliquotas-e-saiba-mais-sobre-medida-que-isenta-o-pagamento-para-quem-ganha-ate-r-5-mil

#reducao

def reducao(renda):
    if (renda < 5000):
        return 312.89 # NAO PAGA NADA
        return 312.89
    elif (renda < 7350):
        return 978.62 - (0.133145 * renda)
    else:
        return 0


#imposto de renda
def calcular_ir(renda, descontos):
    imposto = renda - descontos

    if (renda <= 2428.80):
        aliquota = 0
        deducao = 0
    elif (renda <= 2826.65):
        aliquota = 0.075
        deducao =  182.16
    elif (renda <= 3751.05):
        aliquota = 0.15
        deducao =  394.16
    elif (renda <=  4664.68):
        aliquota = 0.225
        deducao =  675.49
    else:
        aliquota = 0.275
        deducao =  908.73

    red = reducao(renda)


    imposto = (imposto * aliquota) - deducao
    imposto = max(imposto, 0)
    imposto = imposto - red

    return imposto


#menu prinpal
def sistema_ir():
    while (True):
        print("=" * 70)
        print("                    CALCULADORA DE IMPOSTO DE RENDA                 ")
        print("=" * 70)
        print("\n[0] - Imposto de Renda Mensal")
        print("[1] - Imposto de Renda Anual")
        print("[2] - Sair\n")
        print("=" * 70)

        escolha = int(input("\nDigite a opção que deseja: "))

        # mensal
        if escolha == 0:

            print("=" * 70)

            renda = float(input("\nDigite sua renda mensal: \n"))
            print("=" * 70)
            descontos = float(input("\nDigite também os seus descontos mensais [INSS, etc]: "))
            imposto = calcular_ir(renda, descontos)
            liquido = renda - imposto

            print("\n" + "=" * 70)
            print(f"\nImposto: R$ {imposto:.2f}")
            print(f"Renda líquida: R$ {liquido:.2f}\n")


        # anual
        elif escolha == 1:
            print("=" * 70)

            renda_mensal = float(input("\nDigite sua renda mensal: \n"))
            print("=" * 70)
            descontos = float(input("\nDigite também os seus descontos mensais [INSS, etc]: "))
            imposto = calcular_ir(renda, descontos)
            
            descontos = float(input("\nDigite também os seus descontos mensais [INSS, etc]: "))            

            imposto_mensal = calcular_ir(renda_mensal)
            imposto_mensal = calcular_ir(renda_mensal, descontos)

            imposto_anual = imposto_mensal * 12
            renda_anual = renda_mensal * 12
            liquido_anual = renda_anual - imposto_anual

            print("\n" + "=" * 70)
            print(f"\nImposto anual: R$ {imposto_anual:.2f}")
            print(f"Renda líquida anual: R$ {liquido_anual:.2f}\n")

        # sair
        elif escolha == 2:
            print("\n" + "=" * 70)
            print("                              SAINDO...")
            print("=" * 70)
            break

        else:
            print("\nOpção inválida!\n")
sistema_ir()