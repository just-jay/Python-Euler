import math

for a in range(1,999):
	for b in range(2,1000):
		c = math.sqrt((a * a) + (b * b))
		if c % 1 == 0:
			c = int(c)
			if a + b + c == 1000:
				print(a*b*c)