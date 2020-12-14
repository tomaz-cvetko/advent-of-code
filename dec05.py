
def boarding_to_row_seat(b_pass):
    row = int(b_pass[:7].replace('B', '1').replace('F', '0'), base=2)
    seat = int(b_pass[7:].replace('R', '1').replace('L', '0'), base=2)
    seat_ID = row*8 + seat
    # print(row, seat, seat_ID)
    return seat_ID


def solve_first():
    ids = None
    with open("input.txt") as f:
        ids = [boarding_to_row_seat(line) for line in f]
    return max(ids)


def solve_second():
    ids = None
    with open("input.txt") as f:
        ids = sorted([boarding_to_row_seat(line) for line in f])
    print(ids[0], ids[-1], ids[-1] - ids[0], len(ids))
    for idx, sid in zip(range(ids[0], ids[-1]), ids):
        if idx != sid:
            print(idx, sid)
            return idx

if __name__ == "__main__":
    # print(solve_first())
    print(solve_second())