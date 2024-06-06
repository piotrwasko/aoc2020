import string

input_file = open('6.input.txt' , 'r')

input_lines = input_file.readlines()

def read_groups(lines):
    groups = []
    group = []
    for l in lines:
        if l.strip() == "":
            groups.append(group)
            group = []
        else:
            group.append(l)
    groups.append(group)
    return groups

input = read_groups(input_lines)


counts = 0

for g in input:
    answers = reduce(lambda acc, v: acc.intersection(set(list(v.strip()))), g, set(list(string.ascii_lowercase)))
    print(answers)
    counts += len(answers)

print(counts)
