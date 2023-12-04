import os

# Ottieni il percorso assoluto dello script
script_path = os.path.abspath(__file__)  # Percorso assoluto dello script corrente
script_dir = os.path.dirname(script_path)  # Directory dello script corrente
print(script_dir)

# Imposta la directory di lavoro nella directory dello script
os.chdir(script_dir)

file_path = 'todolist.txt'

nuovi_elementi = []

# Chiediamo all'utente quanti elementi vuole inserire
num_elementi = int(input("Quanti elementi vuoi inserire nella todolist? "))

# inseriamo gli elementi in una lista
for i in range(num_elementi):
    elemento = input(f"Inserisci l'elemento {i + 1}: ")
    nuovi_elementi.append(f"{i + 1}. {elemento}")

# Aggiungi i nuovi elementi al file
with open(file_path, 'w') as file:
    for elemento in nuovi_elementi:
        file.write(elemento + '\n')
