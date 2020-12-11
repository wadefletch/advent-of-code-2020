import re


def part_one(input):
    def valid(minimum, maximum, letter, password):
        return int(minimum) <= password.count(letter) <= int(maximum)
    
    lines = map(lambda x: valid(*re.search(r'(\d*)-(\d*)\s(\w):\s(\w*)', x).groups()), input)
    return sum(lines)


def part_two(input):  
    def valid(first_pos, second_pos, letter, password):
        return (password[int(first_pos)-1] == letter) != (password[int(second_pos)-1] == letter)
    
    lines = map(lambda x: valid(*re.search(r'(\d*)-(\d*)\s(\w):\s(\w*)', x).groups()), input)
    return sum(lines)


if __name__ in '__main__':
    input = open('input.txt').readlines()
    
    print(part_one(input))
    print(part_two(input))
