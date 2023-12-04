"""
I file CSV (Comma-Separated Values) vengono utilizzati per memorizzare dati in forma tabellare, dove ciascuna riga del file rappresenta una riga della tabella e le colonne sono separate da delimitatori, spesso una virgola (da cui deriva il nome "Comma-Separated Values").
Inoltre sono ampiamente utilizzati per lo scambio di dati tra diverse applicazioni o sistemi. 
"""

import csv, os

script_path = os.path.abspath(__file__)  
script_dir = os.path.dirname(script_path)  
os.chdir(script_dir)

file_path = 'dati.csv'

# Dati da scrivere nel file CSV
data = [
    ['Nome', 'Cognome', 'Età'],
    ['Pippo', 'Rossi', 28],
    ['Pluto', 'Verdi', 35],
    ['Paperino', 'Bianchi', 22]
]

# Scrivi i dati nel file CSV
with open(file_path, mode='w', newline='', encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("File CSV creato con successo.")

"""
Quando si scrivono file CSV in modalità testuale, specialmente su sistemi Windows, il controllo della nuova riga (newline) può comportarsi in modo diverso a seconda del sistema operativo.
Specificare newline='' quando si apre un file in modalità scrittura evita il comportamento predefinito della gestione delle nuove righe da parte del sistema operativo, garantendo che Python gestisca direttamente la creazione di nuove righe. 
"""

# Leggi i dati dal file CSV
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

