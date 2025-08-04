import socket as so

SRV_ADDR = "127.0.0.1"
SRV_PORT = 44444

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
    # Mi metto in attesa dello stream de client
    data = connection.recv(1024)
    # Se il client chiude la connessione data sara' vuoto
    # quindi megli uscire dal loop con break che blocca il While true
    if not data: break
    # rispondo al client con un saluto
    connection.sendall(b"Letto\n")
    # stampo quello che mi invia il client codificato in utf-8
    # nb: utf-8 e' la codifica del terminale
    print(data.decode('utf-8'))

connection.close()


