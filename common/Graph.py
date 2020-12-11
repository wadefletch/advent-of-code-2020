class Graph:
    def __init__(self, adj_list=None):
        if adj_list is None:
            adj_list = {}
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
