import random

def colore_casuale():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colore = (r, g, b)
    return colore

colore_random = colore_casuale()
print(f"Colore casuale in formato RGB: {colore_random}")

#numero casuale tra 0 e 1 non compreso
# numero_casuale = random.random()
# print(numero_casuale)

#numero casuale tra a e b compresi
# numero_casuale = random.randint(1,10)
# print(numero_casuale)

#numero casuale tra a compreso e b non compreso con la virgola
# numero_casuale = random.uniform(1,10)
# print(numero_casuale)
# print(f"numero_casuale {numero_casuale:.2f}")

# sceglie un elemento a caso da una lista
# frutta = ['mela', 'banana', 'arancia', 'fragola']

# random_el = random.choice(frutta)
# print(random_el)

# # sceglie un elemento a caso da una tupla
# frutta = ('mela', 'banana', 'arancia', 'fragola')

# random_el = random.choice(frutta)
# print(random_el)

# # sceglie una lettera a caso da una stringa
# frutta = "mela"
# random_el = random.choice(frutta)
# print(random_el)

#sceglie k elementi a caso da una lista
# frutta = ['mela', 'banana', 'arancia', 'fragola']

# random_el = random.sample(frutta, 2) 
# print(random_el)

# #mescola a caso gli elementi della lista
# frutta = ['mela', 'banana', 'arancia', 'fragola']

# random.shuffle(frutta)
# print(frutta)