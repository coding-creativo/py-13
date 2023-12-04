"""
Possiamo indicare il percorso assoluto 

__file__: La variabile __file__ contiene il percorso del file Python corrente. Se lo script viene eseguito direttamente, __file__ conterrà il percorso assoluto del file. Se invece lo script è importato come modulo in un altro script, __file__ conterrà il percorso relativo al file."""

file_path = __file__
print(f"Il percorso assoluto del file corrente è:")
print(file_path)

# Aprire il file 'testo.txt' dal percorso assoluto
file_da_leggere = "D:/corsi/python-1/10lezione/spiegazione/file-esempi/1-esempio/testo.txt"

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