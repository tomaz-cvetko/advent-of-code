import re

req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # ignoring missing 'cid'


def required_fields(passport):
    return req.issubset(passport)


def input_to_dict(line):
    return dict([[x for x in entry.split(":")] for entry in line.strip().split()])

def validate(passport):  # assuming passport has all required fields
    byr = iyr = eyr = hgt = hcl = ecl = pid = cid = True
    if not (match := re.findall(r"^(?P<byr>(?:19|20)[0-9]{2})$", passport['byr'])) or not (1920 <= int(match[0]) <= 2002):
        print("BAD byr:", passport['byr'])
        byr = False
        # return False
    
    if not (match := re.findall(r"^(?P<iyr>(?:20)[0-9]{2})$", passport['iyr'])) or not (2010 <= int(match[0]) <= 2020):
        print("BAD iyr:", passport['iyr'])
        iyr = False
        # return False

    if not (match := re.findall(r"^(?P<eyr>(?:20)[0-9]{2})$", passport['eyr'])) or not (2020 <= int(match[0]) <= 2030):
        print("BAD eyr:", passport['eyr'])
        eyr = False
        # return False

    if (match := re.findall(r"^(?P<hgt>[0-9]{2,3})(?P<unt>cm|in)$", passport['hgt'])):
        val = int(match[0][0])
        unit = match[0][1]
        if (unit == 'cm' and not (150 <= val <= 193)) or (unit == 'in' and not (59 <= val <= 76)):
            print("BAD hgt:", passport['hgt'])
            hgt = False
            # return False
        elif unit != 'cm' and unit != 'in':
            print(val, unit, "this shouldn't happen!")
            hgt = False
            # return False
        # else height is ok
    else:
        print("BAD hgt:", passport['hgt'])
        hgt = False
        # return False
    
    if not (match := re.findall(r"^(?P<hcl>#[a-f0-9]{6})$", passport['hcl'])):
        print("BAD hcl:", passport['hcl'])
        hcl = False
        # return False
    
    if not (match := re.findall(r"^(?P<ecl>amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl'])):
        print("BAD ecl:", passport['ecl'])
        ecl = False
        # return False
    
    if not (match := re.findall(r"^(?P<pid>[0-9]{9})$", passport['pid'])):
        print("BAD pid:", passport['pid'])
        pid = False
        # return False
    return all([byr, iyr, eyr, hgt, hcl, ecl, pid, cid])


def solve_first():
    valid = 0
    with open("input.txt") as f:
        ps = [input_to_dict(d) for d in f.read().split('\n\n')]
    for p in ps:
        valid += int(required_fields(p))
    return valid


def solve_second():
    valid = 0
    ps = None
    with open("input.txt") as f:
        ps = [input_to_dict(d) for d in f.read().split('\n\n')]
    for p in ps:
        if required_fields(p) and validate(p):
            valid += 1
    return valid
            



if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())