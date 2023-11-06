# N = 10
# somma = 0 #0 elemento neutro della somma

# for n in range(1, N + 1):
#     # somma = somma + n
#     somma += n
#     # print(somma) #somma progressiva

# print(somma)


# N = 3 - i numeri da sommare sono 1, 2 e 3
# somma = 1
# somma = 1 + 2 = 3
# somma = 3 + 3 = 6
# somma = somma + n

N = 3
somma = 0

for _ in range(N):
    numero = int(input("inserici il numero: "))
    somma += numero

print(somma)
