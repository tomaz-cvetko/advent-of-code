dirs = ['E', 'S', 'W', 'N']
rot = {'R': 1, 'L':-1}
trans = {'E':(1, 0), 'S':(0, -1), 'W':(-1, 0), 'N':(0, 1)}
rot2 = {'R': (-1, 1), 'L':(1, -1)}

def get_input():
    f = open("input.txt")
    instr = f.read().strip().split()
    f.close()
    return instr


def move1(x, y, d, move):
    action, value = move
    # direction dependent part
    if action in rot:
        d += rot[action]*(value // 90)
        d %= len(dirs)
    elif action == 'F':
        action = dirs[d]  # simply a move in the current dir
    
    if action in trans:
        dx, dy = trans[action]
        x += dx*value
        y += dy*value
    return x, y, d


def solve_first():
    moves = [(s[0], int(s[1:])) for s in get_input()]
    print(moves)

    x = y = 0
    d_index = 0
    for move in moves:
        x, y, d_index = move1(x, y, d_index, move)
        print(f"at {x}, {y}; facing {dirs[d_index]}; do ({move[0]}, {move[1]})")
    return abs(x) + abs(y)


def solve_second():
    moves = [(s[0], int(s[1:])) for s in get_input()]
    print(moves)
    x = y = 0
    wx, wy = 10, 1
    for action, value in moves:
        # direction dependent part
        print(f"at ({x}, {y}); waypoint ({wx}, {wy}); do ({action}, {value})")
        if action in rot2:
            for i in range(value//90):
                xy, yx = rot2[action]
                wx, wy = yx*wy, xy*wx
        elif action == 'F':
            # actual movement only occurs in the front instruction
            x += wx*value
            y += wy*value
        
        if action in trans:
            dx, dy = trans[action]
            wx += dx*value
            wy += dy*value
    print(f"at ({x}, {y}); waypoint ({wx}, {wy});")
    return abs(x) + abs(y)

if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())