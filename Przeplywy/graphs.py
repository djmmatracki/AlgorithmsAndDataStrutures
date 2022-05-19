from abc import ABC, abstractmethod
import numpy as np


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
    def __init__(self, node1, node2, capacity, isResidual) -> None:
        self.node1 = node1
        self.node2 = node2
        self.capacity = capacity
        self.currentFlow = 0
        self.residual = capacity
        self.isResidual = isResidual
    
    def __str__(self) -> str:
        return f"{self.capacity} {self.currentFlow} {self.isResidual}"



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
        
        self.graph[vertex1].append(Edge(vertex1, vertex2, weight, False))
        self.graph[vertex2].append(Edge(vertex2, vertex1, 0, True))
    
    def deleteVertex(self, vertex):
        if vertex not in self.nodes:
            return
        
        index = self.map[vertex]
        self.nodes.pop(index)
        self.graph.pop(vertex)

        for node, edges in self.graph.items():
            self.graph[node] = [edge for edge in edges if edge.node1 != vertex and edge.node2 != vertex]

        self.map.pop(vertex)
        for i, node in enumerate(self.nodes):
            self.map[node] = i
    
    def getEdge(self, vertexId1, vertexId2, real=True):
        vertex1 = self.getVertex(vertexId1)
        vertex2 = self.getVertex(vertexId2)

        edges = self.graph.get(vertex1)
        if edges is None:
            return

        for edge in edges:
            if edge.node2 == vertex2:
                return edge

    
    def deleteEdge(self, vertex1, vertex2):
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            return

        self.graph[vertex1] = [edge for edge in self.graph[vertex1] if edge.node2 != vertex2]
        self.graph[vertex2] = [edge for edge in self.graph[vertex2] if edge.node2 != vertex1]

    
    def neighbours(self, vertex_idx):
        if vertex_idx > len(self.nodes):
            return
        return self.graph[self.getVertex(vertex_idx)]
    
    def edges(self):
        edges = []
        # values -> edges
        for u, values in self.graph.items():
            edges.extend(values)
        return edges

    def size(self):
        return len(self.edges())
    
    def printGraph(g):
        n = g.order()
        print("------GRAPH------",n) 
        for i in range(n):
            v = g.getVertex(i)
            print(v, end = " -> ")
            nbrs = g.neighbours(i)
            for edge in nbrs:
                print(edge.node2, edge.currentFlow, end=";")
            print()
        print("-------------------") 
    