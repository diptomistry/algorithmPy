from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.num_vertices = 0
        self.adj_matrix = []

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
            self.num_vertices += 1
            if self.num_vertices > 1:
                for vertices in self.adj_matrix:
                    vertices.append(0)
            temp = [0] * self.num_vertices
            self.adj_matrix.append(temp)

    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)

        self.graph[u].append(v)
        self.adj_matrix[u-1][v-1] = 1

    def delete_vertex(self, v):
        if v in self.graph:
            for vertex in self.graph:
                if v in self.graph[vertex]:
                    self.graph[vertex].remove(v)
            del self.graph[v]

            v_index = v - 1
            for i in range(self.num_vertices):
                del self.adj_matrix[i][v_index]
            del self.adj_matrix[v_index]
            self.num_vertices -= 1

    def delete_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
            self.adj_matrix[u-1][v-1] = 0

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfs(self, start):
        visited = set()
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def print_adj_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    print("BFS Traversal starting from node 1:")
    g.bfs(1)

    print("\nDFS Traversal starting from node 1:")
    g.dfs(1)

    g.print_adj_matrix()

    g.delete_vertex(3)
    g.delete_edge(2, 4)

    print("\nGraph after node and edge deletion:")
    g.print_adj_matrix()
