input_file = open('20.input.txt', 'r')

input_lines = [x.strip() for x in input_file.readlines()]

tiles = {}

def parse_title(text):
    return int(text[5:-1])

def parse_tile(i):
    id = parse_title(input_lines[i])
    tile = []
    idx = i + 1
    while idx < len(input_lines) and input_lines[idx] != "":
        tile.append(input_lines[idx])
        idx += 1
    tiles[id] = tile
    return idx + 1

def find_borders(tile):
    borders = []
    borders.append(tile[0])
    borders.append(tile[0][::-1])
    borders.append(tile[-1])
    borders.append(tile[-1][::-1])
    left = ''.join([x[0] for x in tile])
    right = ''.join([x[-1] for x in tile])
    borders.append(left)
    borders.append(left[::-1])
    borders.append(right)
    borders.append(right[::-1])
    return borders

i = 0
while i < len(input_lines):
    i = parse_tile(i)

matches = {}
for t1 in tiles:
    matches[t1] = []
    for t2 in tiles:
        if t1 == t2:
            continue
        if any([b1 == b2 for b1 in find_borders(tiles[t1]) for b2 in find_borders(tiles[t2])]):
            matches[t1].append(t2)


res = 1
corner = 0
for m in matches:
    if len(matches[m]) == 2:
        print("Found: {}".format(m))
        res *= m
        corner = m

print(res)

def rotate_left(image):
    rotated = []
    for i in range(-1, -len(image[0])):
        rotated.append(''.join([r[i] for r in image]))
    return rotated

def flip_vertical(image):
    return [r[::-1] for r in image]

def matches_right(im_l, im_r):
    right_border = rotate_left(im_l)[0]
    left_border = rotate_left(im_r)[-1][::-1]
    return right_border == left_border

def matches_bot(im_t, im_b):
    return im_t[-1] == im_b[0]


