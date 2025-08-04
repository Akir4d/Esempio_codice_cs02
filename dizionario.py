diz = {
        "nome": "Pinco", 
        "cognome": "Pallino", 
        "interessi":['Musica', 'Sport', 'Viaggi']
      }


print(diz['nome'])

diz["nascita"] = "10/05/1994"

print(diz)
print(diz.keys())
print(diz.values())
print(diz.items())

# destruttazione dati

for chiave, valore in diz.items():
    print("key:",chiave," - value:", valore)

riga = ["Franca", "Rame", "Scrittrice", "Roma"]

nome, cognome, null, null = riga

print(nome)