def part_one(input):
    total = 0

    for group in input.split('\n\n'):
        letters = set()
        for person in group.split('\n'):
            letters.update(list(person))
        total += len(letters)

    return total


def part_two(input):
    total = 0

    for group in input.split('\n\n'):
        people = group.split('\n')
        letters = set(people[0])
        for person in people[1:]:
            letters = letters.intersection(person)

        total += len(letters)

    return total


if __name__ in '__main__':
    input = open('input.txt').read()
    print(part_one(input))
    print(part_two(input))
