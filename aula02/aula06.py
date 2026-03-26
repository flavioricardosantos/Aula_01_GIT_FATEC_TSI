dia = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

diaSeg = dia*24*60*60
horasSeg = horas*60*60
MinSeg = minutos*60

total = diaSeg + horasSeg + MinSeg + segundos

print(total)