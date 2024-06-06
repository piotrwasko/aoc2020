input_file = open('18.input.txt', 'r')

lines = [x.strip() for x in input_file.readlines()]

def parse_number(text, p):
    pos = p
    while pos < len(text) and text[pos].isdigit():
        pos += 1
    return (int(text[p:pos]), pos)

def plus(x, y):
    return x + y

def times(x, y):
    return x * y

def parse_operator(text, pos):
    if text[pos] == '+':
        return (plus, pos + 1)
    if text[pos] == '*':
        return (times, pos + 1) 
    raise Exception("Wrong operator")

def parse_parens(text, p):
    pos = p
    if text[pos] == '(':
        pos += 1
        while not text[pos] == ')':
            (exp, pos) = parse_expr(text, pos)
            
        return (exp, pos + 1)
    raise Exception("Wrong parens") 
        
def calc(exps):
    if len(exps) == 0:
        raise Exception("Empty calc")
    #print("calculating: {}".format(exps))
    for_add = []
    to_add = 0
    i = 0
    while i < len(exps):
        if exps[i] == "+":
            to_add += exps[i + 1]
            i = i + 2
            continue
        if exps[i] == "*":
            for_add.append(to_add)
            i = i + 1
            continue
        to_add = exps[i]
        i += 1
    for_add.append(to_add)
    return reduce(times, for_add, 1)   

LHS = 0
OP = 1
RHS = 2
RET = 3
EXP = 4

def parse_expr(text, p):
    pos = p
    mode = EXP
    exps = []
    while pos < len(text):
        #print("parsing pos {} in {}".format(pos, text))
        if text[pos] == '(':
            (exp, pos) = parse_parens(text, pos)
            exps.append(exp)
            mode = OP
            continue
        if text[pos] == ' ':
            pos += 1
            continue
        if text[pos].isdigit():
            (exp, pos) = parse_number(text, pos)
            exps.append(exp)
            mode = OP
            continue
        if text[pos] in ['+', '*'] and mode == OP:
            exps.append(text[pos])
            mode = EXP
            pos += 1
            continue
        return (calc(exps), pos)
    return (calc(exps), pos)

total = 0
for l in lines:
    res = parse_expr(l, 0)[0]
#    print("{} = {}".format(l, res))
    total += res

print(total)
