n = int(input("Inserisci un numero maggiore di 1: "))
while n <= 1:
    n = int(input("Inserisci un numero maggiore di 1: "))

for numero in range(2, n // 2 + 1):
    if n % numero == 0:
        print(f"Il numero {n} non è un numero primo")
        break
else:
    print(f"Il numero {n} è un numero primo")

    