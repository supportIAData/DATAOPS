import numpy as np

prices = np.array([82, 92, 89, 65, 77, 66, 69, 65, 79, 51], dtype="float64")

mask = prices % 2 == 0
# on a une fonction qui permet de faire la même chose
# np.where( prices % 2, 0 )

print(mask)

prices[mask] = prices[mask] * 1.1

print(prices)

"""
Ajoutez +100 à toutes les valeurs comprises entre 60 et 80 strictement 
Attention l'opérateur ET avec un mask en Numpy est & 
"""
# Attention à la syntaxe tout est codé en C donc les opérateurs et les parenthèses sont nécessaires pour créer l'assertion
mask = (prices > 60) & (prices < 80)
print(mask)

prices[mask] += 100

print(prices) 