"""Scrivere all'inizio di un file senza sovrascrivere il contenuto esistente:
"""

import os

script_path = os.path.abspath(__file__)  
script_dir = os.path.dirname(script_path)  
os.chdir(script_dir)

file_path = 'todolist.txt'

with open(file_path, 'r+') as file:
    content = file.read()
    file.seek(0,0)  # Sposta il puntatore all'inizio del file senza cancellare il contenuto
    file.write("La mia todolist\n" + content)  # Scrive il nuovo contenuto all'inizio



"""Sintassi di seek():
Il metodo seek() accetta due parametri:

offset: Indica il numero di byte da spostare. Se l'offset è positivo, il puntatore si muoverà in avanti; se è negativo, si muoverà all'indietro. L'offset può essere omesso, in tal caso sarà 0 (sposta il puntatore all'inizio o alla fine del file).

from_what (opzionale): Specifica il punto di riferimento da cui iniziare il posizionamento del puntatore. I valori possibili sono:

0 (predefinito): dal punto di inizio del file
1: dal punto corrente nel file
2: dalla fine del file

file.seek(0, 2)  # Sposta il puntatore alla fine del file

"""