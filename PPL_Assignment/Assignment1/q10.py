a = int (input("Enter First Number:"))
r = int (input("Enter Commom Ratio:"))
b = []
for i in range (1, 11):
	b.append (a * ( r ** (i - 1)))
print('The first 10 numbers of a Geometric Progression:')
print(b)
