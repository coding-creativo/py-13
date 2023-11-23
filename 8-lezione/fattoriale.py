# def calcola_fattoriale(numero):
#     fattoriale = 1
    
#     for n in range(1,numero + 1):
#         fattoriale *= n
    
#     return fattoriale
    
# numero = int(input("inserisci un numero:"))
# fattoriale = calcola_fattoriale(numero)
# print(f"Il fattoriale del numero {numero} è {fattoriale}")


def calcola_fattoriale(n):
    risultato = 0 
    if n == 0:
        risultato = 1
    elif n < 0:
        risultato = "Il fattoriale di un numero negativo non è definito."
    else:
        risultato = n * calcola_fattoriale(n - 1)
    return risultato 
 
numero = int(input("Inserisci un numero: "))

risultato = calcola_fattoriale(numero)
print(f"Il fattoriale di {numero} è {risultato}")
