#range - funzione incorporata che genera una sequenza di numeri

# numeri = range(1,11)
# print(numeri)

numeri = list(range(1,11))
print(numeri)

#posso iterare l'oggetto range anche senza convertirlo in lista

for n in range(0,101,2):
    print(n)