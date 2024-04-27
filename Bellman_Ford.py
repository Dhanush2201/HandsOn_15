from collections import namedtuple

Edge = namedtuple('Edge', ['source', 'dest', 'weight'])

def bellman_ford(edges, num_vertices, source):

    # Initialize distances with infinity, except for the source vertex
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    
    # Relax edges (V-1) times
    for _ in range(num_vertices - 1):
        for edge in edges:
            if distances[edge.source] + edge.weight < distances[edge.dest]:
                distances[edge.dest] = distances[edge.source] + edge.weight
    
    # Check for negative cycles
    for edge in edges:
        if distances[edge.source] + edge.weight < distances[edge.dest]:
            return None
    
    return distances

vert = [0, 1, 2, 3, 4]
edges = [
    Edge(vert[0], vert[1], 6),
    Edge(vert[0], vert[3], 7),
    Edge(vert[1], vert[2], 5),
    Edge(vert[1], vert[3], 8),
    Edge(vert[1], vert[4], -4),
    Edge(vert[2], vert[1], -2),
    Edge(vert[3], vert[2], -3),
    Edge(vert[3], vert[4], 9),
    Edge(vert[4], vert[0], 2),
    Edge(vert[4], vert[2], 7)
]

source = 0
distances = bellman_ford(edges, len(vert), source)
if distances is None:
    print("Negative cycle detected.")
else:
    print(f"Distances from vertex {source}: {distances}")