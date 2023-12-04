#*********aprire un file*********#
# Apre un file in modalità lettura
file = open('nome_file.txt', 'r')

# Apre un file in modalità scrittura
file = open('nome_file.txt', 'w')

# Apre un file in modalità append (aggiunge dati alla fine del file)
file = open('nome_file.txt', 'a')



#*********leggere da un file*********#
# Legge tutto il contenuto
content = file.read()

# Legge una singola riga
line = file.readline()

# Legge tutte le righe e memorizzarle in una lista
#Il risultato è una lista in cui ogni elemento corrisponde a una riga del file.
lines = file.readlines()


#*********scrivere nel file*********#
# Scrive nel file
file.write("Nuovo testo\n")


#chiudere un file
file.close()


#utilizzare with
"""L'istruzione with in Python viene utilizzata per gestire correttamente le risorse che devono essere aperte e poi chiuse dopo essere state utilizzate. 
L'utilizzo di un blocco with è consigliato per garantire la chiusura automatica di un file dopo l'utilizzo, anche in caso di eccezioni."""

with open('nome_file.txt', 'r') as file:
    # Operazioni sul file
    content = file.read()
    # Il file si chiude automaticamente alla fine del blocco "with"
