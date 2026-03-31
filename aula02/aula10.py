cap_max =float(input("Qual a capacidade maxima do elevador"))
peso1 = float(input("qual o peso?"))
peso2= float(input("qual o peso?"))
peso3= float(input("qual o peso?"))
peso4 =float(input("qual o peso?"))
peso5 =float(input("qual o peso?"))
total = peso1+peso2+peso3+peso4+peso5
if total < cap_max:
    print("o peso exedeu!")
else:
    print("pode subir!")
