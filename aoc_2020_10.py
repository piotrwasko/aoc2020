input_file = open('10.input.txt', 'r')

input = map(lambda x: int(x), input_file.readlines())

input.sort()

print(input)
diff = [input[0] - 0]

for i in range(len(input) - 1):
    diff.append(input[i + 1] - input[i])

diff.append(3)
print(len(input))
print(len(diff))
print(diff)
print(diff.count(1) * diff.count(3))

ways_to_get = [0] * len(input)

input_t = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
input_t.sort()

def find_ways_t(idx, val, curr):
    i = idx
    while i < len(input_t) and val + 3 >= input_t[i]:
        ways_to_get[i] += curr
        i += 1

find_ways_t(0, 0, 1)

for i in range(len(input_t) - 2):
    find_ways_t(i + 1, input_t[i], ways_to_get[i])

print(ways_to_get)

# Tu cos nie dziala... wynik to suma dwoch ostatnich (?)
# Juz dziala. Jakis glupi blad na indeksach :/
ways_to_get = [0] * len(input)
def find_ways(idx, val, curr):
    i = idx
    while i < len(input) and val + 3 >= input[i]:
        ways_to_get[i] += curr
        i += 1

find_ways(0, 0, 1)

for i in range(len(input) - 1):
    find_ways(i + 1, input[i], ways_to_get[i])

print(ways_to_get)

print(sum(ways_to_get[-3:]))
