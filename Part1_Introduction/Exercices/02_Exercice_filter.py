

def testFilter(l, test):
    
    for e in l:
        if test(e) == False :
            return False
        
    return True
        
        
l = ['A', 'B', 'C' , 'D']

print(  testFilter(l, lambda ch : ch.isupper() )  ) 


def testUpper(l):
    
    for e in l :
        if e.isupper() == False :
            return False 
        
    return True

print(testUpper(l))

l = [11, 12, 15, -4]

print( testFilter(l, lambda t : t > 0) )

m = [
     ['A', 'B', 'C' , 'D'],
     ['A', 'B', 'C' , 'D'],
     ['A', 'B', 'c' , 'D'],
     ['A', 'B', 'C' , 'D'],
     ['A', 'b', 'C' , 'D'],
     ['A', 'B', 'C' , 'D'],
]

sanitize = []

for e in m: 
    if testUpper(e):
        sanitize.append(e)
        
print(sanitize)