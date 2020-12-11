def bpass_to_row_col(bpass):
    row_arr = list(range(0, 128))
    col_arr = list(range(0, 8))

    for letter in bpass.strip():
        if letter == 'F':
            row_arr = row_arr[:(len(row_arr) // 2)]
        elif letter == 'B':
            row_arr = row_arr[(len(row_arr) // 2):]
        elif letter == 'L':
            col_arr = col_arr[:(len(col_arr) // 2)]
        elif letter == 'R':
            col_arr = col_arr[(len(col_arr) // 2):]

    return row_arr[0], col_arr[0]


def get_id(row, col):
    return (row * 8) + col


def part_one(input):
    return max(get_id(*bpass_to_row_col(bpass)) for bpass in input)


def part_two(input):
    ids = sorted(get_id(*bpass_to_row_col(bpass)) for bpass in input)

    for i in range(1, len(ids) - 1):
        if (ids[i - 1] + 1) != ids[i]:
            return ids[i - 1] + 1
        elif ids[i] != (ids[i + 1] - 1):
            return ids[i + 1] - 1


if __name__ in '__main__':
    input = open('input.txt').readlines()
    print(part_one(input))
    print(part_two(input))
