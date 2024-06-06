import re

input_file = open('4.input.txt', 'r')

def read_values(line):
    vals = {}
    for val in line.split(" "):
        [k, v] = val.split(":")
        vals[k] = v
    return vals

def read_passports(lines):
    passports = []
    passport = {}
    for x in lines:
        if x.strip() == "":
            passports.append(passport)
            passport = {}
        else:
            passport.update(read_values(x.strip()))
    passports.append(passport)
    return passports

input = read_passports(input_file.readlines())

FIELDS = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": lambda v: 150 <= int(v[:-2]) <= 193 if v[-2:] == "cm" else (59 <= int(v[:-2]) <= 76 if v[-2:] == "in" else False),
    "hcl": lambda v: re.match(r"^#[0-9a-f]{6}$", v) != None,
    "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda v: re.match(r"^[0-9]{9}$", v) != None
}

print(map(lambda p: all(map(lambda f: f in p, FIELDS)), input).count(True))

def is_valid(passport):
  k = passport.keys()
  k.sort()
  for f in FIELDS.keys():
    if not f in passport or not FIELDS[f](passport[f]):
        print("Invalid:  " + f + ": " + (passport[f] if f in passport else "missing"))
        return False
  return True

print(len(filter(is_valid, input)))

