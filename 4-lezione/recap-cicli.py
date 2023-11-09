#Stampare la tabellina del 2
# for i in range(0, 21, 2):
#     print(i)

# for i in range(0, 11):
#     print(f"2 * {i} = {i * 2}")

# numero = 3
# for i in range(0, numero * 10 + 1, numero):
#     print(i)

#doppi cicli
#tavola pitagorica

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
#...
# n = 10
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end = "\t")
#     print()

# #Sommare dei numeri finchè la somma non raggiunge 1000

# somma = 0

# while somma < 1000:
#     n = int(input("inserire un numero: "))
#     somma += n

# print(somma)


#Inserire N numeri e contare quanti numeri pari e dispari sono stati chiesti

N = int(input("quanti numeri vuoi inserire?: "))
conta_p = conta_d = 0

for _ in range(N):
    numero = int(input("inserisci il numero: "))
    # sintassi ternario: se_vero if condizione else se_falso 
    conta_p, conta_d = (conta_p + 1, conta_d) if numero % 2 == 0 else (conta_p, conta_d + 1)
    # oppure
    # conta_p += 1 if numero % 2 == 0 else 0
    # conta_d += 1 if numero % 2 != 0 else 0
    # oppure
    # if numero % 2 == 0:
    #     conta_p = conta_p + 1
    # else:
    #     conta_d = conta_d + 1

print(f"pari: {conta_p} - dispari: {conta_d}")

