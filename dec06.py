
def solve_first():
    gs = None
    with open("input.txt") as f:
        gs = [len({c for c in d if c != '\n'}) for d in f.read().split('\n\n')]
    print(gs)
    return sum(gs)


def solve_second():
    with open("input.txt") as f:
        gs = [len(set.intersection(*[set(s) for s in group.split('\n')])) for group in f.read().strip().split('\n\n')]
    return sum(gs)


if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())