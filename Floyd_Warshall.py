def floyd_warshall(W):
    n = len(W)
    
    # Initialize the distance matrix
    D = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    
    # Copy the input graph weights to the distance matrix
    for i in range(n):
        for j in range(n):
            D[i][j] = W[i][j]
    
    # Find the shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    
    return D

W = [[0, 3, 8, float('inf'), -4],
     [float('inf'), 0, float('inf'), 1, 7],
     [float('inf'), 4, 0, float('inf'), float('inf')],
     [2, float('inf'), -5, 0, float('inf')],
     [float('inf'), float('inf'), float('inf'), 6, 0]]

D = floyd_warshall(W)
print("Shortest path distances:")
for row in D:
    print(row)
