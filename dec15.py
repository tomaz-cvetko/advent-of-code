
def get_input():
    f = open("input.txt")
    nums = [int(x) for x in f.read().strip().split(',')]
    f.close()
    return nums


def solve_first(end):
    nums = get_input()
    print(nums)

    spoken = []
    memo = {}
    for i, n in enumerate(nums):
        spoken.append(n)
        if i < len(nums)-1:
            memo[n] = i  # always enter memo the previous one

    for i in range(len(nums), end):
        last = spoken[i-1]
        if last in memo:
            new = i-1 - memo[last]
            spoken.append(new)
        else:
            spoken.append(0)
        memo[last] = i-1  # update memo on the previous number
        # print(spoken[-1])
    return spoken[-1]
    


if __name__ == "__main__":
    print(solve_first(2020))
    print(solve_first(30000000))