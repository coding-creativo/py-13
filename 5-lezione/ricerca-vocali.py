user_input = input("Digita una frase per ottenere il numero di vocali al suo interno: ")

vocali = 'aeiou'
counter = 0

for char in user_input:
    if char.lower() in vocali:
        counter += 1

print(f'La frase da te inserita contiene {counter} vocali')
