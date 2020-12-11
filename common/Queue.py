class Queue:
    def __init__(self):
        self.contents = []

    def put(self, v):
        self.contents.append(v)

    def pop(self):
        o = self.contents[0]
        self.contents = self.contents[1:]
        return o

    def empty(self):
        return len(self.contents) == 0
