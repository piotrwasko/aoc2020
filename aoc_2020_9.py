input_file = open('9.input.txt')

lines = map(lambda x: int(x), input_file.readlines())
total_sums = [lines[0]]
for i in range(1, len(lines) - 1):
    total_sums.append(total_sums[i - 1] + lines[i])

def find_number():
    for i in range(25, len(lines) - 1):
        n = lines[i]
        prev = lines[i - 25:i]
        sums = [x + y for x in prev for y in prev]
        if n not in sums:
            print(str(n))
            return n


num = find_number()
i = 1
j = 1
while not total_sums[j] - total_sums[i - 1] == num:
    s = total_sums[j] - total_sums[i - 1]
    if s < num:
        j += 1
    elif s > num:
        i += 1
    else:
        print("Error")
        break

print(str(max(lines[i:j+1]) + min(lines[i:j+1])))
