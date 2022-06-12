from abc import ABC, abstractmethod
import cv2
from matplotlib import pyplot as plt
import numpy as np


class Vertex:
    def __init__(self, cords) -> None:
        self.cords = cords
    
    def __eq__(self, other) -> bool:
        return other.cords == self.cords
    
    def __hash__(self) -> int:
        return self.cords.__hash__()
    
    def __str__(self) -> str:
        return str(self.cords)

class Edge:
    def __init__(self, vertex1, vertex2) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
    
    @property
    def length(self):
        x, y = self.vector
        return np.sqrt(x**2 + y**2)
    
    @property
    def vector(self):
        y1, x1 = self.vertex1.cords
        y2, x2 = self.vertex2.cords
        return y2-y1, x2-x1
    
    @property
    def orientation(self):
        y, x = self.vector
        return np.arctan(y/x)


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
        return self.map.get(vertex)

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


class BiometricGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.graph = dict()
    
    def insertVertex(self, vertex):
        if vertex in self.graph.keys():
            return
        
        self.nodes.append(vertex)
        self.map[vertex] = len(self.nodes) - 1
        self.graph[vertex] = []
    
    def insertEdge(self, vertex1, vertex2):
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            return
        
        self.graph[vertex1].append(Edge(vertex1, vertex2))
        self.graph[vertex2].append(Edge(vertex2, vertex1))
    
    def deleteVertex(self, vertex):
        if vertex not in self.nodes:
            return
        
        index = self.map[vertex]
        self.nodes.pop(index)
        self.graph.pop(vertex)

        for key, edges in self.graph.items():
            self.graph[key] = [edge for edge in edges if edge.vertex2 != vertex]

        self.map.pop(vertex)
        for i, node in enumerate(self.nodes):
            self.map[node] = i

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            return

        self.graph[vertex1] = [edge for edge in self.graph[vertex1] if edge.vertex2 != vertex2]
        self.graph[vertex2] = [edge for edge in self.graph[vertex2] if edge.vertex2 != vertex1]
    
    def neighbours(self, vertex_idx):
        if vertex_idx > len(self.nodes):
            return
        return [self.map[vert] for vert in self.graph[self.getVertex(vertex_idx)]]
    
    def edgesFromNode(self, vertex):
        if vertex not in self.graph.keys():
            return []
        return self.graph[vertex]

    def edges(self):
        edges = []
        for _, edges in self.graph.items():
            edges.extend(edges)
        return edges

    def size(self):
        return len(self.edges())
    
    def plot_graph(self, I):
        rows, cols = I.shape

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        for vertex, edges in self.graph.items():
            y, x = vertex.cords
            ax1.scatter(x, rows-y)

            for edge in edges:
                x = [edge.vertex1.cords[1], edge.vertex2.cords[1]]
                y = [rows-edge.vertex1.cords[0], rows-edge.vertex2.cords[0]]

                ax1.plot(x, y)
        
        ax2.imshow(I)
        plt.show()
        

def moveAndRotate(G, t, cos_alpha):
    """
    t - wektor translacji
    alpha - kat obrotu
    """
    ty, tx = t
    sin_alpha = np.sqrt(1 - cos_alpha**2)

    result = BiometricGraph()

    for node, edges in G.graph.items():
        y, x = node.cords
        newX = int(x * cos_alpha + y * sin_alpha + tx)
        newY = int(- x * sin_alpha + y * cos_alpha + ty)

        vertex1 = Vertex((newY, newX))
        result.insertVertex(vertex1)

        for edge in edges:
            y, x = edge.vertex2.cords
            newX = int(x * cos_alpha + y * sin_alpha + tx)
            newY = int(- x * sin_alpha + y * cos_alpha + ty)

            vertex2 = Vertex((newY, newX))
            result.insertVertex(vertex2)
            result.insertEdge(vertex1, vertex2)

    return result


def generateGraph(I):
    rows, cols = I.shape
    graph = BiometricGraph()

    # Generate graph
    for i in range(rows):
        for j in range(cols):

            if I[i,j] == 255:
                vertex = Vertex((i,j))
                graph.insertVertex(vertex)

                if j > 0:
                    if I[i,j-1] == 255:
                        newVertex = Vertex((i,j-1))
                        graph.insertVertex(newVertex)
                        graph.insertEdge(vertex, newVertex)

                if i > 0 and j > 0:
                    if I[i-1,j-1] == 255:
                        newVertex = Vertex((i-1,j-1))
                        graph.insertVertex(newVertex)
                        graph.insertEdge(vertex, newVertex)

                if i > 0 and j < cols:
                    if I[i-1,j+1] == 255:
                        newVertex = Vertex((i-1,j+1))
                        graph.insertVertex(newVertex)
                        graph.insertEdge(vertex, newVertex)

                if i > 0:
                    if I[i-1,j] == 255:
                        newVertex = Vertex((i-1,j))
                        graph.insertVertex(newVertex)
                        graph.insertEdge(vertex, newVertex)
    
    delete_nodes = []
    add_edges = []


    for vertex, edges in graph.graph.items():
        # Wierzcholki ktore maja dwoch sasiadow nas nie interesuja
        if len(edges) == 2:
            continue

        # Analizujemy krawedzie wychodzace
        for edge in edges:
            # Sprawdzamy wierzcholek sasiadujacy
            previousNode = vertex
            current = edge.vertex2
            currentEdges = graph.edgesFromNode(current)

            while len(currentEdges) == 2:
                delete_nodes.append(current)

                if currentEdges[0].vertex2 == previousNode:
                    previousNode = current
                    current = currentEdges[1].vertex2
                else:
                    previousNode = current
                    current = currentEdges[0].vertex2

                currentEdges = graph.edgesFromNode(current)

            # Znaleziono jakis inny wierzcholek
            if current != edge.vertex2:
                add_edges.append((vertex, current))

    # Usuwamy wierzcholki ze zbioru
    for node in delete_nodes:
        graph.deleteVertex(node)
    
    # Dodajemy krawedzie
    for vert1, vert2 in add_edges:
        graph.insertEdge(vert1, vert2)
    

    bundles = []
    visited = []

    # Szukanie klebka wierzcholkow
    for vertex, edges in graph.graph.items():
        if vertex in visited:
            continue
        bundle = [vertex]
        visited.append(vertex)
        y, x = vertex.cords

        # Sprawdzamy otoczenie wierzcholka
        for i in range(y - 5, y + 6):
            for j in range(x - 5, x + 6):
                otherVertex = Vertex((i,j))
                if graph.getVertexIdx(otherVertex) is not None and otherVertex not in visited:
                    bundle.append(otherVertex)
                    visited.append(otherVertex)

        if len(bundle) != 1:
            bundles.append(bundle)
    
    # Laczenie wierzcholkow
    for bundle in bundles:
        x_cords = [vert.cords[0] for vert in bundle]
        y_cords = [vert.cords[1] for vert in bundle]

        newX = sum(x_cords) // len(x_cords)
        newY = sum(y_cords) // len(y_cords)

        connectedNodes = set()

        for vert in bundle:
            edges = graph.edgesFromNode(vert)
            for edge in edges:
                if edge.vertex2 not in bundle:
                    connectedNodes.add(edge.vertex2)
        
        # Dodajemy nowy wierzcholek
        newVertex = Vertex((newX, newY))
        graph.insertVertex(newVertex)

        # Usuwamy stare nody
        for vertex in bundle:
            if vertex == newVertex:
                continue
            graph.deleteVertex(vertex)

        # Dodajemy krawedzie
        for node in connectedNodes:
            graph.insertEdge(newVertex, node)
    
    # graph.plot_graph(I)
    return graph


def distanceBetweenEdges(edge1, edge2):
    return (1 / (edge1.length + edge2.length)) * np.sqrt((edge1.length - edge2.length)**2 + (edge1.orientation - edge2.orientation)**2)


def distanceBetweenVertexes(vertex1, vertex2):
    y1, x1 = vertex1.cords
    y2, x2 = vertex2.cords
    return np.sqrt((y1 - y2)**2 + (x1 - x2)**2)


def biometria(G1, G2, ni, epsilon):
    edges1 = G1.edges()
    edges2 = G2.edges()
    pairs = []

    for edge1 in edges1:
        for edge2 in edges2:
            s = distanceBetweenEdges(edge1, edge2)
            pairs.append((edge1, edge2, s))
    
    pairs.sort(key=lambda x: x[2])
    pairs = pairs[:ni]
    minimalDk = np.inf
    resultGraph1 = G1
    resultGraph2 = G2

    for pair in pairs:
        edge1, edge2, _ = pair

        y1, x1 = edge1.vector
        y2, x2 = edge2.vector

        movedG1 = moveAndRotate(G1, (-y1, -x1), x1/(edge1.length))
        movedG2 = moveAndRotate(G2, (-y2, -x2), x2/(edge2.length))
    
        C = 0
        used = []
        for node1, _ in movedG1.graph.items():
            for node2, _ in movedG2.graph.items():
                if distanceBetweenVertexes(node1, node2) < epsilon and node2 not in used:
                    C += 1
        
        dk = 1 - C / np.sqrt(G1.order() * G2.order())
        if dk < minimalDk:
            resultGraph1 = movedG1
            resultGraph2 = movedG2
            minimalDk = dk
    return resultGraph1, resultGraph2


if __name__ == "__main__":
    I1 = cv2.imread("Retina_graph_easy_1.png", cv2.IMREAD_GRAYSCALE)
    I2 = cv2.imread("Retina_graph_easy_2.png", cv2.IMREAD_GRAYSCALE)
    I3 = cv2.imread("Retina_graph_easy_3.png", cv2.IMREAD_GRAYSCALE)

    G1 = generateGraph(I1)
    G2 = generateGraph(I2)
    res1, res2 = biometria(G1, G2, 50, 10)
    # G3 = biometric(I3)
