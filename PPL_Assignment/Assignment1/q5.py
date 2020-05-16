b = [1,2,23,15,16,10,20]
flag = 0
c = []
for i in range (1,26):
	for k in b :
		if (i == k):
			flag = 1
			break
	if (flag == 1):
		flag = 0
	else:
		c.append(i)
print('the missing page numbers are:')
print(c)
