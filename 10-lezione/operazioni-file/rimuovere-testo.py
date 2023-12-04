import os

script_path = os.path.abspath(__file__)  # Percorso assoluto dello script corrente
script_dir = os.path.dirname(script_path)  # Directory dello script corrente
os.chdir(script_dir)

file_path = 'todolist.txt'

# Indice dell'elemento da eliminare (da input utente, ad esempio)
indice_da_eliminare = int(input("Inserisci l'indice dell'elemento da eliminare: "))

# Leggi il file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Rimuovi l'elemento basato sull'indice specificato
if 1 <= indice_da_eliminare <= len(lines):
    del lines[indice_da_eliminare - 1]  # Sottrai 1 perché gli indici partono da 0 
    
    # Sovrascrivi il file con i contenuti aggiornati
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)
    print(f"Elemento con indice {indice_da_eliminare} eliminato correttamente.")
else:
    print("Indice non valido. Nessuna eliminazione effettuata.")
