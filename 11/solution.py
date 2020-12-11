class Board:
    def __init__(self, input):
        self.arr = [[x for x in l if x != '\n'] for l in input]

    def show(self):
        return '\n'.join(''.join(x) for x in self.arr)

    def neighbors(self, y, x, radius=1):
        return [
            self.arr[i][j] if 0 <= i < len(self.arr) and 0 <= j < len(self.arr[0])
                              and not ((i == y) and (j == x)) else None
            for j in range(x - radius, x + radius + 1)
            for i in range(y - radius, y + radius + 1)
        ]

    def visible_neighbors(self, y, x):
        def direction(y, x, dy, dx):
            if 0 <= y + dy < len(self.arr) and 0 <= x + dx < len(self.arr[0]):
                if self.arr[y + dy][x + dx] == '.':
                    return direction(y + dy, x + dx, dy, dx)
                else:
                    return self.arr[y + dy][x + dx]

        return [
            direction(y, x, -1, -1),
            direction(y, x, -1, +0),
            direction(y, x, -1, +1),

            direction(y, x, +0, -1),
            direction(y, x, +0, +1),

            direction(y, x, +1, -1),
            direction(y, x, +1, +0),
            direction(y, x, +1, +1),
        ]

    def cycle(self, max_neighbors=4, neighbors_mode=0):
        new_arr = [row[:] for row in self.arr]
        neighbor_func = (self.neighbors, self.visible_neighbors)[neighbors_mode]

        change = False

        for row in range(len(self.arr)):
            for col in range(len(self.arr[row])):
                if self.arr[row][col] == 'L' and neighbor_func(row, col).count('#') == 0:
                    new_arr[row][col] = '#'
                    change = True

                if self.arr[row][col] == '#' and neighbor_func(row, col).count('#') >= max_neighbors:
                    new_arr[row][col] = 'L'
                    change = True

        self.arr = new_arr

        if not change:
            return self.occupied()
        else:
            return self.cycle(max_neighbors=max_neighbors, neighbors_mode=neighbors_mode)

    def occupied(self):
        return sum([x.count('#') for x in self.arr])


def part_one(input):
    b = Board(input)
    return b.cycle()


def part_two(input):
    b = Board(input)
    return b.cycle(max_neighbors=5, neighbors_mode=1)


if __name__ in '__main__':
    input = open('input.txt').readlines()
    # or sometimes
    # input = open('input.txt').read()
    print(part_one(input))
    print(part_two(input))
