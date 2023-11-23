# def celsius_fahrenheit(celsius):
#     return celsius * 9/5 + 32 

# t_celsius = float(input("Inserisci la temperatura in gradi Celsius: "))

# t_fahrenheit = celsius_fahrenheit(t_celsius)

# print(f"{t_celsius} gradi Celsius corrispondono a {t_fahrenheit:.2f} gradi Fahrenheit.")

# #funzione anonima, lambda

# celsius_fahrenheit = lambda celsius: celsius * 9/5 + 32

#lambda
# def saluta():
#     print("hello")

# saluta = lambda: "Hello" 
# print(saluta())

# def somma(a,b):
#     return a + b

# somma = lambda a,b: a + b

#map
# numeri = [1,2,3,4,5]
# quadrati = map(lambda x: x * x, numeri)
# print(list(quadrati))

#filter
numeri = [1,2,3,4,5]
pari = filter(lambda x: x % 2 == 0, numeri)
print(list(pari))