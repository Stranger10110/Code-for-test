from sys import argv
with open(str(argv[1])) as file:
	c = 0
	for line in file:
		c += 1
print(c)
