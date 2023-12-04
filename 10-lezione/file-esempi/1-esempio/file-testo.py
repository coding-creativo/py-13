"""
 Se il percorso specificato è solo il nome del file senza specificare il percorso della cartella, Python cercherà il file nella directory di lavoro corrente.

Se lo script 'file-testo.py' e il file di testo 'testo.txt' si trovano nella stessa cartella "file-esempi", ma lo script viene eseguito da un'altra posizione, potrebbe non trovare correttamente il file.

Per garantire che il file di testo venga aperto correttamente, puoi modificare il percorso di apertura in modo da includere il percorso completo della cartella in cui si trova lo script. """

# file_path = __file__

# print(f"Il percorso assoluto del file corrente è:")
# print(file_path)

# Prova ad aprire il file 'testo.txt' nella directory corrente
file_da_leggere = 'testo.txt'

try:
    with open(file_da_leggere, 'r') as file:
        content = file.read()
        words = content.split()

        print("Le parole nel file sono:")
        for word in words:
            print(word)

        num_words = len(words)
        print(f"Il numero di parole nel file '{file_da_leggere}' è: {num_words}")
except FileNotFoundError:
    print(f"File '{file_da_leggere}' non trovato.")