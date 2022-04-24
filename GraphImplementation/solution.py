from abc import ABC, abstractmethod


class Node:
    def __init__(self, key) -> None:
        self.key = key

    def __eq__(self, __o: object) -> bool:
        if "key" not in dir(__o):
            raise ValueError
        return self.key == __o.key
    
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
    def insertVertex(vertex):
        """Wstawia wezel do grafu"""
        raise NotImplementedError()

    @abstractmethod
    def insertEdge(vertex1, vertex2, edge):
        """Wstawia krawedz do grafu"""
        raise NotImplementedError()

    @abstractmethod
    def deleteVertex(vertex):
        """Usuwa wierzcholek z grafu"""
        raise NotImplementedError()

    @abstractmethod
    def deleteEdge(vertex1, vertex2):
        """Usuwa krawedz z grafu"""
        raise NotImplementedError()

    @abstractmethod
    def getVertexIdx(vertex):
        """Zwraca indeks wezla"""
        raise NotImplementedError()

    @abstractmethod
    def getVertex(vertex_idx):
        """Zwraca wezel o podanym indeksie"""
        raise NotImplementedError()

    @abstractmethod
    def neighbours(vertex_idx):
        """Zwraca liste indeksow wezlow przyleglych do wezla o podanym indeksie"""
        raise NotImplementedError()

    @abstractmethod
    def order(self):
        """Zwraca liczbe wezlow"""
        raise NotImplementedError()

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


class MatrixGraph(Graph):
    def __init__(self) -> None:
        super().__init__()