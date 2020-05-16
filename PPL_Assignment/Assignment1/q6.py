def amicable (x):
	s = 0
	for i in range (1, x):
		if (x % i == 0):
			s += i
	y = s
	s = 0
	for i in range (1, y):
		if (y % i == 0):
			s += i
	if (s == x):
		global b
		b.append (y)
		b.append (x)
		print (x, y)
		return 1
	return 0
count = 0
i = 1
flag = 0
b = []
while 1:
	for j in b:
		if (j == i):
			flag = 1
	if (flag != 1):
		d = amicable (i)
	else:
		flag = 0
	if (d == 1):
		count += 1
	if (count == 10):
		break
	i += 1
