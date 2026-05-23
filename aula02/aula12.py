op = int(input("opção 1 = retangulo opção 2 =triangulo"))
base = float(input("Qual a base?"))
altura= float(input("Qual a altura?"))

if op == 1:
    area = base*altura
    print("a area é!",area)
else:
    area= (base*altura)/2
    print("a area é!",area)
    