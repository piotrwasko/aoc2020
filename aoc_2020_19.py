import string

input_file = open('19.input.txt', 'r')
input_lines = [x.strip() for x in input_file.readlines()]

rules = {}
words = []

stage = 0

def parse_rule(rule):
    return [[expr for expr in alt.strip().split(" ")] for alt in rule.split("|")]

def add_rule(rule):
    [rule_num, r] = rule.split(":")
    rules[rule_num] = parse_rule(r)    

for l in input_lines:
    if l == "":
        stage = 1
        continue
    if stage == 0:
        add_rule(l)
    else:
        words.append(l)

add_rule("8: 42 | 42 8")
add_rule("11: 42 31 | 42 11 31")
print(rules)

tabs = 0

def match_alt(alt, text):
    alt_i = 0
    text_i = 0
    while alt_i < len(alt) and text_i < len(text):
        if alt[alt_i][0] == '"':
            if not text[text_i] == alt[alt_i][1]:
                return (False, 0)
            alt_i += 1
            text_i += 1
        else:
            (res, t_mod_i) = match_rule(alt[alt_i], text[text_i:])
            if not res:
                return (False, 0)
            alt_i += 1
            text_i += t_mod_i
    if alt_i == len(alt):
        return (True, text_i)
    else:
        return(False, 0)
    

def match_rule(rule_num, text):
    global tabs
    tabs += 1
    print("{}matching rule {} for {}".format('\t' * tabs, rule_num, text))
    for alt in rules[rule_num]:
        (res, text_i) = match_alt(alt, text)
        if res:
            print("{}rule {} OK - {}".format('\t' * tabs, rule_num, text_i))
            tabs -= 1
            return (res, text_i)
    tabs -= 1
    return (False, 0)

all_words = {}

keys = rules.keys()
keys.remove("8")
keys.remove("11")
keys.remove("0")

def concat_all(l_words):
    if len(l_words) == 1:
        return l_words[0]
    return [x + w for x in l_words[0] for w in concat_all(l_words[1:])] 

def expand(rule_num):
    res = []
    for alt in rules[rule_num]:
        res.append(concat_all([all_words[k] for k in alt]))
    return [x for y in res for x in y]

while not all(map(lambda k: k in all_words, keys)):
    for k, alts in rules.items():
        if k in all_words:
            continue
        if alts[0][0][0] == '"':
            all_words[k] = [alts[0][0][1]]
        if all([alt_k in all_words for alt in alts for alt_k in alt]):
            all_words[k] = expand(k)

print(all_words["42"])
print(all_words["31"])

def simple_expand(alt):
    return concat_all([all_words[k] for k in alt])

max_len = max([len(x) for x in words])

len42 = len(all_words["42"][0])
len31 = len(all_words["31"][0])

def match_42(word):
    if word[:len42] in all_words["42"]:
        if len(word) == len42:
            return True
        else:
            return match_42(word[len42:])
    return False

def match_word(word):
    if len(word) <= len42 + len31:
        return (match_42(word), False)
    if word[:len42] in all_words["42"] and word[-len31:] in all_words["31"]:
        return (match_word(word[len42:-len31])[0], True)
    rest_42 = match_42(word)
    if rest_42:
        return (True, False)
    return (False, False)

correct = 0
for w in words:
    if all(match_word(w)):
        correct += 1
    

print(correct)
