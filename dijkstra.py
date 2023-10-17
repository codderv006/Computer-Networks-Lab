import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        priority_queue = [(0, src)]

        while priority_queue:
            dist_u, u = heapq.heappop(priority_queue)
            if dist_u < dist[u]:
                continue

            for v, weight in self.graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(priority_queue, (dist[v], v))

        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t{dist[i]}")


g = Graph(5)
g.add_edge(0, 1, 9)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(0, 4, 3)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 4)

g.dijkstra(0)
