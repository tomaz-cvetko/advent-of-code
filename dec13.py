def get_input():
    f = open("input.txt")
    eta = int(next(f).strip())
    bus = [int(x) if x != 'x' else -1 for x in next(f).strip().split(',')]
    f.close()
    return eta, bus


def solve_first():
    eta, buses = get_input()
    print(eta, buses)

    m_wait = max(buses)
    line = m_wait
    for bus in buses:
        if bus == -1:
            continue
        wait = bus*(eta//bus + 1) - eta 
        if wait < m_wait:
            m_wait = wait
            line = bus
    return line*m_wait


def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    i = 2
    while i*i < x:
        if x % i == 0:
            return False
        i += 1
    return True


def solve_second():
    _, buses = get_input()
    print(buses)
    z1 = buses[0]
    b1 = 0
    print(f"a0*{z1} = t")
    for i, z2 in enumerate(buses):
        if z2 == -1 or i == 0:
            continue
        print(f"a{i}*{z2} = t + {i}")
        b2 = i
        a1 = 0
        while True:
            if (a1*z1 - b1 + b2) % z2 == 0:
                print("success!", z1, z2)
                b1 = -(a1*z1 - b1)
                z1 = z1*z2
                break
            a1 += 1

    print(-b1)
    return -b1



if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())
