lim = int(input("Digite o limite da sequência Fibonacci: "))
num = [1,1]
i = 1

while True:
    new = num[i - 1] + num[i]
    if (new >= lim):
        break
    num.append(new)
    i+=1

print(num)