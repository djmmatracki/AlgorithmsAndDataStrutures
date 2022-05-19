import numpy as np
# import networkx as nx
from graphs import AdjmatGraph, Node
# import matplotlib.pyplot as plt


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


def sstPrimAlgorithm(G, start):
    n = G.order()
    prev = [0 for _ in range(n)]
    intree = []
    distances = [np.inf for _ in range(n)]
    current = start

    mst = AdjmatGraph()
    for u, v, w in G.edges():
        node1 = Node(u)
        node2 = Node(v)
        mst.insertVertex(node1)
        mst.insertVertex(node2)

    while len(intree) < n:
        if current not in intree:
             intree.append(current)
        
        neigbours = G.neighbours(current)
        for neigbour, weight in neigbours:
            if neigbour not in intree and distances[neigbour] > weight:
                distances[neigbour] = weight
                prev[neigbour] = current
        
        # Znajdujemy minimalna krawedz ktora dodamy
        minimalNode = None
        minimal = np.inf
        for node, weight in enumerate(distances):
            if node not in intree and minimal > weight:
                minimal = weight
                minimalNode = node

        if minimalNode is None:
            break
        
        # Jezeli znaleziony node nie jest polaczony z bierzacym to sie cofamy do poprzedniego
        if (minimalNode, minimal) not in neigbours:
            current = prev[current]
            continue

        # Dodajemy krawedz
        intree.append(minimalNode)
        node1 = G.getVertex(current)
        node2 = G.getVertex(minimalNode)

        mst.insertEdge(node1, node2, minimal)
        current = minimalNode

    return mst


def printGraph(g):
    n = g.order()
    print("------GRAPH------",n) 
    for i in range(n):
        v = g.getVertex(i)
        #print(v.key, end = " -> ")
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            #print(g.getVertex(j).key, w, end=";")
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


# def plotGraph(edges, sst):
#     G = nx.Graph()
#     G.add_weighted_edges_from(edges)
#     pos = nx.spring_layout(G)

#     nx.draw_networkx_nodes(G, pos, node_color='g', node_size=500)
#     nx.draw_networkx_edges(G, pos, width=1,alpha=0.5,edge_color='b')
#     nx.draw_networkx_edges(G, pos, edgelist=sst, width=2,alpha=0.8,edge_color='g')

#     nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels = nx.get_edge_attributes(G,'weight'))
#     nx.draw_networkx_labels(G, pos, font_size=16)

#     plt.title("Graph")
#     plt.show()

if __name__ == "__main__":
    G = AdjmatGraph()
    for u, v, w in graf:
        node1 = Node(u)
        node2 = Node(v)

        G.insertVertex(node1)
        G.insertVertex(node2)
        G.insertEdge(node1, node2, w)

    
    sst = sstPrimAlgorithm(G, 0)
    printGraph(sst)
