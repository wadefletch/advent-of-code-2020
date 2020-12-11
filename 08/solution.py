import sys
sys.path.insert(0, '..')
from common.AOCLang import *


def possible_changes(instructions):
    poss = []

    for i, line in enumerate(instructions):
        ins, val = line
        nw = instructions[::]

        if ins == 'jmp':
            nw[i] = ('nop', val)

        if ins == 'nop':
            nw[i] = ('jmp', val)

        poss.append(nw)

    return poss


def part_one(input):
    a = AOCLang(input)
    return a.run()[0]


def part_two(input):
    a = AOCLang(input)
    for sol in possible_changes(a.instructions):
        b = AOCLang(input)
        b.instructions = sol
        res = b.run()
        if res[1]:
            return res[0]


if __name__ in '__main__':
    input = open('input.txt').readlines()
    print(part_one(input))
    print(part_two(input))
