
"""numerint = 5
def reduzriNumero(numerint):   
   while numerint > 0:
     print(numerint)
     numerint -= 1


reduzriNumero(5)
"""


def reduzriNumero(numeroInt):   
   if numeroInt > 0:
      
      reduzriNumero(numeroInt - 1)


reduzriNumero(5)
