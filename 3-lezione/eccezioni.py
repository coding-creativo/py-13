# try:
#     punteggio = int(input("inserisci un numero!: "))
# except ValueError:
#     print("Attenzione non hai inserito un intero!")

# punteggio = int(input("inserisci un numero!: "))

while True:
    try:
        punteggio = int(input("inserisci un numero!: "))
        break #uscita immediata dal ciclo
    except ValueError:
        print("Attenzione non hai inserito un intero!")