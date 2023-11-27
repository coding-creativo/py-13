from datetime import datetime

data_inizio = datetime(2023, 1, 1)
data_fine = datetime(2023, 12, 31)

differenza = data_fine - data_inizio
print("differenza", differenza)

numero_giorni = differenza.days

print(f"Numero di giorni tra le due date: {numero_giorni} giorni")


# from datetime import datetime
# data_corrente = datetime.now()

# print(data_corrente)

#stampare solo la data - date()
# solo_data = data_corrente.date()
# print(solo_data)

#stampare solo l'orario - time()
# solo_orario = data_corrente.time()
# print(solo_orario)

# orario_formattato = solo_orario.strftime("%H:%M:%S")
# print(orario_formattato)