x = int(input("Inserisci un numero: "))

if (x < 10):
    print("hai inserito un numero minore di 10")
elif x == 10:
    print("hai inserito 10")
else:
    print("hai inserito un numero maggiore di 10")

x = input("Dammi una frase: ").lower()

if ("ciao" in x) or ("hey" in x) :
    print("Ciao come stai?")
else:
    print("Perche' non saluti?")