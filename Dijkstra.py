import heapq
from collections import namedtuple

Edge = namedtuple('Edge', ['source', 'dest', 'weight'])

def dijkstra(edges, num_vertices, source):

    # Initialize distances with infinity, except for the source vertex
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    
    # Create a priority queue
    pq = [(0, source)]
    
    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)
        
        # If we've already found a shorter path, skip this vertex
        if curr_dist > distances[curr_vertex]:
            continue
        
        # Update distances for all neighbors
        for edge in edges:
            if edge.source == curr_vertex:
                new_dist = curr_dist + edge.weight
                if new_dist < distances[edge.dest]:
                    distances[edge.dest] = new_dist
                    heapq.heappush(pq, (new_dist, edge.dest))
    
    return distances

vert = [0, 1, 2, 3, 4]
edges = [
    Edge(vert[0], vert[1], 10),
    Edge(vert[0], vert[3], 5),
    Edge(vert[1], vert[2], 1),
    Edge(vert[1], vert[3], 2),
    Edge(vert[2], vert[4], 4),
    Edge(vert[3], vert[1], 3),
    Edge(vert[3], vert[2], 9),
    Edge(vert[3], vert[4], 2),
    Edge(vert[4], vert[0], 7),
    Edge(vert[4], vert[2], 6)
]

source = 0
distances = dijkstra(edges, len(vert), source)
print(f"Distances from vertex {source}: {distances}")