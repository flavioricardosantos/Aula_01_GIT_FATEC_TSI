escolha = int(input("O que voce deseja calcular digite 1 para lata de oleo 2 para caixa de papelão"))
if escolha == 1:
    r = float(input("qual o raio da lata"))
    a = float(input("Qual a altura da lata"))
    volume = 3.14 * r**2 * a
    print("o volume é!",volume)
else:
    altura = float(input("Qual a altura?"))
    largura = float(input("Qual a largura?"))
    comprimento = float(input("Qual o comprimento?"))
    volume = altura * largura * comprimento
    print("o volume é !",volume)
