matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

# Compréhension
print( list( zip(*matrix)  )) 

# méthode classique avec les compréhensions de liste
print([
   [ matrix[i][j] for i in range(0, len(matrix)) ] for j in range(0, len(matrix[0]))
])