import socket as so

# chiediamo come scansire le porte di un trget
target = input("Inserisci l'indirizzo da scansire: ")
prange = input("Inserisci il range delle porte (es 5-200): ")

# uso split per ricavare un array con la porta superiore e inferiore
rrange = prange.split("-")
lowport = int(rrange[0]) # questo c'e' sempre anche se l'utente dimentica -
highport = 65535 # qui mettiamo la porta massima
if len(rrange) > 1:
    highport = int(rrange[1])
print(f"Scansisco il target {target} dalla porta {lowport} alla porta {highport}")
porte_chiuse = []
#faccio partire un ciclo for con il range porte da scansire
for port in range(lowport, highport+1):
    # avviamo una connessione tcp ipv4
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    # testiamo il 3-way handshake
    status = s.connect_ex((target, port))
    
    if(status == 0):
        # se 0 la connessione e' avvenuta, quindi siamo contenti
        print(f"*** Porta {port} - Aperta ***")
    else:
        porte_chiuse.append(port)
        #print(f"Porta {port} - chiusa")
    s.close()

domanda = input("vuoi vedere le porte chiuse? ")
if domanda.upper().startswith("S"):
        # faccio il join di tutti le porte chiuse
        print(", ".join([str(n) for n in porte_chiuse]))