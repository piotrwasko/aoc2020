import re

input_file = open('7.input.txt', 'r');

input = input_file.readlines()

graph = {}
graph_contains = {}

BAG_PATTERN = re.compile("(\d+) ([^\d]*) bags?")
EMPTY_BAG_PATTERN = re.compile("no other bags.")

empty_bags = []
for l in input:
    [bag, children_str] = l.split(" bags contain ")
    empty_match = EMPTY_BAG_PATTERN.match(children_str)
    if empty_match:
        empty_bags.append(bag)
    else:
        children = BAG_PATTERN.findall(children_str)
        for ch in children:
            if ch[1] not in graph:
                graph[ch[1]] = []
            graph[ch[1]].append((ch[0], bag))
        graph_contains[bag] = children


print(graph)

START_BAG = 'shiny gold'

visited = []
to_visit = [START_BAG]

while len(to_visit) > 0:
    bag = to_visit.pop(0)
    if bag in visited:
        continue
    visited.append(bag)
    if bag in graph:
        for b in graph[bag]:
            to_visit.append(b[1])

print(visited)
print(len(visited))

bags_inside = {}


print(graph_contains)
def count_bags(bag):
    if bag not in graph_contains:
        return 1
    print(bag, sum(map(lambda x: int(x[0]) * count_bags(x[1]), graph_contains[bag])))
    return 1 +  sum(map(lambda x: int(x[0]) * count_bags(x[1]), graph_contains[bag]))
      
print(count_bags(START_BAG)) 
