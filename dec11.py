def get_input():
    f = open("input.txt")
    seats = [[0] + [1 if c == 'L' else 0 for c in line.strip()] + [0] for line in f]
    seats = [[0]*len(seats[0])] + seats + [[0]*len(seats[0])]
    f.close()
    return seats


def get_zeros(m, n):
    return [[0 for j in range(n)] for i in range(m)]


def string(state, layout):
    return ''.join([''.join(['.' if layout[i][j] == 0 else 'L' if state[i][j] == 0 else '#' for j in range(1, len(state[0])-1)])+'\n' for i in range(1, len(state)-1)]).strip()

def game_of_seats(state, layout):
    new = get_zeros(len(state), len(state[0]))
    flag = False
    for i in range(1, len(state)-1):
        for j in range(1, len(state[0])-1):
            if layout[i][j] == 0:
                continue

            surr = 0
            surr += state[i-1][j-1] + state[i-1][j] + state[i-1][j+1]
            surr += state[i][j-1] + state[i][j+1]
            surr += state[i+1][j-1] + state[i+1][j] + state[i+1][j+1]
            if state[i][j] == 0 and surr == 0 and layout[i][j] == 1:
                new[i][j] = 1
                flag = True  # sth has changed
            elif state[i][j] == 1 and surr >= 4 and layout[i][j] == 1:
                # print("i, j, surr", i, j, surr)
                new[i][j] = 0
                flag = True  # sth has changed
            else:
                new[i][j] = state[i][j]
    return new, flag


def visible(layout):
    vis = get_zeros(len(layout), len(layout[0]))
    for i in range(1, len(layout)-1):
        for j in range(1, len(layout)-1):
            vis[i][j] = []
            if layout[i][j] == 0:
                continue
            
            # to the right
            if 1 in layout[i][j+1:]:
                l = layout[i].index(1, j+1)
                vis[i][j].append((i, l))
            # to the left
            if 1 in layout[i][:j]:
                l = layout[i][j-1:0:-1].index(1)
                vis[i][j].append((i, j-l-1))
            
            col = [row[j] for row in layout]
            # downward
            if 1 in col[i+1:]:
                k = col.index(1, i+1)
                vis[i][j].append((k, j))
            # upward
            if 1 in col[:i]:
                k = col[i-1:0:-1].index(1)
                vis[i][j].append((i-k-1, j))
            
            k, l = i, j
            while 0 < k < len(layout)-1 and 0 < l < len(layout[0])-1:
                k += 1
                l += 1
                if layout[k][l] == 1:
                    vis[i][j].append((k, l))
                    break
            k, l = i, j
            while 0 < k < len(layout)-1 and 0 < l < len(layout[0])-1:
                k -= 1
                l -= 1
                if layout[k][l] == 1:
                    vis[i][j].append((k, l))
                    break
            k, l = i, j
            while 0 < k < len(layout)-1 and 0 < l < len(layout[0])-1:
                k += 1
                l -= 1
                if layout[k][l] == 1:
                    vis[i][j].append((k, l))
                    break
            k, l = i, j
            while 0 < k < len(layout)-1 and 0 < l < len(layout[0])-1:
                k -= 1
                l += 1
                if layout[k][l] == 1:
                    vis[i][j].append((k, l))
                    break
    return vis
                

def game_of_seats2(state, layout, visible):
    new = get_zeros(len(state), len(state[0]))
    flag = False
    for i in range(1, len(state)-1):
        for j in range(1, len(state[0])-1):
            if layout[i][j] == 0:
                continue

            surr = 0
            for seat in visible[i][j]:
                surr += state[seat[0]][seat[1]]
            
            if state[i][j] == 0 and surr == 0 and layout[i][j] == 1:
                new[i][j] = 1
                flag = True  # sth has changed
            elif state[i][j] == 1 and surr >= 5 and layout[i][j] == 1:
                # print("i, j, surr", i, j, surr)
                new[i][j] = 0
                flag = True  # sth has changed
            else:
                new[i][j] = state[i][j]
    return new, flag


def solve_first():
    layout = get_input()
    # [print(x) for x in layout]

    state = get_zeros(len(layout), len(layout[0]))
    flag = True
    step = 0
    while flag:
        # print("step:", step)
        # [print(x[1:-1]) for x in state[1:-1]]
        # print(string(state, layout))
        state, flag = game_of_seats(state[:], layout)
        step += 1
    return string(state, layout).count("#")


def solve_second():
    layout = get_input()
    # print(string(layout, layout))
    vis = visible(layout)
    # [print(x[1:-1]) for x in vis[1:-1]]
    # return 0
    state = get_zeros(len(layout), len(layout[0]))
    flag = True
    step = 0
    while flag:
        # print("step:", step)
        # [print(x[1:-1]) for x in state[1:-1]]
        # print(string(state, layout))
        state, flag = game_of_seats2(state[:], layout, vis)
        step += 1
    return string(state, layout).count("#")
    


if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())