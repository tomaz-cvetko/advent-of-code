def get_input():
    f = open("input.txt")
    data = [int(x) for x in f.read().strip().split()]
    f.close()
    return data


def find_invalid(nums, p):
    pre = set(nums[:p])

    in_there = False
    # print(nums)
    for i in range(p, len(nums)):
        x = nums[i]
        for y in pre:
            # print(x, y)
            if x - y in pre:
                in_there = True
                break
        if not in_there:
            return x
        else:
            in_there = False

        pre.remove(nums[i-p])
        pre.add(nums[i])

    return nums[-1]


def weakness(nums, inv):
    indices = None
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s = sum(nums[i:j+1])
            if s == inv:
                indices = (i, j)
            elif s > inv:
                break  # no point in adding more summands once we're over the limit
        if indices is not None:
            break
    
    srng = sorted(nums[indices[0]:indices[1]+1])
    return srng[0] + srng[-1]


def solve_first(p):
    nums = get_input()
    return find_invalid(nums, p)


def solve_second(p):
    nums = get_input()
    inv = find_invalid(nums, p)  # this sets the goal of the algo
    return weakness(nums, inv)



if __name__ == "__main__":
    # print(solve_first(25))
    print(solve_second(25))
