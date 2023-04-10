import networkx as nx


class dfsMRV:
    def __init__(self, graph):
        self.graph = graph
        self.colors = {}
        self.node_order = list(graph.nodes())

    def mrv_heuristic(self, node):
        used_colors = set(self.colors.get(neighbor) for neighbor in self.graph[node] if neighbor in self.colors)
        all_colors = set(range(1, len(self.graph) + 1))
        available_colors = all_colors - used_colors
        return len(available_colors)

    def dfs_chromatic(self, node):
        colors_used = set(self.colors.get(neighbour) for neighbour in self.graph[node] if neighbour in self.colors)
        for color in range(1, len(self.graph) + 1):
            if color not in colors_used:
                self.colors[node] = color
                break
        for neighbour in sorted(self.graph[node], key=lambda n: self.mrv_heuristic(n)):
            if neighbour not in self.colors:
                self.dfs_chromatic(neighbour)

    def run(self):
        for node in self.graph:
            if node not in self.colors:
                self.dfs_chromatic(node)
        return self.colors
