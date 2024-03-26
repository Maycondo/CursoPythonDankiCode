"""
como achar o fatorial de um numero 
"""

numero = int(input("Digite um número: "))
fatorial = 1

if numero < 0:
    print("Nao existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatorial de {numero} eh 1")
else:
    for i in range(1 , numero+1):
       fatorial = fatorial * i
       print(fatorial)
    print(f"O fatorial de {numero} é {fatorial}") 