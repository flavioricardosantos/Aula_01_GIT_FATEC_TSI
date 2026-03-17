nome = str (input("Informe seu nome ........!"))
nasc = int(input("Informe seu nascimento ........!"))
hoje = int(input("Informe ano atual........!"))
idade = hoje - nasc

print("Olá, %s" % nome)
print("voce possui em torno de %d anos de idade" % idade)