def part_one(input):
    for x in input:
        x = int(x)
        for y in input:
            y = int(y)

            if x + y == 2020:
                return (x * y)

def part_two(input):
    for x in input:
        x = int(x)
        for y in input:
            y = int(y)
            for z in input:
                z = int(z)

                if x + y + z == 2020:
                    return (x * y * z)

if __name__ in '__main__':
    input = open('input.txt').readlines()
    
    print(part_one(input))
    print(part_two(input))
