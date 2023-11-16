# numeri = []

# for i in range(3):
#     numero = int(input("Inserisci un numero"))
#     numeri.append(numero)

# print(numeri)

# numeri = [13,2,4,6,2]
# numeri.clear()
# print(numeri)

# el = numeri.remove(2)
# print(numeri)
# print(el)

# el = numeri.pop(2)
# print(numeri)
# print(el)

# del numeri[2]
# print(numeri)

numeri = [13,2,4,6,2]

numero = 2

while numero in numeri:
    numeri.remove(numero)

print(numeri)
