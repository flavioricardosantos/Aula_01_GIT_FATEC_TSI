lim = int(input("Digite o limite da sequencia: "))

n1 = 1
n2 = 1

print(n1)
print(n2)

if lim <=2:
    print()
else:
    for i in range(3, lim + 1, 1):
        resultado = n1 + n2

        n1 = n2
        n2 = resultado
        print(resultado)