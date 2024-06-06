import string

input_file = open('11.input.txt', 'r')

board = [l for l in [x.strip() for x in input_file.readlines()]]

def print_board(b):
    pass
    print('-' * 80)
    for r in b:
        print("|" + string.join(r) + "|")
    print('-' * 80)

def find_chair(x, y, x_dir, y_dir):
    (a, b) = (x + x_dir, y + y_dir)
    while len(board) > a >= 0 and len(board[a]) > b >= 0:
        if board[a][b] == '#':
            return 1
        elif board[a][b] == 'L':
            return 0
        (a, b) = (a + x_dir, b + y_dir)
    return 0
    

def adjacent_occupied(x, y):
    to_check = [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]]
    count = 0
    for (a, b) in to_check:
        if a == 0 and b == 0:
            continue
        count += find_chair(x, y, a, b)
    return count

def should_sit(x, y):
#    print("Should sit ({},{}) {}: {}".format(x, y, board[x][y], adjacent_occupied(x, y)))
    return (board[x][y] == 'L'
            and adjacent_occupied(x, y) == 0)

def should_empty(x, y):
    return (board[x][y] == '#'
            and adjacent_occupied(x, y) >= 5)

new_state = []
for i in range(len(board)):
    new_state.append(['.'] * len(board[i]))

print_board(board)
while True:
    for x in range(len(board)):
        for y in range(len(board[x])):
            if should_sit(x, y):
                new_state[x][y] = '#'
            elif should_empty(x, y):
                new_state[x][y] = 'L'
            else:
                new_state[x][y] = board[x][y]
    print_board(new_state)
    if str(board) == str(new_state):
        break
    board = new_state
    new_state = []
    for i in range(len(board)):
        new_state.append(['.'] * len(board[i]))

print(sum([s.count('#') for s in board]))
