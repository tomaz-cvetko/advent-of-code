import re


def get_input():
    f = open("input.txt")
    rules, my, nearby = f.read().strip().split("\n\n")
    f.close()
    rules = rules.split("\n")
    my = [int(x) for x in my.split("\n")[1].split(",")]
    nearby = [[int(x) for x in s.split(",")] for s in nearby.split("\n")[1:]]
    return rules, my, nearby


def parse_rules(rules):
    temp = {}
    for rule in rules:
        # print(rule)
        m = re.match(r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$", rule).groups()
        temp[m[0]] = ((int(m[1]), int(m[2])), (int(m[3]), int(m[4])))
    return temp


def check(val, rule):
    (m1, M1), (m2, M2) = rule
    if m1 <= val <= M1 or m2 <= val <= M2:
        return True
    else:
        return False

def valid_in_any_field(val, rules):
    # for (m1, M1), (m2, M2) in rules.values():
    for rule in rules.values():
        # if m1 <= val <= M1 or m2 <= val <= M2:
        if check(val, rule):
            return True
    return False


def valid(ticket, rules):
    for num in ticket:
        if not valid_in_any_field(num, rules):
            return False
    return True


def applies(rule, pos, tickets):
    for t in tickets:
        if not check(t[pos], rule):
            return False
    return True
    

def solve_first():
    rules, my, nearby = get_input()
    rules = parse_rules(rules)

    suma = 0
    for ticket in nearby:
        for num in ticket:
            if not valid_in_any_field(num, rules):
                suma += num
    return suma


def solve_second():
    rules, my, nearby = get_input()
    rules = parse_rules(rules)
    nearby = [ticket for ticket in nearby if valid(ticket, rules)]
    
    # print(rules)
    # print(my)
    # print(nearby)
    
    # pos = {name:[] for name in rules.keys()}
    possible = {i:set() for i in range(len(nearby[0]))}
    for i in range(len(nearby[0])):
        for name, rule in rules.items():
            if applies(rule, i, nearby):
                # pos[name].append(i)
                possible[i].add(name)
            else:
                continue
    # print(pos)
    # print(possible)
    fields = {}
    while possible:
        for key, val in possible.items():
            if len(val) == 1:
                name = val.pop()
                fields[key] = name # save it in the bijection dict
                for other in possible.values():
                    if name in other:
                        other.remove(name)  # we already used the rule, it's not possible for others
                break
        del possible[key]  # done with this one
    print(fields)

    prod = 1
    for idx, name in fields.items():
        if name.count("departure") > 0:
            prod *= my[idx]
    
    return prod

if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())