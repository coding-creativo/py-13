
studente = {
    'nome': 'Pippo',
    'eta': 20,
    'corso': 'Informatica'
}

# print(studente['nome']) 

# studente['eta'] = 25
# print(studente['eta'])

# Iterazione attraverso i valori del dizionario
for valore in studente.values():
    print(valore)

# Iterazione attraverso le chiavi del dizionario
for chiave in studente:
    print(chiave)

# Iterazione attraverso le coppie chiavi-valore del dizionario
for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")


# altro esempio
# studente['indirizzo'] = ['via delle rose', '00200', 'modica']

# print(studente)
# print(studente['indirizzo'][0])