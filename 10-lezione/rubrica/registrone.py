"""Realizzare un programma a piacere per il registro dei voti per gli studenti utilizzando i dizionari."""

def aggiungi_voto(registro):
    studente = input("Inserisci il nome dello studente: ")
    voto = float(input("Inserisci il voto dello studente: "))
    
    if studente in registro:
        registro[studente].append(voto)
    else:
        registro[studente] = [voto]

def stampa_voti(registro, studente):
    if studente in registro:
        voti = registro[studente]
        print(f"I voti di {studente} sono: {voti}")
    else:
        print("Lo studente non è presente nel registro.")


def elimina_studente(registro, studente):
    if studente in registro:
        del registro[studente]
        print(f"{studente} è stato rimosso dal registro.")
    else:
        print("Lo studente non è presente nel registro.")

        
def main():
    registro_voti = {}
    scelta = None

    while scelta != "0":
        print("\n1. Aggiungi voto")
        print("2. Calcola media voti di uno studente")
        print("3. Elimina uno studente")
        print("0. Esci")
        
        scelta = input("\nScegli un'opzione: ")
        
        if scelta == "1":
            aggiungi_voto(registro_voti)
        elif scelta == "2":
            studente = input("Inserisci il nome dello studente di cui vuoi calcolare la media voti: ")
            media = stampa_voti(registro_voti, studente)
            print(f"La media voti di {studente} è: {media}")
        elif scelta == "3":
            studente = input("Inserisci il nome dello studente da eliminare: ")
            elimina_studente(registro_voti, studente)
        elif scelta == "0":
            print("Uscita dal programma.")
        else:
            print("Opzione non valida. Riprova.")

"""
La variabile main viene utilizzata per determinare se lo script Python è stato eseguito direttamente dall'interprete Python o se è stato importato come modulo in un altro script. Quando uno script è eseguito direttamente, il valore di il valore di __name__ diventa '__main__'"""



def saluta_tutti():
    print("ciao")



if __name__ == "__main__":
    print(__name__) #in questo fil stampa main
    saluta_tutti()
    main()


