
def validate_1st():
    count = 0
    with open("input.txt") as f:
        while(s := f.readline()):
            data = s.strip().split()
            low, high = [int(x) for x in data[0].split('-')]
            char = data[1].strip(':')
            # print(data, (low, high), char, data[2].count(char))
            if low <= data[2].count(char) <= high:
                count += 1
    return count

def validate_2nd():
    count = 0
    bool1 = bool2 = False
    with open("input.txt") as f:
        while(s := f.readline()):
            data = s.strip().split()
            i, j = [int(x) for x in data[0].split('-')]
            char = data[1].strip(':')
            password = data[2]
            # print(data, (low, high), char, data[2].count(char))
            if 0 <= i-1 < len(password):
                bool1 = (password[i-1] == char)
            else:
                bool1 = False
            if 0 <= j-1 < len(password):
                bool2 = (password[j-1] == char)
            else:
                bool2 = False

            if bool1 != bool2:
                count += 1
    return count


if __name__ == "__main__":
    print(validate_1st())
    print(validate_2nd())
            

