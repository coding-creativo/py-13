import os

script_path = os.path.abspath(__file__) 
script_dir = os.path.dirname(script_path) 
os.chdir(script_dir)

file_path = 'todolist.txt'

# Leggiamo e stampiamo il contenuto attuale del file
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("Contenuto attuale del file:")
        print(content)
except FileNotFoundError:
    print("Il file non esiste o non è accessibile.")

# Indice dell'elemento da modificare (da input utente, ad esempio)
indice_da_modificare = int(input("Inserisci l'indice dell'elemento da modificare: "))

# Nuovo testo per l'elemento modificato
nuovo_testo = input("Inserisci il nuovo testo per l'elemento: ")

# Leggi il file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Modifica l'elemento basato sull'indice specificato
if 1 <= indice_da_modificare <= len(lines):
    lines[indice_da_modificare - 1] = f"{indice_da_modificare}. {nuovo_testo}\n"

    # Sovrascrivi solo la riga modificata nel file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"Elemento con indice {indice_da_modificare} modificato correttamente.")
else:
    print("Indice non valido. Nessuna modifica effettuata.")
