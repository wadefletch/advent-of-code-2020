def part_one(input):
    preamble = 25

    input = [int(x) for x in input]

    for i, line in enumerate(input):
        if i < preamble:
            continue

        space = input[i - preamble:i]
        solves = 0
        for x in space:
            for y in space:
                if x + y == line:
                    solves += 1
        if solves == 0:
            return line


def part_two(input):
    input = [int(x) for x in input]

    target = part_one(input)

    size = 2
    while True:
        for x in input[:-size]:
            r = sum(input[x:size + 1])
            if r == target:
                out = input[x:size + 1]
                return min(out) + max(out)
        size += 1


if __name__ in '__main__':
    input = open('input.txt').readlines()
    # or sometimes
    # input = open('input.txt').read()
    print(part_one(input))
    print(part_two(input))
