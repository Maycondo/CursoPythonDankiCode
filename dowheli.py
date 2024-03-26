

"""

do while

"""

palpite = 0
numero = 9


while True: # Nós executamos sem verificar
   print("Qual o numero correto? ")
   palpite = int(input(""))
   if palpite == numero: # Estamos verificando o nosso codigo
     print("Parabens voce acertou")
     break
   else:
      print("Errado, tente novamente")

