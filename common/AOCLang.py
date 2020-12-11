class AOCLang:
    def __init__(self, input):
        self.val = 0
        self.instructions = []
        self.visited = []
        self.index = 0

        for line in input:
            parsed = line.strip().split()
            self.instructions.append((parsed[0], int(parsed[1])))

    def execute_line(self, index, acc, visited=None):
        if visited is None:
            visited = []
        if index in visited:
            return acc, False
        if index >= len(self.instructions):
            return acc, True

        visited += [index]
        ins, val = self.instructions[index]

        if ins == 'acc':
            return self.execute_line(index + 1, acc + int(val), visited)
        elif ins == 'jmp':
            return self.execute_line(index + val, acc, visited)
        elif ins == 'nop':
            return self.execute_line(index + 1, acc, visited)

    def run(self):
        while True:
            if self.index in self.visited:
                return self.val, False
            if self.index >= len(self.instructions):
                return self.val, True

            self.visited += [self.index]

            ins, val = self.instructions[self.index]

            getattr(self, ins)(val)

    def acc(self, val):
        self.index += 1
        self.val += val

    def jmp(self, val):
        self.index += val

    def nop(self, val):
        self.index += 1
