x = 10

def incremento(z):
    global x # Global mi consente di manipolare le varibili globali
    # in assenza di global quello che segue da errore
    x = x + z
    return x

print("prima del test la x e' uguale a:", x)
print("Testo la funzione che restituisce", incremento(5))
print("dopo test la x e' uguale a:", x)