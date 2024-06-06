import re

input_file = open('8.input.txt', 'r')

input_lines = input_file.readlines()

def read_program(lines):
    return map(read_command, lines)

COMMAND_PATTERN = re.compile("(\w\w\w) ([+-]\d+)")
def read_command(line):
    match = COMMAND_PATTERN.match(line)
    return (match.group(1), int(match.group(2)))


ERROR = "ERROR"
LOOP = "LOOP"
TERMINATED = "TERMINATED"

current_line = 0
global_counter = 0
def execute_program(program):
    global current_line
    global global_counter
    current_line = 0
    global_counter = 0
  
    def update_line(arg):
        global current_line
        current_line += arg

    def update_counter(arg):
        global global_counter
        global_counter += arg
 
    def nop(arg):
        update_line(1)
        return True

    def acc(arg):
        update_counter(arg)
        update_line(1)
        return True

    def jmp(arg):
        update_line(arg)
        if current_line < 0 or current_line > len(program):
            print("Invalid jmp in line {}: {}".format(current_line - arg, arg))
            return False
        return True

    COMMANDS = {
        'nop': nop,
        'acc': acc,
        'jmp': jmp
    }

    def execute_command(command):
        cmd = command[0]
        arg = command[1]
        return COMMANDS[cmd](arg)

    executed_lines = []
    
    while True:
        if current_line in executed_lines:
#            print("Loop detected at {}".format(current_line))
            return (LOOP, global_counter)
        if current_line == len(program):
            return (TERMINATED, global_counter)
#        print("Current counter: {}".format(global_counter))
        executed_lines.append(current_line)
        result = execute_command(program[current_line])
        if not result:
            return (ERROR, global_counter)


program = read_program(input_lines)

for i in range(len(program)):
    new_program = program[:]
    if program[i][0] == 'nop':
        new_program[i] = ('jmp', program[i][1])
    elif program[i][0] == 'jmp':
        new_program[i] = ('nop', program[i][1])
    else:
        continue
    (result, counter) = execute_program(new_program)
    if result == TERMINATED:
        print("Terminated with counter: {}".format(counter))
        
