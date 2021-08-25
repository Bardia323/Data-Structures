# Here is a universally-applicable graph structure in python.


class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_map = {}

    def __repr__(self):
        return 'Graph(%s, %s)' % (self.nodes, self.edges)

    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.node_map[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.edges.append((node1, node2))
        self.node_map[node1].append(node2)
        self.node_map[node2].append(node1)

    def remove_edge(self, node1, node2):
        self.edges.remove((node1, node2))
        self.node_map[node1].remove(node2)
        self.node_map[node2].remove(node1)

    def remove_node(self, node):
        self.nodes.remove(node)
        for other_node in self.nodes:
            self.node_map[other_node].remove(node)
        for edge in list(self.edges):
            if node in edge:
                self.edges.remove(edge)

    def depth_first_search(self, value):
        nodes = [self.nodes[0]]
        visited_nodes = set()
        while nodes:
            node = nodes.pop()
            if node in visited_nodes:
                continue
            if node.value == value:
                return node
            visited_nodes.add(node)
            nodes.extend(self.node_map[node])
        return None

    def breadth_first_search(self, value):
        nodes = [self.nodes[0]]
        visited_nodes = set()
        while nodes:
            node = nodes.pop(0)
            if node in visited_nodes:
                continue
            if node.value == value:
                return node
            visited_nodes.add(node)
            nodes.extend(self.node_map[node])
        return None

    def shortest_path(self, node1, node2):
        nodes_to_visit = [node1]
        visited_nodes = set()
        distance_from_start = {node1: 0}
        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node in visited_nodes:
                continue
            visited_nodes.add(node)
            if node == node2:
                return distance_from_start[node]
            nodes_to_visit.extend(self.node_map[node])
            distance_from_start[node] = distance_from_start[node] + 1
        return None

    def are_connected(self, node1, node2):
        return self.shortest_path(node1, node2) is not None

    def find_all_paths(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return [path]
        if node1 not in self.node_map:
            return []
        paths = []
        for node in self.node_map[node1]:
            if node not in path:
                newpaths = self.find_all_paths(node, node2, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

