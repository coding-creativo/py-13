stringa1 = "12345"  # Contiene solo cifre decimali
stringa2 = "-123"    # Non contiene solo cifre decimali
stringa3 = "½"     # Contiene una frazione
stringa4 = "IV"    # Contiene numeri romani
stringa5 = "123④"  # Contiene oltre alle cifre decimali comuni un simbolo di numero (④)

# Esempi con isnumeric()
print(stringa1.isnumeric())  # True
print(stringa2.isnumeric())  # False
print(stringa3.isnumeric())  # True
print(stringa4.isnumeric())  # False
print(stringa5.isnumeric())  # True

# Esempi con isdecimal()
print(stringa1.isdecimal())  # True
print(stringa2.isdecimal())  # False
print(stringa3.isdecimal())  # False
print(stringa4.isdecimal())  # False
print(stringa4.isdecimal())  # False

# Esempi con isdigit()
print(stringa1.isdigit())  # True
print(stringa2.isdigit())  # False 
print(stringa3.isdigit())  # False 
print(stringa4.isdigit())  # False 
print(stringa5.isdigit())  # True (accetta simboli numerici aggiuntivi)
