# def saluta():
#     print("ciao a tutti")

# saluta()

# def saluta():
#     saluto = "ciao"
#     return saluto

# saluto = saluta()
# print(saluto)

#passaggio di parametri

def saluta(saluto): #sto passando un parametro formale
    print(saluto)

saluta("ciao") #sto passando un argomento ovvero un parametro attuale
saluta("ciao a tutti") #sto passando un argomento ovvero un parametro attuale

#sto passando un oggetto mutabile come la lista
def modifica_lista(lista):
    lista.append(4)

nums = [2,4,5]
modifica_lista(nums)
print(nums) #abbiamo modificato la lista originale

#sto passando un oggetto immutabile come un intero
def incrementa(numero):
    numero += 10
    return numero

val = 5
num = incrementa(val)
print(val)
print(num)
