from graphs import Node, AdjmatGraph
import numpy as np


def bfs(G):
    queue = []
    n = G.order()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    # Poczatkowy wierzcholek
    start = 0
    # Dodajemy wierzcholek do kolejki oraz oznaczamy jako odwiedzony
    queue.append(start)
    visited[start] = True

    while len(queue) > 0:
        current = queue.pop(0)
        neighbours = G.neighbours(current)

        for edge in neighbours:
            endIndex = G.getVertexIdx(edge.node2)
            if visited[endIndex] == False and edge.residual > 0:
                queue.append(endIndex)
                parent[endIndex] = current
                visited[endIndex] = True
    
    return parent


def graphPath(G,start,end,parent):
    minimal = np.inf
    current = end
    if parent[current] is None:
        return 0
    
    while current != start:
        # Niema przejscia
        if current is None:
            return

        edge1 = G.getEdge(current, parent[current])
        edge2 = G.getEdge(parent[current], current)

        # Zakladamy ze sa dwie krawedzie miedzy wierzcholkami!!!
        edge = edge1 if not edge1.isResidual else edge2
        minimal = min(minimal, edge.residual)
        current = parent[current]
    
    return minimal
    

def augmentPath(G, start, end, parent, minimalCapacity):
    current = end

    if parent[current] is None:
        return
    
    while current != start:
        # Kod ktory zaklada ze jest jedna krawedz rzeczywista oraz jedna resiudalna
        realEdge = G.getEdge(parent[current], current, real=True)
        realEdge.currentFlow += minimalCapacity
        realEdge.residual -= minimalCapacity

        residualEdge = G.getEdge(current, parent[current], real=False)
        residualEdge.residual += minimalCapacity
        current = parent[current]


def ford_fulkerson(G):
    start = 0
    end = G.order() - 1

    parent = bfs(G)
    result = graphPath(G, 0, end, parent)
    if result is None:
        return
    
    minimal = result
    while minimal > 0:
        augmentPath(G, 0, end, parent, minimal)
        parent = bfs(G)
        minimal = graphPath(G, start, end, parent)
    
    flow = 0
    edges = G.edges()
    for edge in edges:
        if G.getVertexIdx(edge.node2) == end:
            flow += edge.currentFlow

    return flow


def test_graph1():
    G = AdjmatGraph()
    node1 = Node('S')
    node2 = Node('U')
    node3 = Node('V')
    node4 = Node('T')

    G.insertVertex(node1)
    G.insertVertex(node2)
    G.insertVertex(node3)
    G.insertVertex(node4)

    G.insertEdge(node1, node2, 2)
    G.insertEdge(node2, node3, 3)
    G.insertEdge(node1, node3, 1)
    G.insertEdge(node2, node4, 1)
    G.insertEdge(node3, node4, 2)
    return G


def test_graph2():
    G = AdjmatGraph()
    s = Node('s')
    a = Node('a')
    c = Node('c')
    b = Node('b')
    d = Node('d')
    t = Node('t')

    G.insertVertex(s)
    G.insertVertex(a)
    G.insertVertex(c)
    G.insertVertex(b)
    G.insertVertex(d)
    G.insertVertex(t)

    G.insertEdge(s, a, 16)
    G.insertEdge(s, c, 13)
    G.insertEdge(a, c, 10)
    G.insertEdge(c, a, 4)
    G.insertEdge(a, b, 12)
    G.insertEdge(b, c, 9)
    G.insertEdge(c, d, 14)
    G.insertEdge(d, b, 7)
    G.insertEdge(b, t, 20)
    G.insertEdge(d, t, 4)
    return G


def test_graph3():
    G = AdjmatGraph()
    s = Node('s')
    a = Node('a')
    c = Node('c')
    b = Node('b')
    d = Node('d')
    e = Node('e')
    t = Node('t')

    G.insertVertex(s)
    G.insertVertex(a)
    G.insertVertex(c)
    G.insertVertex(b)
    G.insertVertex(d)
    G.insertVertex(e)
    G.insertVertex(t)

    G.insertEdge(s, a, 3)
    G.insertEdge(s, c, 3)
    G.insertEdge(a, b, 4)
    G.insertEdge(b, s, 3)
    G.insertEdge(b, c, 1)
    G.insertEdge(b, d, 2)
    G.insertEdge(c, d, 2)
    G.insertEdge(c, e, 6)
    G.insertEdge(d, t, 1)
    G.insertEdge(d, a, 1)
    G.insertEdge(e, t, 9)
    return G


def test_graph4():
    G = AdjmatGraph()
    s = Node('s')
    a = Node('a')
    b = Node('b')
    d = Node('d')
    c = Node('c')
    t = Node('t')

    G.insertVertex(s)
    G.insertVertex(a)
    G.insertVertex(b)
    G.insertVertex(d)
    G.insertVertex(c)
    G.insertVertex(t)

    G.insertEdge(s, a, 8)
    G.insertEdge(s, d, 3)
    G.insertEdge(a, b, 9)
    G.insertEdge(d, c, 4)
    G.insertEdge(d, b, 7)
    G.insertEdge(b, d, 7)
    G.insertEdge(b, t, 2)
    G.insertEdge(c, t, 5)
    return G


if __name__ == "__main__":
    G = test_graph1()
    flow = ford_fulkerson(G)
    print(f"Maksymalny przeplyw: {flow}")
    print("Graph po operacji szukania maksymalnego przeplywu:")
    G.printGraph()

    G = test_graph2()
    flow = ford_fulkerson(G)
    print(f"Maksymalny przeplyw: {flow}")
    print("Graph po operacji szukania maksymalnego przeplywu:")
    G.printGraph()
    
    G = test_graph3()
    flow = ford_fulkerson(G)
    print(f"Maksymalny przeplyw: {flow}")
    print("Graph po operacji szukania maksymalnego przeplywu:")
    G.printGraph()
    
    G = test_graph4()
    flow = ford_fulkerson(G)
    print(f"Maksymalny przeplyw: {flow}")
    print("Graph po operacji szukania maksymalnego przeplywu:")
    G.printGraph()
