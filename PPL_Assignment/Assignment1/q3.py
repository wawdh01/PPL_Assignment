path = '/etc/hosts'
redirect = "127.0.0.1"
x = input('Enter the website:')
y = int(input("Enter 0 to block or 1 to unblock:"))
if (y == 0):
	with open(path, 'r+') as file:
		content = file.read()
		if x in content:
			pass
		else:
			file.write(redirect + " " + x + "\n")
else:
	with open(path, 'r+') as file:
		content = file.readlines()
		file.seek(0)
		for line in content:
			if not any (x in line for x in x):
				file.write(line)
		file.truncate()
