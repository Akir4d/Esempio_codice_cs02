import socket as so, platform as pl, os 

SRV_ADDR = ""
SRV_PORT = 1236

# Creo l'oggetto per gestire la connessione
s = so.socket(so.AF_INET, so.SOCK_STREAM)
# Configuriamo l'oggetto in modo che si colleghi
# su ogni interfaccia (SRV_ADDR) alla porta 1234 (SRV_PORT)
s.bind((SRV_ADDR, SRV_PORT))
# configuriamo l'oggetto in modo che accetti 1 connessione alla volta
s.listen(1)
# Avviamo la connessione e destrutturiamo la tupla risultante
connection, address = s.accept() # qui il codice si ferma in attesa del client
# connection che e' l'oggetto che gestira' l'instanza del client
# address che e' una tupla che contiene l'indirizzo e la porta della connessione

while True:
    #connection.sendall("1 per info\n2 per lista file\n0 per uscire\n".encode())
    try:
        # qui attendiamo che il client invii dati
        data = connection.recv(1024)
    except: continue # se dovesse andare in timeout riprendiamo da while True

    command = data.decode('utf-8').strip() # convertiamo il comando in utf-8
    # opzione 1
    if command == '1':
        tosend = f"{pl.platform()} {pl.machine()}\n"
        connection.sendall(tosend.encode()) 
    elif command == '2':
        data = connection.recv(1024)
        try:
            path = data.decode('utf-8').strip()
            # questo comando legge una path che inviamo dopo
            filelist = os.listdir(path)
            tosend = ""
            for x in filelist: tosend += "," + x
        except:
            tosend = "percorso sbagliato\n"
        connection.sendall(tosend.encode())
    elif command == '9':
        connection.close()
        break
    elif command == '0':
        # chiudo la connessione
        connection.close()
        # la riapro in modo che attenda una nuova connessione
        connection, address = s.accept()
s.close()

