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


class MatrixGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.graph = []
    
    def insertVertex(self, vertex):
        if vertex in self.nodes:
            return

        self.nodes.append(vertex)
        self.map[vertex] = len(self.nodes) - 1
        for row in self.graph:
            row.append(0)
        self.graph.append([0 for _ in range(len(self.nodes))])
    
    def insertEdge(self, vertex1, vertex2, weight):
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            return

        index1 = self.map[vertex1]
        index2 = self.map[vertex2]

        self.graph[index1][index2] = weight
        self.graph[index2][index1] = weight
    
    def deleteVertex(self, vertex):
        if vertex not in self.nodes:
            return
        
        index = self.map[vertex]
        self.nodes.pop(index)
        self.map.pop(vertex)

        for i, node in enumerate(self.nodes):
            self.map[node] = i
        
        self.graph.pop(index)
        for row in self.graph:
            row.pop(index)
    
    def deleteEdge(self, vertex1, vertex2):
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            return
        
        index1 = self.map[vertex1]
        index2 = self.map[vertex2]

        self.graph[index1][index2] = 0
        self.graph[index2][index1] = 0
    
    def neighbours(self, vertex_idx):
        
        indexes = []
        for i in range(len(self.nodes)):
            if self.graph[vertex_idx][i] == 1:
                indexes.append(i)
        return indexes

    def size(self):
        return len(self.edges())
    
    def get_matrix(self):
        return self.graph

    def getDegree(self, idx):
        degree = 0
        for i in range(self.order()):
            degree = degree + 1 if self.graph[idx][i] > 0 else degree
        return degree

    def edges(self):
        edges = []
        for i in range(self.order()):
            for j in range(self.order()):
                if self.graph[i][j] != 0:
                    edges.append((self.nodes[i], self.nodes[j], self.graph[i][j]))
        return edges

