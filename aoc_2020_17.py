import string

input_file = open('17.test.input.txt', 'r')

layers = []

layers.append([[[x for x in l.strip()] for l in input_file.readlines()]])

ITER = 2

def extend(layer):
    return [['.' for i in range(len(layer[0]) + 2)]] + [['.'] + l + ['.'] for l in layer] + [['.' for i in range(len(layer[0]) + 2)]]

def extend_layers(w):
    for i in range(len(layers[w])):
        layers[w][i] = extend(layers[w][i])
    layers[w].append(empty_layer(layers[w][0]))

def extend_cubes():
    for i in range(len(layers)):
        extend_layers(i)

def empty_layer(layer):
    return [['.' for i in range(len(layer))] for j in range(len(layer[0]))]

def empty_cube():
    return [empty_layer(l) for l in layers[0]]

def empty_state():
    return [empty_cube() for c in layers]

def is_active(x, y, neg_z, neg_w):
    w = abs(neg_w)
    z = abs(neg_z)
    if w < len(layers) and z < len(layers[w]) and 0 <= y < len(layers[w][z]) and 0 <= x < len(layers[w][z][y]):
        return layers[w][z][y][x] == '#'
    return False

def neighbours_active(x, y, z, w):
    active = 0
    for p in [-1, 0, 1]:
        for q in [-1, 0, 1]:
            for r in [-1, 0, 1]:
                for s in [-1, 0, 1]:
                    if p == q == r == s == 0:
                        continue
                    if is_active(x + p, y + q, z + r, w + s):
                        active += 1
    return active

def update_cell(x, y, z, w):
    n = neighbours_active(x, y, z, w)
    if layers[w][z][y][x] == '#':
        if n == 2 or n == 3:
            return '#'
        else:
            return '.'
    else:
        if n == 3:
            return '#'
    return '.'

def print_state(state):
    for i, c in enumerate(state):
        for idx, l in enumerate(c):
            print("z = {}, w = {}".format(idx, i))
            for r in l:
                print(string.join(r))
    print("")

print_state(layers)

for iter in range(ITER):
    extend_cubes()
    layers.append(empty_cube())
    new_state = empty_state()
    for w in range(len(layers)):
        for z in range(len(layers[w])):
            for y in range(len(layers[w][z])):
                for x in range(len(layers[w][z][y])):
                    new_state[w][z][y][x] = update_cell(x, y, z, w)
    print_state(new_state)
    layers = new_state
        
total = 0

def sum_layer(layer):
    s = 0
    for r in layer:
        s += r.count('#')
    return s

def sum_cube(cube):
    s = sum_layer(cube[0])
    for l in cube[1:]:
        s += (sum_layer(l) * 2)
    return s


total += sum_cube(layers[0])

for c in layers[1:]:
    total += (sum_cube(c) * 2)

print(total)
