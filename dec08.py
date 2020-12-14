def get_code():
    f = open("input.txt")
    code = [parse_cmd(x) for x in f.read().strip().split('\n')]
    f.close()
    return code


def parse_cmd(line):
    x = line.strip().split(' ')
    return (x[0], int(x[1]))


def is_infinite(code):
    safety = len(code)*[0]
    a = 0
    i = 0
    while i < len(code):
        if safety[i] != 0:
            break
        else:
            safety[i] = 1

        cmd, arg = code[i]
        if cmd == 'acc':
            a += arg
            i += 1
        elif cmd == 'jmp':
            i += arg
        elif cmd == 'nop':
            i += 1
    return (a, i, i != len(code))


def solve_first():
    code = get_code()
    a, _, inf = is_infinite(code)
    print(inf)
    return a


def solve_second():
    original = get_code()
    cpy = original.copy()
    for i in range(len(original)):
        cmd, arg = original[i]
        print(i, cmd, arg)

        if cmd == 'nop':
            cpy[i] = ('jmp', arg)
            print("  =>", cpy[i])
        elif cmd == 'jmp':
            cpy[i] = ('nop', arg)
            print("  =>", cpy[i])
        
        a, j, inf = is_infinite(cpy)
        print("    |", a, j, inf)
        if not inf:
            return a

        cpy[i] = (cmd, arg) # put it back in case this was not the right move
    print("apparently this didn't work")


if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())