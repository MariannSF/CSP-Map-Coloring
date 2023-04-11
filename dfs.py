class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.colors = {}
        self.node_order = list(graph.nodes())

    def dfs_chromatic(self, node):
        colors_used = set(self.colors.get(neighbour) for neighbour in self.graph[node] if neighbour in self.colors)
        for color in range(1, len(self.graph) + 1):
            if color not in colors_used:
                self.colors[node] = color
                break
        for neighbour in self.graph[node]:
            if neighbour not in self.colors:
                self.dfs_chromatic(neighbour)

    def run(self):
        for node in self.graph:
            if node not in self.colors:
                self.dfs_chromatic(node)
        return self.colors
