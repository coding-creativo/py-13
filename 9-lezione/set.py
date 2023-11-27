
#pangramma
def is_pangram(frase):
    alfabeto = set('abcdefghilmnopqrstuvz')
    print("alfabeto", alfabeto)
    frase = set(frase.lower()) 
    print("frase", frase)
    
    return alfabeto.issubset(frase)

frase_da_verificare = 'Il coding ha vero fascino, grazie a quanto buon impegno'
risultato = is_pangram(frase_da_verificare)

if risultato:
    print(f"'{frase_da_verificare}' è un pangramma.")
else:
    print(f"'{frase_da_verificare}' non è un pangramma.")

