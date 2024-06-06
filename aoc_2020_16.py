import re

input_file = open('16.input.txt', 'r')

input_lines = input_file.readlines()

rules = {}
my_ticket = []
tickets = []

def rule(a, b, c, d):
    return lambda x: a <= x <= b or c <= x <= d

RULE_PATTERN = re.compile("(.*): (\d+)-(\d+) or (\d+)-(\d+)")
def add_rule(line):
    match = RULE_PATTERN.match(line)
    rules[match.group(1)] = rule(int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)))



stage = 0

for line in input_lines:
    if line.strip() == "":
        stage += 1
        continue
    if stage == 0:
        add_rule(line)
    if stage == 1 or stage == 3:
        stage += 1
        continue
    if stage == 2:
        my_ticket = map(lambda x: int(x), line.strip().split(","))
    if stage == 4:
        tickets.append(map(lambda x: int(x), line.strip().split(",")))


def number_valid(num):
    return any([rule(num) for rule in rules.values()])


invalid_sum = 0
for ticket in tickets:
    for num in ticket:
        if not number_valid(num):
            invalid_sum += num


def ticket_valid(ticket):
    return all([number_valid(num) for num in ticket])

valid_tickets = filter(ticket_valid, tickets)

possible_positions = {}

for f in rules.keys():
    possible_positions[f] = [x for x in range(0, len(rules.keys()))]

for t in valid_tickets:
    for i in range(len(t)):
        for field, rule in rules.items():
            if not rule(t[i]):
                possible_positions[field].remove(i)

for x in range(20):
    for field in possible_positions.keys():
        if len(possible_positions[field]) == 1:
            for f, p in possible_positions.items():
                if not f == field and possible_positions[field][0] in p:
                    p.remove(possible_positions[field][0])

my_ticket_sum = 1

print(possible_positions)
print(my_ticket)

for field, pos in possible_positions.items():
    if field[:9] == "departure":
        print("Summing {}: {}".format(field, my_ticket[pos[0]]))
        my_ticket_sum *= my_ticket[pos[0]]

print(my_ticket_sum)
