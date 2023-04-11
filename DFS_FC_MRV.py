# DFS_FC.py
import networkx as nx


class FC_MRV:
    def __init__(self, graph):
        self.graph = graph
        self.colors = {}
        self.domain = {node: set(range(1, len(graph) + 1)) for node in graph}
        self.node_order = list(graph.nodes())


    def mrv(self, node):
        used_colors = set(self.colors.get(neighbor) for neighbor in self.graph[node] if neighbor in self.colors)
        all_colors = set(range(1, len(self.graph) + 1))
        available_colors = all_colors - used_colors
        return len(available_colors)

    def forward_checking(self, node):
        for neighbor in self.graph[node]:
            if neighbor not in self.colors and len(self.domain[neighbor]) == 1:
                color = self.domain[neighbor].pop()
                if color in self.domain[node]:
                    self.domain[node].remove(color)
            elif neighbor in self.colors and self.colors[neighbor] in self.domain[node]:
                self.domain[node].remove(self.colors[neighbor])
        return self.domain

    def select_mrv_node(self):
        uncolored_nodes = [n for n in self.graph if n not in self.colors]
        return min(uncolored_nodes, key=lambda n: self.mrv(n))
    def dfs_fc(self):
        if len(self.colors) == len(self.graph):
            return True
        node = self.select_mrv_node()
        self.node_order.remove(node)
        for color in self.domain[node]:
            if color not in set(self.colors.get(neighbor) for neighbor in self.graph[node] if neighbor in self.colors):
                self.colors[node] = color

                domain_copy = self.domain.copy()
                domain_copy = self.forward_checking(node)

                if all(domain_copy[key] for key in domain_copy):
                    node_order_copy = self.node_order.copy()
                    node_order_copy.sort(key=lambda n: len(domain_copy[n]))
                    if self.dfs_fc():
                        return True

                self.colors.pop(node, None)

        self.node_order.insert(0, node)
        return False

    def run(self):
        self.dfs_fc()
        return self.colors
