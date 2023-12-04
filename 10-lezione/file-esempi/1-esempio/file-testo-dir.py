import os

# Il modulo os in Python fornisce funzioni per l'interazione con il sistema operativo. Questo modulo consente di eseguire molte operazioni che coinvolgono file, directory, processi, variabili d'ambiente e altro ancora.

# Ottieni il percorso assoluto dello script
script_path = os.path.abspath(__file__)  # Percorso assoluto dello script corrente
script_dir = os.path.dirname(script_path)  # Directory dello script corrente
print("dir", script_dir)

# Imposta la directory di lavoro nella directory dello script
os.chdir(script_dir)
print(os.getcwd())  # getcwd restituisce il percorso della directory di lavoro corrente -Verifica la directory di lavoro

# Prova ad aprire il file 'testo.txt' nella directory corrente
file_path = 'testo.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        num_words = len(words)
        print(f"Il numero di parole nel file '{file_path}' è: {num_words}")
except FileNotFoundError:
    print(f"File '{file_path}' non trovato.")