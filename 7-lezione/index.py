numeri = [10, 2, 13, 4, 5, 24, 5, 8]
el_da_cercare = 5
indici = []

index = -1
while el_da_cercare in numeri [index+ 1:]:
    index = numeri.index(el_da_cercare,index+ 1)
    indici.append(index)

print(f"Gli indici sono:{indici}")