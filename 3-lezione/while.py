n = int(input("inserisci un numero: "))

while n < 2:
    print("il numero è minore di 2!")
    n = int(input("inserisci un numero: "))

massimo = int(input("inserisci il primo numero!: "))

for i in range(n - 1):
    numero = int(input("inserisci un numero: "))

    if numero > massimo:
        massimo = numero

print(massimo)