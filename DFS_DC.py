import networkx as nx

class DFS_DC:
    def __init__(self, graph):
        self.graph = graph
        self.colors = {}
        self.node_order = list(graph.nodes())

    def degree_constraint(self, node):
        count = 0
        for neighbor in self.graph.neighbors(node):
            count += 1
        return count

    def dfs_chromatic(self, node):
        colors_used = set(self.colors.get(neighbor) for neighbor in self.graph[node] if neighbor in self.colors)
        for color in range(1, len(self.graph) + 1):
            if color not in colors_used:
                self.colors[node] = color
                break
        for neighbor in sorted(self.graph[node], key=lambda n: self.degree_constraint(n)):
            if neighbor not in self.colors:
                self.dfs_chromatic(neighbor)

    def run(self):
        for node in self.graph:
            if node not in self.colors:
                self.dfs_chromatic(node)
        return self.colors
