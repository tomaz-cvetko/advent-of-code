def get_input():
    f = open("input.txt")
    adapters = [int(s) for s in f.read().strip().split()]
    f.close()
    return adapters


def solve_first():
    a = sorted(get_input())
    a.append(0)
    ds = [0, 0, 1]
    for i in range(len(a)-1):
        step = a[i] - a[i-1]
        ds[step-1] += 1
    print(ds)
    return ds[0]*ds[2]


def solve_second():
    a = sorted(get_input())
    a = [0] + a + [a[-1]+3]
    # print(a)
    jmp_to = [0]*len(a)
    jmp_to[0] = 1
    for i in range(1, len(a)):
        for j in range(1, 4):
            if 0 < a[i] - a[i-j] <= 3:
                jmp_to[i] += 1
    # print(jmp_to)
    for i in range(1, len(a)):
        jmp_to[i] = sum(jmp_to[i-jmp_to[i]:i])
    return jmp_to[-1]


if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())