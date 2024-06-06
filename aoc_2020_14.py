import re
input_file = open('14.input.txt', 'r')

input = input_file.readlines()

memory = {} 
mask_and = 0
mask_or = 0
mask_pattern = ""

def map_to_mask(mask):
    global mask_or
    global mask_and
    global mask_pattern
    mask_or = int(re.sub(r"X", "0", mask), 2)
    mask_and = int(re.sub(r"X", "1", mask), 2)
    mask_pattern = mask.strip()

def extend_with(b, arr):
    return [b + x for x in arr]

def gen_replaced(add, mask):
    if len(mask) == 1:
        if mask == "X":
            return ['0', '1']
        elif mask == "0":
            return [add[0]]
        else:
            return ['1']
    rest = gen_replaced(add[1:], mask[1:])
    if mask[0] == "X":
        return extend_with('0', rest) + extend_with('1', rest)
    elif mask[0] == "1":
        return extend_with('1', rest)
    else:
        return extend_with(add[0], rest)

def gen_addresses(address):
    a = "{0:036b}".format(address)
    print("mask: {} ({}), a: {}, ({})".format(mask_pattern, len(mask_pattern), a, len(a)))
    r = [int(x, 2) for x in gen_replaced(a, mask_pattern)]
    print(gen_replaced(a, mask_pattern))
    return r

COMMAND_PATTERN = re.compile("mem\[(\d+)\] = (\d+)")
for cmd in input:
    if cmd[:4] == "mask":
        map_to_mask(cmd[6:])
        continue
    match = COMMAND_PATTERN.match(cmd)
    address = int(match.group(1)) | mask_or
    for a in gen_addresses(address):
        memory[a] = int(match.group(2))

print(sum(memory.values()))

print(mask)
print(commands)
