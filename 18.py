with open("18input.txt") as file:

	prevRow = []
	for line in file:
		l = line.strip().split(" ")
		
		if len(l) == 1: #initialize first row 
			prevRow = [int(l[0])]
		else:	
			newRow = []
			for i in range(len(l)):
				curr = int(l[i])
				if i == 0:
					newRow.append(prevRow[0] + curr)
				elif i == len(l) - 1:
					newRow.append(prevRow[-1] + curr)					
				else:
					newRow.append(max(prevRow[i-1],prevRow[i]) + curr)
			prevRow = newRow

	print(max(prevRow)) 

'''
dynamic programming approach 

only need to store previous row
edges of triangle will be the current val plus parent
internal elements of triangle will be current val plus max of the two parents
'''