#Ricerca di un carattere in una stringa

stringa = "Coding Creativo"
car = "z"

for carattere in stringa:
    if carattere == car:
        print(f"Ho trovato '{car}' nella stringa {stringa}")
        break #provoca l'uscita immediata dal ciclo
else:
    print(f"Non ho trovato '{car}' nella stringa {stringa}")

