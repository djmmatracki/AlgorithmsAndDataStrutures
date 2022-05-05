import polska
from graphs import Node, MatrixGraph


def colorGraph(G, type):
    if type not in ('dfs', 'bfs'):
        return

    stack = []
    stack.append(0)

    colors = dict()

    while len(stack) > 0:
        if type == "dfs":
            current = stack.pop()
        else:
            current = stack.pop(0)
        neighbours = G.neighbours(current)

        usedColors = []
        for neighbour in neighbours:
            result = colors.get(neighbour)
            if result is None:
                stack.append(neighbour)
                continue
            usedColors.append(result)
        
        found = False
        i = 0
        while not found:
            if i in usedColors:
                i += 1
                continue
            found = True
        colors[current] = i
    return colors


if __name__ == "__main__":
    edges = polska.graf
    graph = MatrixGraph()

    for u, v in edges:
        graph.insertVertex(Node(u))
        graph.insertVertex(Node(v))
        graph.insertEdge(Node(u), Node(v), 1)

    method = "bfs"

    if method == "dfs":
        colors = colorGraph(graph, method)
        colors = {graph.getVertex(index): color for index, color in colors.items()}
        polska.draw_map(graph.edges(), list(colors.items()))
    else:
        colors = colorGraph(graph, 'bfs')
        colors = {graph.getVertex(index): color for index, color in colors.items()}
        polska.draw_map(graph.edges(), list(colors.items()))

