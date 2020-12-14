import re

def get_input():
    f = open("input.txt")
    data = f.read().strip().split('mask = ')
    f.close()
    masks = []
    commands = []
    for entry in data:
        if entry == '':
            continue
        
        mask = re.search('[X10]{36}', entry).group()
        print(mask)
        cmds = re.findall(r'mem\[(\d+)\] = (\d+)', entry)
        print(cmds)
        masks.append(mask)
        commands.append(cmds)
    return masks, commands


def bitmasks(mask):
    # returns (or_mask, and_mask)
    return (int(mask.replace('X', '0'), base=2), int(mask.replace('X', '1'), base=2))


def mask(address, mask):
    address = '{:0>36}'.format(bin(address)[2:])
    masked = ''.join([m if m == 'X' or m == '1' else c for c, m in zip(address, mask)])
    return masked


def write_to(addr, val, mem):
    if 'X' not in addr:
        idx = int(addr, base=2)
        mem[idx] = val
        print("writing at:", idx, val)
        return None
    else:
        write_to(addr.replace('X', '0', 1), val, mem)
        write_to(addr.replace('X', '1', 1), val, mem)
        return None


def solve_first():
    masks, commands = get_input()
    mem = {}

    for m, cs in zip(masks, commands):
        or_mask, and_mask = bitmasks(m)
        for loc, val in cs:
            mem[int(loc)] = ( int(val) | or_mask) & and_mask
    return sum(mem.values())


def solve_second():
    masks, commands = get_input()
    mem = {}

    for m, cs in zip(masks, commands):
        for loc, val in cs:
            mloc = mask(int(loc), m)
            write_to(mloc, int(val), mem)
    return sum(mem.values())


if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())
