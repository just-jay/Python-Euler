sumOfSquares = 0
for i in range(101):
	sumOfSquares += (i ** 2)

squareOfSums = ((100 * 101 ) // 2) ** 2

print(squareOfSums - sumOfSquares)