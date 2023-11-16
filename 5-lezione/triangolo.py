
n = 5
for i in range(n, 0, -1): #crea intervallo di valori da 5 a 1
    for j in range(i, 0, -1): #crea intervallo di valori da (i) 5 a 1 - poi da (i) 4 a 1
        print(j, end="")
    print()