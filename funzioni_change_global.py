

def cambia_globale():
    global x # Global mi consente di manipolare le varibili globali
    # in assenza di global quello che segue da errore
    x = 1

x = 10

print("prima del test la x e' uguale a:", x)
cambia_globale()
print("dopo test la x e' uguale a:", x)