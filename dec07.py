import re

def containing(color, rules):
    res = set()
    next_order = {o for o in rules if color in rules[o]}

    while next_order:
        res.update(next_order)

        next_order = {o for o in rules for c in next_order if c in rules[o] and o not in res}
    return res


def contents(color, qrules):
    def process_order(bags):
        new = set()
        num = 0
        for b in bags:
            for sub_b, q in qrules[b]:
                new.add(sub_b)
                num += q
        return num, new
    res = 0
    delta, next_order = process_order({color})
    res += delta
    while next_order:
        break


def r_contents(color, qrules):
    if qrules[color] is None:
        return 0
    else:
        cnt = 0
        for c, q in qrules[color]:
            cnt += q*(1 + r_contents(c, qrules))  # q-times the c-colored bag + q-times whatever the c-colored bag contains
        return cnt


def solve_first():
    rules = {}
    with open("input.txt") as f:
        for line in f:
            d = re.search('(?P<color>[a-z]+ [a-z]+) bags contain (?P<empty>no other bags.)?(?(empty)|(?P<cnt>(\d [a-z]+ [a-z]+ bags?,|.)+))', line).groupdict()
            # print(d)
            if d['empty'] is None:
                value = re.findall('\d ([a-z]+ [a-z]+) bags?', d['cnt'])
                rules[d['color']] = set(value)
            else:
                rules[d['color']] = set()
        print(rules)
        containers = containing('shiny gold', rules)
    return len(containers)


def solve_second():
    rules = {}
    with open("input.txt") as f:
        for line in f:
            d = re.search('(?P<color>[a-z]+ [a-z]+) bags contain (?P<empty>no other bags.)?(?(empty)|(?P<cnt>(\d [a-z]+ [a-z]+ bags?,|.)+))', line).groupdict()
            # print(d)
            if d['empty'] is None:
                value = re.findall('(\d) ([a-z]+ [a-z]+) bags?', d['cnt'])
                rules[d['color']] = {(color, int(q)) for q, color in value}
            else:
                rules[d['color']] = None
        for k, v in rules.items():
            print(k, v)
    return r_contents('shiny gold', rules)


if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())