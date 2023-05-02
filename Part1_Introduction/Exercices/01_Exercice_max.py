

def max_list(l):  
    m = l[0]
    for e in l[1:]:
         if e > m :
             m = e
             
    return m

l = [9,10, 7, 5, 76, 800, 11, 13]

print(max_list(l))

## Avec l'indice

def max_indice_list(l):
    # assignation par tuple
    m = l[0]
    i, j, m = 0, 0
    for e in l[1:]:
        j+=1
        if e > m :
             m, i = e, j
                 
    return m, i

print(max_indice_list(l))