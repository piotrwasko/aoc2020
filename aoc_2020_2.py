import re

inputFile = open('./2.input.txt', 'r')
input = inputFile.readlines()

count = 0

def task_one_policy(min, max, letter, password):
	return min <= password.count(letter) <= max

def task_two_policy(first, second, letter, password):
	return (password[first - 1] == letter) != (password[second - 1] == letter) 

for l in input:
	print(l)
	match = re.search(r"(\d+)-(\d+) (\w): (\w*)", l)
	min = int(match.group(1))
	max = int(match.group(2))
	letter = match.group(3)
	password = match.group(4)
	if task_two_policy(min, max, letter, password):
		count += 1

print(count)
