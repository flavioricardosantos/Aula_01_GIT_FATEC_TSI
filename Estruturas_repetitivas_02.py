while (True):
    num = (int(input("Digite um número inteiro:")))
    for i in range(0, 11):
        print(i*num)
    exibi_outra = (str(input("Deseja continuar? (s/n): ")))
    if  exibi_outra.lower() != 's':
        print("finalizando...")
        break
    else:
        exibi_outra.lower() != 'n'
        while True:
                num = (int(input("Digite um número inteiro:")))
                for i in range(0, 11):
                    print(i*num)