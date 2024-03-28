
conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}
 
# utilizado para uni os conjuntos
"""
conjunto3 = conjunto1.union(conjunto2)
print("Conjunto União: ", conjunto3)
"""

conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)