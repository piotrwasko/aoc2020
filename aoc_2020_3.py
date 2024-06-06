file = open('3.input.txt', 'r')
input = file.readlines()

def count_trees(down, right):
	trees = 0
	position = right

	for l in input[down::down]:
#		print(str(position) + ": " + l + " (" + str(len(l)))
		if l[position] == '#':
			trees += 1
		position = (position + right) % (len(l) - 1)
	print(str(down) + ", " + str(right) + ": " + str(trees))
	return trees


print(count_trees(1, 1) * count_trees(1, 3) * count_trees(1, 5) * count_trees(1, 7) * count_trees(2, 1))
