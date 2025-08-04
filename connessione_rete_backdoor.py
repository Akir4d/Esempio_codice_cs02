import socket as so
import os
SRV_ADDR = "127.0.0.1"
SRV_PORT = 44445

# creando un oggetto che gestice la connessione in ipv4 e tcp
s = so.socket(so.AF_INET, so.SOCK_STREAM)
# configuriamo l'oggetto s con l'address e la port
s.bind((SRV_ADDR, SRV_PORT))
# spieghiamo all'oggetto quante connessioni accettare
s.listen(1)
# mandiamo un messaggio spiegando che stiamo attendendo connessioni
print("Server partito! Sto attendendo la connessione ...")
# in realta' questo comando attende la connessione
connection, address = s.accept()
print("Client connesso con indirizzo:", address)
# per dialogare dobbiamo avviare un loop che gestisca la connessione
while True:
    # invio un prompt
    path = os.getcwd()
    connection.sendall(path.encode() + b"$ ")
    # Mi metto in attesa dello stream de client
    data = connection.recv(1024)
    # Se il client chiude la connessione data sara' vuoto
    # quindi megli uscire dal loop con break che blocca il While true
    if not data: break
    
    # stampo quello che mi invia il client codificato in utf-8
    # nb: utf-8 e' la codifica del terminale
    # pulisco da \n
    comando = data.decode('utf-8').rstrip("\n")
    # print(comando)
    if comando.startswith("cd "):
        os.chdir(comando.split(" ")[1])
    else:
        esegui = os.popen(comando).read().rstrip('\n')
        connection.sendall(esegui.encode() + "\n".encode())

connection.close()


