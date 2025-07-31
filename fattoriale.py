x = int(input("Calacolo del fattoriale di: "))
num = 1
fattoriale = x
while num < x:
    fattoriale *= num
    num += 1

print(f"{x}! = {fattoriale}")

