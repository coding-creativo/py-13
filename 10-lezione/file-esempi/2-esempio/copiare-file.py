import os

script_path = os.path.abspath(__file__)  
script_dir = os.path.dirname(script_path)  
os.chdir(script_dir)

file_da_copiare = 'primo-file.txt'  # Specifica il file da copiare
nuovo_file = 'secondo-file.txt'  # Specifica il nuovo file di destinazione

# Leggi il contenuto dal file di origine e copialo nel nuovo file
with open(file_da_copiare, 'r') as file_origine:
    contenuto = file_origine.read()

    with open(nuovo_file, 'w') as file_destinazione:
        file_destinazione.write(contenuto)

print(f"File '{file_da_copiare}' copiato correttamente in '{nuovo_file}'.")
