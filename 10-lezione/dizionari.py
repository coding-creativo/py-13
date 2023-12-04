
studente = {
    'nome': 'Pippo',
    'eta': 20,
    'corso': 'Informatica'
}

# print(studente['nome'])

# studente['eta'] = 40
# studente['matricola'] = 'abc13'

# print(studente)

# for k, item in studente.items():
#     print(f"key {k} - valore {item}")



rubrica = {
    'Pippo': {
        'numero': '123456789',
        'indirizzo': 'Via Roma, 1',
        'email': 'pippo@example.com'
    },
    'Paperina': {
        'numero': '987654321',
        'indirizzo': 'Piazza Venezia, 5',
        'email': 'paperina@example.com'
    },
    'Pluto': {
        'numero': '555123456',
        'indirizzo': 'Corso Italia, 10',
        'email': 'pluto@example.com'
    }
}

print(rubrica['Pippo']['numero'])

for item in rubrica['Pippo'].values():
    print(item)
