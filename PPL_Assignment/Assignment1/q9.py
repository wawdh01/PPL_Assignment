s = 1.0
count = 0
i = 1
c = 0
while 1:
	for j in range (1, int (i / 2) + 1):
		if ( i % j == 0):
			f =  1.0 / j
			s = s + f
			c += 1
	if (s != 0):
		t = c / s
		while t > 0:
			t = t - 1
		if (t == 0):
			print (i)
			count += 1
	if (count == 10):
		break;
	i += 1
	
