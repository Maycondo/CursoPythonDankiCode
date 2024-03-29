
"""numerint = 5
def reduzriNumero(numerint):   
   while numerint > 0:
     print(numerint)
     numerint -= 1


reduzriNumero(5)
"""


"""def reduzriNumero(numeroInt):   
   if numeroInt > 0:
      
      reduzriNumero(numeroInt - 1)


reduzriNumero(5)"""



def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial


print(fatorialS(4))


def fatorialR(numero):
    if numero == 0:
        fatorialR = 1
    else:
        fatorialR(numero - 1)