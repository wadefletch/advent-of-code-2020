class Graph:
    def __init__(self, adj_list={}):
        self.adj_list = adj_list

    def add_node(self, node):
        self.adj_list[node] = []

    def add_edge(self, start, end):
        self.adj_list[start] += [end]

    def nodes(self):
        return self.adj_list.keys()

    def neighbors(self, node):
        if node in self.adj_list:
            return self.adj_list[node]
        else:
            return []

    def invert(self):
        rev_adj_list = {}
        for u in self.nodes():
            for v in self.adj_list[u]:
                if v[1] in rev_adj_list:
                    rev_adj_list[v[1]].append((v[0], u))
                else:
                    rev_adj_list[v[1]] = [(v[0], u)]

        return Graph(adj_list=rev_adj_list)

    def cost(self, node):
        m = self.neighbors(node)
        count = 0
        if m:
            for n in m:
                count += n[0]
                count += n[0] * self.cost(n[1])

        return count

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


def parse_input(input):
    out = []

    for l in input:
        l_ = l.split('contain')
        l_ = [x.strip() for x in l_]
        l_[0] = l_[0].rsplit(' ', 1)[0]
        l_[1] = l_[1].split(',')
        for i, x in enumerate(l_[1]):
            l_[1][i] = x.rsplit(' ', 1)[0].strip()
            l_[1][i] = tuple(l_[1][i].split(' ', 1))

        out.append(l_)

    return out


def build_graph_from_rules(rules):
    g = Graph()

    for rule in rules:
        g.add_node(rule[0])
        for sub in rule[1]:
            if sub[1] != 'other':
                g.add_edge(rule[0], (0 if sub[0] == 'no' else int(sub[0]), sub[1]))

    return g


def part_one(input):
    rules = parse_input(input)
    g = build_graph_from_rules(rules)

    color = set()

    # print(g.adj_list)

    rev = g.invert()
    q = Queue()
    q.put('shiny gold')
    while not q.empty():
        for n in rev.neighbors(q.pop()):
            q.put(n[1])
            color.add(n[1])

    return len(color)


def part_two(input):
    rules = parse_input(input)
    g = build_graph_from_rules(rules)

    return g.cost('shiny gold')


if __name__ in '__main__':
    input = open('input.txt').readlines()
    print(part_one(input))
    print(part_two(input))
