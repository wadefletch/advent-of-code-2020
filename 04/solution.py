def serialize_input(input):
    return [
        {field.split(':')[0]: field.split(':')[1] for field in passport.split()}
        for passport in input.split('\n\n')
    ]


def count_fields(passport):
    keys = list(passport.keys())
    key_count = len(keys)
    key_count -= 'cid' in keys
    return key_count


def part_one(input):
    return sum(count_fields(p) == 7 for p in serialize_input(input))


def part_two(input):
    passports = serialize_input(input)

    def valid(key, value) -> bool:
        numbers = '0123456789'
        letters = 'abcdef'

        def digits(value, count):
            return len(str(value)) == count

        if key == 'byr':
            return digits(value, 4) and (1920 <= int(value) <= 2002)
        elif key == 'iyr':
            return digits(value, 4) and (2010 <= int(value) <= 2020)
        elif key == 'eyr':
            return digits(value, 4) and (2020 <= int(value) <= 2030)
        elif key == 'hgt':
            if value[-2:] == 'cm':
                return 150 <= int(value[:-2]) <= 193
            elif value[-2:] == 'in':
                return 59 <= int(value[:-2]) <= 76
            else:
                return False
        elif key == 'hcl':
            return (value[0] == '#') and all(x in numbers + letters for x in value[1:])
        elif key == 'ecl':
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif key == 'pid':
            return all(x in numbers for x in value) and digits(value, 9)
        elif key == 'cid':
            return True
        else:
            return False

    out = 0

    for p in passports:
        if count_fields(p) == 7:
            for field in p:
                print(f'p[{field}] = {p[field]} ({valid(field, p[field])})')

            if all(valid(k, v) for k, v in p.items()):
                out += 1
        print('=='*4)

    return out


if __name__ in '__main__':
    input = open('input.txt').read()
    print(part_one(input))
    print(part_two(input))
