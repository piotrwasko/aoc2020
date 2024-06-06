input_file = open('12.input.txt', 'r')

input = map(lambda x: (x[0], int(x[1:].strip())), input_file.readlines())

print(input)

wp_x = 10
wp_y = 1
pos_x = 0
pos_y = 0
direction = 0
dirs = ['E', 'S', 'W', 'N']

def rotate_l():
    global wp_x
    global wp_y
    (wp_x, wp_y) = (-wp_y, wp_x)

def rotate_r():
    global wp_x
    global wp_y
    (wp_x, wp_y) = (wp_y, -wp_x)

def move(cmd, val):
    print("{} {}".format(cmd, val))
    global pos_x
    global pos_y
    global wp_x
    global wp_y
    global direction
    if cmd == 'N':
        wp_y += val
    if cmd == 'S':
        wp_y -= val
    if cmd == 'E':
        wp_x += val
    if cmd == 'W':
        wp_x -= val
    if cmd == 'L':
        for i in range(val / 90):
            rotate_l()
    if cmd == 'R':
        for i in range(val / 90):
            rotate_r()
    if cmd == 'F':
        print("Moving by ({}, {}) from ({}, {}) {} times.".format(wp_x, wp_y, pos_x, pos_y, val)) 
        pos_y += wp_y * val
        pos_x += wp_x * val


for c in input:
    move(c[0], c[1])

print("x: {}, y: {}, md: {}".format(pos_x, pos_y, abs(pos_x) + abs(pos_y)))
