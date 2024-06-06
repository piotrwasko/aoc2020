input_file = open('13.input.txt', 'r')

input = [x.strip() for x in input_file.readlines()]

time = int(input[0])
buses = [x for x in filter(lambda c: True, input[1].split(","))]

earliest_dep = time + 100000
earliest_bus = 0

for bus in buses:
    if bus == 'x':
        continue
    bus = int(bus)
    time_since_last_dep = time % bus
    dep = bus - time_since_last_dep
    if dep < earliest_dep:
        earliest_dep = dep
        earliest_bus = bus

print(earliest_dep)
print(earliest_bus)
print(earliest_dep * earliest_bus)


current = int(buses[0])
ans = 0

for i in range(1, len(buses)):
    if buses[i] == 'x':
        continue
    bus = int(buses[i])
    z = 1
    while not (ans + current * z) % bus == bus - (i % bus):
#        print("Checking: {}, rest = {}".format((ans + current * z), (ans + current * z) % bus))
        z += 1
    ans = ans + current * z
    current = current * bus
    print("For {} ans is {}".format(bus, ans))

print(ans) 
for i in range(len(buses)):
    print("bus {} ({}) departs at {}? {}".format(buses[i], i, ans + i, 0 if buses[i] == 'x' else ans % int(buses[i])))
