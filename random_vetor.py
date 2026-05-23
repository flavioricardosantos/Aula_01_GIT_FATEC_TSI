from random import randint
L=[]
for i in range(10):

    L.append(randint(1,50))
    for i in L:
        if i % 2 == 0:
            print("Positivo");
    else:
        print("negativo")
        print(L)