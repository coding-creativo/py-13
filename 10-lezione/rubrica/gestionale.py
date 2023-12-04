import registrone
# from registrone import aggiungi_voto, stampa_voti

def saluta():
    print("benvenuti nel registro di classe: !")

saluta()
print("Hello")

registro_voti = {}
registrone.aggiungi_voto(registro_voti)

# aggiungi_voto(registro_voti)
# studente = input('inserisci il nome dello studente: ')
# stampa_voti(registro_voti,studente)

# def main():
#     registro_voti = {}
#     scelta = None

#     while scelta != "0":
#         print("\n1. Aggiungi voto")
#         print("2. Calcola media voti di uno studente")
#         print("3. Elimina uno studente")
#         print("0. Esci")
        
#         scelta = input("\nScegli un'opzione: ")
        
#         if scelta == "1":
#             registrone.aggiungi_voto(registro_voti)
#         elif scelta == "2":
#             studente = input("Inserisci il nome dello studente di cui vuoi calcolare la media voti: ")
#             media = registrone.media_voti(registro_voti, studente)
#             print(f"La media voti di {studente} è: {media}")
#         elif scelta == "3":
#             studente = input("Inserisci il nome dello studente da eliminare: ")
#             registrone.elimina_studente(registro_voti, studente)
#         elif scelta == "0":
#             print("Uscita dal programma.")
#         else:
#             print("Opzione non valida. Riprova.")

