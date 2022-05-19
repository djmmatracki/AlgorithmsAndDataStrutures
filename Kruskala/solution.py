from graphs import AdjmatGraph, Node


class UnionFind:
    def __init__(self, n) -> None:
        self.numNodes = n
        self.prev = [i for i in range(self.numNodes)]
        self.size = [1 for _ in range(self.numNodes)]
    
    def find(self, u):
        if self.prev[u] == u:
            return u
        return self.find(self.prev[u])

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return
        
        if self.size[root_u] > self.size[root_v]:
            self.prev[root_v] = root_u
            self.size[root_v] += 1
        else:
            self.prev[root_u] = root_v
            self.size[root_u] += 1

    
    def same_component(self, u, v):
        return self.find(u) == self.find(v)


def getEdgesFromPrev(prev):
    edges = []
    for i, p in enumerate(prev):
        current = i
        while current != prev[current]:
            if (current, prev[current]) not in edges:
                edges.append((current, prev[current]))
            current = prev[current]

    return edges


def kruskala(G):
    edges = G.edges()
    edges.sort(key=lambda edge: edge[2])
    union_find = UnionFind(G.order())
    sst = []

    for u, v, w in edges:
        if not union_find.same_component(u, v):
            sst.append((G.getVertex(u), G.getVertex(v)))
            union_find.union(u, v)

    return sst


if __name__ == "__main__":
    graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]
    G = AdjmatGraph()
    for u, v, w in graf:
        node1 = Node(u)
        node2 = Node(v)
        G.insertVertex(node1)
        G.insertVertex(node2)
        G.insertEdge(node1, node2, w)
    print(kruskala(G))
