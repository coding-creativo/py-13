import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)  

os.chdir(script_dir)

file_path = 'my_file.txt' 

# Contenuto da scrivere nel nuovo file
contenuto = """\
Corso su Python
Lunedì e Giovedì
"""

# Crea il nuovo file e scrivi il contenuto
try:
    with open(file_path, 'w') as file:
        file.write(contenuto)
    print(f"Creato il file '{file_path}' con successo.")
except IOError:
    print("Errore durante la creazione del file.")
