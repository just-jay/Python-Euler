def coll(n):
	chainLength = 1
	while n != 1:
		chainLength += 1
		if n % 2 == 0:
			n = n // 2
		else:
			n = (3*n) + 1
	return chainLength

longestChainLength = 0
start = 0

#takes ~1 minute to run 
for i in range(1, 1000001):
	temp = coll(i)
	if temp > longestChainLength:
		longestChainLength = temp
		start = i

print(start)