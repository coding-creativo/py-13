import os

script_path = os.path.abspath(__file__)  # Percorso assoluto dello script corrente
script_dir = os.path.dirname(script_path)  # Directory dello script corrente
os.chdir(script_dir)

file_path = 'todolist.txt'

# Leggiamo il file per estrarre l'ultimo indice utilizzato
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1] if lines else '0'  # In caso il file sia vuoto

        # Estraiamo l'ultimo numero dall'ultima riga
        last_number = int(last_line.split('.')[0])
except FileNotFoundError:
    # Se il file non esiste, inizia dall'elemento 1
    last_number = 0

num_elementi = int(input("Quanti elementi vuoi aggiungere alla todolist? "))

# Inizializzamo una lista vuota per contenere i nuovi elementi
# Apri il file in modalità append (aggiunta) e aggiungi i nuovi elementi
with open(file_path, 'a') as file:
    for i in range(num_elementi):
        elemento = input(f"Inserisci l'elemento {last_number + i + 1}: ")
        file.write(f"{last_number + i + 1}. {elemento}\n")
