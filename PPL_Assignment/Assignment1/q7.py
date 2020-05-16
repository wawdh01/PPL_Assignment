x = int (input("Enter Lower Bound:"))
y = int (input("Enter Upper Bound:"))
b = []
total = 0
for i in range (x, y, 1):
	j = i
	while j != 0:
		rem = j % 10
		j = j // 10
		total += rem ** 3
	if (total == i):
		b.append (i)
	total = 0
print ("The amstrong number's are:")
print (b)
