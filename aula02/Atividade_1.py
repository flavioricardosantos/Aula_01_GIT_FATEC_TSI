preco = float(input("Qual o preço do combustivel?"))
desempenho = float(input("Quantos km faz com 1L?"))
distancia = float(input("Qual a distancia a ser percorrida?"))

total_litros = distancia/desempenho
gasto = total_litros*preco
print("voce gastará!",gasto, "reais e",total_litros, "litros de combustivel")
