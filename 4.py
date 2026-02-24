def isPalindrome(n):
	s = str(n)

	i = 0 
	j = len(s) - 1 

	while i < j:
		if s[i] != s[j]:
			return False
		i += 1
		j -= 1
	return True


best = 0
for i in range(100,1000):
	for j in range(100,1000):
		temp = i * j 
		if isPalindrome(temp) and temp > best:
			best = temp

print(best)