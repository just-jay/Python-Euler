def lattice(n):

	grid = [[0] * (n+1) for _ in range(n+1)]

	for i in range(n+1):
		grid[i][0] = 1
		grid[0][i] = 1

	for i in range(1,n+1):
		for j in range(1,n+1):
			grid[i][j] = grid[i-1][j] + grid[i][j-1]

	print(grid[n][n])


lattice(20)


'''
 _ _
|_|_|
|_|_|

._._.
| | |
._._.
| | |
._._.

[] [] []
[] [] []
[] [] [] 

dynamic programming 
each vertex is an item in a list 
the item stores how many paths pass through that vertex
top row and left column prepopulate with 1

recurrance: add i-1 and j-1 
return n,n

'''