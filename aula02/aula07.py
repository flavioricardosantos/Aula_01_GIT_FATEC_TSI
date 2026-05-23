salario = int(input("Digite seu salário: "))

reajuste = int(input("Digite o reajuste [em '%']: "))

novoSalario = salario + (salario * (reajuste / 100))

print(novoSalario)