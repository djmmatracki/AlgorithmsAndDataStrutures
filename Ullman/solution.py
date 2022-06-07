import numpy as np
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




def is_isomorfizm(M, G, P):
    return (P == M @ (M@G).T).all()

def find_mapped_neighbours(M, row, col):
    rows, columns = M.shape
    col_neighbours = []
    row_neighbours = []

    for i in range(rows):
        if M[row][i] == 1:
            col_neighbours.append(i)

    for j in range(columns):
        if M[j][col] == 1:
            row_neighbours.append(j)

    for i in col_neighbours:
        found = False
        for j in row_neighbours:
            if M[i][j] == 1:
                found = True
                break
        
        if found == False:
            return True
    return False


def ullman0(used_columns, current_row, G, P, M, no_rec=0):
    rows, columns = M.shape
    found = 0

    if current_row == rows:
        if is_isomorfizm(M, G, P):
            return 1, no_rec
        return 0, no_rec

    for i in range(columns):
        if i in used_columns:
            continue

        M[current_row] = [1 if k == i else 0 for k in range(columns)]
        used_columns.add(i)
        result = ullman0(used_columns, current_row+1, G, P, M, no_rec)
        found += result[0]
        no_rec = result[1]
        no_rec += 1
        used_columns.remove(i)
    
    return found, no_rec
    
    

def get_M0(P, G):
    M0 = np.zeros((P.order(), G.order()))
    rows, cols = M0.shape

    for i in range(rows):
        for j in range(cols):
            if P.getDegree(i) <= G.getDegree(j):
                M0[i][j] = 1
    return M0


def ullman1(used_columns, current_row, G, P, M, M0, rec_num=0):
    rows, columns = M.shape
    found = 0

    if current_row == rows:
        if is_isomorfizm(M, G, P):
            return 1, rec_num
        return 0, rec_num

    for i in range(columns):
        if i in used_columns:
            continue

        if M0[current_row][i] != 1:
            continue

        M[current_row] = [1 if k == i else 0 for k in range(columns)]
        used_columns.add(i)

        result = ullman1(used_columns, current_row+1, G, P, M, M0, rec_num=rec_num)
        found += result[0]
        rec_num = result[1]
        rec_num += 1
        used_columns.remove(i)
    
    return found, rec_num


def prune(M):
    rows, columns = M.shape
    changed = True

    while changed:
        changed = False
        for i in range(rows):
            for j in range(columns):
                if M[i][j] == 1:
                    if find_mapped_neighbours(M, i, j):
                        M[i][j] = 0
                        changed = True


def ullman2(used_columns, current_row, G, P, M, M0, rec_num=0):
    rows, columns = M.shape
    found = 0

    if current_row == rows:
        if is_isomorfizm(M, G, P):
            return 1, rec_num
        return 0, rec_num

    M_prim = M.copy()

    for i in range(columns):
        if i in used_columns:
            continue

        if M0[current_row][i] != 1:
            continue

        M_prim[current_row] = [1 if k == i else 0 for k in range(columns)]
        used_columns.add(i)

        result = ullman1(used_columns, current_row+1, G, P, M_prim, M0, rec_num=rec_num)
        found += result[0]
        rec_num = result[1]
        rec_num += 1

        used_columns.remove(i)
    
    return found, rec_num


if __name__ == "__main__":
    G = MatrixGraph()
    P = MatrixGraph()

    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    for key1, key2, weight in graph_G:
        node1 = Node(key1)
        G.insertVertex(node1)

        node2 = Node(key2)
        G.insertVertex(node2)
        G.insertEdge(node1, node2, weight)

    for key1, key2, weight in graph_P:
        node1 = Node(key1)
        P.insertVertex(node1)

        node2 = Node(key2)
        P.insertVertex(node2)
        P.insertEdge(node1, node2, weight)


    matrix_G = np.array(G.get_matrix())
    matrix_P = np.array(P.get_matrix())

    M = np.zeros((P.order(), G.order()))

    M0 = get_M0(P, G)
    print(ullman0(set(), 0, matrix_G, matrix_P, M))
    print(ullman1(set(), 0, matrix_G, matrix_P, M, M0))
    print(ullman2(set(), 0, matrix_G, matrix_P, M, M0))

