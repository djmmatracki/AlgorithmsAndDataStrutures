from abc import ABC, abstractmethod

class Node:
    def __init__(self, key) -> None:
        self.key = key

    def __str__(self) -> str:
        return str(self.key)

    def __repr__(self) -> str:
        return str(self.key)

    def __eq__(self, __o: object) -> bool:
        if "key" in dir(__o):
            return self.key == __o.key
        return self.key == __o
    
    def __hash__(self) -> int:
        return hash(self.key)


class Edge:
    def __init__(self, node1, node2) -> None:
        self.node1 = node1
        self.node2 = node2



class Graph(ABC):
    def __init__(self) -> None:
        self.nodes = []
        self.map = dict()
    
    @abstractmethod
    def insertVertex(self, vertex):
        """Wstawia wezel do grafu"""
        raise NotImplementedError()

    @abstractmethod
    def insertEdge(self, vertex1, vertex2, edge):
        """Wstawia krawedz do grafu"""
        raise NotImplementedError()

    @abstractmethod
    def deleteVertex(self, vertex):
        """Usuwa wierzcholek z grafu"""
        raise NotImplementedError()

    @abstractmethod
    def deleteEdge(self, vertex1, vertex2):
        """Usuwa krawedz z grafu"""
        raise NotImplementedError()

    def getVertexIdx(self, vertex):
        """Zwraca indeks wezla"""
        if vertex not in self.map.keys():
            return
        return self.map[vertex]

    def getVertex(self, vertex_idx):
        """Zwraca wezel o podanym indeksie"""
        if vertex_idx > len(self.nodes):
            return
        return self.nodes[vertex_idx]

    @abstractmethod
    def neighbours(self, vertex_idx):
        """Zwraca liste indeksow wezlow przyleglych do wezla o podanym indeksie"""
        raise NotImplementedError()

    def order(self):
        """Zwraca liczbe wezlow"""
        return len(self.nodes)

    @abstractmethod
    def size(self):
        """Zwraca liczbe krawedzi"""
        raise NotImplementedError()

    @abstractmethod
    def edges(self):
        """Zwraca liste krawedzi w postaci (klucz_pocz, klucz_konc)"""
        raise NotImplementedError()


class AdjmatGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.graph = dict()
    
    def insertVertex(self, vertex):
        if vertex in self.graph.keys():
            return
        
        self.nodes.append(vertex)
        self.map[vertex] = len(self.nodes) - 1
        self.graph[vertex] = []
    
    def insertEdge(self, vertex1, vertex2, weight):
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            return
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))
    
    def deleteVertex(self, vertex):
        if vertex not in self.nodes:
            return
        
        index = self.map[vertex]
        self.nodes.pop(index)
        self.graph.pop(vertex)

        for key, value in self.graph.items():
            if vertex in value:
                self.graph[key] = [el for el in value if el[0] != vertex]

        self.map.pop(vertex)
        for i, node in enumerate(self.nodes):
            self.map[node] = i
    
    def getEdge(self, vertexId1, vertexId2):
        vertex1 = self.getVertex(vertexId1)
        vertex2 = self.getVertex(vertexId2)

        edges = self.graph.get(vertex1)
        if edges is None:
            return

        for edge in edges:
            if edge[0] == vertex2:
                return edge[1]

    
    def deleteEdge(self, vertex1, vertex2):
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            return

        self.graph[vertex1].remove(vertex2)
        self.graph[vertex2].remove(vertex1)

        self.graph[vertex1] = [el for el in self.graph[vertex1] if el[0]!= vertex2]
        self.graph[vertex2] = [el for el in self.graph[vertex2] if el[0]!= vertex1]
    
    
    def neighbours(self, vertex_idx):
        if vertex_idx > len(self.nodes):
            return
        return [(self.map[vert], weight) for vert, weight in self.graph[self.getVertex(vertex_idx)]]
    
    def edges(self):
        edges = []
        for u, values in self.graph.items():
            for v, w in values:
                edges.append((self.getVertexIdx(u), self.getVertexIdx(v), w))
        return edges

    def size(self):
        return len(self.edges())
