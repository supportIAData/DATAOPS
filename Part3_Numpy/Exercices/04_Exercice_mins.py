import numpy as np

A = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 10, 69, 12]
])

# tous les mins par ligne
mins = A.min(1) 

# compteur enumerate donne un compteur 
res = [] 
# i indice et line une ligne de matrice 
for i, line in enumerate(A) :
    for pos, el in enumerate(line) :
        if el == mins[i]:
            res.append((pos, el))
            continue # on passe à l'itération suivante 

print(res)

# Avec la méthode where


mi=[]
for a in A:
    ind=np.where(a == min(a))[0][0]
    mi.append((ind,a[ind]))
 
print(mi)