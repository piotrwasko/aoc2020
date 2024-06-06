
test = [0, 3, 6]
data = [2,20,0,4,1,17]

input = data

last_occurence = {}

for i, v in enumerate(input):
    last_occurence[v] = i

turn = len(input)
last_number = input[-1]

while turn < 30000000:
    if last_number in last_occurence:
        new_number = turn - last_occurence[last_number] - 1
    else:
        new_number = 0
    last_occurence[last_number] = turn - 1
    last_number = new_number
    turn += 1
    # print(new_number)

print(last_number)
